"""Sublab Hard: stories in, CVs out, the winner decided by code.

python -m sublab_hard.cv_extract_and_rank
"""
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
MODEL = os.getenv("MODEL", "gpt-5.6-luna")
client = OpenAI()
DATA = Path(__file__).resolve().parent.parent / "data"

# Сюда добавляй СВОЁ правило, когда какая-то история сломает извлечение (вопрос 1 письменной части).
EXTRA_RULES = []

# Что делать с противоречивым полем при оценке. Реши сам и опиши в ответе на вопрос 4.
CONTRADICTION_SCORING_RULE = (
    "If a field is null because the story contradicts itself, score the criterion "
    "only on the evidence that remains; do not pick one of the contradicting values."
)

RUBRIC = json.loads((DATA / "candidate_rubric.json").read_text(encoding="utf-8"))

RULES = [
    "A fact the story does not state is null. Never estimated, never inferred. No GPA in the story means gpa_4_scale is null.",
    "A GPA on another scale is converted to a 4.0 scale in gpa_4_scale, and the original goes in gpa_original as {\"value\", \"scale\"}.",
    "A paper is published ONLY when the story says published or accepted. Submitted, under review, in preparation and in press are NOT published: "
    "list each in unpublished_outputs with its status and do NOT count it in published_outputs.",
    "Contradictions are not resolved and not averaged: the field is null and the contradiction is recorded in contradictions "
    "as {\"field\", \"values\": [...], \"quotes\": [...]}.",
    "Every non-null field needs a verbatim evidence quote copied from the story, in evidence {field_name: quote}.",
    "experience_months is the total COUNTABLE months of relevant experience under the counting rules in the RUBRIC below; "
    "write the arithmetic in experience_notes. If dates are too vague to count, it is null.",
] + EXTRA_RULES

RECORD_SHAPE = """{
 "candidate_id": string,
 "full_name": string|null,
 "degree": string|null,
 "graduation_year": integer|null,
 "gpa_4_scale": number|null,
 "gpa_original": {"value": number|null, "scale": string|null},
 "languages": [string]|null,
 "published_outputs": integer|null,
 "unpublished_outputs": [{"description": string, "status": string}],
 "experience_months": integer|null,
 "experience_notes": string,
 "contradictions": [{"field": string, "values": [any], "quotes": [string]}],
 "evidence": {"<field name>": "<verbatim quote>"}
}"""

EXTRACT_SYSTEM = (
    "You extract a structured CV record from a written scholarship application. "
    "The story may be in any language (e.g. Kazakh); quotes stay in the original language.\n\n"
    "RULES (obey exactly):\n" + "\n".join(f"{i}. {r}" for i, r in enumerate(RULES, 1))
    + f"\n\nRUBRIC (for the counting rules):\n{json.dumps(RUBRIC, ensure_ascii=False, indent=1)}"
    + f"\n\nReply with ONE JSON object and nothing else, in this shape:\n{RECORD_SHAPE}"
)


def criteria():
    c = RUBRIC.get("criteria") or RUBRIC
    if isinstance(c, dict):
        c = [{"id": k, **v} for k, v in c.items() if isinstance(v, dict)]
    out = []
    for x in c:
        cid = x.get("id") or x.get("name") or x.get("key")
        if cid is None or "weight" not in x:
            raise KeyError(f"Не понял структуру рубрики: {x}. Поправь criteria().")
        out.append((str(cid), float(x["weight"])))
    return out


CRIT = criteria()
SCORE_SYSTEM = (
    "You score a scholarship candidate against a rubric. Give an integer 0-5 for each criterion "
    "and a one-sentence note per criterion. Do NOT compute any total or ranking.\n"
    f"{CONTRADICTION_SCORING_RULE}\n\n"
    f"RUBRIC:\n{json.dumps(RUBRIC, ensure_ascii=False, indent=1)}\n\n"
    "Reply with ONE JSON object and nothing else:\n"
    '{"scores": {' + ", ".join(f'"{c}": int' for c, _ in CRIT) + '}, '
    '"notes": {' + ", ".join(f'"{c}": string' for c, _ in CRIT) + "}}"
)


def call(system, user, json_mode=True):
    kw = {"response_format": {"type": "json_object"}} if json_mode else {}
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        **kw,
    )
    return r.choices[0].message.content


def record_problems(o):
    if not isinstance(o, dict):
        return ["not an object"]
    p = []
    types = {"full_name": (str, type(None)), "degree": (str, type(None)),
             "graduation_year": (int, type(None)), "gpa_4_scale": (int, float, type(None)),
             "gpa_original": dict, "languages": (list, type(None)),
             "published_outputs": (int, type(None)), "unpublished_outputs": list,
             "experience_months": (int, float, type(None)), "experience_notes": str,
             "contradictions": list, "evidence": dict}
    for k, t in types.items():
        if k not in o:
            p.append(f"missing {k}")
        elif not isinstance(o[k], t):
            p.append(f"bad type {k}")
    return p


