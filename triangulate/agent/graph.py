"""LangGraph 状态图：plan -> approve(interrupt) -> [Send: 每个方向一个 subagent + markets] -> judge
-> (可选一轮 base-rate 方向 -> judge) -> compute -> published -> [离散目标：jev 对照臂] -> final。
裁判可以为 formula_mc 提出假设输入（assumptions.py 校验）；--ablate-own-history 时按 ablation.py 去掉目标自身的历史。
离散目标（plan 给出 outcome_type = discrete）只用 outcome_probs；结果列表由裁判第一轮根据证据定义（v2.3，state["outcomes"]），
规则在 discrete.py；Jev 对照臂在 jev.py。
published（v2.4，只在真实使用时）：保留的点里有目标本身（已公布）时，结果就是这个值，估计方法只作参考（published.py）。

图里只放可序列化的数据；预算、LLM、哨兵等放在 Context 里，通过闭包交给节点。
"""
import math
import operator
import re
import urllib.parse
from typing import Annotated, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send, interrupt

from . import ablation as AB
from . import assumptions as AS
from . import compute as C
from . import discrete as D
from . import jev as J
from . import published as PB
from .markets import search_markets
from .pipeline import BudgetExceeded, Context, dumps, run_direction
from .prompts import (AUDIT_OUTCOMES, AUDIT_SYSTEM, AUDIT_USER, CHECKLIST, DISCRETE_METHODS_SPEC, DISCRETE_OUTCOMES_DEFINE,
                      DISCRETE_OUTCOMES_GIVEN, DISCRETE_REVISE, DISCRETE_REVISE_DONE, EXTRA_RULE_R1, EXTRA_RULE_R2,
                      FINAL_SYSTEM, FINAL_USER, FINAL_USER_DISCRETE, JUDGE_SYSTEM, JUDGE_USER, METHODS_SPEC, PLAN_SYSTEM,
                      PLAN_USER)

CATEGORIES = {"own_history", "related_series", "physical_flow", "capacity_consumption", "administrative", "attention",
              "shocks", "persona", "forecasts_markets", "base_rates"}
PLACEHOLDER = re.compile(r"\[\[([a-z0-9_]+)\]\]")


class AgentState(TypedDict, total=False):
    qid: str
    question: str
    as_of: str
    plan: dict
    plan_notes: list
    approval: dict
    directions: list
    results: Annotated[list, operator.add]
    judge_rounds: Annotated[list, operator.add]
    points: list
    compute: dict
    assumptions: dict
    outcomes: dict   # 离散目标：裁判定义的结果列表（discrete.accept_outcomes 的记录）
    jev: dict
    published: dict   # v2.4：「答案已公布」检查的记录（published.py）
    final: dict
    aborted: str


def _clean_direction(d: dict, i: int, prefix: str) -> dict:
    cat = str(d.get("category", "")).strip()
    try:
        info = min(max(int(d.get("expected_information", 3)), 1), 5)
    except (TypeError, ValueError):
        info = 3
    return {"id": f"{prefix}{i}", "category": cat if cat in CATEGORIES else "related_series",
            "perspective": str(d.get("perspective", ""))[:200], "hypothesis": str(d.get("hypothesis", ""))[:600],
            "data_to_find": str(d.get("data_to_find", ""))[:600],
            "search_hints": [str(h)[:120] for h in (d.get("search_hints") or [])][:4], "expected_information": info}


def select_directions(cands: list, cap: int) -> list:
    """plan 列出的全部候选 -> 实际要跑的方向（最多 cap 个，cap 由预算推出）。
    排序 = 预期信息量从高到低（同分按 plan 给的顺序）。先保证每个出现过的类别至少一个（own_history 最先），
    再按排序补满。这样一类出几个方向是允许的，排在清单后面的类别（例如 persona）也不会因为名额被整类挤掉。
    返回的方向按排序重新编号 d1..dN；候选本身带 selected 标记，留在 state 里。"""
    order = sorted(range(len(cands)), key=lambda i: (-cands[i]["expected_information"], i))
    chosen, seen = [], set()
    for i in sorted(order, key=lambda i: cands[i]["category"] != "own_history"):
        if len(chosen) < cap and cands[i]["category"] not in seen:
            chosen.append(i)
            seen.add(cands[i]["category"])
    for i in order:
        if len(chosen) < cap and i not in chosen:
            chosen.append(i)
    chosen.sort(key=order.index)
    for i, c in enumerate(cands):
        c["selected"] = i in chosen
    return [{**cands[i], "id": f"d{n}", "candidate_id": cands[i]["id"]} for n, i in enumerate(chosen, start=1)]


_NUM_TOKEN = re.compile(r"\d(?:[\d,.]*\d)?%?")
_YEAR_CONTEXT = re.compile(r"(?:\b(?:in|since|of|from|to|during|until|by|for|between|and|or|through|before|after|year|years|"
                           r"fiscal|fy|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|january|february|march|april|"
                           r"june|july|august|september|october|november|december)\.?|[,(/-])\s*$", re.I)


def scrub_digits(text: str, as_of_year: int, keep_ids=frozenset()) -> tuple:
    """把模型自己写的数字换成 [n]，返回 (文字, 替换个数)。保留：年份上下文里（in / since / 月份名 / 逗号 ... 后面）、
    离 as_of 不超过 10 年的四位年份；紧跟字母的已知方法 id（m1、m2）。其余一律替换，包括 [800,000、USD900,000、about900k。"""
    out, n, pos = [], 0, 0
    for m in _NUM_TOKEN.finditer(text):
        tok, s0 = m.group(), m.start()
        prev = text[s0 - 1] if s0 else ""
        keep = False
        if re.fullmatch(r"(?:19|20)\d{2}", tok) and abs(int(tok) - as_of_year) <= 10 and not prev.isalnum():
            keep = bool(_YEAR_CONTEXT.search(text[max(0, s0 - 16):s0]))
        elif prev.isalpha() and re.fullmatch(r"\d+", tok):
            j = s0
            while j > 0 and text[j - 1].isalpha():
                j -= 1
            keep = text[j:m.end()] in keep_ids
        if keep:
            continue
        out.append(text[pos:s0] + "[n]")
        pos, n = m.end(), n + 1
    out.append(text[pos:])
    return "".join(out), n


def _fmt_num(v):
    if v is None or not isinstance(v, (int, float)) or not math.isfinite(v):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:.4g}"


