"""打印一次 agent 运行的方法、输入、假设、裁判修正记录（只读 state.json，不发请求）。
用法：python probes/inspect_run.py <question_id> <tag>
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
qid, tag = sys.argv[1], sys.argv[2]
s = json.loads((Path(__file__).resolve().parents[1] / "results" / "agent" / qid / tag / "state.json").read_text(encoding="utf-8"))
pts = {p["id"]: p for p in s["points"]}
r = s["compute"]["result"]
print(f"== {qid} [{tag}] central {r.get('central')} p10 {r.get('p10')} p90 {r.get('p90')} basis {r.get('basis')} weights {r.get('weights')}")
print(f"   points {len(pts)}, kept {sum(1 for p in pts.values() if p.get('keep'))}")
for jr in s.get("judge_rounds") or []:
    rep = jr.get("repair")
    print(f"   judge round {jr.get('round')}: methods {len(jr.get('methods') or [])}, repair {'yes' if rep else 'no'}")
    if rep:
        print("     errors:", json.dumps(rep.get("errors"), ensure_ascii=False)[:500])
        print("     after :", json.dumps(rep.get("errors_after"), ensure_ascii=False)[:300])
for m in s["compute"]["methods"]:
    print(f"   M {m['id']} {m['method']} est {m.get('estimate')} err {m.get('error')}")
    print(f"     params {json.dumps(m.get('params'), ensure_ascii=False)[:240]}")
    for d in m.get("inputs_detail") or []:
        p = pts.get(d["id"])
        print(f"     - {d['name']}={d['id']} [{d['kind']}] unit={d.get('unit')!r}",
              (p["name"][:70], p["value"], p.get("period_end")) if p else "")
    if m.get("target_series"):
        print(f"     target_series {m['target_series']}")
for a in (s.get("assumptions") or {}).get("kept") or []:
    print(f"   A {a['id']} {a['name'][:80]} = {a['value']} [{a['low']}, {a['high']}] {a['unit']} used_by {a.get('used_by')}")
for a in (s.get("assumptions") or {}).get("rejected") or []:
    print(f"   REJ {a.get('id')} {a.get('name', '')[:70]}: {a.get('reason')}")
