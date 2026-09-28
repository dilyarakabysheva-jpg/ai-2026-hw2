"""Sublab Medium: memory you choose.

python -m sublab_medium.chat_memory                # scripted run, twice (compress on / skipped)
python -m sublab_medium.chat_memory --interactive  # live chat: type compress / tokens / state / quit
"""
import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
MODEL = os.getenv("MODEL", "gpt-5.6-luna")
client = OpenAI()
DATA = Path(__file__).resolve().parent.parent / "data"

# ---------------- ПОДСТРОЙ ПОД СВОИ JSON (открой data/chat_script.json) ----------------
TURN_KEYS = ["user", "content", "text", "message", "turn"]
PROBE_Q_KEYS = ["question", "q", "probe", "prompt", "text"]
PROBE_EXPECT_KEYS = ["expect", "expected", "fact", "contains", "must_contain", "keywords", "answer"]
COMPRESS_MARK = "<compress>"
JSON_REPLIES = True  # README: контракт JSON действует везде. Если скрипт — свободный чат, поставь False.
# ---------------------------------------------------------------------------------------


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


SCRIPT = load("chat_script.json")
SCHEMA = load("memory_state.schema.json")
RECORDS = load("records.json")
POLICY = load("policy.json")

TURNS = SCRIPT.get("turns") or SCRIPT.get("script") or SCRIPT.get("conversation")
PROBES = SCRIPT.get("probes")
assert TURNS and PROBES, f"Не нашёл turns/probes. Ключи файла: {list(SCRIPT)}"

SHAPE = """Reply with ONE JSON object and nothing else, exactly these keys:
{"applicant_id": string or null, "found": boolean,
 "decision": "granted"|"refused"|"more_info"|"not_found",
 "amount": integer, "missing_documents": [string], "reason": string}
Put anything you tell the applicant, and any fact from the conversation you are asked about, in "reason"."""

SYSTEM = (
    "You are the assistant of a grant office and you chat with an applicant.\n\n"
    f"RECORDS ON FILE:\n{json.dumps(RECORDS, ensure_ascii=False)}\n\n"
    f"POLICY:\n{json.dumps(POLICY, ensure_ascii=False)}\n\n"
    + (SHAPE if JSON_REPLIES else "Answer briefly in plain text.")
)


def first_key(d, keys, what):
    if isinstance(d, str):
        return d
    for k in keys:
        if k in d:
            return d[k]
    raise KeyError(f"Не нашёл {what}. Ключи: {list(d)}. Поправь константы вверху файла.")


def validate(obj, schema):
    try:
        import jsonschema  # pip install jsonschema
        jsonschema.validate(obj, schema)
    except ImportError:  # запасной вариант: только required + тип объекта
        assert isinstance(obj, dict), "state is not an object"
        missing = [k for k in schema.get("required", []) if k not in obj]
        assert not missing, f"missing required: {missing}"


def api(messages, json_mode):
    kw = {"response_format": {"type": "json_object"}} if json_mode else {}
    r = client.chat.completions.create(model=MODEL, messages=messages, **kw)
    return r.choices[0].message.content, r.usage.prompt_tokens


class Session:
    def __init__(self):
        self.history = []   # user/assistant сообщения
        self.state = None   # сжатое состояние после compress
        self.log = []       # (label, tokens_sent)
        self.last_tokens = 0

    def messages(self):
        m = [{"role": "system", "content": SYSTEM}]
        if self.state is not None:
            m.append({"role": "system",
                      "content": "STATE of the earlier conversation (JSON):\n"
                                 + json.dumps(self.state, ensure_ascii=False)})
        return m + self.history

    def say(self, text, label):
        self.history.append({"role": "user", "content": text})
        reply, tok = api(self.messages(), JSON_REPLIES)
        self.history.append({"role": "assistant", "content": reply})
        self.log.append((label, tok))
        self.last_tokens = tok
        return reply

    def ask(self, text, label):
        """Проба: спрашиваем, но в историю НЕ записываем."""
        reply, tok = api(self.messages() + [{"role": "user", "content": text}], JSON_REPLIES)
        self.log.append((label, tok))
        self.last_tokens = tok
        return reply

    def compress(self):
        transcript = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in self.history)
        prior = f"PREVIOUS STATE:\n{json.dumps(self.state, ensure_ascii=False)}\n\n" if self.state else ""
        msgs = [
            {"role": "system", "content":
                "Summarise the conversation into ONE JSON object that validates against this "
                "JSON Schema. Output only the JSON object. Keep every concrete fact that fits a "
                "field (names, ids, numbers, dates, documents, promises). Never invent.\n\nSCHEMA:\n"
                + json.dumps(SCHEMA, ensure_ascii=False)},
            {"role": "user", "content": prior + transcript},
        ]
        try:
            text, tok = api(msgs, True)
            obj = json.loads(text)
            validate(obj, SCHEMA)
        except Exception as e:
            print(f"!! compress FAILED ({type(e).__name__}: {e}). История СОХРАНЕНА, продолжаем без сжатия.")
            return False
        self.log.append(("compress (summary call, не считается в peak)", tok))
        self.state, self.history = obj, []
        print(f"-- compressed. summary call sent {tok} tokens; turns thrown away; state is now sent instead.")
        return True