def _table(points: list) -> str:
    rows = ["id | dir | name | value | unit | period | published | source | via | quote"]
    for p in points:
        dom = urllib.parse.urlsplit(p.get("source_url", "")).netloc
        via = f"snapshot {p['page_date']}" if p.get("via") == "snapshot" else f"{p.get('via')} {p.get('page_date') or ''}"
        rows.append(" | ".join([p["id"], p["direction_id"], p["name"][:90], _fmt_num(p["value"]), p.get("unit", "")[:25],
                                f"{p.get('period_start') or '?'}..{p.get('period_end') or '?'}",
                                p.get("published_at_if_visible") or "", dom, via.strip(), p.get("quote", "")[:150]]))
    return "\n".join(rows)


def assumption_placeholders(a: dict) -> dict:
    """一条假设的占位符：value 是裁判提的值，low / high 是代码实际采样用的 P10 / P90（已放宽、% 按原写法显示）。"""
    f = 100.0 if a.get("is_pct") else 1.0
    pct = "%" if a.get("is_pct") else ""
    return {f"{a['id']}_value": _fmt_num(a["value"]) + pct, f"{a['id']}_low": _fmt_num(a["p10_used"] * f) + pct,
            f"{a['id']}_high": _fmt_num(a["p90_used"] * f) + pct}


def _pct(p) -> str:
    """概率 -> 「56.4%」（离散目标的占位符值）。"""
    return "n/a" if p is None or not isinstance(p, (int, float)) or not math.isfinite(p) else f"{100 * p:.1f}%"


def key_assumptions_template(used: list, year: int, keep_ids=frozenset(), discrete: bool = False) -> str:
    """最终答案末尾的「Key assumptions」：由代码按校验后的假设生成，数字只通过占位符出现。
    discrete：离散目标的假设是某个结果的概率，代码直接用它的值（不采样），所以不列范围。"""
    if not used:
        return ("Key assumptions: none (every probability input is an observed data point)." if discrete else
                "Key assumptions: none (every formula input is an observed data point).")
    lines = ["Key assumptions (proposed by the analyst model, not observed; code uses each value as given):" if discrete else
             "Key assumptions (proposed by the analyst model, not observed; code samples each one between the "
             "bounds shown):"]
    def clean(t):  # 模型写的文字：数字换成 [n]，不许拼出占位符
        return scrub_digits(t, year, keep_ids)[0].replace("[[", "[ [").replace("]]", "] ]")

    for a in used:
        unit = "" if a.get("is_pct") else " " + clean(a["unit"])
        widened = " (range widened by code)" if a.get("widened_by_floor") else ""
        line = (f"- {a['id']} {clean(a['name'])}: [[{a['id']}_value]]{unit}; used by {', '.join(a['used_by'])}." if discrete else
                f"- {a['id']} {clean(a['name'])}: [[{a['id']}_value]]{unit}, range [[{a['id']}_low]] to "
                f"[[{a['id']}_high]]{widened}; used by {', '.join(a['used_by'])}.")
        if a.get("falsified_by"):
            line += f" Overturned by: {clean(a['falsified_by'])}"
        lines.append(line)
    return "\n".join(lines)


JUDGE_MAX_TOKENS = 12000   # v2 的 6000 在 167 个数据点时被截断过
REPAIR = """

Your previous reply proposed these methods and assumptions:
{previous}

Code found these problems:
{errors}

Return the complete JSON object again. Keep your assessment and decisions unless the problems show they were wrong. Fix or drop each failing method. Where methods that do execute disagree strongly, decide which input or assumption is wrong and fix or drop that method instead of letting the methods be averaged. Keep at least one credible method that executes under the rules above. Do not repeat a rejected assumption in another wording."""
# 离散目标的修正轮（v2.3）：这一轮的结果列表通过了就固定不变；被拒了就要裁判在修正回复里给改好的列表
REPAIR_OUTCOMES_KEPT = """

The outcome list was accepted by code: keep it unchanged and copy its labels exactly:
__OUTCOMES__"""
# v2.3.1：修正轮看不到第一次回复的 decisions（表格里也不标），而代码按第一次回复的 decisions 校验依据 id
# （discrete6 两轮的修正列表都因此被拒）；修正回复里的 decisions 代码不采用，这里由代码列出已丢弃的点
REPAIR_DISCARDED = """

These points are discarded (by your decisions in the previous reply or in an earlier round), and decisions in this reply do not change that: do not use them in "outcomes_basis" or as method inputs: __IDS__"""
REPAIR_OUTCOMES_REJECTED = """

Code rejected the outcome list in your previous reply (see the problems above): return a corrected "outcomes" and "outcomes_basis"."""
REPAIR_OUTCOMES_REJECTED_KEEP = """ To keep the current list instead, leave "outcomes" out."""
OUTCOME_KEYS = ("outcomes", "outcomes_basis", "outcomes_revision_reason")


SERIES_METHODS = ("series_naive", "yoy_scaling", "linear_fit", "ratio")
TARGET_HISTORY_ROLE = "the target quantity itself (same entity and measure), for an earlier period of the same calendar span"


def _code_check(jr: dict, pts: list, target: dict, only_methods=None) -> tuple:
    """按 compute 的规则试跑裁判选的方法（纯代码，不调模型）。返回 (compute 结果, 假设校验结果, {方法下标: 失败原因})。"""
    by_id = {p["id"]: p for p in pts}
    av = AS.validate(jr.get("assumptions") or [], target)
    out = C.run(jr.get("methods") or [], by_id, target, assumptions=av, only_methods=only_methods)
    failed = {i: (m.get("error") or "no estimate") for i, m in enumerate(out.get("methods") or []) if not C.produced(m)}
    return out, av, failed


def _repair_errors(jr: dict, out: dict, av: dict, failed: dict) -> list:
    """至少一个方法能用 = 空列表；否则给裁判看的错误清单（每个方法为什么不能用 + 被拒的假设）。"""
    if len(failed) < len(jr.get("methods") or []):
        return []
    errs = [f"method {m.get('label') or m.get('id')} ({m.get('method')}): {failed.get(i, 'no estimate')}"
            for i, m in enumerate(out.get("methods") or [])]
    errs += [f"assumption {a.get('id')} rejected: {a.get('reason')}" for a in av["rejected"]]
    return errs or ["no methods were proposed"]


CONFLICT_RATIO = 3.0   # 能跑的方法之间差到这个倍数以上，就当作「至少一条路线的输入或假设错了」交回裁判
CONFLICT_TVD = 0.5     # 离散方法的对应规则：两个分布的 total variation distance 超过它（一半以上的概率换了结果）就交回裁判


