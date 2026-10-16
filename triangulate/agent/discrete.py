"""离散结果模式：目标只能是几个互斥结果之一（一次会议后的政策利率、选举赢家、是 / 否事件）。

- plan（v2.3 起）：target 只带 outcome_type 和可选的 outcome_kind（「policy rate in fixed steps」这类提示），不列结果。
  v2.2 由 plan 在搜索前定结果列表，规划模型的先验错了就无法纠正（FOMC discrete5：列表 4.50%-5.75%，当前值 4.00% 不在里面）。
- 裁判第一轮（v2.3）：根据保留的证据定义结果列表 outcomes（2-6 个，label 唯一；数值型时最低的带 le、最高的带 ge，
  两个合并尾部保证覆盖全部可能），并在 outcomes_basis 里给出依据的点 id（都必须是保留的点）。不合格的列表交回裁判的修正轮。
  之后的轮次沿用这个列表；新证据和它矛盾时，裁判可以修订一次（要给 outcomes_revision_reason）。记录在 state["outcomes"]。
- 裁判：只能用 outcome_probs，每个结果的概率引用一个保留的数据点或一条假设；可以指定一个结果取「余下的概率」。
- 代码（这里）：% 转小数；每个概率在 [0, 1]；有余下结果时其余之和 <= 1 + SUM_TOL_REMAINDER，余下 = 1 - 和（截到 0）；
  没有余下结果时和必须在 SUM_RANGE 内；最后都归一化到 1。没有输入、也不是余下结果的结果概率为 0（记进 notes）；未知 label 拒绝。
  （live 运行 discrete1/2/4 都因为「每个结果都要有输入」这条没出数：证据只给有概率的结果，比如 FedWatch 只报维持和加息。）
  v2.2.1 起另有：每个方法至少一个保留的观测点（同 formula_mc）；一个 id 只能给一个结果；当概率用的观测点 name 或 unit
  要说明是概率（PROB_WORDS）；百分点 / 基点（变化量）拒绝。
  多个方法等权线性平均（linear pool）；最可能的结果 = 概率最大的（并列时取列表里排在前面的）。
- 假设输入用裁判给的 value（离散结果是点分布，不做 Monte Carlo）；low / high 只记录。
连续值模式（compute.run 的其余部分）不经过这里。
"""
import math
import re

from . import compute as C
from .methods import MethodError

MIN_OUTCOMES, MAX_OUTCOMES = 2, 6   # 裁判定义的结果个数（v2.2 由 plan 定时是 2-10）
KIND_CHARS = 120
SUM_TOL_REMAINDER = 0.02
SUM_RANGE = (0.9, 1.1)
LABEL_CHARS = 80
PCT_UNIT = re.compile(r"%|\bper ?cent\b|\bpercentage\b|\bpct\b", re.I)
# 变化量的单位（百分点、基点）不是概率（v2.2.1；FOMC discrete4 的「FedWatch 概率变化 22.1 percentage points」曾被当成 0.221）
CHANGE_UNIT = re.compile(r"\bpercentage[- ]?points?\b|\bpp\b|\bp\.p\.|\bbps?\b|\bbasis[- ]?points?\b", re.I)
# 当概率用的观测点，name 或 unit 必须说明它是概率（markets.py 的点 unit = "probability"；FedWatch 的点 name 都带 probability）。
# 不收 implied / priced：「market-implied rate 4.0%」是水平，不是概率
PROB_WORDS = re.compile(r"probab|\bodds\b|\bchances?\b|likelihood", re.I)


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


def parse_outcome_type(raw: dict) -> tuple:
    """plan 回复里的 target -> ({"outcome_type": ..., 离散时另有 "outcome_kind": ...}, 说明)。说明为空 = 没有问题。
    plan 不再列结果（v2.3）：回复里还带着 outcomes 就忽略，记一条说明。"""
    raw = raw if isinstance(raw, dict) else {}
    kind = str(raw.get("outcome_type") or "continuous").strip().lower()
    if kind != "discrete":
        note = "" if kind == "continuous" else f"outcome_type {kind!r} not recognised; treated as continuous"
        return {"outcome_type": "continuous"}, note
    note = "plan listed outcomes; ignored (the judge defines them from the evidence)" if raw.get("outcomes") else ""
    return {"outcome_type": "discrete", "outcome_kind": " ".join(str(raw.get("outcome_kind") or "").split())[:KIND_CHARS]}, note


