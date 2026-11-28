"""Builds paper/prereg/runs.json, the frozen run list of the tier-3 repeat batch (pool A + pool B), and checks it.

Read-only inputs: paper/analysis/data/runs.csv (design columns only: qid, code_version, thinking, noown, tag, started_at,
wall_s, scored/catastrophic flags to pick the catastrophic cells), the archive state.json of each reference run (question
text and as_of), read-only git (rev-parse). No model call. Deterministic: the within-round order is a seeded permutation.
Writes runs.json and prints a log (tee'd to 10_build_runs_log.txt).
"""
import csv
import json
import math
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREREG = ROOT / "paper" / "prereg"
WT_BASE = "D:/triangulate-agent-rep"      # proposed location of the old-version worktrees (outside the main checkout)
SEED_BASE = 20261127                      # order of round r = random.Random(SEED_BASE + r).shuffle(...)
MIN_MARGIN_MIN = 20                       # never start a run less than 20 minutes before a DeepSeek peak window
SAFETY = 1.5                              # margin >= 1.5 x the longest archived thinking-off wall time of that code version

rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout.strip()


def state(run_id):
    return json.loads((ROOT / "results/agent" / run_id / "state.json").read_text(encoding="utf-8"))


# ---- code versions: label -> (slug, tree commit the worktree checks out, agent-code commit, note)
# tree commit = the latest commit of any kind before the archive run started (what its working tree held); its agent code
# is byte-identical to the agent-code commit (03_old_versions_log.txt: "agent-code diff code..tree: <none>").
VERSIONS = {
    "v2.17a": ("v217a", "HEAD", "2c69959", "main checkout; triangulate/ differs from tag v2.17a only in two comment lines "
                                           "(forecast.py line 121, showcase_engine.py line 1)"),
    "v2.1*": ("v21s", "2bbe8ae", "2bbe8ae", "untagged commit 'v2.1: allow change factors ...' (before the v2.1 tag's fix)"),
    "v2.1b": ("v21b", "66e70a8", "66e70a8", "tag v2.1b"),
    "v2.8r": ("v28r", "48e6b45", "c64d3a3", "tag v2.8r / frozen-v2.8r = c64d3a3; tree 48e6b45 adds only BUGS.md"),
    "v2.11f": ("v211f", "8e3b64e", "8e3b64e", "tag v2.11f"),
    "v2.11g": ("v211g", "1ff32f6", "1ff32f6", "tag v2.11g"),
    "v2.12a": ("v212a", "cf3413e", "cf3413e", "tag v2.12a"),
    "v2.16e": ("v216e", "31e0021", "b77e098", "tag v2.16e = b77e098; tree 31e0021 adds only probes/run_v216_groups.py"),
}

# ---- margins from the archive's thinking-off CLI wall times per code version
margin = {}
for v in VERSIONS:
    w = [float(r["wall_s"]) for r in rows if r["code_version"] == v and r["thinking"] == "False" and r["wall_s"]
         and r["model"] == "deepseek-flash" and not r["dir_tag"].startswith("web_")]
    margin[v] = max(MIN_MARGIN_MIN, math.ceil(SAFETY * max(w) / 60)) if w else MIN_MARGIN_MIN
    print(f"margin {v:7s}: archived thinking-off wall max {max(w) / 60 if w else float('nan'):5.1f} min (n={len(w)}) -> {margin[v]} min")

# ---- pool A: the 23 scored questions
scored_q = sorted({r["qid"] for r in rows if r["scored"] == "True"})
assert len(scored_q) == 23, len(scored_q)

# ---- pool B: every catastrophic scored run, with a decision per cell
MECH = {
    "fc_jnto_2026_08/v21_noown": "M5 v2.1 wrong input quantity (ratio x flights as level), own-history ablation",
    "fc_kr_births_2026_07/v21": "M5 v2.1 wrong input quantity (YoY increase used as a level)",
    "fc_kr_births_2026_07/v21_noown": "M5 v2.1 wrong input quantity (growth rate used as a level), own-history ablation",
    "fc_yell_2026_09/v21_noown": "M5 v2.1 wrong input quantity (share used as a level), own-history ablation",
    "fc_jnto_2026_08/v21b": "M6 single assumption-only route (BUGS A2)",
    "fc_kr_births_2026_07/v21c": "M7 v2.1c-pre averaging with a 7x-off assumption route",
    "fc_de_cars_2026_09/test2": "M1 S24 German '.' thousands separator read as a decimal point",
    "fc_de_cars_2026_09/v211_reg": "M1 S24 German '.' thousands separator read as a decimal point",
    "fc_de_cars_2026_09/v216_reg": "M1 S24 German '.' thousands separator read as a decimal point",
    "fc_de_cars_2026_09/v211g_reg": "M4 S72 constant cancelled inside the formula (x12/12)",
    "fc_lhr_pax_2026_09/v211_reg": "M3 S60 year-to-month conversion applied twice",
    "fc_jp_movers_2026_08/v211_reg": "M3 S60 year-to-month conversion applied twice",
    "fc_us_retail_2026_06/test3": "M2 S66 multiplier ('millions of USD') left in the point unit",
    "fc_cn_profits_2026_09/test4": "M2 S66 multiplier (亿元) left in the point unit",
}
EXCLUDED = {
    "fc_kr_births_2026_07/v21c": "not re-runnable as the same configuration: the run started on an uncommitted working tree "
                                 "(f5fe773 + unknown edits; DATA_NOTES.md section 9 override, check/CHECK.md fix F2)",
    "fc_cn_profits_2026_09/test4": "not re-runnable as the same configuration: the archive run was real-use mode on its own "
                                   "day (as_of 2026-10-24, 40 live-dated pages, 0 snapshots); any run now with as_of "
                                   "2026-10-24 is a backtest (Wayback snapshots only), i.e. a fetch-mode toggle",
}
cat = sorted([r for r in rows if r["scored"] == "True" and r["catastrophic"] == "True"], key=lambda r: (r["qid"], r["started_at"]))
assert len(cat) == 14 and len({r["qid"] for r in cat}) == 8
cells_b = [r for r in cat if r["run_id"] not in EXCLUDED]
print("pool B cells:", len(cells_b), "excluded:", list(EXCLUDED))
for r in cat:
    assert r["thinking"] == "False", r["run_id"]

