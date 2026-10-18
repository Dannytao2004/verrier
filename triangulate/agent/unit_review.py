"""v2.8e：钉了单位时，formula_mc 方法的结果单位交给模型核对（用户 10-18 的设计）。

1. 三个核对模型各自看同一份输入（每个输入一行 JSON：代码实际用的值、证据记录的单位、描述、原文、期间、角色分开写），
   给每个输入写出明确的单位、记录的单位对不对、理由，再推出公式结果的单位。
2. 第四个模型（裁定）看三份回答，定下每个输入的单位和公式结果的单位，并自己判断它和目标单位是不是同一类量。
3. 裁定说不合适、或者代码（pint）换不到目标单位，就带着原因重新裁定，一共最多 ARBITER_TRIES 次；仍不行，这个方法记为失败
   （原因交给修正轮）。
定下的单位写回裁判方法的 "unit"（裁判原来写的放进 "unit_from_judge"），compute 照它换算；全部回答存进这一轮的
judge_rounds[...]["unit_reviews"]。核对调用本身失败（出错、超预算）时不拦方法，照裁判写的单位算（同输入核对）。"""
import math
from concurrent.futures import ThreadPoolExecutor

from ..config import MAX_TOKENS
from . import qty as Q
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


def _sig(v):
    return float(f"{v:.6g}")


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
            v = math.sqrt(d["p10"] * d["p90"])   # 观测点按 v / 1.2 .. v * 1.2 采样，v 就是代码用的值（百分数已除以 100）
            x.update(kind="data point", value_used=_sig(v), unit_as_recorded=p.get("unit", ""), description=p.get("name", ""),
                     period=f"{p.get('period_start') or '?'}..{p.get('period_end') or '?'}", quote=str(p.get("quote", ""))[:300])
            if p.get("value") and abs(v * 100 / p["value"] - 1) < 1e-6:
                x["note"] = f"recorded as {p['value']:g} {p.get('unit', '')}; code divided it by 100, so the formula uses the fraction {v:g}"
        x["role"] = roles.get(d["name"], "")
        rows.append(dumps(x))
    return rows


def _ask(llm, system, user, role, qid, key):
    try:
        return llm.ask(system, user, role=role, qid=qid, max_tokens=MAX_TOKENS[key])
    except BudgetExceeded as e:
        return None, str(e)


def _conv(unit: str, tu: str) -> str:
    f, err = Q.convert_factor(unit, tu) if unit else (None, "no result_unit")
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
        conv = _conv(str(out.get("result_unit") or "").strip(), tu)
        checkers.append({"reply": out, "converts_to_target": conv})
        answers.append(f"checker {k + 1}: {dumps({**out, 'converts_to_target': conv})}")
    arb_user = sub(UNIT_ARBITER_USER, {"__ANSWERS__": "\n".join(answers)})
    rec = {"method": mid, "label": m_out.get("label"), "judge_unit": declared, "checkers": checkers, "arbiter": []}
    user = arb_user
    for t in range(ARBITER_TRIES):
        out, err = _ask(llm, UNIT_ARBITER_SYSTEM, user, f"unit_arbiter:{mid}:{t + 1}", qid, "unit_arbiter")
        if out is None:   # 裁定调用本身失败：不拦方法，照裁判写的单位
            rec["arbiter"].append({"error": err})
            return rec
        ru = str(out.get("result_unit") or "").strip()
        f, problem = None, ""
        if out.get("fits_target") is not True:
            problem = f"you judged that it does not fit the target unit '{tu}': {out.get('fit_reason', '')}"
        elif not ru:
            problem = "result_unit is empty"
        else:
            f, cerr = Q.convert_factor(ru, tu)
            if cerr:
                problem = f"code cannot convert '{ru}' to the target unit '{tu}': {cerr}"
        rec["arbiter"].append({"reply": out, "problem": problem})
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