def is_discrete(target: dict) -> bool:
    return (target or {}).get("outcome_type") == "discrete"


def with_outcomes(target: dict, rec) -> dict:
    """plan 的 target 加上裁判定义的结果列表（rec = state["outcomes"]）。没有记录时原样返回（旧运行的 plan 自带 outcomes）。"""
    if not rec or not rec.get("list"):
        return target
    return {**(target or {}), "outcomes": rec["list"], "outcomes_basis": rec.get("basis") or {}}


def value_text(o: dict, unit: str) -> str:
    """结果的数值说明：「 (value 4 percent)」；合并尾部加 or lower / or higher；没有数值时为空。"""
    if o.get("value") is None:
        return ""
    tail = " or lower" if o.get("le") is not None else " or higher" if o.get("ge") is not None else ""
    return f" (value {o['value']:g} {unit}{tail})"


def outcomes_text(target: dict) -> str:
    """给裁判看的结果列表（每行一个 label，带数值和单位）。"""
    unit = (target or {}).get("unit", "")
    return "\n".join(f'- "{o["label"]}"' + value_text(o, unit) for o in (target or {}).get("outcomes") or [])


def validate_outcomes(raw, basis, kept_ids) -> tuple:
    """裁判给的结果列表 -> (干净的列表, 依据 {"ids", "note"}, 问题清单)。问题清单为空 = 通过。
    规则：2-6 个；label 非空且唯一；数值要么全有要么全没有；数值型时数值不重复，最低的带 le、最高的带 ge（等于它的 value），
    中间的不带界（两个合并尾部保证覆盖全部可能的结果）；带界的结果 value 取界，所以非数值列表里带界会被「全有或全没有」挡下；
    依据至少一个 id，每个都是这一轮保留的数据点。"""
    errs, clean, seen = [], [], set()
    if not isinstance(raw, list):
        return [], {}, ['"outcomes" must be a list of {"label", "value"} objects (with "le" / "ge" on the two tails)']
    if not MIN_OUTCOMES <= len(raw) <= MAX_OUTCOMES:
        errs.append(f"{len(raw)} outcomes (need {MIN_OUTCOMES} to {MAX_OUTCOMES}; merge unlikely results into the tails)")
    for n, o in enumerate(raw, start=1):
        label = _norm_label(o.get("label")) if isinstance(o, dict) else ""
        if not label:
            errs.append(f"outcome {n} has no label")
            continue
        if label.casefold() in seen:
            errs.append(f"duplicate outcome label {label!r}")
            continue
        seen.add(label.casefold())
        v = _value(o.get("value"))
        c = {"label": label, "value": v}
        for k in ("le", "ge"):
            if o.get(k) is None:
                continue
            b = _value(o.get(k))
            if b is None:
                errs.append(f"outcome {label!r}: {k} must be a number")
            elif v is not None and abs(v - b) > 1e-9 * max(1.0, abs(b)):
                errs.append(f"outcome {label!r}: {k} = {b:g} must equal its value {v:g}")
            else:
                c["value"], c[k] = b, b
        if "le" in c and "ge" in c:
            errs.append(f"outcome {label!r} has both le and ge")
        clean.append(c)
    nums = [c for c in clean if c["value"] is not None]
    if nums and len(nums) != len(clean):
        errs.append(f"either every outcome has a numeric value or none has (no value: "
                    f"{[c['label'] for c in clean if c['value'] is None]})")
    elif nums:
        vals = sorted(c["value"] for c in nums)
        if len(set(vals)) != len(vals):
            errs.append("two outcomes have the same value")
        lo, hi = min(nums, key=lambda c: c["value"]), max(nums, key=lambda c: c["value"])
        if "le" not in lo:
            errs.append(f"the lowest outcome {lo['label']!r} must be a merged tail with \"le\": {lo['value']:g} "
                        f"(\"... or lower\"), so that the outcomes cover every possible result")
        if "ge" not in hi:
            errs.append(f"the highest outcome {hi['label']!r} must be a merged tail with \"ge\": {hi['value']:g} "
                        f"(\"... or higher\"), so that the outcomes cover every possible result")
        inner = [c["label"] for c in nums if ("le" in c and c is not lo) or ("ge" in c and c is not hi)]
        if inner:
            errs.append(f"only the lowest outcome may carry le and only the highest ge (also bounded: {inner})")
    b = basis if isinstance(basis, dict) else {"ids": basis} if isinstance(basis, list) else {}
    ids = [str(i) for i in b.get("ids")] if isinstance(b.get("ids"), list) else []
    if not ids:
        errs.append('"outcomes_basis" must give {"ids": [...], "note": "..."}: the kept data-point ids the list relies on')
    bad = [i for i in ids if i not in kept_ids]
    if bad:
        errs.append(f"outcomes_basis ids {bad} are not kept data points (assumptions, discarded or unknown ids cannot "
                    f"ground the outcome list)")
    return clean, {"ids": ids, "note": str(b.get("note") or "")[:400]}, errs


