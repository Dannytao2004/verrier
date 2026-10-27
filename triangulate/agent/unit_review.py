"""v2.8e：钉了单位时，formula_mc 方法的结果单位交给模型核对（用户 10-18 的设计）。

1. 三个核对模型各自看同一份输入（每个输入一行 JSON：代码实际用的值、证据记录的单位、描述、原文、期间、角色分开写），
   给每个输入写出明确的单位、记录的单位对不对、理由，再推出公式结果的单位。
2. 第四个模型（裁定）看三份回答，定下每个输入的单位和公式结果的单位，并自己判断它和目标单位是不是同一类量。
3. 裁定说不合适、或者代码（pint）换不到目标单位，就带着原因重新裁定，一共最多 ARBITER_TRIES 次；仍不行，这个方法记为失败
   （原因交给修正轮）。
定下的单位写回裁判方法的 "unit"（裁判原来写的放进 "unit_from_judge"），compute 照它换算；全部回答存进这一轮的
judge_rounds[...]["unit_reviews"]。核对调用本身失败（出错、超预算）时不拦方法，照裁判写的单位算（同输入核对）。"""
import ast
import calendar
import math
from concurrent.futures import ThreadPoolExecutor

import pint

from ..config import MAX_TOKENS
from ..expr import Formula, FormulaError
from . import qty as Q
from .evidence import PERCENT, norm, parse_date, period_text, split_multiplier
from .pipeline import BudgetExceeded, dumps
from .prompts import (UNIT_ARBITER_RETRY, UNIT_ARBITER_SYSTEM, UNIT_ARBITER_USER, UNIT_CHECK_SYSTEM, UNIT_CHECK_USER,
                      UNIT_RULES)

N_CHECKERS = 3
ARBITER_TRIES = 3
# compute.py 换单位出错时的报错开头：这两种失败的方法也送去核对（裁定的单位可能把它救回来）
UNIT_ERRORS = ('give the method a "unit"', "unit of the formula's result")
# 代码给的常数在公式里只是数字，这里写出它们的单位和含义给模型看
CONSTANTS = {"k_days_target": ("day", "days in the target period"),
             "k_days_per_week": ("day/week", "days per week"),
             "k_days_per_year": ("day/year", "days per year"),
             "k_weeks_per_year": ("week/year", "weeks per year"),
             "k_months_per_year": ("month/year", "months per year"),
             "k_bp_per_pct_point": ("bp/pp", "basis points per percentage point"),
             "k_percent_per_unit": ("percent", "percent per whole (100 percent = 1)")}


class ScaleError(ValueError):
    pass


def _same_scale(a, b):
    """加、减、mean、min、max 的各项：公式里是直接拿数相加，所以各项必须是同一个单位、同一个尺度（一年的数加一个月的数不行）。"""
    if a.dimensionality != b.dimensionality:
        raise pint.DimensionalityError(a.units, b.units)
    if not math.isclose(a.to(b.units).magnitude, b.magnitude, rel_tol=1e-9):
        raise ScaleError(f"it adds or compares a quantity in {a.magnitude:g} {a.units} with one in {b.magnitude:g} {b.units}, "
                         "which are on different scales; convert one of them first")


def _qeval(node, env):
    """公式的语法树按 pint 的量求值（加减要求同类量，pint 不同类就报 DimensionalityError）。"""
    if isinstance(node, ast.BinOp):
        a = _qeval(node.left, env)
        if isinstance(node.op, ast.Pow):
            return a ** int(node.right.value if isinstance(node.right, ast.Constant) else -node.right.operand.value)
        b = _qeval(node.right, env)
        if isinstance(node.op, (ast.Add, ast.Sub)):   # 这里只推单位和尺度，数由代码另算：同尺度的两项相加，尺度不变
            _same_scale(a, b)
            return a
        return a * b if isinstance(node.op, ast.Mult) else a / b
    if isinstance(node, ast.UnaryOp):
        v = _qeval(node.operand, env)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Constant):
        return Q.UREG.Quantity(float(node.value), "dimensionless")
    if isinstance(node, ast.Call):
        args = [_qeval(x, env) for x in node.args]
        if node.func.id == "sqrt":
            return args[0] ** 0.5
        for x in args[1:]:
            _same_scale(args[0], x)
        return args[0]   # mean / min / max：各项同一尺度（上面查过），结果也是这个尺度
    raise FormulaError(f"cannot work out units of {type(node).__name__}")


def _same_unit(a: str, b: str) -> bool:
    """两个单位串是不是同一个量、同一个尺度（解析不了的当作不同）。"""
    f, err = Q.convert_factor(a, b) if a and b else (None, "empty")
    return not err and f is not None and math.isclose(f, 1.0, rel_tol=1e-9)


