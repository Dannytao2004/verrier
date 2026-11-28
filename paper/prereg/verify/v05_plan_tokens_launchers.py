"""v_prereg: (b) the first 'plan' call's prompt_tokens is deterministic given (code version, question): equal within
every same-configuration archive cell, which makes it a usable request-identity check for the new runs (PREREG E0),
with the reference value of every pool-B original and v2.17a archive run; (c) the launcher of the v2.1* / v2.1b
originals (one process, 8 threads, shared fetch limiter). Read-only (git show, results files)."""
import csv
import glob
import json
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path("D:/triangulate-agent")


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, encoding="utf-8").stdout


def plan_tokens(rid):
    for p in sorted(glob.glob(str(ROOT / "results/agent" / rid / "calls*.jsonl"))):
        for l in open(p, encoding="utf-8"):
            try:
                c = json.loads(l)
            except json.JSONDecodeError:
                continue
            if c.get("arm") == "plan" and c.get("prompt_tokens"):
                return c["prompt_tokens"]
    return None


rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
print("[b] first plan-call prompt_tokens within same-configuration archive cells (thinking-off; version, question)")
g = defaultdict(list)
for r in rows:
    if r["has_truth"] == "True":
        g[(r["qid"], r["config_key"])].append(r["run_id"])
n_cells = n_equal = 0
for k, v in sorted(g.items()):
    if len(v) > 1:
        t = [plan_tokens(x) for x in v]
        n_cells += 1
        n_equal += len(set(t)) == 1
        print(f"    {k[0]:24s} {k[1]:45s} {list(zip(v, t))}")
print(f"    cells with >= 2 runs: {n_cells}; equal plan prompt_tokens: {n_equal}")
print("    reference values for the pool-B cells (original catastrophic run):")
for ref in sorted({o["reference_run"] for o in json.load(open(ROOT / "paper/prereg/runs.json", encoding="utf-8"))
                   if o["pool"] == "B"}):
    print(f"      {ref:36s} plan prompt_tokens = {plan_tokens(ref)}")
print("    v2.17a archive runs (pool-A references):")
for r in rows:
    if r["code_version"] == "v2.17a" and r["thinking"] == "False" and r["has_truth"] == "True":
        print(f"      {r['run_id']:36s} plan prompt_tokens = {plan_tokens(r['run_id'])}")

print("[c] launchers of the v2.1* / v2.1b originals")
for tag in ("v21", "v21_noown", "v21b", "v21b_noown"):
    st = sorted({json.loads(open(p, encoding="utf-8").read())["started_at"]
                 for p in glob.glob(str(ROOT / "results/agent/*" / tag / "state.json"))})
    print(f"    tag {tag:11s}: started_at values {st}")
for lg in ("run_v21.log", "run_v21b.log"):
    lines = (ROOT / "results/agent" / lg).read_text(encoding="utf-8", errors="replace").splitlines()
    print(f"    {lg}: {sum('plan:' in l for l in lines)} plan lines, {sum('done in' in l for l in lines)} 'done in' lines "
          f"(several questions interleaved in one log)")
src = git("show", "2bbe8ae:probes/run_v2_backtests.py")
print("    probes/run_v2_backtests.py at 2bbe8ae uses ThreadPoolExecutor:", "ThreadPoolExecutor" in src,
      "| docstring mentions shared net.LIMITER:", "net.LIMITER" in src)
