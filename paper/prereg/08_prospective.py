"""O2 material (read-only, no official value is looked up or read): the prospective runs on the 13 questions listed in
topic/checks/check_9_counts_log.txt, with code version, thinking, start time, estimate presence, unit, and which of the
two signals of the frozen statement can be evaluated on each run (past-only flag: >= 1 earlier usable run of the same
question in the same unit; gate replay: an archived thinking-off naive answer exists). Writes prospective_runs.json.
It does not compute any flag value (that needs only estimates, but is part of the frozen statement's outcome)."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
P13 = ["fc_byd_rev_2026_q3", "fc_de_unemployed_2026_10", "fc_eqnr_prod_2026_q3", "fc_googl_tokens_2026_q3", "fc_jnto_2026_09",
       "fc_kr_births_2026_08", "fc_meta_capex_2026_q3", "fc_mx_exports_2026_09", "fc_tw_restaurants_2026_09",
       "fc_uk_carprod_2026_09", "fc_uk_homesales_2026_09", "fc_uk_mortgages_2026_09", "fc_us_milk_2026_09"]
roles = {"prospective_prereg_no_truth_registered", "prospective_rerun_no_truth_registered"}
pr = sorted([r for r in rows if r["qid"] in P13 and r["eval_role"] in roles], key=lambda r: (r["qid"], r["started_at"]))
other = [r for r in rows if r["qid"] in P13 and r["eval_role"] not in roles]
out = []
for r in pr:
    earlier = [x for x in pr if x["qid"] == r["qid"] and x["started_at"] < r["started_at"] and x["has_estimate"] == "True"
               and x["mode"] == "continuous" and x["unit_canonical"] == r["unit_canonical"]]
    naive = None
    for p in (ROOT / f"results/forecast/raw/naive/{r['qid']}.json", ROOT / f"results/test4/raw/naive_off/{r['qid']}.json"):
        if p.exists():
            naive = str(p.relative_to(ROOT)).replace("\\", "/")
    out.append({"run_id": r["run_id"], "qid": r["qid"], "tag": r["tag"], "set": r["set"], "eval_role": r["eval_role"],
                "code_version": r["code_version"], "thinking": r["thinking"] == "True", "started_at": r["started_at"],
                "as_of": r["as_of"], "mode": r["mode"], "has_estimate": r["has_estimate"] == "True",
                "unit_canonical": r["unit_canonical"], "answer_unit": r["answer_unit"], "unit_factor": r["unit_factor"],
                "unit_conversion_applied": r["unit_conversion_applied"],
                "n_earlier_usable_same_unit": len(earlier), "earlier_run_ids": [x["run_id"] for x in earlier],
                "naive_off_reference": naive})
(ROOT / "paper/prereg/prospective_runs.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
for o in out:
    print(f"{o['run_id']:42s} {o['eval_role'][:28]:28s} {o['code_version']:8s} think={o['thinking']!s:5s} start={o['started_at'][:16]} "
          f"est={o['has_estimate']!s:5s} mode={o['mode']:10s} unit={o['unit_canonical']!s:12.12s} ans_unit={o['answer_unit']!s:6s} factor={o['unit_factor']} "
          f"earlier={o['n_earlier_usable_same_unit']} naive={'yes' if o['naive_off_reference'] else 'no'}")
print("runs", len(out), "questions", len({o['qid'] for o in out}), "with estimate", sum(o["has_estimate"] for o in out),
      "| past-only flag evaluable (>=1 earlier usable, run has estimate):", sum(1 for o in out if o["has_estimate"] and o["n_earlier_usable_same_unit"] >= 1),
      "| gate replay evaluable (estimate + naive_off):", sum(1 for o in out if o["has_estimate"] and o["naive_off_reference"]))
print("other (non-prospective) runs on these 13 questions:", [(r["run_id"], r["eval_role"]) for r in other])
