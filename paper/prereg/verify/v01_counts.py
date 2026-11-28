"""v_prereg check 1: independent recount of the scored questions, catastrophic runs, versions, thinking and
same-configuration status from the frozen paper/analysis/data/runs.csv; cross-check against paper/prereg/runs.json.
Offline, read-only."""
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("D:/triangulate-agent")
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
print("[0] runs.csv rows:", len(rows))
T = lambda v: str(v).strip().lower() == "true"
scored = [r for r in rows if T(r["scored"])]
print("[1] scored runs:", len(scored), " questions:", len({r["qid"] for r in scored}))
qs = sorted({r["qid"] for r in scored})
print("    ", qs)

# catastrophic: recompute from abs_ln_err as well as the stored flag
def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None
cat_flag = [r for r in scored if T(r["catastrophic"])]
cat_re = [r for r in scored if f(r["abs_ln_err"]) is not None and f(r["abs_ln_err"]) > math.log(2)]
print("[2] catastrophic (flag):", len(cat_flag), " (recomputed |ln err|>ln2):", len(cat_re),
      " same set:", {r["run_id"] for r in cat_flag} == {r["run_id"] for r in cat_re})
print("    questions with a catastrophic run:", len({r["qid"] for r in cat_flag}))
for r in sorted(cat_flag, key=lambda r: (r["qid"], r["started_at"])):
    print(f"    {r['run_id']:45s} ver={r['code_version']:22s} commit={r['code_commit'][:10]} think={r['thinking']:5s} "
          f"noown={r['noown']:5s} conf={r['version_confidence'][:30]:30s} ln_err={f(r['ln_err']):+.3f} "
          f"n_same_cfg_scored={r['n_same_config_scored_on_question']} key={r['config_key']}")

# scored with estimate / no estimate
est = [r for r in scored if T(r["has_estimate"])]
print("[3] scored with estimate:", len(est), " without:", len(scored) - len(est))

# config cells over scored runs
cells = Counter(r["config_key"] + "||" + r["qid"] for r in scored)
print("[4] scored (question, config) cells:", len(cells), " size distribution:", Counter(cells.values()))
for k, v in cells.items():
    if v > 1:
        print("     multi:", k, v)

# thinking settings across scored
print("[5] thinking among scored:", Counter(r["thinking"] for r in scored))
print("    model among scored:", Counter(r["model"] for r in scored))

# runs.json cross-check
rj = json.load(open(ROOT / "paper/prereg/runs.json", encoding="utf-8"))
A = [o for o in rj if o["pool"] == "A"]
B = [o for o in rj if o["pool"] == "B"]
print("[6] runs.json:", len(rj), " A:", len(A), " B:", len(B))
print("    pool A questions == scored questions:", sorted({o["qid"] for o in A}) == qs,
      " repeats per question:", Counter(Counter(o["qid"] for o in A).values()))
print("    pool A thinking:", Counter(o["thinking"] for o in A), " noown:", Counter(o["noown"] for o in A),
      " versions:", Counter(o["code_version"] for o in A))
print("    pool A tags per round:", sorted(Counter((o["round"], o["tag"]) for o in A).items()))
bref = Counter(o["reference_run"] for o in B)
print("    pool B reference runs (n repeats):", dict(bref))
cat_ids = {r["run_id"] for r in cat_flag}
print("    pool B refs all catastrophic:", set(bref) <= cat_ids, " catastrophic not in pool B:", sorted(cat_ids - set(bref)))
by_id = {r["run_id"]: r for r in rows}
print("[7] pool-B same-configuration check (runs.json vs runs.csv reference row)")
for ref in sorted(bref):
    r = by_id[ref]
    os_ = [o for o in B if o["reference_run"] == ref]
    for o in os_:
        ok_think = (str(o["thinking"]).lower() == r["thinking"].lower())
        ok_noown = (str(o["noown"]).lower() == r["noown"].lower())
        ok_commit = r["code_commit"][:7] in (o["code_commit"][:7], o["tree_commit"][:7])
        print(f"    {ref:40s} tag={o['tag']:22s} r{o['round']} think {o['thinking']}/{r['thinking']} ok={ok_think} "
              f"noown {o['noown']}/{r['noown']} ok={ok_noown} code {o['code_commit'][:7]}/{r['code_commit'][:10]} "
              f"ok={ok_commit} ver {o['code_version']}/{r['code_version']} model={r['model']}")
# tags unique per qid
pairs = Counter((o["qid"], o["tag"]) for o in rj)
print("[8] duplicate (qid, tag):", [k for k, v in pairs.items() if v > 1])
pairs2 = Counter((o["qid"], o["rerun_tag"]) for o in rj)
print("    duplicate (qid, rerun_tag):", [k for k, v in pairs2.items() if v > 1])
# collision with existing archive dirs
exist = [f"{o['qid']}/{t}" for o in rj for t in (o["tag"], o["rerun_tag"]) if (ROOT / "results/agent" / o["qid"] / t).exists()]
print("    batch tags already present in results/agent:", exist)
# rounds
print("[9] per round:", sorted(Counter((o["round"], o["pool"]) for o in rj).items()))
for rnd in (1, 2, 3):
    m = sorted([o for o in rj if o["round"] == rnd], key=lambda o: o["order_in_round"])
    print(f"    round {rnd}: order_in_round 1..{len(m)} contiguous:",
          [o["order_in_round"] for o in m] == list(range(1, len(m) + 1)))
# tags vs ablation: noown tags end with _noown
print("[10] noown tag suffix ok:", all(o["tag"].endswith("_noown") == bool(o["noown"]) for o in rj),
      all(o["rerun_tag"].endswith("_noown") == bool(o["noown"]) for o in rj))
print("     B tags:", sorted({o["tag"] for o in B}))
print("     B rerun tags:", sorted({o["rerun_tag"] for o in B}))
# v2.17a archive runs with thinking off (drift anchor)
v217 = [r for r in scored if r["code_version"].startswith("v2.17a")]
print("[11] scored runs on v2.17a*:", len(v217))
for r in v217:
    print(f"     {r['run_id']:40s} think={r['thinking']} noown={r['noown']} est={r['has_estimate']} started={r['started_at']} ver={r['code_version']}")
# as-is tail rate 11/108 check context: scored with estimate
print("[12] catastrophic among scored with estimate:", sum(T(r['catastrophic']) for r in est), "/", len(est))
# questions with >= 3 scored runs, and >= 2 core estimates
per_q = defaultdict(list)
for r in est:
    per_q[r["qid"]].append(r)
print("     questions with >=3 scored estimates:", sum(len(v) >= 3 for v in per_q.values()),
      " >=2 core estimates:", sum(sum(not T(x['catastrophic']) for x in v) >= 2 for v in per_q.values()))
per_q_all = Counter(r["qid"] for r in scored)
print("     questions with >=3 scored runs (any):", sum(v >= 3 for v in per_q_all.values()))