def derive_unit(formula: str, units: dict) -> tuple:
    """v2.13a：按定下的各输入单位，由代码（pint）推出公式结果的单位。返回 (单位串, 错误)。
    单位代数是确定的算术，交给代码；模型只判断每个输入是什么、按什么算（德国新车的探针里，裁定把
    p75 * k * a2 / k 的推导写漏了一个 / k，结果单位错了，换算出 19,735）。"""
    try:
        f = Formula(formula)
    except FormulaError as e:
        return "", str(e)
    env = {}
    for n in sorted(f.names):
        u = units.get(n)
        if not u:
            return "", f"no unit was decided for input {n}"
        q, err = Q.parse_unit(u)
        if q is None:
            return "", err
        env[n] = q
    try:
        with Q._LOCK:
            r = _qeval(f.root, env)
    except pint.DimensionalityError as e:
        return "", f"the formula adds or compares quantities of different kinds ({e})"
    except ScaleError as e:
        return "", str(e)
    except (FormulaError, ZeroDivisionError, TypeError, ValueError, AttributeError) as e:
        return "", f"units could not be worked out ({type(e).__name__}: {e})"
    if not isinstance(r, pint.Quantity):
        r = Q.UREG.Quantity(r, "dimensionless")
    if r.dimensionless:   # 纯数（year/month 这种也化成 12）：单位写 1，倍数写成数
        r = r.to("dimensionless")
        return f"{r.magnitude:.10g}", ""
    unit = f"{r.units:C}"
    return (unit if r.magnitude == 1 else f"{r.magnitude:.10g} {unit}"), ""


def _sig(v):
    return float(f"{v:.6g}")


def _multiplier(p: dict) -> float:
    """v2.8q：代码给这个数据点乘过的倍数（scale_word 或写法末尾的 万 / million，evidence.split_multiplier）；没有就是 1。"""
    sw = str(p.get("scale_word") or "")
    try:
        return split_multiplier(str(p.get("value_as_written") or ""), "" if norm(sw).lower() in PERCENT else sw)[1]
    except ValueError:
        return 1.0


def _doubled(out: dict, mults: dict) -> str:
    """v2.8q：代码已乘过倍数 f 的数据点，裁定又给它一个系数恰好是 f 的单位（10000 CNY/year），pint 会再乘一次
    （恒顺题 v2.8p：4,774.13 万元 -> 69.5 亿瓶）。返回交给裁定重试的问题，没有就是空串。birth/(1000 person) 的系数是 1/1000，不算。"""
    for x in out.get("inputs") or []:
        if not isinstance(x, dict) or x.get("name") not in mults:
            continue
        q, _ = Q.parse_unit(str(x.get("unit") or ""))
        f = mults[x["name"]]
        if q is not None and math.isclose(float(q.magnitude), f, rel_tol=1e-9):
            return (f"input {x['name']}: code already multiplied this data point by {f:,.0f}, so its value_used is in base units; "
                    f"its unit must not contain the factor {f:.0f} (for example 'CNY/year', not '{f:.0f} CNY/year'). "
                    "Correct that input's unit and the result unit")
    return ""


def input_lines(m_in: dict, m_out: dict, by_id: dict, kept_a: dict) -> list:
    """给核对和裁定看的输入，每个一行 JSON；值、记录的单位、描述分开写。"""
    roles = {n: (s.get("role", "") if isinstance(s, dict) else "") for n, s in ((m_in.get("params") or {}).get("inputs") or {}).items()}
    rows = []
    for d in m_out.get("inputs_detail") or []:
        x = {"name": d["name"]}
        if d["kind"] == "constant":
            u, text = CONSTANTS.get(d["id"], ("1", d["id"]))
            x.update(kind="constant supplied by code", value_used=_sig(d["p10"]), unit_as_recorded=u, description=text)
        elif d["kind"] == "assumption":
            a = kept_a[d["id"]]
            v = a["value"] / 100 if a.get("is_pct") else a["value"]
            x.update(kind="analyst assumption", value_used=_sig(v), unit_as_recorded=a.get("unit", ""), description=a.get("name", ""),
                     rationale=str(a.get("rationale", ""))[:300])
            if a.get("is_pct"):
                x["note"] = f"recorded as {a['value']:g} {a['unit']}; code divided it by 100, so the formula uses the fraction {v:g}"
        else:
            p = by_id[d["id"]]
            # 观测点按 v / 1.2 .. v * 1.2 采样，v 就是代码用的值（百分数已除以 100）；v2.8o 区间点的 v 是区间中点（detail 里记着）
            v = d["value"] if "value" in d else math.sqrt(d["p10"] * d["p90"])
            x.update(kind="data point", value_used=_sig(v), unit_as_recorded=p.get("unit", ""),
                     **({"unit_at_extraction": p["unit_calc"]} if p.get("unit_calc") else {}), description=p.get("name", ""),
                     period=period_text(p), quote=str(p.get("quote", ""))[:300])
            if "low" in d:
                x["range_used"] = f"{_sig(d['low'])}..{_sig(d['high'])}"
            if p.get("value") and abs(v * 100 / p["value"] - 1) < 1e-6:
                x["note"] = f"recorded as {p['value']:g} {p.get('unit', '')}; code divided it by 100, so the formula uses the fraction {v:g}"
            mult = _multiplier(p)
            if mult != 1:   # v2.8q：倍数照百分数的写法说明；倍数为 1 的点这一行和以前逐字相同
                sw = f" with multiplier {p.get('scale_word')}" if p.get("scale_word") else ""
                note = (f"written as {p.get('value_as_written')}{sw}; code already multiplied it by {mult:,.0f}, so value_used "
                        f"{_sig(v)} is in base units (not in units of {mult:,.0f}), even if unit_as_recorded names the multiplier")
                x["note"] = f"{x['note']}; {note}" if x.get("note") else note
        x["role"] = roles.get(d["name"], "")
        rows.append(dumps(x))
    return rows


