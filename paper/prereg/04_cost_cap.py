"""Pre-registration cost facts (read-only): token fees, assumed search fees, usd cap and cap aborts per code version;
searcher-call token usage before / after DeepSeek's 2026-11-18 12:00 Beijing (04:00 UTC) billing change.
Reads runs.csv, state.json budget blocks and calls.jsonl usd fields. No outcome of the planned analyses is computed."""
import csv, json, statistics as S
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
CHANGE = "2026-11-18T04:00:00+00:00"
VERS = ["v2.1*", "v2.1b", "v2.1c-pre", "v2.1c", "v2.8r", "v2.11f", "v2.11g", "v2.12a", "v2.13b", "v2.14a", "v2.15g", "v2.16e", "v2.17a"]
print("[1] per code version (deepseek-flash, non-web CLI runs): n, usd_tokens median/max, usd_total max, usd_cap values, cap aborts, wall_s median/max")
for v in VERS:
    rs = [r for r in rows if r["code_version"] == v and r["model"] == "deepseek-flash" and not r["dir_tag"].startswith("web_")]
    caps, aborts = set(), []
    for r in rs:
        st = json.loads((ROOT / "results/agent" / r["run_id"] / "state.json").read_text(encoding="utf-8"))
        b = st.get("budget") or {}
        caps.add(b.get("usd_cap"))
        a = str(b.get("aborted") or st.get("aborted") or "")
        if "usd cap" in a:
            aborts.append((r["run_id"], a[:90]))
    tok = [float(r["usd_tokens"]) for r in rs if r["usd_tokens"]]
    tot = [float(r["usd_total"]) for r in rs if r["usd_total"]]
    wall = [float(r["wall_s"]) for r in rs if r["wall_s"]]
    print(f"   {v:10s} n={len(rs):2d} tok_med={S.median(tok) if tok else None} tok_max={max(tok) if tok else None} "
          f"total_max={max(tot) if tot else None} caps={sorted(c for c in caps if c is not None)} cap_aborts={aborts} "
          f"wall_med={S.median(wall) if wall else None} wall_max={max(wall) if wall else None}")
print("[2] all deepseek CLI runs with a 'usd cap' abort anywhere in the archive")
n = 0
for r in rows:
    if "usd cap" in (r["aborted_reason"] or "") and not r["dir_tag"].startswith("web_"):
        n += 1; print("   ", r["run_id"], r["code_version"], r["aborted_reason"][:120])
print("   count", n)
print("[3] searcher calls (kind == search, ok) in post_v2.13b_3x12 runs: per-call input+cache tokens and usd, before vs after the billing change")
grp = defaultdict(list)
for r in rows:
    if r["search_regime"] != "post_v2.13b_3x12" or r["model"] != "deepseek-flash":
        continue
    p = ROOT / "results/agent" / r["run_id"] / "calls.jsonl"
    if not p.exists():
        continue
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            c = json.loads(line)
        except Exception:
            continue
        if c.get("kind") == "search" and c.get("ok"):
            k = "after" if c["at"] >= CHANGE else "before"
            grp[k].append((c.get("input_tokens", 0) + c.get("cache_read_input_tokens", 0), c.get("usd", 0), c.get("web_search_requests", 0)))
for k, v in grp.items():
    print(f"   {k}: n_calls={len(v)} median_tokens={S.median(x[0] for x in v)} median_usd={S.median(x[1] for x in v)} "
          f"median_searches={S.median(x[2] for x in v)} max_usd={max(x[1] for x in v)}")
print("[4] v2.17a + v2.16e regression runs (tag v216_reg*, results/agent/*/v216_reg*/calls.jsonl): token fee = sum(usd), wall_s, searches")
fees, walls, srch = [], [], []
for r in rows:
    if r["tag"].startswith("v216_reg") and r["model"] == "deepseek-flash":
        p = ROOT / "results/agent" / r["run_id"] / "calls.jsonl"
        cs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
        fee = sum(float(c.get("usd") or 0) for c in cs)
        ns = sum(int(c.get("web_search_requests") or 0) for c in cs if c.get("kind") == "search")
        fees.append(fee); walls.append(float(r["wall_s"] or 0)); srch.append(ns)
        print(f"   {r['run_id']:42s} ver={r['code_version']:7s} think={r['thinking']:5s} fee={fee:.4f} wall_s={r['wall_s']} searches={ns} usd_total={r['usd_total']}")
print(f"   n={len(fees)} fee median={S.median(fees):.4f} max={max(fees):.4f} sum={sum(fees):.4f}; wall median={S.median(walls)/60:.1f} min max={max(walls)/60:.1f} min; searches median={S.median(srch)}")
print("[5] deepseek CLI runs (non-web) by recorded usd_cap: count, max usd_total (cap aborts: see [2], 0)")
caps = defaultdict(list)
for r in rows:
    if r["model"] != "deepseek-flash" or r["dir_tag"].startswith("web_"):
        continue
    st = json.loads((ROOT / "results/agent" / r["run_id"] / "state.json").read_text(encoding="utf-8"))
    caps[(st.get("budget") or {}).get("usd_cap")].append((float(r["usd_total"] or 0), r["run_id"]))
for c, v in sorted(caps.items(), key=lambda kv: str(kv[0])):
    print(f"   usd_cap={c}: n={len(v)} max usd_total={max(v)[0]} ({max(v)[1]})")
