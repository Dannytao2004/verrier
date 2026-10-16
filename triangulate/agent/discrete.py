"""离散结果模式（v2.2）：目标只能是几个互斥结果之一（一次会议后的政策利率、选举赢家、是 / 否事件）。

- plan：target 带 outcome_type 和 outcomes（2-10 个，label 唯一，value 是数或 null）；不合格就退回 continuous，原因进 plan_notes。
- 裁判：只能用 outcome_probs，每个结果的概率引用一个保留的数据点或一条假设；可以指定一个结果取「余下的概率」。
- 代码（这里）：% 转小数；每个概率在 [0, 1]；有余下结果时其余之和 <= 1 + SUM_TOL_REMAINDER，余下 = 1 - 和（截到 0）；
  没有余下结果时和必须在 SUM_RANGE 内；最后都归一化到 1。每个结果都要有概率，未知 label 拒绝。
  多个方法等权线性平均（linear pool）；最可能的结果 = 概率最大的（并列时取 plan 里排在前面的）。
- 假设输入用裁判给的 value（离散结果是点分布，不做 Monte Carlo）；low / high 只记录。
连续值模式（compute.run 的其余部分）不经过这里。
"""
import math
import re

from . import compute as C
from .methods import MethodError

MIN_OUTCOMES, MAX_OUTCOMES = 2, 10
SUM_TOL_REMAINDER = 0.02
SUM_RANGE = (0.9, 1.1)
LABEL_CHARS = 80
PCT_UNIT = re.compile(r"%|\bper ?cent\b|\bpercentage\b|\bpct\b", re.I)


def _norm_label(x) -> str:
    return " ".join(str(x if x is not None else "").split())[:LABEL_CHARS]


def _value(v):
    """结果的数值：有限数字（或能解析成数字的字符串）；其余 None。"""
    if isinstance(v, bool):
        return None
    if isinstance(v, str):
        try:
            v = float(v.strip().rstrip("%"))
        except ValueError:
            return None
    if isinstance(v, (int, float)) and math.isfinite(float(v)):
        return float(v)
    return None


def parse_outcomes(raw: dict) -> tuple:
    """plan 回复里的 target -> ({"outcome_type": ..., 离散时另有 "outcomes": [...]}, 说明)。说明为空 = 没有问题。"""
    kind = str((raw or {}).get("outcome_type") or "continuous").strip().lower()
    if kind != "discrete":
        note = "" if kind == "continuous" else f"outcome_type {kind!r} not recognised; treated as continuous"
        return {"outcome_type": "continuous"}, note
    outs, clean, seen, why = (raw or {}).get("outcomes"), [], set(), ""
    if not isinstance(outs, list):
        why = "outcomes is not a list"
    elif not MIN_OUTCOMES <= len(outs) <= MAX_OUTCOMES:
        why = f"{len(outs)} outcomes (need {MIN_OUTCOMES} to {MAX_OUTCOMES})"
    else:
        for o in outs:
            label = _norm_label(o.get("label")) if isinstance(o, dict) else ""
            if not label:
                why = "an outcome has no label"
                break
            if label.casefold() in seen:
                why = f"duplicate outcome label {label!r}"
                break
            seen.add(label.casefold())
            clean.append({"label": label, "value": _value(o.get("value"))})
    if why:
        return {"outcome_type": "continuous"}, f"discrete outcomes rejected ({why}); fell back to continuous"
    return {"outcome_type": "discrete", "outcomes": clean}, ""


def is_discrete(target: dict) -> bool:
    t = target or {}
    return t.get("outcome_type") == "discrete" and len(t.get("outcomes") or []) >= MIN_OUTCOMES


def outcomes_text(target: dict) -> str:
    """给裁判看的结果列表（每行一个 label，带数值和单位）。"""
    unit = (target or {}).get("unit", "")
    return "\n".join(f'- "{o["label"]}"' + ("" if o.get("value") is None else f" (value {o['value']:g} {unit})")
                     for o in (target or {}).get("outcomes") or [])


