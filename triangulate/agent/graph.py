"""LangGraph 状态图：plan -> approve(interrupt) -> [Send: 每个方向一个 subagent + markets] -> judge
-> (可选一轮 base-rate 方向 -> judge) -> compute -> final。
裁判可以为 formula_mc 提出假设输入（assumptions.py 校验）；--ablate-own-history 时按 ablation.py 去掉目标自身的历史。

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
from .markets import search_markets
from .pipeline import BudgetExceeded, Context, dumps, run_direction
from .prompts import (CHECKLIST, EXTRA_RULE_R1, EXTRA_RULE_R2, FINAL_SYSTEM, FINAL_USER, JUDGE_SYSTEM, JUDGE_USER,
                      METHODS_SPEC, PLAN_SYSTEM, PLAN_USER)

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


def key_assumptions_template(used: list, year: int, keep_ids=frozenset()) -> str:
    """最终答案末尾的「Key assumptions」：由代码按校验后的假设生成，数字只通过占位符出现。"""
    if not used:
        return "Key assumptions: none (every formula input is an observed data point)."
    lines = ["Key assumptions (proposed by the analyst model, not observed; code samples each one between the "
             "bounds shown):"]
    def clean(t):  # 模型写的文字：数字换成 [n]，不许拼出占位符
        return scrub_digits(t, year, keep_ids)[0].replace("[[", "[ [").replace("]]", "] ]")

    for a in used:
        unit = "" if a.get("is_pct") else " " + clean(a["unit"])
        widened = " (range widened by code)" if a.get("widened_by_floor") else ""
        line = (f"- {a['id']} {clean(a['name'])}: [[{a['id']}_value]]{unit}, range [[{a['id']}_low]] to "
                f"[[{a['id']}_high]]{widened}; used by {', '.join(a['used_by'])}.")
        if a.get("falsified_by"):
            line += f" Overturned by: {clean(a['falsified_by'])}"
        lines.append(line)
    return "\n".join(lines)


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
        try:
            out, err = ctx.llm.ask(JUDGE_SYSTEM, JUDGE_USER.format(
                question=state["question"], as_of=state["as_of"], target=dumps(state["plan"]["target"]),
                directions=dirs, table=_table(shown) if shown else "(no verified data points)",
                methods_spec=AB.methods_spec() if ablate else METHODS_SPEC,
                extra_rule=EXTRA_RULE_R1 if rnd == 1 else EXTRA_RULE_R2), role=f"judge:r{rnd}", qid=ctx.qid, max_tokens=6000)
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
        upd.update(points=pts, judge_rounds=[jr])
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
        target = state["plan"]["target"]
        av = AS.validate(jr.get("assumptions") or [], target)
        out = C.run(jr.get("methods") or [], pts, target, assumptions=av,
                    only_methods=AB.ALLOWED_METHODS if ablate else None)
        out["methods_from_round"] = jr.get("round")
        labels = {m["id"]: m.get("label") for m in out["methods"]}
        for a in av["kept"]:
            a["used_by"] = out["assumptions_used_by"].get(a["id"], [])
            a["used_by_labels"] = [labels.get(m) for m in a["used_by"]]
        av.update(from_round=jr.get("round"), min_width=AS.MIN_WIDTH, max_per_run=AS.MAX_PER_RUN,
                  max_per_method=AS.MAX_PER_METHOD)
        return {"compute": out, "assumptions": av}

    def final(state: AgentState):
        comp = state.get("compute") or {}
        r = comp.get("result") or {}
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

    g = StateGraph(AgentState)
    for name, fn in [("plan", plan), ("approve", approve), ("subagent", subagent), ("markets", markets),
                     ("judge", judge), ("compute", compute), ("final", final)]:
        g.add_node(name, fn)
    g.add_edge(START, "plan")
    g.add_edge("plan", "approve")
    g.add_conditional_edges("approve", fan_out, ["subagent", "markets", END])
    g.add_edge("subagent", "judge")
    g.add_edge("markets", "judge")
    g.add_conditional_edges("judge", after_judge, ["subagent", "compute"])
    g.add_edge("compute", "final")
    g.add_edge("final", END)
    return g.compile(checkpointer=InMemorySaver())
