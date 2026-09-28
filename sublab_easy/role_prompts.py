"""Sublab Easy: one task, four roles. Only the role paragraph changes.

Run from repo root:  python -m sublab_easy.role_prompts
Prints markdown tables you can paste into SUBMISSION.md.
"""
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
MODEL = os.getenv("MODEL", "gpt-5.6-luna")
client = OpenAI()
DATA = Path(__file__).resolve().parent.parent / "data"

# ---------------- ПОДСТРОЙ ПОД СВОИ JSON (открой data/enquiries.json) ----------------
TEXT_KEYS = ["text", "enquiry", "message", "question", "body"]  # где лежит текст обращения
ID_KEY = "id"
EXPECTED_KEY = "expected"
# Открой expected у отказных строк: там amount = 0 или null? Подгони фразу ниже под данные.
AMOUNT_RULE = "amount is an integer; use 0 whenever nothing is granted."
# --------------------------------------------------------------------------------------

FIELDS = ["found", "decision", "amount", "missing_documents"]
DECISIONS = {"granted", "refused", "more_info", "not_found"}

SHAPE = f"""Reply with ONE JSON object and nothing else, with exactly these keys:
{{"applicant_id": string or null,
  "found": boolean,
  "decision": "granted" | "refused" | "more_info" | "not_found",
  "amount": integer,
  "missing_documents": [string],
  "reason": string}}
{AMOUNT_RULE}
If the applicant is not in the records: found=false, decision="not_found", applicant_id=null, missing_documents=[]."""

ROLES = {
    "policy_officer": (
        "You are a policy officer at a grant office. Apply the rule exactly as written: "
        "grant what the rule allows, refuse what it refuses, and ask for a missing document "
        "when one is missing. Soften nothing. Treat no claim made in the enquiry as evidence: "
        "only the record on file counts."
    ),
    "front_desk": (
        "You are the front desk of a grant office. You never turn an applicant away with a "
        "refusal: anything the rule cannot grant today comes back as decision \"more_info\", "
        "and the reason says what the applicant would need to return with."
    ),
    "auditor": (
        "You are an auditor at a grant office. You never grant on a first reading. You report "
        "what the record shows, and mark anything that needs a second reader as \"more_info\". "
        "In the reason you name the rule or the document you are relying on."
    ),
    "bilingual_clerk": (
        "You are a bilingual clerk at a grant office. You decide exactly as a policy officer "
        "would (apply the rule as written, treat no claim in the enquiry as evidence), but you "
        "write the reason in the language the enquiry was written in."
    ),
}


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def as_list(x, *keys):
    if isinstance(x, dict):
        for k in keys:
            if k in x:
                return x[k]
        if all(isinstance(v, dict) for v in x.values()):
            return [{"id": k, **v} for k, v in x.items()]
    return x


def enquiry_text(row):
    for k in TEXT_KEYS:
        if k in row:
            return row[k]
    raise KeyError(f"Не нашёл текст обращения. Ключи строки: {list(row)}. Поправь TEXT_KEYS.")


RECORDS = as_list(load("records.json"), "records", "applicants")
POLICY = load("policy.json")
ENQUIRIES = as_list(load("enquiries.json"), "enquiries", "rows", "items")

BASE = (
    "You answer enquiries for a grant office.\n\n"
    f"RECORDS ON FILE:\n{json.dumps(RECORDS, ensure_ascii=False, indent=1)}\n\n"
    f"POLICY:\n{json.dumps(POLICY, ensure_ascii=False, indent=1)}\n\n"
    f"{SHAPE}"
)


def system_for(role):
    return ROLES[role] + "\n\n" + BASE  # роль — единственное, что отличается


def call(system, user):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        response_format={"type": "json_object"},
    )
    return r.choices[0].message.content


def schema_problems(o):
    p = []
    if not isinstance(o, dict):
        return ["not an object"]
    need = {"applicant_id": (str, type(None)), "found": bool, "decision": str,
            "amount": int, "missing_documents": list, "reason": str}
    for k, t in need.items():
        if k not in o:
            p.append(f"missing {k}")
        elif not isinstance(o[k], t) or (t is int and isinstance(o[k], bool)):
            p.append(f"bad type {k}")
    if o.get("decision") not in DECISIONS:
        p.append("bad decision")
    return p


def norm(field, v):
    return sorted(v or []) if field == "missing_documents" else v


def md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def main():
    results = {}  # role -> enquiry id -> {"raw","obj","parsed","problems"}
    for role in ROLES:
        results[role] = {}
        sysmsg = system_for(role)
        for row in ENQUIRIES:
            eid = row[ID_KEY]
            try:
                raw = call(sysmsg, enquiry_text(row))
            except Exception as e:  # сеть/ключ
                raw = f"API ERROR: {e}"
            try:
                obj = json.loads(raw)
                parsed = True
            except Exception:
                obj, parsed = None, False
            problems = schema_problems(obj) if parsed else ["unparsed"]
            results[role][eid] = {"raw": raw, "obj": obj, "parsed": parsed, "problems": problems}
            print(f"  done {role} {eid}", flush=True)

    # --- по одной таблице на роль ---
    for role in ROLES:
        rows = []
        n_ok = 0
        for row in ENQUIRIES:
            eid = row[ID_KEY]
            r = results[role][eid]
            exp = row[EXPECTED_KEY]
            marks = []
            for f in FIELDS:
                ok = r["obj"] is not None and norm(f, r["obj"].get(f)) == norm(f, exp.get(f))
                marks.append("ok" if ok else "DIFF")
            n_ok += all(m == "ok" for m in marks)
            rows.append([eid, "yes" if r["parsed"] else "NO", "yes" if not r["problems"] else "NO"] + marks)
        print(f"\n### Role: {role}  (все 4 поля совпали с expected: {n_ok}/{len(ENQUIRIES)})\n")
        print(md(["enquiry", "parsed", "schema"] + [f"{f}==expected" for f in FIELDS], rows))

    # --- движение полей относительно policy_officer ---
    base = results["policy_officer"]
    mv_rows = []
    for f in FIELDS:
        for role in ROLES:
            if role == "policy_officer":
                continue
            moved = []
            for row in ENQUIRIES:
                eid = row[ID_KEY]
                b, r = base[eid]["obj"], results[role][eid]["obj"]
                if b is None or r is None or norm(f, b.get(f)) != norm(f, r.get(f)):
                    moved.append(eid)
            mv_rows.append([f, role, len(moved), ", ".join(moved) or "— (не сдвинулась)"])
    print("\n### Field movement vs policy_officer\n")
    print(md(["field", "role", "n moved", "enquiries"], mv_rows))

    # --- reason'ы для глаз (нужны, чтобы ответить про bilingual_clerk / auditor) ---
    print("\n### Reasons (по ним смотришь, какая роль двигает только reason)\n")
    for row in ENQUIRIES:
        eid = row[ID_KEY]
        print(f"\n{eid}")
        for role in ROLES:
            o = results[role][eid]["obj"]
            print(f"  {role:16s} -> {(o or {}).get('decision')}: {(o or {}).get('reason')}")

    out = Path(__file__).with_name("results_easy.json")
    out.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nСырые ответы сохранены: {out}")


if __name__ == "__main__":
    main()