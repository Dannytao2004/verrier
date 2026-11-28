"""O2 frozen confirmatory statement (PREREG.md section F): scorer, written before any official value of the 13 prospective
questions was looked up. Run it only after the lookup unit has written paper/prereg/o2/official_values.json (format in
PREREG.md F4). Offline; reads prospective_runs.json, paper/analysis/data/runs.csv and the archived thinking-off naive
answers; writes paper/prereg/o2/o2_results.json. Needs the project venv (triangulate.arms.check_naive, unit library).

Usage: PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe -B paper/prereg/o2_score.py
"""
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREREG = ROOT / "paper" / "prereg"
OFFICIAL = PREREG / "o2" / "official_values.json"
LN2 = math.log(2)
GATE_RATIO = 2.0          # triangulate/agent/magnitude.py RATIO; b6 v07 replay threshold
SECONDARY = ["fc_googl_tokens_2026_q3/test2_think", "fc_meta_capex_2026_q3/test2_think",
             "fc_tw_restaurants_2026_09/test2_think", "fc_us_milk_2026_09/test2_think"]   # v2.9a thinking-arm runs


def cp(k, n, a=0.05):
    from scipy import stats
    lo = 0.0 if k == 0 else stats.beta.ppf(a / 2, k, n - k + 1)
    hi = 1.0 if k == n else stats.beta.ppf(1 - a / 2, k + 1, n - k)
    return [round(lo, 4), round(hi, 4)]


def upper95(k, n):
    """Exact one-sided 95% upper bound; for k = 0 also the rule of three 3/n."""
    from scipy import stats
    return {"exact_one_sided": round(1.0 if k == n else stats.beta.ppf(0.95, k + 1, n - k), 4),
            "rule_of_three": round(3 / n, 4) if k == 0 and n else None}


def main():
    if not OFFICIAL.exists():
        raise SystemExit(f"{OFFICIAL} does not exist: the official values have not been registered (PREREG.md F4)")
    sys.path.insert(0, str(ROOT))
    from triangulate import forecast as FC        # noqa: E402
    from triangulate.arms import check_naive      # noqa: E402
    off = json.loads(OFFICIAL.read_text(encoding="utf-8"))
    pros = json.loads((PREREG / "prospective_runs.json").read_text(encoding="utf-8"))
    rows = {r["run_id"]: r for r in csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8"))}
    by_q = {q["id"]: q for q in FC.QUESTIONS}

    def naive_ref(qid):
        for p in (ROOT / f"results/test4/raw/naive_off/{qid}.json", ROOT / f"results/forecast/raw/naive/{qid}.json"):
            if p.exists():
                d = json.loads(p.read_text(encoding="utf-8"))
                q = by_q[qid]
                return check_naive(d["attempts"][-1].get("reply"), q.get("answer_unit", ""), q.get("strict", True))[1]
        return None

    def evaluate(run_ids):
        recs = []
        for rid in run_ids:
            r = rows[rid]
            qid = r["qid"]
            o = off.get(qid) or {}
            if o.get("status") != "ok":
                recs.append({"run_id": rid, "qid": qid, "scorable": False, "why": o.get("status", "no official value")})
                continue
            truth = float(o["value_in_answer_unit"])
            est = float(r["est"]) if r["est"] else None
            rec = {"run_id": rid, "qid": qid, "scorable": True, "has_estimate": est is not None, "est": est,
                   "official": truth}
            if est is not None:
                rec["ln_err"] = math.log(est / truth)
                rec["catastrophic"] = abs(rec["ln_err"]) > LN2
                ref = naive_ref(qid)
                rec["gate_ref"] = ref
                rec["gate_flag"] = (max(est / ref, ref / est) > GATE_RATIO) if ref else None
                earlier = [x for x in rows.values() if x["qid"] == qid and x["started_at"] < r["started_at"]
                           and x["has_estimate"] == "True" and x["mode"] == "continuous" and x["est"]
                           and x["unit_canonical"] == r["unit_canonical"]]
                if earlier:
                    le = sorted(math.log(float(x["est"])) for x in earlier)
                    m = le[len(le) // 2] if len(le) % 2 else (le[len(le) // 2 - 1] + le[len(le) // 2]) / 2
                    rec["past_flag"] = abs(math.log(est) - m) > LN2
                    rec["past_refs"] = [x["run_id"] for x in earlier]
                else:
                    rec["past_flag"] = None
                ly = r.get("last_year")
                rec["last_year_flag"] = (max(est / float(ly), float(ly) / est) > GATE_RATIO) if ly else None
            recs.append(rec)
        sc = [x for x in recs if x["scorable"]]
        est_ = [x for x in sc if x["has_estimate"]]
        bad = [x for x in est_ if x["catastrophic"]]
        good = [x for x in est_ if not x["catastrophic"]]
        out = {"n_runs": len(recs), "n_scorable": len(sc), "n_questions_scorable": len({x["qid"] for x in sc}),
               "n_no_estimate": len(sc) - len(est_)}
        k = len(bad)
        out["a_catastrophic"] = {"k": k, "n": len(est_), "rate": round(k / len(est_), 4) if est_ else None,
                                 "cp95": cp(k, len(est_)) if est_ else None, "upper95": upper95(k, len(est_)) if est_ else None,
                                 "questions_with_catastrophic": len({x["qid"] for x in bad}),
                                 "questions": len({x["qid"] for x in est_})}
        for name, key in (("b_gate", "gate_flag"), ("c_past_only_flag", "past_flag"), ("secondary_last_year", "last_year_flag")):
            g = [x for x in good if x.get(key) is not None]
            b = [x for x in bad if x.get(key) is not None]
            fa = sum(bool(x[key]) for x in g)
            ca = sum(bool(x[key]) for x in b)
            out[name] = {"false_alarms": fa, "n_good": len(g), "fa_upper95": upper95(fa, len(g)) if g else None,
                         "fa_cp95": cp(fa, len(g)) if g else None, "catches": ca, "n_bad": len(b)}
        return out, recs

    prim, prim_rows = evaluate([p["run_id"] for p in pros])
    sec, sec_rows = evaluate([r for r in SECONDARY if r in rows])
    g = prim["b_gate"]
    reading = ("supports C2 for the gate row (the archive-tuned 2x band did not transfer)"
               if g["false_alarms"] >= 1 or g["catches"] < g["n_bad"] else
               "cuts against C2 for the gate row (no false alarm and every catastrophic run caught on unseen runs; "
               "report the exact upper bound)")
    res = {"statement": "PREREG.md section F (frozen 2026-11-27)", "primary": prim, "secondary_v29a_think": sec,
           "pre_registered_reading_gate": reading, "rows": prim_rows, "secondary_rows": sec_rows}
    (PREREG / "o2" / "o2_results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if "rows" not in k}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