def period_length(target: dict) -> str:
    """目标期间的长度（pint 写法）：整月 1 month、整年 1 year、7 天 1 week，其余 N day。"""
    s, e = parse_date(target.get("period_start")), parse_date(target.get("period_end"), end=True)
    if s is None or e is None:
        return ""
    if s.day == 1 and (e.year, e.month) == (s.year, s.month) and e.day == calendar.monthrange(e.year, e.month)[1]:
        return "1 month"
    if (s.month, s.day, e.month, e.day) == (1, 1, 12, 31) and s.year == e.year:
        return "1 year"
    n = (e - s).days + 1
    return "1 week" if n == 7 else f"{n} day"


def to_target(unit: str, tu: str, target: dict) -> tuple:
    """(实际用的单位串, 倍数, 错误)。先直接换；换不了、目标是一段时间的总量（单位里没有时间，如 bottle）而且目标期间已知，
    再乘上期间长度（bottle/year × 1 year -> bottle）。目标本身是速率（t/day）时不乘，免得把错单位凑成对的。
    v2.8j：恒顺题目标锁成 bottle（一年的瓶数），裁定给的是 1000 bottle/year，换不过去就判失败，方法照用裁判的错单位，结果小了 1000 倍"""
    f, err = Q.convert_factor(unit, tu)
    if not err:
        return unit, f, ""
    q, _ = Q.parse_unit(tu)
    period = period_length(target)
    if period and q is not None and not q.dimensionality.get("[time]", 0):
        u2 = f"({unit}) * {period}"
        f2, err2 = Q.convert_factor(u2, tu)
        if not err2:
            return u2, f2, ""
    return unit, None, err


def _ask(llm, system, user, role, qid, key):
    try:
        return llm.ask(system, user, role=role, qid=qid, max_tokens=MAX_TOKENS[key])
    except BudgetExceeded as e:
        return None, str(e)


def _conv(unit: str, tu: str, target: dict) -> str:
    _, f, err = to_target(unit, tu, target) if unit else (None, None, "no result_unit")
    return f"{f:.6g}" if not err else f"cannot be converted: {err}"


