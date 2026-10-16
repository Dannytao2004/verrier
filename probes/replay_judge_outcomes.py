"""离线重放（v2.3）：FOMC 运行 discrete4 / discrete5 保存的裁判证据，过一遍「裁判定义结果列表」的新校验。不调模型、不联网。

保存的回复里没有裁判定义的列表（v2.2 由 plan 定），所以只能重放这几件事：
1. 把 plan 当时的列表原样当作裁判的列表（没有 le / ge、没有 outcomes_basis）：新校验怎么说；
2. 同一列表补上两个尾部的 le / ge、依据给第一轮保留的「当前利率」点：新校验怎么说（代码能不能发现列表不含现实的结果）；
3. 按新 prompt 的要求、由第一轮保留的点构造的列表（当前值 ± 一档 + 两个尾部）：校验结果；
4. 保存的第二轮方法（修正前、修正后）对 3 的列表重算：原 label 直接用、和按数值把原 label 换成 3 里包含该数值的结果。
用法：.venv/Scripts/python.exe probes/replay_judge_outcomes.py [输出 json 路径]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import discrete as D  # noqa: E402

RUN_DIR = ROOT / "results" / "agent" / "ask_0e2d5021"
LEVEL = re.compile(r"upper bound", re.I)      # 「当前利率上限」点（名字里带 upper bound、值 4.0、不是预期 / 概率）
PROB = re.compile(r"fedwatch.*probab|probab.*(?:hold|unchanged|hike)", re.I)


def round1_kept(st: dict) -> dict:
    """第一轮裁判看到并保留的点（第一轮的点减去第一轮丢掉的）。"""
    drop = {d["id"] for d in st["judge_rounds"][0].get("decisions") or [] if not d.get("keep", False)}
    return {p["id"]: p for p in st["points"] if p.get("round") == 1 and p["id"] not in drop}


def grounded_list(level: float, step: float = 0.25) -> list:
    """新 prompt 要的形状：当前值、上下各一档，再加两个合并尾部。"""
    lo, hi = level - step, level + step
    return [{"label": f"{lo:.2f}% or lower", "value": lo, "le": lo}, {"label": f"{level:.2f}%", "value": level},
            {"label": f"{hi:.2f}%", "value": hi}, {"label": f"{hi + step:.2f}% or higher", "value": hi + step, "ge": hi + step}]


def relabel(methods: list, old: list, new: list) -> list:
    """按数值把原 label 换成新列表里包含该数值的结果（尾部按 le / ge 认）；找不到就保留原 label。"""
    val = {o["label"]: o.get("value") for o in old}

    def find(v):
        for o in new:
            if v is not None and (o.get("le") is not None and v <= o["le"] or o.get("ge") is not None and v >= o["ge"]
                                  or abs(o["value"] - v) < 1e-9):
                return o["label"]
        return None
    out = []
    for m in methods:
        prm = dict(m.get("params") or {})
        prm["probs"] = {(find(val.get(k)) or k): spec for k, spec in (prm.get("probs") or {}).items()}
        if prm.get("remainder") in val:
            prm["remainder"] = find(val[prm["remainder"]]) or prm["remainder"]
        out.append({**m, "params": prm})
    return out


def run_methods(methods, assumptions, pts, target) -> list:
    out = D.run(methods, pts, target, AS.validate(assumptions or [], target))
    rows = []
    for m in out["methods"]:
        if m.get("error"):
            rows.append({"id": m["id"], "error": m["error"][:300]})
        else:
            rows.append({"id": m["id"], "distribution": {k: round(v, 4) for k, v in m["distribution"].items()}})
    r = out["result"]
    rows.append({"pooled_most_likely": r["most_likely"], "prob": None if r["most_likely_prob"] is None else round(r["most_likely_prob"], 4)})
    return rows


def main():
    report = {}
    for tag in ("discrete4", "discrete5"):
        st = json.loads((RUN_DIR / tag / "state.json").read_text(encoding="utf-8"))
        target, pts = st["plan"]["target"], {p["id"]: p for p in st["points"]}
        k1 = round1_kept(st)
        k_final = {i for i, p in pts.items() if p.get("keep")}
        level_ids = [i for i, p in k1.items() if LEVEL.search(p["name"]) and p["value"] == 4.0 and "xpected" not in p["name"]]
        prob_r1 = [i for i, p in k1.items() if PROB.search(p["name"])]
        plan_list = target["outcomes"]
        rec = {"plan_list": [o["label"] for o in plan_list], "round1_kept": len(k1), "current_level_ids_round1": level_ids,
               "probability_ids_round1": prob_r1}
        # 1. plan 的列表原样
        rec["1_plan_list_as_is"] = D.validate_outcomes(plan_list, None, set(k1))[2]
        # 2. 补上尾部和依据
        tails = [dict(o) for o in plan_list]
        tails[0]["le"], tails[-1]["ge"] = tails[0]["value"], tails[-1]["value"]
        rec["2_plan_list_with_tails_and_basis"] = D.validate_outcomes(tails, {"ids": level_ids}, set(k1))[2]
        # 3. 按证据构造的列表
        g = grounded_list(4.0)
        basis = {"ids": level_ids + prob_r1}
        rec["3_grounded_list"] = [o["label"] for o in g]
        rec["3_grounded_list_errors_round1"] = D.validate_outcomes(g, basis, set(k1))[2]
        rec["3_basis_ids_still_kept_after_round2"] = [i for i in basis["ids"] if i in k_final]
        t_new = {**{k: v for k, v in target.items() if k != "outcomes"}, "outcomes": g}
        # 4. 保存的第二轮方法对构造的列表重算
        j2 = st["judge_rounds"][-1]
        rep = j2.get("repair") or {}
        variants = {"r2_final": (j2.get("methods") or [], j2.get("assumptions"))}
        if rep.get("previous_methods") is not None:
            variants["r2_before_repair"] = (rep["previous_methods"], rep.get("previous_assumptions"))
        for name, (ms, av) in variants.items():
            rec[f"4_{name}_original_labels"] = run_methods(ms, av, pts, t_new)
            rec[f"4_{name}_relabelled_by_value"] = run_methods(relabel(ms, plan_list, g), av, pts, t_new)
        report[tag] = rec
    txt = json.dumps(report, indent=1, ensure_ascii=False)
    print(txt)
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(txt + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