def score_problems(o):
    if not isinstance(o, dict) or not isinstance(o.get("scores"), dict):
        return ["no scores object"]
    p = []
    for c, _ in CRIT:
        v = o["scores"].get(c)
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 5:
            p.append(f"bad score {c}={v!r}")
    return p


def squash(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def extract(cid, story):
    raw, obj, probs = "", None, ["unparsed"]
    for _ in range(2):  # одна повторная попытка
        raw = call(EXTRACT_SYSTEM, f"candidate_id: {cid}\n\nSTORY:\n{story}")
        try:
            obj = json.loads(raw)
            probs = record_problems(obj)
            if not probs:
                break
        except Exception:
            obj, probs = None, ["unparsed"]
    if isinstance(obj, dict):
        obj["candidate_id"] = cid  # id решает код, не модель
    return obj, probs


def main():
    stories = {p.stem: p.read_text(encoding="utf-8") for p in sorted((DATA / "candidates").glob("story-*.md"))}

    # ---------- Part 1: extraction ----------
    records, rows = {}, []
    for cid, story in stories.items():
        obj, probs = extract(cid, story)
        parsed = obj is not None
        records[cid] = obj
        nulls, bad_quotes, contr, unpub = [], [], 0, 0
        if parsed:
            nulls = [k for k, v in obj.items() if v is None]
            contr = len(obj.get("contradictions") or [])
            unpub = len(obj.get("unpublished_outputs") or [])
            text = squash(story)
            for f, q in (obj.get("evidence") or {}).items():
                if squash(q) not in text:
                    bad_quotes.append(f)  # цитата не найдена дословно => возможно выдумана
        rows.append([cid, "yes" if parsed else "NO", "yes" if parsed and not probs else f"NO {probs}",
                     ", ".join(nulls) or "-", contr, unpub, ", ".join(bad_quotes) or "-"])
        print(f"  extracted {cid}", flush=True)
    print("\n### Part 1: extraction per story\n")
    print(md(["story", "parsed", "validated", "null fields", "contradictions", "unpublished", "evidence not verbatim"], rows))
    print("\nПолные записи (по ним заполняешь trap table: GPA-шкала, submitted/in press, противоречия и т.д.):\n")
    for cid, o in records.items():
        print(cid, json.dumps(o, ensure_ascii=False, indent=1))

    # ---------- Part 2: scores by model, total by code ----------
    scored = {}
    for cid, o in records.items():
        if o is None:
            continue
        s = None
        for _ in range(3):
            try:
                cand = json.loads(call(SCORE_SYSTEM, json.dumps(o, ensure_ascii=False)))
            except Exception:
                continue
            if not score_problems(cand):
                s = cand
                break
        scored[cid] = s
    wsum = sum(w for _, w in CRIT)
    table = []
    for cid, s in scored.items():
        if s is None:
            table.append([cid] + ["FAILED"] * len(CRIT) + ["-"])
            continue
        total = sum(s["scores"][c] * w for c, w in CRIT) / wsum  # ВЕС считает код
        s["total"] = round(total, 4)
        table.append([cid] + [s["scores"][c] for c, _ in CRIT] + [s["total"]])
    table_ok = [r for r in table if r[-1] != "-"]
    table_ok.sort(key=lambda r: r[-1], reverse=True)
    print("\n### Part 2: scores (model) and weighted total (code), 0-5 scale\n")
    print("weights:", {c: w for c, w in CRIT})
    print(md(["candidate"] + [c for c, _ in CRIT] + ["total"], table_ok))
    if table_ok:
        print(f"\nCOMPUTED WINNER: {table_ok[0][0]} ({table_ok[0][-1]})")
        if len(table_ok) > 1:
            gap = round(table_ok[0][-1] - table_ok[1][-1], 4)
            print(f"Gap top-2: {gap}" + ("  <-- в пределах 0.05!" if gap <= 0.05 else ""))
    print("\nNotes от модели:")
    for cid, s in scored.items():
        if s:
            print(f"  {cid}: {json.dumps(s.get('notes'), ensure_ascii=False)}")

    # ---------- prose comparison, separate call ----------
    prose = call(
        "You advise a scholarship committee. Answer in prose, no JSON.",
        f"RUBRIC:\n{json.dumps(RUBRIC, ensure_ascii=False)}\n\n"
        f"CANDIDATE RECORDS:\n{json.dumps(records, ensure_ascii=False)}\n\n"
        "Which candidate should win the one scholarship, and why? Rank all six.",
        json_mode=False,
    )
    print("\n### Prose answer (separate call)\n")
    print(prose)

    Path(__file__).with_name("results_hard.json").write_text(
        json.dumps({"records": records, "scores": scored, "prose": prose}, ensure_ascii=False, indent=1),
        encoding="utf-8")


if __name__ == "__main__":
    main()