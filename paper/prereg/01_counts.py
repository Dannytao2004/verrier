"""Pre-registration counts (read-only): scored questions, catastrophic runs, their configurations.
Reads paper/analysis/data/runs.csv only. No outcome of the planned analyses is computed."""
import csv, json, collections
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "analysis" / "data" / "runs.csv"
rows = list(csv.DictReader(open(P, encoding="utf-8")))
print("rows", len(rows))
scored = [r for r in rows if r["scored"] == "True"]
qs = sorted({r["qid"] for r in scored})
print("[1] scored runs", len(scored), "scored questions", len(qs))
for q in qs:
    rq = [r for r in rows if r["qid"] == q]
    print("   ", q, "set=", rq[0]["set"], "runs_with_truth=", sum(r["has_truth"] == "True" for r in rq),
          "scored=", sum(r["scored"] == "True" for r in rq))
cat = [r for r in scored if r["catastrophic"] == "True"]
print("[2] catastrophic scored runs", len(cat), "on", len({r["qid"] for r in cat}), "questions")
for r in sorted(cat, key=lambda r: (r["qid"], r["started_at"])):
    print("   ", r["run_id"], "| ver", r["code_version"], "| commit", r["code_commit"], "| think", r["thinking"],
          "| noown", r["noown"], "| started", r["started_at"], "| role", r["eval_role"], "| regime", r["search_regime"],
          "| n_same_cfg", r["n_same_config_runs_on_question"], "| config_flags", r["config_flags"])
print("[3] all runs of catastrophic questions by config_key (has_truth runs)")
for q in sorted({r["qid"] for r in cat}):
    c = collections.Counter(r["config_key"] for r in rows if r["qid"] == q and r["has_truth"] == "True")
    print("   ", q, dict(c))
print("[4] v2.17a runs on scored questions (code_version == v2.17a)")
for r in rows:
    if r["code_version"] == "v2.17a":
        print("   ", r["run_id"], "think", r["thinking"], "scored", r["scored"], "started", r["started_at"],
              "usd_tokens", r["usd_tokens"], "usd_total", r["usd_total"], "usd_search", r["usd_search"], "wall_s", r["wall_s"],
              "has_est", r["has_estimate"], "cat", r["catastrophic"])