def probe_hit(reply, probe):
    exp = None
    for k in PROBE_EXPECT_KEYS:
        if isinstance(probe, dict) and k in probe:
            exp = probe[k]
            break
    if exp is None:
        return None
    exp = exp if isinstance(exp, list) else [exp]
    low = reply.lower()
    return any(str(e).lower() in low for e in exp)  # any-of; проверь глазами ответы!


def run_script(compress_on):
    s = Session()
    n = 0
    for t in TURNS:
        text = first_key(t, TURN_KEYS, "текст реплики")
        if text.strip() == COMPRESS_MARK:
            if compress_on:
                s.compress()
            else:
                print("-- <compress> skipped")
            continue
        n += 1
        s.say(text, f"turn {n}")
    probe_rows = []
    for i, p in enumerate(PROBES, 1):
        q = first_key(p, PROBE_Q_KEYS, "вопрос пробы")
        reply = s.ask(q, f"probe {i}")
        hit = probe_hit(reply, p)
        probe_rows.append((i, q, hit, reply))
    return s, probe_rows


def md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def scripted():
    print("=== RUN A: uncompressed ===")
    a, pa = run_script(False)
    print("=== RUN B: compressed ===")
    b, pb = run_script(True)

    la = [x for x in a.log if not x[0].startswith("compress")]
    lb = [x for x in b.log]
    # в B есть строка compress — покажем как есть
    rows_b = {x[0]: x[1] for x in lb}
    rows = [[l, dict(la).get(l, "-"), rows_b.get(l, "-")] for l in
            [x[0] for x in lb] + [x[0] for x in la if x[0] not in rows_b]]
    print("\n### Tokens sent per call\n")
    print(md(["call", "uncompressed", "compressed"], rows))

    peak = lambda log: max(t for l, t in log if not l.startswith("compress"))
    print("\n### Peak tokens sent in one call\n")
    print(md(["run", "peak"], [["uncompressed", peak(a.log)], ["compressed", peak(b.log)]]))

    print("\n### Probes (проверь ответы глазами: автосовпадение — подстрока, перефраз он не поймёт)\n")
    rows = []
    for (i, q, ha, ra), (_, _, hb, rb) in zip(pa, pb):
        rows.append([i, q[:60], ha, hb])
    print(md(["probe", "question", "uncompressed hit", "compressed hit"], rows))
    print(f"\nretrieved: uncompressed {sum(1 for r in pa if r[2])}/{len(pa)}, "
          f"compressed {sum(1 for r in pb if r[2])}/{len(pb)}")
    for (i, q, ha, ra), (_, _, hb, rb) in zip(pa, pb):
        print(f"\nP{i}: {q}\n  A: {ra}\n  B: {rb}")

    print("\n### State object (compressed run)\n")
    print(json.dumps(b.state, ensure_ascii=False, indent=2))
    Path(__file__).with_name("state_compressed.json").write_text(
        json.dumps(b.state, ensure_ascii=False, indent=2), encoding="utf-8")


def interactive():
    s = Session()
    print("Чат. Команды: compress | tokens | state | quit. Всё остальное — реплика.")
    while True:
        try:
            text = input("\nyou> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            continue
        if text == "quit":
            break
        if text == "compress":
            s.compress()
            continue
        if text == "tokens":
            print(f"last call sent {s.last_tokens} tokens; history turns kept: {len(s.history)}; "
                  f"state present: {s.state is not None}")
            continue
        if text == "state":
            print(json.dumps(s.state, ensure_ascii=False, indent=2))
            continue
        reply = s.say(text, f"turn {len(s.log) + 1}")
        print(f"bot> {reply}\n[sent {s.last_tokens} tokens, messages in call: {len(s.messages())}]")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--interactive", action="store_true")
    args = ap.parse_args()
    interactive() if args.interactive else scripted()