def _probability(label: str, spec, pts: dict, kept_a: dict, rejected_a: dict) -> dict:
    """一个结果的概率输入 -> 明细（含 prob）。引用规则和 formula_mc 一样：保留的点或通过校验的假设，假设不许复述保留的点。"""
    spec = spec if isinstance(spec, dict) else {"id": spec}
    iid = str(spec.get("id"))
    if iid in kept_a:
        a = kept_a[iid]
        dup = C.restated_point(a, pts)
        if dup:
            raise MethodError(f"outcome {label!r}: assumption {iid} restates kept data point {dup} (same value and unit); "
                              f"reference {dup} instead")
        v, unit, kind = a["value"], a.get("unit") or "", "assumption"
        pct = bool(a.get("is_pct")) or bool(PCT_UNIT.search(unit))
    elif iid in rejected_a:
        raise MethodError(f"outcome {label!r}: assumption {iid} was rejected ({rejected_a[iid]})")
    else:
        p = pts.get(iid)
        if p is None or not p.get("keep", True):
            raise MethodError(f"outcome {label!r}: id {iid} unknown or discarded")
        v, unit, kind = p["value"], p.get("unit") or "", "point"
        pct = bool(PCT_UNIT.search(unit))
    prob = v / 100 if pct else v
    if not (isinstance(prob, (int, float)) and math.isfinite(prob) and 0 <= prob <= 1):
        hint = "" if pct else " (only a unit with % or percent is converted from a percentage)"
        raise MethodError(f"outcome {label!r}: {iid} = {v:g} {unit} is not a probability in [0, 1]{hint}")
    return {"label": label, "id": iid, "kind": kind, "value": v, "unit": unit, "prob": float(prob),
            "role": str(spec.get("role") or "")}


def outcome_probs(prm: dict, pts: dict, kept_a: dict, rejected_a: dict, outcomes: list) -> dict:
    """一个 outcome_probs 方法 -> {distribution, inputs_detail, ...}；不合规则抛 MethodError。"""
    labels = [o["label"] for o in outcomes]
    canon = {lab.casefold(): lab for lab in labels}
    probs = prm.get("probs")
    if not isinstance(probs, dict) or not probs:
        raise MethodError("outcome_probs needs params.probs = {outcome label: {id, role}}")
    rem_raw = prm.get("remainder")
    rem = None
    if rem_raw is not None and _norm_label(rem_raw).lower() not in ("", "null", "none"):
        rem = canon.get(_norm_label(rem_raw).casefold())
        if rem is None:
            raise MethodError(f"remainder {rem_raw!r} is not one of the outcomes {labels}")
    # 一个方法的问题全部收齐再报（修正轮一次看到全部问题；live 运行 discrete2 里只报了第一个，漏掉的结果没被修）
    given, detail, errs, seen = {}, [], [], set()
    for k, spec in probs.items():
        lab = canon.get(_norm_label(k).casefold())
        if lab is None:
            errs.append(f"unknown outcome label {k!r}; use one of {labels}")
            continue
        if lab == rem:
            errs.append(f"outcome {lab!r} has a probability input and is also the remainder")
            continue
        if lab in seen:
            errs.append(f"outcome {lab!r} is given twice")
            continue
        seen.add(lab)
        try:
            d = _probability(lab, spec, pts, kept_a, rejected_a)
        except MethodError as e:
            errs.append(str(e))
            continue
        given[lab] = d["prob"]
        detail.append(d)
    missing = [lab for lab in labels if lab not in seen and lab != rem]
    if missing:
        errs.append(f"outcomes without a probability: {missing} (give each one an input, or name one as the remainder)")
    s = sum(given.values())   # 求和检查也并进同一条消息（有输入失败时只按通过的输入算；没有余下结果又缺结果时不查和）
    if rem is not None and s > 1 + SUM_TOL_REMAINDER:
        errs.append(f"the given probabilities sum to {s:.3f} (more than 1 + {SUM_TOL_REMAINDER:g}), so the remainder "
                    f"{rem!r} would be negative; drop the remainder or lower the other inputs")
    elif rem is None and not missing and len(given) == len(labels) and not SUM_RANGE[0] <= s <= SUM_RANGE[1]:
        errs.append(f"probabilities sum to {s:.3f}; without a remainder outcome they must sum to between "
                    f"{SUM_RANGE[0]:g} and {SUM_RANGE[1]:g}")
    if errs:
        raise MethodError("; ".join(errs))
    if rem is not None:
        given[rem] = max(0.0, 1.0 - s)
    total = sum(given.values())
    return {"distribution": {lab: given[lab] / total for lab in labels}, "inputs_detail": detail, "sum_given": s,
            "remainder": rem, "remainder_prob_before_normalising": None if rem is None else given[rem],
            "normalised_by": total, "used_ids": [d["id"] for d in detail if d["kind"] == "point"],
            "used_assumptions": sorted({d["id"] for d in detail if d["kind"] == "assumption"})}


