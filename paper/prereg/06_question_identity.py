"""Pre-registration check (read-only): does the question bank (triangulate/forecast.py) at each worktree commit give the
same question text and as_of as the archive run being repeated? forecast.py is taken with `git show` and executed with
its package imports stubbed out (no package import, no key, no model call). Pool A: HEAD vs the reference runs.
Writes nothing except this script's stdout (tee'd to 06_question_identity_log.txt)."""
import json, re, subprocess, types
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def show(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
def load_questions(rev):
    src = show(rev, "triangulate/forecast.py")
    # drop the package-relative imports; give their names dummy values (only used inside functions)
    names = set()
    keep = []
    for line in src.splitlines():
        m = re.match(r"\s*from \.[\w.]* import (.+)", line)
        if m:
            names |= {n.strip().split(" as ")[-1] for n in m.group(1).replace("(", "").replace(")", "").split(",") if n.strip()}
            continue
        keep.append(line)
    g = {n: None for n in names}
    g["__name__"] = "forecast_snapshot"
    class _P:   # stand-in for config paths (RESULTS / "forecast" etc.)
        def __truediv__(self, o): return self
    for n in ("RESULTS", "GRAPHS", "ROOT", "DATA"):
        if n in g: g[n] = _P()
    exec(compile("\n".join(keep), f"{rev}:forecast.py", "exec"), g)
    return g
def state(run_id):
    return json.loads((ROOT / "results/agent" / run_id / "state.json").read_text(encoding="utf-8"))
POOL_B = [("2bbe8ae", "fc_jnto_2026_08/v21_noown"), ("2bbe8ae", "fc_kr_births_2026_07/v21"),
          ("2bbe8ae", "fc_kr_births_2026_07/v21_noown"), ("2bbe8ae", "fc_yell_2026_09/v21_noown"),
          ("66e70a8", "fc_jnto_2026_08/v21b"), ("48e6b45", "fc_de_cars_2026_09/test2"),
          ("8e3b64e", "fc_de_cars_2026_09/v211_reg"), ("8e3b64e", "fc_lhr_pax_2026_09/v211_reg"),
          ("8e3b64e", "fc_jp_movers_2026_08/v211_reg"), ("1ff32f6", "fc_de_cars_2026_09/v211g_reg"),
          ("cf3413e", "fc_us_retail_2026_06/test3"), ("31e0021", "fc_de_cars_2026_09/v216_reg")]
print("[B] pool B: question bank at the worktree commit vs the archive run")
cache = {}
for rev, rid in POOL_B:
    g = cache.setdefault(rev, load_questions(rev))
    st = state(rid)
    q = next((x for x in g["QUESTIONS"] if x["id"] == st["qid"]), None)
    same_q = q is not None and q.get("question") == st["question"]
    same_a = q is not None and q.get("as_of") == st["as_of"]
    print(f"   {rev} {rid:34s} question identical={same_q} as_of identical={same_a} leak_values={q.get('leak_values') if q else None!s:.60}")
print("[A] pool A: HEAD question bank vs every archive run of the question (count of runs with identical question+as_of)")
g = load_questions("HEAD")
by = {x["id"]: x for x in g["QUESTIONS"]}
import csv
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
scored_q = sorted({r["qid"] for r in rows if r["scored"] == "True"})
for qid in scored_q:
    q = by[qid]
    if q.get("question") is None:   # test4: question_template + as_of of the archive runs
        st = state(f"{qid}/test4")
        q = g["with_as_of"](q, st["as_of"])
    rs = [r for r in rows if r["qid"] == qid and r["has_truth"] == "True"]
    same = [r["run_id"] for r in rs if (lambda s: s["question"] == q["question"] and s["as_of"] == q["as_of"])(state(r["run_id"]))]
    v217 = [r["run_id"] for r in rs if r["code_version"] == "v2.17a" and r["thinking"] == "False"]
    v217_same = [x for x in v217 if x in same]
    print(f"   {qid:24s} as_of={q['as_of']} runs={len(rs):2d} identical={len(same):2d} v2.17a-off runs={v217} identical={v217_same}")