def review_method(llm, qid: str, mid: str, m_in: dict, m_out: dict, by_id: dict, kept_a: dict, target: dict) -> dict:
    """一个方法：三个核对 + 裁定（最多 ARBITER_TRIES 次）。返回记录；record["unit"] 是定下的单位，失败时 record["failure"] 是原因。"""
    tu = target["unit_canonical"]
    declared = m_in.get("unit") if isinstance(m_in.get("unit"), str) and m_in.get("unit").strip() else "(none)"
    fill = {"__TARGET__": dumps({"what": str(target.get("what", ""))[:300]}), "__TARGET_UNIT__": tu,
            "__PERIOD__": f"{target.get('period_start')}..{target.get('period_end')}",
            "__FORMULA__": str((m_in.get("params") or {}).get("formula", "")), "__DECLARED__": declared,
            "__INPUTS__": "\n".join(input_lines(m_in, m_out, by_id, kept_a)), "__RULES__": UNIT_RULES}

    def sub(tpl, extra=None):
        for k, v in {**fill, **(extra or {})}.items():
            tpl = tpl.replace(k, v)
        return tpl

    check_user = sub(UNIT_CHECK_USER)
    with ThreadPoolExecutor(N_CHECKERS) as ex:
        got = list(ex.map(lambda k: _ask(llm, UNIT_CHECK_SYSTEM, check_user, f"unit_check:{mid}:{k + 1}", qid, "unit_check"),
                          range(N_CHECKERS)))
    checkers, answers = [], []
    for k, (out, err) in enumerate(got):
        if out is None:
            checkers.append({"error": err})
            answers.append(f"checker {k + 1}: no answer")
            continue
        conv = _conv(str(out.get("result_unit") or "").strip(), tu, target)
        checkers.append({"reply": out, "converts_to_target": conv})
        answers.append(f"checker {k + 1}: {dumps({**out, 'converts_to_target': conv})}")
    arb_user = sub(UNIT_ARBITER_USER, {"__ANSWERS__": "\n".join(answers)})
    rec = {"method": mid, "label": m_out.get("label"), "judge_unit": declared, "checkers": checkers, "arbiter": []}
    mults = {d["name"]: m for d in m_out.get("inputs_detail") or [] if d["kind"] == "point" and (m := _multiplier(by_id[d["id"]])) != 1}
    user = arb_user
    for t in range(ARBITER_TRIES):
        out, err = _ask(llm, UNIT_ARBITER_SYSTEM, user, f"unit_arbiter:{mid}:{t + 1}", qid, "unit_arbiter")
        if out is None:   # 裁定调用本身失败：不拦方法，照裁判写的单位
            rec["arbiter"].append({"error": err})
            return rec
        ru = str(out.get("result_unit") or "").strip()
        f, problem = None, ""
        # v2.13a：结果单位由代码按裁定的各输入单位推出来（代码给的常数用代码自己的单位），不用裁定自己写的推导
        decided = {str(x.get("name")): str(x.get("unit") or "") for x in out.get("inputs") or [] if isinstance(x, dict)}
        decided.update({d["name"]: CONSTANTS[d["id"]][0] for d in m_out.get("inputs_detail") or []
                        if d["kind"] == "constant" and d["id"] in CONSTANTS})
        derived, derr = derive_unit(str((m_in.get("params") or {}).get("formula", "")), decided)
        if dbl := _doubled(out, mults):   # v2.8q：倍数乘两次
            problem = dbl
        elif derr:
            problem = f"code could not work out the result unit from your input units: {derr}"
        elif out.get("fits_target") is not True and _same_unit(ru, derived):
            # v2.13a：裁定说「不符」只在它自己写的结果单位和代码推出来的一致时才算（推导写错了，它的判断是对着错单位下的）
            problem = f"you judged that it does not fit the target unit '{tu}': {out.get('fit_reason', '')}"
        else:
            ru, f, cerr = to_target(derived, tu, target)
            if cerr:
                problem = f"code cannot convert '{ru}' (worked out by code from your input units) to the target unit '{tu}': {cerr}"
        rec["arbiter"].append({"reply": out, "problem": problem, **({"derived_unit": derived} if derived else {})})
        if not problem:
            rec.update(unit=ru, factor=f)
            return rec
        user = arb_user + UNIT_ARBITER_RETRY.replace("__PREVIOUS__", dumps(out)).replace("__PROBLEM__", problem)
    rec["failure"] = (f"unit check: the formula's result is '{ru or '?'}' ({str(out.get('derivation', ''))[:200]}), which is not a "
                      f"'{tu}' quantity: {problem}")
    return rec


def review(llm, qid: str, jr: dict, out: dict, av: dict, pts: list, failed: dict, target: dict):
    """对试跑的结果做单位核对。没有钉单位、或没有要核对的方法时返回 None（流程和以前完全相同）；
    否则把定下的单位写回 jr["methods"]，记录追加到 jr["unit_reviews"]，返回 {方法下标: 失败原因}。"""
    if not (target or {}).get("unit_canonical"):
        return None
    by_id, kept_a = {p["id"]: p for p in pts}, {a["id"]: a for a in av["kept"]}
    todo = [i for i, (mi, mo) in enumerate(zip(jr.get("methods") or [], out.get("methods") or []))
            if mo.get("method") == "formula_mc" and mo.get("inputs_detail") and not mo.get("coverage_excluded")
            and (i not in failed or str(failed[i]).startswith(UNIT_ERRORS))]
    if not todo:
        return None
    with ThreadPoolExecutor(len(todo)) as ex:
        recs = list(ex.map(lambda i: review_method(llm, qid, out["methods"][i]["id"], jr["methods"][i], out["methods"][i],
                                                   by_id, kept_a, target), todo))
    fails = {}
    for i, rec in zip(todo, recs):
        mi = jr["methods"][i]
        if rec.get("unit"):
            if mi.get("unit") != rec["unit"]:
                mi["unit_from_judge"] = mi.get("unit")
                mi["unit"] = rec["unit"]
        elif rec.get("failure"):
            fails[i] = rec["failure"]
    jr.setdefault("unit_reviews", []).append({"check": len(jr.get("unit_reviews") or []) + 1, "methods": recs})
    return fails
