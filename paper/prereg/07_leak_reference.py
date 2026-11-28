"""Builds paper/prereg/leak_reference.json: for each of the 23 scored questions, the archive's own thinking-off naive
(direct-ask) answer that the pre-round-1 leakage check compares against: source file, the archived call's time and
prompt_tokens, the attempt-1 reply as stored, and how the question text is formed. Read-only; no model call; no error
against the truth is computed here (that happens only in run_repeats.py --leak-decide, after the check)."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
scored_q = sorted({r["qid"] for r in rows if r["scored"] == "True"})
def calls(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []
fc_calls = calls(ROOT / "results/forecast/calls.jsonl")
out = []
for qid in scored_q:
    rec = None
    for src, cpath in [(ROOT / f"results/forecast/raw/naive/{qid}.json", None),
                       (ROOT / f"results/test3/raw/naive_off/{qid}.json", ROOT / f"results/test3/raw/naive_off/{qid}.calls.jsonl"),
                       (ROOT / f"results/test4/raw/naive_off/{qid}.json", ROOT / f"results/test4/raw/naive_off/{qid}.calls.jsonl")]:
        if src.exists():
            d = json.loads(src.read_text(encoding="utf-8"))
            cs = calls(cpath) if cpath else [c for c in fc_calls if c.get("qid") == qid]
            c1 = [c for c in cs if c.get("arm") == "naive" and c.get("attempt") == 1]
            rec = {"qid": qid, "source": str(src.relative_to(ROOT)).replace("\\", "/"),
                   "calls_source": str((cpath or ROOT / "results/forecast/calls.jsonl").relative_to(ROOT)).replace("\\", "/"),
                   "n_attempt1_calls_logged": len(c1),
                   "archived_at": c1[-1]["at"] if c1 else None,
                   "archived_prompt_tokens": c1[-1].get("prompt_tokens") if c1 else None,
                   "archived_thinking": (d.get("thinking_by_role") or {}),
                   "final_attempt": d.get("final_attempt"),
                   "attempt1_reply": d["attempts"][0].get("reply"),
                   "attempt1_problems": d["attempts"][0].get("problems"),
                   "target_unit": d.get("target_unit"),
                   "question_from": ("forecast.with_as_of(question_template, as_of)" if d.get("as_of") else "forecast.QUESTIONS[question]"),
                   "as_of_for_template": d.get("as_of")}
            break
    out.append(rec if rec else {"qid": qid, "source": None})
(ROOT / "paper/prereg/leak_reference.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
for r in out:
    print(r["qid"], "|", r["source"], "| at", r.get("archived_at"), "| ptok", r.get("archived_prompt_tokens"),
          "| n_att1", r.get("n_attempt1_calls_logged"), "| final_attempt", r.get("final_attempt"), "| problems", r.get("attempt1_problems"),
          "| think", r.get("archived_thinking"), "|", r.get("question_from"), r.get("as_of_for_template"))
print("questions with a reference:", sum(1 for r in out if r.get("source")), "of", len(out))
