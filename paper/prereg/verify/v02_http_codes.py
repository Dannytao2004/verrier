"""v_prereg: which HTTP status codes and call errors appear in the archive's calls*.jsonl, and in runs with/without an
estimate? Tests whether run_repeats.classify_infra would call archive runs infrastructure failures that are outcomes.
Also applies classify_infra itself (imported from the runner, offline) to every archive run dir. Read-only."""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("D:/triangulate-agent")
sys.path.insert(0, str(ROOT / "paper" / "_tools"))
import run_repeats as RR  # noqa: E402  (module import only: no main(), no model call)

dirs = sorted(p.parent for p in (ROOT / "results" / "agent").rglob("state.json"))
print("[0] run dirs with state.json:", len(dirs))
codes = Counter()
by_code_est = defaultdict(Counter)
errs = Counter()
cls = Counter()
cls_est = defaultdict(list)
for d in dirs:
    st = json.loads((d / "state.json").read_text(encoding="utf-8"))
    has_est = ((st.get("compute") or {}).get("result") or {}).get("central") is not None
    calls = RR.read_calls(d)
    seen = set()
    for c in calls:
        h = c.get("http")
        if h is not None:
            codes[h] += 1
            seen.add(h)
        if c.get("error"):
            errs[str(c.get("error"))[:40]] += 1
    for h in seen:
        by_code_est[h]["with_est" if has_est else "no_est"] += 1
    k = RR.classify_infra(d, 0, "", False)
    cls[k] += 1
    if k:
        cls_est[k].append((str(d.relative_to(ROOT / "results" / "agent")), has_est))
print("[1] http codes over all calls:", dict(codes))
print("[2] runs containing each http code, by estimate:", {k: dict(v) for k, v in by_code_est.items()})
print("[3] call error strings:", errs.most_common(25))
print("[4] classify_infra over archive dirs:", dict(cls))
for k, v in cls_est.items():
    print(f"    {k}: {len(v)} runs, with estimate {sum(e for _, e in v)}")
    for rid, e in v[:40]:
        print(f"       {rid}  has_estimate={e}")
