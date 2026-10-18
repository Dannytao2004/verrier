"""冒烟测试结果速览：每道题的单位、方法（单位换算、覆盖范围、出错原因）、合并结果、最终文字。离线，只读 results/ 和 probes/out/smoke/。"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for qid in sys.argv[1:] or ["smoke_pizza", "smoke_tdr", "smoke_nyc", "smoke_tea"]:
    s = json.loads((ROOT / "results/agent" / qid / "smoke1/state.json").read_text(encoding="utf-8"))
    t = s["plan"]["target"]
    print(f"===== {qid}  unit={t.get('unit')!r} canonical={t.get('unit_canonical')!r}  wall={s.get('wall_s')}s usd={s.get('budget', {}).get('usd')}")
    print("  published:", json.dumps(s.get("published"), ensure_ascii=False)[:300])
    c = s["compute"] or {}
    print("  methods_from_round", c.get("methods_from_round"), "rounds", len(s["judge_rounds"]))
    for m in c.get("methods", []):
        print(f"  - {m.get('id')} est={m.get('estimate')} cov={json.dumps(m.get('coverage'))} uc={m.get('unit_check')} err={str(m.get('error') or '')[:300]}")
    r = c.get("result") or {}
    print("  result:", {k: r.get(k) for k in ("central", "p10", "p90", "weights", "basis", "assumption_weight_share")})
    f = s.get("final") or {}
    print("  final:", (f.get("text") if isinstance(f, dict) else str(f))[:900] if f else None)