def _list_key(lst) -> list:
    return [(_norm_label(o.get("label")).casefold(), _value(o.get("value")), _value(o.get("le")), _value(o.get("ge")))
            if isinstance(o, dict) else None for o in lst or []] if isinstance(lst, list) else [lst]


def accept_outcomes(reply: dict, current, rnd: int, kept_ids) -> tuple:
    """裁判一轮回复 -> (这一轮之后在用的结果记录, 交回裁判的问题清单)。current = 之前在用的记录（None = 还没定）。
    还没定：回复必须给 outcomes 和 outcomes_basis，校验通过就是新记录。已定：没给 outcomes、或给的和现在的一样，就沿用；
    给了不同的 = 修订：只许一次、要 outcomes_revision_reason，校验通过才换。没通过时沿用 current（可能是 None）。
    记录 = {"list", "basis": {"ids", "note"}, "defined_round", "revised_round", "revision_reason", "previous_list"}。"""
    reply = reply if isinstance(reply, dict) else {}
    raw = reply.get("outcomes")
    if current and (not raw or _list_key(raw) == _list_key(current["list"])):
        return current, []
    if not raw:
        return current, ['outcome list: this discrete target has no outcome list yet; add "outcomes" and "outcomes_basis" '
                         'to the reply']
    clean, basis, errs = validate_outcomes(raw, reply.get("outcomes_basis"), kept_ids)
    reason = " ".join(str(reply.get("outcomes_revision_reason") or "").split())[:400]
    if current and current.get("revised_round"):
        errs = [f"the outcome list was already revised in round {current['revised_round']}; keep it and leave "
                f"\"outcomes\" out of the reply"]
    elif current and not reason:
        errs.append("a revised outcome list needs \"outcomes_revision_reason\" (the kept points that contradict the "
                    "current list)")
    if errs:
        return current, [f"outcome list: {e}" for e in errs]
    if current:
        return {**current, "list": clean, "basis": basis, "revised_round": rnd, "revision_reason": reason,
                "previous_list": current["list"], "previous_basis": current.get("basis")}, []
    return {"list": clean, "basis": basis, "defined_round": rnd, "revised_round": None, "revision_reason": "",
            "previous_list": None}, []


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
        if not PROB_WORDS.search(f"{p.get('name') or ''} {unit}"):
            raise MethodError(f"outcome {label!r}: data point {iid} ({str(p.get('name') or '')[:80]!r}, unit {unit!r}) is not "
                              f"stated as a probability: its name or unit must say probability, odds, chance or likelihood "
                              f"(a rate, a level or a share of something else is not the probability of an outcome)")
    if CHANGE_UNIT.search(unit):
        raise MethodError(f"outcome {label!r}: {iid} = {v:g} {unit} is a change or difference (percentage points or basis "
                          f"points), not a probability")
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
    given, detail, errs, seen, id_label = {}, [], [], set(), {}
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
        if d["id"] in id_label:   # 一个概率只对应一个结果（discrete2 的 p87、discrete4 的 a2 曾同时给两个互斥结果）
            errs.append(f"id {d['id']} is used for outcomes {id_label[d['id']]!r} and {lab!r}; one probability denotes one outcome")
            continue
        id_label[d["id"]] = lab
        given[lab] = d["prob"]
        detail.append(d)
    if not any(d["kind"] == "point" for d in detail):   # 和 formula_mc 一样：至少一个保留的观测点（discrete1/4 第 1 轮只有假设）
        errs.append("outcome_probs needs at least one kept data point among its inputs; a method made only of assumptions "
                    "and the remainder is rejected")
    zero = [lab for lab in labels if lab not in seen and lab != rem]   # 没有输入的结果：概率 0（和的检查管住漏掉的概率）
    s = sum(given.values())   # 求和检查也并进同一条消息（有输入失败时只按通过的输入算，不查和）
    if rem is not None and s > 1 + SUM_TOL_REMAINDER:
        errs.append(f"the given probabilities sum to {s:.3f} (more than 1 + {SUM_TOL_REMAINDER:g}), so the remainder "
                    f"{rem!r} would be negative; drop the remainder or lower the other inputs")
    elif rem is None and len(given) == len(seen) and not SUM_RANGE[0] <= s <= SUM_RANGE[1]:
        errs.append(f"probabilities sum to {s:.3f}; without a remainder outcome they must sum to between "
                    f"{SUM_RANGE[0]:g} and {SUM_RANGE[1]:g}" + (f" (outcomes without an input count as 0: {zero})" if zero else ""))
    if errs:
        raise MethodError("; ".join(errs))
    if rem is not None:
        given[rem] = max(0.0, 1.0 - s)
    total = sum(given.values())
    return {"distribution": {lab: given.get(lab, 0.0) / total for lab in labels}, "inputs_detail": detail, "sum_given": s,
            "zero_outcomes": zero,
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
    top = max(outs, key=lambda o: o["prob"])   # max 取第一个最大值：并列时取结果列表里排在前面的
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
            if not outcomes:   # v2.3：结果列表由裁判定义；列表被拒（修正后仍不合格）时没有可算的结果
                raise MethodError("no outcome list: the judge did not define a valid outcome list for this discrete target")
            if r["method"] != "outcome_probs":
                raise MethodError(f"method {r['method']!r} is not available for a discrete target (outcome_type 'discrete'); "
                                  f"use outcome_probs with one probability per outcome")
            r.update(outcome_probs(r["params"], pts, kept_a, rejected_a, outcomes))
            if r["zero_outcomes"]:
                r["notes"].append(f"no input for {r['zero_outcomes']}: probability 0")
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


TAIL_LE = re.compile(r"\bor (?:lower|below|less|fewer)\b", re.I)
TAIL_GE = re.compile(r"\bor (?:higher|above|more|greater)\b", re.I)


def _matches(o: dict, ans, tails: bool = False) -> bool:
    """tails=False：数值相等或 label 相同。tails=True：合并的尾部结果认超出它的数值真值（真值 3.75 落在「4.00% or lower」里）；
    裁判定义的列表（v2.3）用 le / ge 标尾部，旧列表没有时看 label 里的 or lower / or higher 等。"""
    if isinstance(ans, (int, float)) and not isinstance(ans, bool):
        v = o.get("value")
        if v is None:
            return False
        if not tails:
            return abs(v - ans) <= 1e-9 * max(1.0, abs(ans))
        if o.get("le") is not None or o.get("ge") is not None:
            return bool(o.get("le") is not None and ans < o["le"] or o.get("ge") is not None and ans > o["ge"])
        return bool(TAIL_LE.search(o["label"]) and ans < v or TAIL_GE.search(o["label"]) and ans > v)
    return not tails and _norm_label(ans).casefold() == o["label"].casefold()


def score(res: dict, ans) -> dict:
    """离散目标的打分（有真值时）：真结果得到的概率、Brier 分数（各结果 (p - 是否发生)^2 之和；真值不在结果列表里时，
    相当于多一个概率为 0 的「其他」结果，加 1）、最可能的结果对不对。先找精确相等的结果，没有再找合并的尾部结果。"""
    outs = res.get("outcomes") or []
    true = next((o["label"] for t in (False, True) for o in outs if _matches(o, ans, t)), None)
    if not outs or any(o.get("prob") is None for o in outs):
        return {"true_outcome": true, "prob_true": None, "brier": None, "most_likely_correct": None}
    brier = sum((o["prob"] - (1.0 if o["label"] == true else 0.0)) ** 2 for o in outs) + (0.0 if true else 1.0)
    return {"true_outcome": true, "prob_true": next((o["prob"] for o in outs if o["label"] == true), 0.0), "brier": brier,
            "most_likely_correct": res.get("most_likely") == true and true is not None}
