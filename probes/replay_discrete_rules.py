"""离线重放：FOMC 离散运行（results/agent/ask_0e2d5021/discrete*）每一轮裁判回复（含修正前的原始方法），
用当前代码的 discrete.run 重算每个方法（错误或分布），再算几道审查意见里构造的例子。不调模型、不联网。

用法：.venv/Scripts/python.exe probes/replay_discrete_rules.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import discrete as D  # noqa: E402

RUN_DIR = ROOT / "results" / "agent" / "ask_0e2d5021"


def show(tag: str, methods: list, assumptions: list, pts: dict, target: dict):
    out = D.run(methods, pts, target, AS.validate(assumptions or [], target))
    for m in out["methods"]:
        if m.get("error"):
            print(f"  {tag} {m['id']}: ERROR {m['error'][:230]}")
        else:
            top = max(m["distribution"], key=m["distribution"].get)
            print(f"  {tag} {m['id']}: ok, points {m['n_point_inputs']}, assumptions {m['n_assumption_inputs']}, "
                  f"top {top} {100 * m['distribution'][top]:.1f}%")
    r = out["result"]
    print(f"  {tag} pooled: {r['most_likely']} ({'n/a' if r['most_likely_prob'] is None else f'{100 * r['most_likely_prob']:.1f}%'})")
    return out


def main():
    states = {}
    for d in sorted(RUN_DIR.glob("discrete*")):
        st = json.loads((d / "state.json").read_text(encoding="utf-8"))
        states[d.name] = st
        pts, target = {p["id"]: p for p in st["points"]}, st["plan"]["target"]
        print(f"== {d.name}: outcomes {[o['label'] for o in target['outcomes']]}")
        for jr in st["judge_rounds"]:
            rep = jr.get("repair") or {}
            if rep.get("previous_methods") is not None:
                show(f"r{jr['round']} before repair", rep["previous_methods"], rep.get("previous_assumptions"), pts, target)
            if jr.get("methods"):
                show(f"r{jr['round']}", jr["methods"], jr.get("assumptions"), pts, target)
    # 审查意见里构造的例子
    st = states["discrete4"]
    pts, target = {p["id"]: p for p in st["points"]}, st["plan"]["target"]
    labels = [o["label"] for o in target["outcomes"]]
    print("== constructed (discrete4 points)")
    show("level/change points", [{"method": "outcome_probs", "params": {"probs": {labels[1]: {"id": "p95", "role": "r"},
                                                                                     labels[2]: {"id": "p117", "role": "r"}},
                                                                           "remainder": labels[0]}}], [], pts, target)
    st = states["discrete2"]
    pts, target = {p["id"]: p for p in st["points"]}, st["plan"]["target"]
    print("== constructed (discrete2 points): m1 = {4.25%: p22}, remainder 3.25%")
    show("remainder", [{"method": "outcome_probs", "params": {"probs": {"4.25%": {"id": "p22", "role": "r"}},
                                                              "remainder": "3.25%"}}], [], pts, target)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
