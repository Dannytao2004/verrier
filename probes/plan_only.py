"""只跑 plan 节点（当前 prompt）：开发集 4 题 + 留出测试 3 题（triangulate/forecast.py），看规划给的 outcome_type。
图跑到 approve 的 interrupt 就停（不搜索、不抽取、不裁判）。allow_discrete 设成 True，记录的是规划模型自己的选择，
不被「有真值的题只认 continuous」那条代码规则改写。每题一次 plan 调用，计量写 calls.jsonl。

用法：TRIANGULATE_KEY_FILE=... .venv/Scripts/python.exe probes/plan_only.py <输出目录>
"""
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent.graph import build  # noqa: E402
from triangulate.agent.pipeline import Context  # noqa: E402
from triangulate.agent.run import initial_input  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402


def plan_one(q: dict, out_dir: Path) -> dict:
    ctx = Context(q["id"], q["question"], q["as_of"], out_dir / "calls.jsonl")
    ctx.allow_discrete = True
    g = build(ctx)
    cfg = {"configurable": {"thread_id": f"plan-{q['id']}"}}
    t0 = time.time()
    out = g.invoke(initial_input(q), cfg)
    st = dict(g.get_state(cfg).values)
    t = (st.get("plan") or {}).get("target") or {}
    return {"id": q["id"], "set": q.get("set", "dev"), "interrupted_at_approve": bool(out.get("__interrupt__")),
            "outcome_type": t.get("outcome_type"), "outcome_kind": t.get("outcome_kind"), "target_keys": sorted(t),
            "what": t.get("what"), "unit": t.get("unit"), "plan_notes": st.get("plan_notes"), "aborted": st.get("aborted"),
            "usd": ctx.budget.snapshot()["usd_total_assumed"], "wall_s": round(time.time() - t0, 1)}


def main():
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(len(QUESTIONS)) as ex:
        rows = list(ex.map(lambda q: plan_one(q, out_dir), QUESTIONS))
    summary = {"n": len(rows), "all_continuous": all(r["outcome_type"] == "continuous" for r in rows),
               "usd_total": round(sum(r["usd"] for r in rows), 4), "rows": rows}
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r['set']:4s} {r['id']:22s} outcome_type={r['outcome_type']} kind={r['outcome_kind']!r} usd={r['usd']} "
              f"wall={r['wall_s']}s notes={r['plan_notes']}")
    print(f"all_continuous={summary['all_continuous']} usd_total={summary['usd_total']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