runs = []


def add(pool, qid, version, noown, rnd, rep, purpose, ref=None, mech=None):
    slug, tree, code, _ = VERSIONS[version]
    base = f"rep217a_r{rep}" if pool == "A" else f"repB_{slug}_r{rep}"
    tag = base + ("_noown" if noown else "")
    rerun = base + "_rerun" + ("_noown" if noown else "")
    q = next(x for x in rows if x["qid"] == qid)
    test4 = q["set"] == "test4"
    o = {"qid": qid, "code_version": version, "thinking": False, "round": rnd, "tag": tag, "purpose": purpose,
         "pool": pool, "repeat_index": rep, "cell_id": f"{qid}|{version}|think=False|noown={noown}",
         "noown": noown, "slug": slug, "tree_commit": git("rev-parse", tree + "^{commit}") if tree != "HEAD" else "HEAD",
         "code_commit": git("rev-parse", code + "^{commit}"),
         "code_root_hint": str(ROOT).replace("\\", "/") if version == "v2.17a" else f"{WT_BASE}/{slug}",
         "cli_mode": "ask" if test4 else "question", "reference_run": ref, "mechanism": mech,
         "margin_min": margin[version], "rerun_tag": rerun}
    if test4:   # test4 questions have no fixed as_of / question in forecast.py: repeat the archive runs' exact text
        st = state(f"{qid}/test4")
        o["as_of"], o["ask_question"] = st["as_of"], st["question"]
    runs.append(o)


for rep in (1, 2, 3):
    for qid in scored_q:
        add("A", qid, "v2.17a", False, rep, rep,
            f"pool A: same-configuration repeat {rep} of 3 on frozen v2.17a, thinking off (repeat floor; same-config "
            f"counterparts of the as-is statistics; drift anchor)")
for rep in (1, 2):
    for r in cells_b:
        add("B", r["qid"], r["code_version"], r["noown"] == "True", rep, rep,
            f"pool B: same-configuration repeat {rep} of 2 of catastrophic run {r['run_id']} on its own code version "
            f"{r['code_version']} (recurrence; regression to the mean)", ref=r["run_id"], mech=MECH[r["run_id"]])

# ---- within-round order: seeded permutation
for rnd in (1, 2, 3):
    rr = [o for o in runs if o["round"] == rnd]
    rr.sort(key=lambda o: (o["pool"], o["qid"], o["code_version"], o["noown"]))
    random.Random(SEED_BASE + rnd).shuffle(rr)
    for i, o in enumerate(rr, 1):
        o["order_in_round"] = i
runs.sort(key=lambda o: (o["round"], o["order_in_round"]))

# ---- checks
tags = [(o["qid"], o["tag"]) for o in runs] + [(o["qid"], o["rerun_tag"]) for o in runs]
assert len(tags) == len(set(tags)), "duplicate (qid, tag)"
for qid, tag in tags:
    assert not (ROOT / "results/agent" / qid / tag).exists(), f"collision with an existing run dir: {qid}/{tag}"
for o in runs:   # the noown tags must survive run.ablation_tag unchanged (it appends _noown unless the tag ends with noown)
    assert (not o["noown"]) or (o["tag"].endswith("noown") and o["rerun_tag"].endswith("noown"))
for o in runs:   # the question text and as_of of pool B come from the worktree's own forecast.py (06_question_identity_log.txt)
    if o["pool"] == "B":
        assert o["cli_mode"] == "question"
n = {(p, r): sum(1 for o in runs if o["pool"] == p and o["round"] == r) for p in "AB" for r in (1, 2, 3)}
print("runs per (pool, round):", n, "total", len(runs))
print("pool B cells by version:", {v: sum(1 for c in cells_b if c["code_version"] == v) for v in VERSIONS})
(PREREG / "runs.json").write_text(json.dumps(runs, indent=1, ensure_ascii=False), encoding="utf-8")
(PREREG / "excluded_cells.json").write_text(json.dumps(
    [{"reference_run": k, "mechanism": MECH[k], "reason": v} for k, v in EXCLUDED.items()], indent=1, ensure_ascii=False),
    encoding="utf-8")
(PREREG / "worktrees.json").write_text(json.dumps(
    {v: {"slug": s, "tree_commit": git("rev-parse", t + "^{commit}") if t != "HEAD" else "HEAD",
         "code_commit": git("rev-parse", c + "^{commit}"), "path": str(ROOT).replace("\\", "/") if v == "v2.17a" else f"{WT_BASE}/{s}",
         "note": note, "margin_min": margin[v]} for v, (s, t, c, note) in VERSIONS.items()
     if v == "v2.17a" or any(o["code_version"] == v for o in runs)}, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote runs.json, excluded_cells.json, worktrees.json")
for o in runs:
    print(f"  r{o['round']} #{o['order_in_round']:2d} {o['pool']} {o['qid']:24s} {o['code_version']:7s} noown={o['noown']!s:5s} "
          f"tag={o['tag']:22s} root={o['code_root_hint']} margin={o['margin_min']}")