def _problems(jr: dict, out: dict, av: dict, failed: dict) -> tuple:
    """(能跑的方法数, 交给裁判的问题清单)：失败的方法和原因、被拒的假设、能跑的方法之间差 CONFLICT_RATIO 倍以上
    （离散方法：分布的 total variation distance 超过 CONFLICT_TVD）。
    已有两条以上能跑而且互相吻合的方法时返回空清单。"""
    ms = out.get("methods") or []
    ok = [(i, m) for i, m in enumerate(ms) if i not in failed and C.produced(m)]
    num = [(i, m) for i, m in ok if m.get("estimate")]   # 离散方法没有 estimate，不做倍数冲突检查（连续值时 num == ok）
    probs = [f"method {m.get('label') or m.get('id')} ({m.get('method')}): {failed[i]}" for i, m in enumerate(ms) if i in failed]
    if probs:
        probs += [f"assumption {a.get('id')} rejected: {a.get('reason')}" for a in av["rejected"]]
    if len(num) >= 2:
        hi, lo = max(num, key=lambda x: x[1]["estimate"]), min(num, key=lambda x: x[1]["estimate"])
        if hi[1]["estimate"] / lo[1]["estimate"] > CONFLICT_RATIO:
            probs.append(f"methods disagree: {hi[1].get('label') or hi[1]['id']} gives {hi[1]['estimate']:,.0f} but "
                         f"{lo[1].get('label') or lo[1]['id']} gives {lo[1]['estimate']:,.0f} (more than {CONFLICT_RATIO:g}x apart); "
                         f"at least one route's input or assumption is wrong")
    dist = [(i, m) for i, m in ok if m.get("distribution")]   # 离散方法：分布之间的 total variation distance（连续值时为空）
    pairs = [(0.5 * sum(abs(a[1]["distribution"][k] - b[1]["distribution"].get(k, 0.0)) for k in a[1]["distribution"]), a, b)
             for n, a in enumerate(dist) for b in dist[n + 1:]]
    if pairs and max(pairs, key=lambda x: x[0])[0] > CONFLICT_TVD:
        tv, a, b = max(pairs, key=lambda x: x[0])

        def top(m):
            k = max(m["distribution"], key=m["distribution"].get)
            return f"most likely {k!r} ({100 * m['distribution'][k]:.1f}%)"
        probs.append(f"methods disagree: {a[1].get('label') or a[1]['id']} gives {top(a[1])} but {b[1].get('label') or b[1]['id']} "
                     f"gives {top(b[1])} (total variation distance {tv:.2f}, more than {CONFLICT_TVD:g}); at least one route's "
                     f"input, outcome assignment or remainder is wrong")
    if not ms:
        probs = ["no methods were proposed"]
    if len(ok) >= 2 and not any(x.startswith("methods disagree") for x in probs):
        return len(ok), []   # 已有两条以上互相吻合的路线：不交回裁判，免得把好结果改坏
    return len(ok), probs


def _dry_run_errors(jr: dict, pts: list, target: dict, only_methods=None) -> list:
    """只按代码规则检查（不做输入核对）。"""
    out, av, failed = _code_check(jr, pts, target, only_methods)
    return _repair_errors(jr, out, av, failed)


def _evidence(iid: str, by_id: dict, kept_a: dict) -> str:
    if iid in kept_a:
        a = kept_a[iid]
        return f'analyst assumption {iid}: "{a["name"]}" = {a["value"]} {a["unit"]}'
    p = by_id.get(iid)
    if p is None:
        return f"{iid}: unknown id"
    dom = urllib.parse.urlsplit(p.get("source_url", "")).netloc
    return (f'data point {iid}: "{p["name"]}" = {_fmt_num(p["value"])} {p.get("unit", "")}, period '
            f'{p.get("period_start") or "?"}..{p.get("period_end") or "?"}, source {dom}')


def _outcome_role(label: str, target: dict) -> str:
    """核对行里代码写的 role：target 取这个结果（裁判定义的列表里的那个，合并尾部带 or lower / or higher）的概率。"""
    o = next((o for o in (target or {}).get("outcomes") or [] if o["label"] == label), {})
    return f"probability that the target resolves to outcome '{label}'{D.value_text(o, (target or {}).get('unit', ''))}"


def _discrete_spec(target: dict, rec) -> str:
    """离散目标交给裁判的方法说明：结果列表一段（还没有 = 请裁判定义；已有 = 列出来、说明能否修订）+ outcome_probs。"""
    if rec and rec.get("list"):
        head = (DISCRETE_OUTCOMES_GIVEN.replace("__ROUND__", str(rec.get("revised_round") or rec.get("defined_round")))
                .replace("__IDS__", ", ".join((rec.get("basis") or {}).get("ids") or []) or "(none)")
                .replace("__OUTCOMES__", D.outcomes_text(D.with_outcomes(target, rec)))
                .replace("__REVISE__", DISCRETE_REVISE_DONE if rec.get("revised_round") else DISCRETE_REVISE))
    else:
        head = DISCRETE_OUTCOMES_DEFINE.replace("__KIND__", (target or {}).get("outcome_kind") or "not given")
    return head + "\n" + DISCRETE_METHODS_SPEC


def audit_rows(m_in: dict, m_out: dict, by_id: dict, kept_a: dict, target=None) -> list:
    """一个方法里要核对的输入：[(输入名, id, 裁判写的 role, 证据描述)]。日历常数不核对；序列方法核对 target_history。
    outcome_probs：role 由代码写成「target 取这个结果的概率」再附上裁判的 role（裁判没写 role 时留空，照旧拦下）；
    余下结果也核对一行（代码算的 1 - 其余之和、其余输入覆盖了哪些结果）。"""
    prm = m_in.get("params") or {}
    if m_out.get("method") == "formula_mc":
        rows = []
        for name, spec in (prm.get("inputs") or {}).items():
            spec = spec if isinstance(spec, dict) else {"id": spec}
            iid = str(spec.get("id"))
            if not iid.startswith("k_"):
                rows.append((name, iid, str(spec.get("role") or "").strip(), _evidence(iid, by_id, kept_a)))
        return rows
    if m_out.get("method") in SERIES_METHODS:
        return [(str(i), str(i), TARGET_HISTORY_ROLE, _evidence(str(i), by_id, kept_a)) for i in prm.get("target_history") or []]
    if m_out.get("method") == "outcome_probs":   # 每个结果的概率输入各核对一次，余下结果另核对一次
        rows, covered = [], []
        for label, spec in (prm.get("probs") or {}).items():
            spec = spec if isinstance(spec, dict) else {"id": spec}
            iid, role = str(spec.get("id")), str(spec.get("role") or "").strip()
            lab = next((d["label"] for d in m_out.get("inputs_detail") or [] if d["id"] == iid), str(label))
            covered.append(f"'{lab}' from {iid}")
            rows.append((str(label), iid, f"{_outcome_role(lab, target)}; analyst's role: {role}" if role else "",
                         _evidence(iid, by_id, kept_a)))
        rem = m_out.get("remainder")
        if rem and m_out.get("remainder_prob_before_normalising") is not None:
            rows.append((rem, "remainder", f"{_outcome_role(rem, target)}, taken as the rest (1 minus the other inputs)",
                         f"computed by code: 1 - {m_out.get('sum_given', 0):.3f} = {m_out['remainder_prob_before_normalising']:.3f}; "
                         f"the other inputs cover {', '.join(covered)}; outcomes with no input get 0: "
                         f"{m_out.get('zero_outcomes') or []}"))
        return rows
    return []


