"""v2.8e：在已存的冒烟运行上重放单位核对（三个核对 + 裁定，真模型）。裁判方法取 compute 用的那一轮，代码试跑用当前代码；
打印每个方法裁判写的单位、裁定的单位、核对前后的估计，全部回答存进 probes/out/unit_review/replay.json。不写 results/。
用法：.venv/Scripts/python.exe probes/unit_review_replay.py smoke_pizza/smoke2 smoke_pizza/smoke1 ..."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import graph as G  # noqa: E402
from triangulate.agent import unit_review as UR  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget  # noqa: E402

OUT = ROOT / "probes" / "out" / "unit_review"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    llm = AgentLLM(OUT / "calls.jsonl", Budget(usd=5.0))
    dump = {}
    for run in sys.argv[1:]:
        s = json.loads((ROOT / "results" / "agent" / run / "state.json").read_text(encoding="utf-8"))
        t, pts = s["plan"]["target"], s["points"]
        jr = copy.deepcopy(s["judge_rounds"][s["compute"]["methods_from_round"] - 1])
        out0, av, failed = G._code_check(jr, pts, t)
        fails = UR.review(llm, run.replace("/", "_"), jr, out0, av, pts, dict(failed), t)
        out1, _, failed1 = G._code_check(jr, pts, t)
        failed1.update(fails or {})
        print(f"===== {run}  target {t.get('unit_canonical')!r}  period {UR.period_length(t)!r}")
        recs = {r["method"]: r for r in (jr.get("unit_reviews") or [{"methods": []}])[-1]["methods"]}
        for i, (m0, m1) in enumerate(zip(out0["methods"], out1["methods"])):
            r = recs.get(m0["id"])
            if r is None:
                continue
            arb = [a.get("reply", {}).get("result_unit") for a in r["arbiter"]]
            chk = [c.get("reply", {}).get("result_unit") for c in r["checkers"]]
            print(f"  {m0['id']}: judge {r['judge_unit']!r} | checkers {chk} | arbiter tries {arb} -> unit {r.get('unit')!r}")
            print(f"      estimate before {m0.get('estimate')} after {m1.get('estimate')} | failure {failed1.get(i, '')[:160]!r}")
        dump[run] = jr.get("unit_reviews")
    (OUT / "replay.json").write_text(json.dumps(dump, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