def pool(ok: list, outcomes: list) -> dict:
    """等权线性平均（只放算出了 distribution 的方法）。result 的形状见模块说明；p10 / p90 恒为 None。"""
    base = {"mode": "discrete", "p10": None, "p90": None, "weight_rule": "equal_linear_pool"}
    if not ok:
        return {**base, "outcomes": [{**o, "prob": None} for o in outcomes], "most_likely": None, "most_likely_prob": None,
                "central": None, "weights": {}, "basis": "no_method", "assumption_weight_share": 0}
    w = 1 / len(ok)
    outs = [{**o, "prob": sum(w * r["distribution"][o["label"]] for r in ok)} for o in outcomes]
    top = max(outs, key=lambda o: o["prob"])   # max 取第一个最大值：并列时取 plan 里排在前面的
    return {**base, "outcomes": outs, "most_likely": top["label"], "most_likely_prob": top["prob"], "central": top["value"],
            "weights": {r["id"]: w for r in ok}, "basis": "outcome_probabilities",
            "assumption_weight_share": sum(w for r in ok if r.get("used_assumptions"))}


def run(methods: list, pts: dict, target: dict, assumptions=None) -> dict:
    """离散目标的 compute：和 compute.run 同样的方法编号（m1..mN）和返回结构（methods / result / assumptions_used_by）。"""
    av = assumptions or {"kept": [], "rejected": []}
    kept_a = {a["id"]: a for a in av.get("kept") or []}
    rejected_a = {a.get("id"): a.get("reason", "") for a in av.get("rejected") or [] if a.get("id") and a.get("id") not in kept_a}
    outcomes = target.get("outcomes") or []
    results = []
    for n, m in enumerate(methods or [], start=1):
        r = {"id": f"m{n}", "label": str(m.get("id", ""))[:40], "method": m.get("method"), "params": m.get("params") or {},
             "rationale": str(m.get("rationale", ""))[:400], "estimate": None, "backtest": [], "notes": []}
        try:
            if r["method"] != "outcome_probs":
                raise MethodError(f"method {r['method']!r} is not available for a discrete target (outcome_type 'discrete'); "
                                  f"use outcome_probs with one probability per outcome")
            r.update(outcome_probs(r["params"], pts, kept_a, rejected_a, outcomes))
        except MethodError as e:
            r["error"] = str(e)
        except (TypeError, ValueError, KeyError, AttributeError) as e:
            r["error"] = f"bad params: {type(e).__name__}: {e}"[:200]
        results.append(r)
    for r in results:
        r["n_point_inputs"] = len(set(r.get("used_ids") or []))
        r["n_assumption_inputs"] = len(r.get("used_assumptions") or [])
        r["rests_mainly_on_assumptions"] = r["n_assumption_inputs"] > 0 and r["n_assumption_inputs"] >= r["n_point_inputs"]
    ok = [r for r in results if r.get("distribution")]
    used_by = {}
    for r in ok:
        for aid in r.get("used_assumptions") or []:
            used_by.setdefault(aid, []).append(r["id"])
    return {"mode": "discrete", "methods": results, "result": pool(ok, outcomes), "assumptions_used_by": used_by}


def _matches(o: dict, ans) -> bool:
    if isinstance(ans, (int, float)) and not isinstance(ans, bool):
        return o.get("value") is not None and abs(o["value"] - ans) <= 1e-9 * max(1.0, abs(ans))
    return _norm_label(ans).casefold() == o["label"].casefold()


def score(res: dict, ans) -> dict:
    """离散目标的打分（有真值时）：真结果得到的概率、Brier 分数（各结果 (p - 是否发生)^2 之和；真值不在结果列表里时，
    相当于多一个概率为 0 的「其他」结果，加 1）、最可能的结果对不对。"""
    outs = res.get("outcomes") or []
    true = next((o["label"] for o in outs if _matches(o, ans)), None)
    if not outs or any(o.get("prob") is None for o in outs):
        return {"true_outcome": true, "prob_true": None, "brier": None, "most_likely_correct": None}
    brier = sum((o["prob"] - (1.0 if o["label"] == true else 0.0)) ** 2 for o in outs) + (0.0 if true else 1.0)
    return {"true_outcome": true, "prob_true": next((o["prob"] for o in outs if o["label"] == true), 0.0), "brier": brier,
            "most_likely_correct": res.get("most_likely") == true and true is not None}