def _audit_header(mi: dict, mo: dict) -> str:
    prm = mi.get("params") or {}
    if mo.get("method") == "outcome_probs":
        rem = prm.get("remainder")
        return (f"{mo['id']} (outcome_probs): each input must be the probability of the named outcome. Mark it \"mismatch\" "
                f"when the evidence is the probability of a different outcome or event, or is not a probability at all (a "
                f"level, a rate, a change)" +
                (f"; the remainder outcome {rem!r} gets 1 minus the others: mark it \"mismatch\" when the probability left "
                 f"over by the other inputs does not belong to that outcome" if rem else ""))
    return f"{mo['id']} ({mo.get('method')}): {prm.get('formula') or mo.get('method')}"


def audit_methods(llm, qid: str, jr: dict, out: dict, av: dict, pts: list, failed: dict, target: dict) -> dict:
    """输入核对：对代码能跑的方法，问一次模型「每个输入的证据是不是公式需要的那个量」。返回 {方法下标: 原因}。
    核对本身失败（调用出错、超预算）时不拦方法，原因记在 jr["audit_error"]。"""
    by_id, kept_a = {p["id"]: p for p in pts}, {a["id"]: a for a in av["kept"]}
    res, blocks, index = {}, [], {}
    for i, (mi, mo) in enumerate(zip(jr.get("methods") or [], out.get("methods") or [])):
        if i in failed:
            continue
        rows = audit_rows(mi, mo, by_id, kept_a, target)
        no_role = [r[0] for r in rows if not r[2]]
        if no_role:
            res[i] = f"input audit: no role stated for {', '.join(no_role)}"
            continue
        if rows:
            index[mo["id"]] = i
            blocks.append(_audit_header(mi, mo) + "\n" +
                          "\n".join(f'  - {n}: role = "{role}"; evidence = {ev}' for n, _, role, ev in rows))
    if not blocks:
        return res
    basis = (target or {}).get("outcomes_basis") or {}
    if index and D.is_discrete(target) and (target or {}).get("outcomes"):   # 离散：先说明结果列表和它依据的点
        blocks.insert(0, AUDIT_OUTCOMES.replace("__OUTCOMES__", D.outcomes_text(target)).replace(
            "__BASIS__", "\n".join(f"  - {_evidence(i, by_id, {})}" for i in basis.get("ids") or []) or "  (not recorded)"))
    try:
        out_a, err = llm.ask(AUDIT_SYSTEM, AUDIT_USER.format(target=dumps(target), methods="\n\n".join(blocks)),
                                 role="audit", qid=qid, max_tokens=4000)
    except BudgetExceeded as e:
        out_a, err = None, str(e)
    if out_a is None:
        jr["audit_error"] = err
        return res
    for m in out_a.get("methods") or []:
        i = index.get(str(m.get("id")))
        bad = [f"{x.get('name')}: {x.get('reason', '')}"[:200] for x in m.get("inputs") or []
               if isinstance(x, dict) and str(x.get("verdict", "")).lower() == "mismatch"]
        if i is not None and bad:
            res[i] = "input audit: " + "; ".join(bad)
    return res


def build(ctx: Context):
    b = ctx.budget
    ablate = bool(getattr(ctx, "ablate_own_history", False))

    def plan(state: AgentState):
        notes = []
        try:
            out, err = ctx.llm.ask(PLAN_SYSTEM, PLAN_USER.format(question=state["question"], as_of=state["as_of"],
                                                                checklist=CHECKLIST), role="plan", qid=ctx.qid,
                                   max_tokens=6000)
        except BudgetExceeded as e:
            return {"aborted": str(e), "plan": {}, "directions": []}
        if out is None:
            return {"aborted": f"plan failed: {err}", "plan": {}, "directions": []}
        raw = [d for d in (out.get("directions") or []) if isinstance(d, dict)]
        cands = [_clean_direction(d, i + 1, "c") for i, d in enumerate(raw)]
        pool = cands
        if ablate:  # 消融：目标自身历史的方向一个都不跑，名额留给别的类别
            pool = [c for c in cands if c["category"] != "own_history"]
            for c in cands:
                if c["category"] == "own_history":
                    c.update(selected=False, ablation_dropped=True)
            notes.append(f"ablation: dropped {len(cands) - len(pool)} own_history candidate direction(s)")
        dirs = select_directions(pool, b.directions)
        notes.append(f"plan proposed {len(cands)} candidate directions in {len({c['category'] for c in cands})} categories; "
                     f"running {len(dirs)} (budget cap {b.directions})")
        if not any(d["category"] == "own_history" for d in dirs):
            notes.append("no own_history direction in plan")
        target = {k: str((out.get("target") or {}).get(k, ""))[:300]
                  for k in ("what", "unit", "period_start", "period_end", "publisher", "cadence", "caveats")}
        kind, note = D.parse_outcome_type(out.get("target") if isinstance(out.get("target"), dict) else {})
        if kind["outcome_type"] == "discrete" and not getattr(ctx, "allow_discrete", True):   # 见 run.prepare_run
            kind, note = {"outcome_type": "continuous"}, ("plan chose a discrete target, but this scored question is not "
                                                          "marked outcome_type 'discrete'; treated as continuous")
        target.update(kind)
        if note:
            notes.append(note)
        kws = [str(k).lower()[:30] for k in (out.get("market_keywords") or [])][:3]
        return {"plan": {"target": target, "market_keywords": kws, "candidates": cands}, "directions": dirs,
                "plan_notes": notes}

    def approve(state: AgentState):
        if state.get("aborted"):
            return {"approval": {"approved": False, "by": "abort"}}
        decision = interrupt({"target": state["plan"]["target"], "directions": state["directions"]})
        decision = decision if isinstance(decision, dict) else {"approved": bool(decision)}
        upd = {"approval": decision}
        if decision.get("directions"):  # 人可以改方向列表
            ds = [_clean_direction(d, i + 1, "d") for i, d in enumerate(decision["directions"][: b.directions])]
            upd["directions"] = [d for d in ds if not (ablate and d["category"] == "own_history")]
        return upd

    def fan_out(state: AgentState):
        if not state.get("approval", {}).get("approved"):
            return END
        t = state["plan"]["target"]
        sends = [Send("subagent", {"direction": d, "round": 1, "target": t}) for d in state["directions"]]
        return sends + [Send("markets", {"keywords": state["plan"].get("market_keywords", [])})]

    def subagent(task: dict):
        return {"results": [run_direction(ctx, task["target"], task["direction"], task["round"])]}

    def markets(task: dict):
        try:
            rec = search_markets(task.get("keywords") or [], ctx.as_of)
        except Exception as e:  # noqa: BLE001  外部接口出任何意外都不能让整题崩掉
            rec = {"keywords": task.get("keywords") or [], "markets": [], "points": [],
                   "note": f"markets tool error {type(e).__name__}: {e}"[:200]}
        for p in rec["points"]:
            p.update(direction_id="markets", round=1, order=(0, 0), keep=True)
        return {"results": [{"direction_id": "markets", "round": 1, "markets": rec, "points": rec["points"],
                             "pages": [], "dropped_points": []}]}

    def judge(state: AgentState):
        rnd = len(state.get("judge_rounds") or []) + 1
        # 给新数据点编号：按 (轮次, 方向, 页面顺序, 点顺序) 排序，保证可复现
        old = {(p["direction_id"], tuple(p["order"]), p["source_url"]): p for p in state.get("points") or []}
        new = []
        for res in sorted(state.get("results") or [], key=lambda r: (r["round"], r["direction_id"])):
            for p in res.get("points") or []:
                k = (p["direction_id"], tuple(p["order"]), p["source_url"])
                if k not in old:
                    new.append(p)
        pts = [dict(p) for p in old.values()]
        for i, p in enumerate(new, start=len(pts) + 1):
            pts.append({**p, "id": f"p{i}", "keep": True})
        if ablate:  # 消融：目标自身更早期间的值不进裁判的表格（规则见 ablation.py），state 里保留并标原因
            by_id = {d["id"]: d for d in state.get("directions") or []}
            for p in pts:
                why = p.get("ablation_excluded") or AB.own_value_reason(p, state["plan"]["target"], by_id)
                if why:
                    p.update(keep=False, ablation_excluded=why)
        shown = [p for p in pts if not p.get("ablation_excluded")]
        upd = {"points": pts}
        if state.get("aborted") or b.aborted:
            return {**upd, "judge_rounds": [{"round": rnd, "skipped": b.aborted or state.get("aborted")}]}
        dirs = "\n".join(f"- {d['id']} [{d['category']}] {d['hypothesis']}" for d in state["directions"])
        target0 = state["plan"]["target"]
        disc, orec = D.is_discrete(target0), state.get("outcomes")   # orec：之前的轮次定下的结果列表（离散目标）

        def judge_prompt(rec):
            return JUDGE_USER.format(
                question=state["question"], as_of=state["as_of"], target=dumps(target0),
                directions=dirs, table=_table(shown) if shown else "(no verified data points)",
                methods_spec=(_discrete_spec(target0, rec) if disc else AB.methods_spec() if ablate else METHODS_SPEC),
                extra_rule=EXTRA_RULE_R1 if rnd == 1 else EXTRA_RULE_R2)
        judge_user = judge_prompt(orec)
        try:
            out, err = ctx.llm.ask(JUDGE_SYSTEM, judge_user, role=f"judge:r{rnd}", qid=ctx.qid, max_tokens=JUDGE_MAX_TOKENS)
        except BudgetExceeded as e:
            return {**upd, "aborted": str(e), "judge_rounds": [{"round": rnd, "skipped": str(e)}]}
        if out is None:
            return {**upd, "judge_rounds": [{"round": rnd, "error": err}]}
        ids = {p["id"] for p in shown}
        # 裁判只列要丢的点（逐点表态会让输出超过 max_tokens，9 月第二轮就是这样失败的）；没列的点 = 保留
        dec = {str(x.get("id")): x for x in out.get("decisions") or [] if isinstance(x, dict)}
        for p in shown:
            p["judged_round"] = rnd
            if p["id"] in dec:
                p["keep"] = bool(dec[p["id"]].get("keep", False))
                p["judge_reason"] = str(dec[p["id"]].get("reason", ""))[:300]
        extra = []
        if rnd == 1:
            raw = [x for x in out.get("extra_directions") or [] if isinstance(x, dict)][: b.extra_directions]
            extra = [{**_clean_direction(x, i + 1, "b"), "category": (str(x.get("category", "")).strip() if str(x.get("category", "")).strip() in CATEGORIES else "base_rates")} for i, x in enumerate(raw)]
        dropped_extra = [x["id"] for x in extra if ablate and x["category"] == "own_history"]
        extra = [x for x in extra if x["id"] not in dropped_extra]
        raw_a = out.get("assumptions") if isinstance(out.get("assumptions"), list) else []
        jr = {"round": rnd, "assessment": out.get("assessment") or [], "decisions": list(dec.values()),
              "extra_directions": extra, "methods": [m for m in out.get("methods") or [] if isinstance(m, dict)],
              "assumptions": raw_a[:20], "unknown_ids_in_decisions": sorted(set(dec) - ids)}
        if dropped_extra:
            jr["ablation_dropped_extra_directions"] = dropped_extra
        oerrs, orec_new = [], orec
        if disc:   # 离散目标（v2.3）：裁判这一轮的结果列表（定义 / 沿用 / 修订）先过代码校验；依据的 id 必须是这一轮保留的点
            kept_ids = {p["id"] for p in shown if p.get("keep")}
            jr["outcomes_reply"] = {k: out[k] for k in OUTCOME_KEYS if k in out}
            orec_new, oerrs = D.accept_outcomes(out, orec, rnd, kept_ids)
            jr["outcome_errors"] = oerrs
        need_check = rnd == 2 or not extra
        if need_check or oerrs:
            # 这一轮的方法就是 compute 要用的：代码试跑 + 输入核对（另一次模型调用：每个输入实际是什么 vs 公式需要它是什么），
            # 一个方法都过不了就把原因交回裁判修一次；核对没过的方法 compute 不用。
            # 离散目标的结果列表被拒时也交回修正轮（第一轮还要再搜时只修列表，方法留到第二轮再核对）
            only = None if disc else (AB.ALLOWED_METHODS if ablate else None)   # 消融只针对连续值目标

            def check(t):
                out_c, av_c, failed = _code_check(jr, pts, t, only)
                aud = audit_methods(ctx.llm, ctx.qid, jr, out_c, av_c, pts, failed, t)
                failed.update(aud)
                return (aud, *_problems(jr, out_c, av_c, failed))

            target = D.with_outcomes(target0, orec_new) if disc else target0
            # 有方法失败、或能跑的方法互相打架，就交回裁判修一次；修完一个都跑不了而原来能跑，就退回原方案
            aud, n_ok, errs = check(target) if need_check else ({}, 0, [])
            errs = oerrs + errs
            if errs:
                jr["repair"] = {"errors": errs}
                prev_reply = {"methods": jr["methods"], "assumptions": jr["assumptions"]}
                note, repair_user = "", judge_user
                if disc:
                    prev_reply = {**jr["outcomes_reply"], **prev_reply}
                    note = (REPAIR_OUTCOMES_REJECTED + (REPAIR_OUTCOMES_REJECTED_KEEP if orec else "") if oerrs else
                            REPAIR_OUTCOMES_KEPT.replace("__OUTCOMES__", D.outcomes_text(D.with_outcomes(target0, orec_new))))
                    gone = [p["id"] for p in shown if not p.get("keep")]
                    if gone:
                        note += REPAIR_DISCARDED.replace("__IDS__", ", ".join(gone))
                    if orec and orec_new is not orec:   # 这一轮修订了列表、已通过：方法说明按新列表重写（不再写旧列表和「可以修订」）
                        repair_user = judge_prompt(orec_new)
                try:
                    out2, err2 = ctx.llm.ask(JUDGE_SYSTEM, repair_user + REPAIR.format(
                        previous=dumps(prev_reply), errors="\n".join(f"- {e}" for e in errs)) + note,
                        role=f"judge:r{rnd}:repair", qid=ctx.qid, max_tokens=JUDGE_MAX_TOKENS)
                except BudgetExceeded as e:
                    out2, err2 = None, str(e)
                if out2 is None:
                    jr["repair"]["error"] = err2
                else:
                    prev = (jr["methods"], jr["assumptions"], aud, orec_new)
                    jr["repair"]["previous_methods"], jr["repair"]["previous_assumptions"] = prev[0], prev[1]
                    jr["methods"] = [m for m in out2.get("methods") or [] if isinstance(m, dict)]
                    a2 = out2.get("assumptions")
                    jr["assumptions"] = (a2 if isinstance(a2, list) else [])[:20]
                    oerrs2 = []
                    if disc:   # 修正回复里的 decisions 只记录、不采用（保留的点仍按第一次回复定）
                        jr["repair"]["decisions_in_reply"] = [x for x in out2.get("decisions") or [] if isinstance(x, dict)]
                    if oerrs:   # 离散目标的列表被拒过：修正回复里的列表重新校验（通过了的列表在这一轮里不再改）
                        jr["repair"]["outcomes_reply"] = {k: out2[k] for k in OUTCOME_KEYS if k in out2}
                        orec_new, oerrs2 = D.accept_outcomes(out2, orec, rnd, kept_ids)
                        jr["repair"]["outcome_errors_after"] = oerrs2
                        target = D.with_outcomes(target0, orec_new)
                    if need_check:
                        aud, n_ok2, errs_after = check(target)
                        jr["repair"]["errors_after"] = oerrs2 + errs_after
                        if n_ok2 == 0 and n_ok > 0:
                            jr["methods"], jr["assumptions"], aud, orec_new = prev
                            jr["repair"]["reverted"] = "repaired methods could not execute; kept the original ones"
                    else:
                        jr["repair"]["errors_after"] = oerrs2
            if need_check:
                jr["audit_failed"] = {str(i): r for i, r in aud.items()}
        upd.update(points=pts, judge_rounds=[jr])
        if disc:
            upd["outcomes"] = orec_new
        if extra:
            upd["directions"] = state["directions"] + extra
        return upd

    def after_judge(state: AgentState):
        jr = state["judge_rounds"][-1]
        if jr.get("round") == 1 and jr.get("extra_directions") and not b.aborted:
            t = state["plan"]["target"]
            return [Send("subagent", {"direction": d, "round": 2, "target": t}) for d in jr["extra_directions"]]
        return "compute"

    def compute(state: AgentState):
        jr = next((j for j in reversed(state.get("judge_rounds") or []) if j.get("methods")), {})
        pts = {p["id"]: p for p in state.get("points") or []}
        target = D.with_outcomes(state["plan"]["target"], state.get("outcomes"))   # 离散：裁判定义的结果列表
        av = AS.validate(jr.get("assumptions") or [], target)
        bad = jr.get("audit_failed") or {}
        methods = [m for i, m in enumerate(jr.get("methods") or []) if str(i) not in bad]
        out = C.run(methods, pts, target, assumptions=av,
                    only_methods=AB.ALLOWED_METHODS if ablate and not D.is_discrete(target) else None)
        out["excluded_by_input_audit"] = [{"label": str(m.get("id", "")), "method": m.get("method"), "reason": bad[str(i)]}
                                          for i, m in enumerate(jr.get("methods") or []) if str(i) in bad]
        out["methods_from_round"] = jr.get("round")
        labels = {m["id"]: m.get("label") for m in out["methods"]}
        for a in av["kept"]:
            a["used_by"] = out["assumptions_used_by"].get(a["id"], [])
            a["used_by_labels"] = [labels.get(m) for m in a["used_by"]]
        av.update(from_round=jr.get("round"), min_width=AS.MIN_WIDTH, max_per_run=AS.MAX_PER_RUN,
                  max_per_method=AS.MAX_PER_METHOD)
        return {"compute": out, "assumptions": av}

    def published(state: AgentState):
        """「答案已公布」（v2.4，规则在 published.py）：只在真实使用时检查（ctx.check_published 由 run.prepare_run 设定：
        as_of 是今天、题目没有登记真值）；回测不调模型。确认了就把 compute.result 换成这个值，原来的估计留作参考。"""
        if not getattr(ctx, "check_published", False):
            return {"published": {"status": "not_checked", "note": PB.NOT_CHECKED}}
        target = state["plan"]["target"]
        cands, note = PB.candidates(state.get("points") or [], target, ctx.as_of)
        if not cands:
            return {"published": {"status": "no_candidates", "note": note, "candidates": []}}
        system, user = PB.prompt(target, state["as_of"], cands)
        try:
            out, err = ctx.llm.ask(system, user, role="published", qid=ctx.qid, max_tokens=3000)
        except BudgetExceeded as e:
            return {"published": {"status": "skipped", "note": f"{note}; {e}", "candidates": [PB._summary(p) for p in cands]}}
        if out is None:
            return {"published": {"status": "error", "error": err, "note": note, "candidates": [PB._summary(p) for p in cands]}}
        tw = D.with_outcomes(target, state.get("outcomes"))
        rec = {**PB.resolve(out, cands, tw), "note": note}
        upd = {"published": rec}
        if rec["status"] == "published":
            comp = state.get("compute") or {}
            upd["compute"] = {**comp, "result": PB.result(rec, comp.get("result") or {}, tw),
                              "estimate_result": comp.get("result")}
        return upd

    def after_compute(state: AgentState):
        return "jev" if D.is_discrete(state["plan"]["target"]) else "final"

    def jev(state: AgentState):
        """离散目标的 Jev 对照臂（代码写简报、问一次；不并入 agent 的答案）。没配置 key 文件就记 not_configured。"""
        if b.aborted:
            return {"jev": {"arm": "jev", "status": "skipped", "note": f"run aborted: {b.aborted}"}}
        kept = [p for p in state.get("points") or [] if p.get("keep") and p.get("judged_round")]
        target = D.with_outcomes(state["plan"]["target"], state.get("outcomes"))
        if not target.get("outcomes"):
            return {"jev": {"arm": "jev", "status": "skipped", "note": "no outcome list (the judge did not define a valid one)"}}
        try:
            return {"jev": J.run_arm(target, kept, state["as_of"], qid=ctx.qid,
                                     log=getattr(ctx.llm, "_log", None))}
        except Exception as e:  # noqa: BLE001  对照臂出任何意外都不能让整题崩掉（同 markets 节点）
            return {"jev": {"arm": "jev", "status": "error", "error": f"jev arm error {type(e).__name__}"[:200]}}

    def final(state: AgentState):
        """已公布（published.py）：终稿由代码写；确认的点互相矛盾：照常写估计的终稿，后面附一句。"""
        pub = state.get("published") or {}
        if pub.get("status") == "published":
            return {"final": PB.final_text(state)}
        out = final_estimate(state)
        if pub.get("status") == "conflict":
            note = "\n\n" + PB.conflict_note(pub)
            out["final"] = {**out["final"], "text": out["final"]["text"] + note, "template": out["final"]["template"] + note}
        return out

    def final_estimate(state: AgentState):
        comp = state.get("compute") or {}
        r = comp.get("result") or {}
        if r.get("mode") == "discrete":
            return {"final": final_discrete(state, comp, r)}
        ph = {"estimate": _fmt_num(r.get("central")), "p10": _fmt_num(r.get("p10")), "p90": _fmt_num(r.get("p90")),
              "interval_level": "80%", "interval_basis": str(r.get("basis", "")).replace("_", " "),
              "n_points_kept": str(sum(1 for p in state.get("points") or [] if p.get("keep") and p.get("judged_round"))),
              "n_methods": str(sum(1 for m in comp.get("methods") or [] if m.get("estimate")))}
        summary = []
        for m in comp.get("methods") or []:
            mid = re.sub(r"[^a-z0-9]", "", m["id"].lower()) or "m"
            ph[f"{mid}_estimate"] = _fmt_num(m.get("estimate"))
            ph[f"{mid}_weight"] = f"{100 * (r.get('weights') or {}).get(m['id'], 0):.0f}%"
            e = m.get("backtest_mean_abs_log_err")
            ph[f"{mid}_backtest_error"] = "n/a" if e is None else f"{100 * (math.exp(e) - 1):.1f}%"
            summary.append(f"- {m['id']} {m['method']}: estimate {ph[f'{mid}_estimate']}, weight {ph[f'{mid}_weight']}, "
                           f"backtest mean error {ph[f'{mid}_backtest_error']}, error: {m.get('error', '')}; {m.get('rationale', '')}")
            if m.get("inputs_detail"):
                summary.append(f"  inputs of {m['id']}: observed points {m.get('used_ids') or []}, "
                               f"assumptions {m.get('used_assumptions') or []}")
        used_a = [a for a in (state.get("assumptions") or {}).get("kept") or [] if a.get("used_by")]
        for a in used_a:
            ph.update(assumption_placeholders(a))
            summary.append(f"- assumption {a['id']} (proposed by the analyst, not observed; used by {a['used_by']}): "
                           f"{a['name']}, value {ph[a['id'] + '_value']}, range used by code {ph[a['id'] + '_low']} to "
                           f"{ph[a['id'] + '_high']} ({a['unit']}); rationale: {a['rationale']}")
        summary.insert(0, f"combined estimate {ph['estimate']}, 80% interval {ph['p10']} to {ph['p90']} (basis: {ph['interval_basis']})")
        default = ("Estimate: [[estimate]] ([[interval_level]] interval [[p10]] to [[p90]], basis: [[interval_basis]]), "
                   "from [[n_methods]] method(s) over [[n_points_kept]] kept data points.")
        text, model_text, digits_removed, err = default, None, 0, None
        if r.get("central") is not None and not b.aborted:
            try:
                out, err = ctx.llm.ask(FINAL_SYSTEM, FINAL_USER.format(
                    question=state["question"], as_of=state["as_of"], target=dumps(state["plan"]["target"]),
                    summary="\n".join(summary), placeholders=", ".join(f"[[{k}]]" for k in ph)), role="final", qid=ctx.qid)
                model_text = (out or {}).get("answer") if out else None
            except BudgetExceeded as e:
                err = str(e)
        if isinstance(model_text, str) and model_text.strip():
            text = model_text
        # 模型不许写数字：占位符以外的数字一律换成 [n]（只留年份上下文里、离 as_of 不超过 10 年的四位年份和方法 id）。
        # 渲染按切分后的片段拼，不再对拼好的文字重新找占位符，"[" + "[n]" + "]" 不会被当成占位符。
        parts = PLACEHOLDER.split(text)
        year = int(state["as_of"][:4])
        mids = {m["id"] for m in comp.get("methods") or []} | {a["id"] for a in used_a}
        for i in range(0, len(parts), 2):
            parts[i], n = scrub_digits(parts[i], year, mids)
            digits_removed += n
        text = "".join(p if i % 2 == 0 else f"[[{p}]]" for i, p in enumerate(parts))
        if r.get("central") is not None:  # 代码生成的假设清单：数字只走占位符，模型写的名字和理由里的数字同样替换掉
            extra = "\n\n" + key_assumptions_template(used_a, year, mids)
            text += extra
            eparts = PLACEHOLDER.split(extra)  # 只切新加的这段，前面已经切好的片段不重新找占位符
            parts[-1] += eparts[0]
            parts += eparts[1:]
        rendered = "".join(p if i % 2 == 0 else ph.get(p, "[unknown placeholder]") for i, p in enumerate(parts))
        if r.get("central") is None:
            rendered = "No estimate: no estimation method could be computed from the verified evidence."
        return {"final": {"template": text, "text": rendered, "placeholders": ph, "digits_removed": digits_removed,
                          "model_error": err, "used_model_text": model_text is not None}}

    def final_discrete(state: AgentState, comp: dict, r: dict) -> dict:
        """离散目标的终稿：代码生成「每个结果 + 概率」的几行（数字只走占位符），后面接模型写的简短理由（数字换成 [n]），
        再接代码生成的假设清单。"""
        ok = [m for m in comp.get("methods") or [] if m.get("distribution")]
        ph = {"n_methods": str(len(ok)), "most_likely": str(r.get("most_likely") or "n/a"),
              "most_likely_prob": _pct(r.get("most_likely_prob")),
              "n_points_kept": str(sum(1 for p in state.get("points") or [] if p.get("keep") and p.get("judged_round")))}
        lines = ["Outcome probabilities for the pinned target (computed by code from the cited evidence; equal-weight "
                 "average of [[n_methods]] method(s) over [[n_points_kept]] kept data points):"]
        for i, o in enumerate(r.get("outcomes") or [], start=1):
            ph[f"o{i}_label"], ph[f"o{i}_prob"], ph[f"o{i}_value"] = o["label"], _pct(o.get("prob")), _fmt_num(o.get("value"))
            lines.append(f"- [[o{i}_label]]: [[o{i}_prob]]")
        lines.append("Most likely outcome: [[most_likely]] ([[most_likely_prob]]).")
        summary = [f"pooled outcome probabilities: " + "; ".join(f"{o['label']} {_pct(o.get('prob'))}" for o in r.get("outcomes") or [])]
        for m in comp.get("methods") or []:
            mid = re.sub(r"[^a-z0-9]", "", m["id"].lower()) or "m"
            if m.get("distribution"):
                for i, o in enumerate(r.get("outcomes") or [], start=1):
                    ph[f"{mid}_o{i}_prob"] = _pct(m["distribution"].get(o["label"]))
                src = "; ".join(f"{d['label']} <- {d['kind']} {d['id']}" for d in m.get("inputs_detail") or [])
                summary.append(f"- {m['id']} outcome_probs: inputs {src}; remainder {m.get('remainder')}; {m.get('rationale', '')}")
            else:
                summary.append(f"- {m['id']} {m.get('method')}: failed: {m.get('error', '')}")
        used_a = [a for a in (state.get("assumptions") or {}).get("kept") or [] if a.get("used_by")]
        for a in used_a:
            ph.update(assumption_placeholders(a))
            summary.append(f"- assumption {a['id']} (proposed by the analyst, not observed; used by {a['used_by']}): "
                           f"{a['name']}, value {ph[a['id'] + '_value']}; rationale: {a['rationale']}")
        model_text, err = None, None
        if r.get("most_likely") is not None and not b.aborted:
            try:
                out, err = ctx.llm.ask(FINAL_SYSTEM, FINAL_USER_DISCRETE.format(
                    question=state["question"], as_of=state["as_of"], target=dumps(D.with_outcomes(state["plan"]["target"], state.get("outcomes"))),
                    summary="\n".join(summary), placeholders=", ".join(f"[[{k}]]" for k in ph)), role="final", qid=ctx.qid)
                model_text = (out or {}).get("answer") if out else None
            except BudgetExceeded as e:
                err = str(e)
        year = int(state["as_of"][:4])
        # 保留方法 id、假设 id，以及方法实际引用的数据点 id（理由里要说概率来自哪个点）；其余数字一律换成 [n]
        mids = ({m["id"] for m in comp.get("methods") or []} | {a["id"] for a in used_a} |
                {i for m in ok for i in m.get("used_ids") or []})
        segs, digits_removed = ["\n".join(lines)], 0
        if isinstance(model_text, str) and model_text.strip():
            parts = PLACEHOLDER.split(model_text)
            for i in range(0, len(parts), 2):   # 模型写的数字一律换成 [n]（规则同连续值的终稿）
                parts[i], n = scrub_digits(parts[i], year, mids)
                digits_removed += n
            segs.append("".join(p if i % 2 == 0 else f"[[{p}]]" for i, p in enumerate(parts)))
        segs.append(key_assumptions_template(used_a, year, mids, discrete=True))
        text = "\n\n".join(segs)
        # 渲染：先切好每一段再拼，"[" + "[n]" + "]" 不会被当成占位符（同连续值的终稿）
        rendered = "\n\n".join("".join(p if i % 2 == 0 else ph.get(p, "[unknown placeholder]")
                                       for i, p in enumerate(PLACEHOLDER.split(s))) for s in segs)
        if r.get("most_likely") is None:
            rendered = ("No estimate: no outcome-probability method could be computed from the verified evidence."
                        if r.get("outcomes") else "No estimate: the judge did not define a valid outcome list for this "
                                                  "discrete target.")
        return {"template": text, "text": rendered, "placeholders": ph, "digits_removed": digits_removed,
                "model_error": err, "used_model_text": model_text is not None}

    g = StateGraph(AgentState)
    for name, fn in [("plan", plan), ("approve", approve), ("subagent", subagent), ("markets", markets),
                     ("judge", judge), ("compute", compute), ("published", published), ("jev", jev), ("final", final)]:
        g.add_node(name, fn)
    g.add_edge(START, "plan")
    g.add_edge("plan", "approve")
    g.add_conditional_edges("approve", fan_out, ["subagent", "markets", END])
    g.add_edge("subagent", "judge")
    g.add_edge("markets", "judge")
    g.add_conditional_edges("judge", after_judge, ["subagent", "compute"])
    g.add_edge("compute", "published")
    g.add_conditional_edges("published", after_compute, ["jev", "final"])
    g.add_edge("jev", "final")
    g.add_edge("final", END)
    return g.compile(checkpointer=InMemorySaver())
