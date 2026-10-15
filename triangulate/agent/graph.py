"""LangGraph 状态图：plan -> approve(interrupt) -> [Send: 每个方向一个 subagent + markets] -> judge
-> (可选一轮 base-rate 方向 -> judge) -> compute -> final。

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
    final: dict
    aborted: str


def _clean_direction(d: dict, i: int, prefix: str) -> dict:
    cat = str(d.get("category", "")).strip()
    return {"id": f"{prefix}{i}", "category": cat if cat in CATEGORIES else "related_series",
            "perspective": str(d.get("perspective", ""))[:200], "hypothesis": str(d.get("hypothesis", ""))[:600],
            "data_to_find": str(d.get("data_to_find", ""))[:600],
            "search_hints": [str(h)[:120] for h in (d.get("search_hints") or [])][:4]}


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


def build(ctx: Context):
    b = ctx.budget

    def plan(state: AgentState):
        notes = []
        try:
            out, err = ctx.llm.ask(PLAN_SYSTEM, PLAN_USER.format(question=state["question"], as_of=state["as_of"],
                                                                checklist=CHECKLIST), role="plan", qid=ctx.qid)
        except BudgetExceeded as e:
            return {"aborted": str(e), "plan": {}, "directions": []}
        if out is None:
            return {"aborted": f"plan failed: {err}", "plan": {}, "directions": []}
        dirs = [d for d in (out.get("directions") or []) if isinstance(d, dict)]
        if len(dirs) > b.directions:
            notes.append(f"plan proposed {len(dirs)} directions; kept the first {b.directions} (soft cap)")
        dirs = [_clean_direction(d, i + 1, "d") for i, d in enumerate(dirs[: b.directions])]
        if not any(d["category"] == "own_history" for d in dirs):
            notes.append("no own_history direction in plan")
        target = {k: str((out.get("target") or {}).get(k, ""))[:300]
                  for k in ("what", "unit", "period_start", "period_end", "publisher", "cadence", "caveats")}
        kws = [str(k).lower()[:30] for k in (out.get("market_keywords") or [])][:3]
        return {"plan": {"target": target, "market_keywords": kws}, "directions": dirs, "plan_notes": notes}

    def approve(state: AgentState):
        if state.get("aborted"):
            return {"approval": {"approved": False, "by": "abort"}}
        decision = interrupt({"target": state["plan"]["target"], "directions": state["directions"]})
        decision = decision if isinstance(decision, dict) else {"approved": bool(decision)}
        upd = {"approval": decision}
        if decision.get("directions"):  # 人可以改方向列表
            upd["directions"] = [_clean_direction(d, i + 1, "d") for i, d in enumerate(decision["directions"][: b.directions])]
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
        rec = search_markets(task.get("keywords") or [], ctx.as_of)
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
        upd = {"points": pts}
        if state.get("aborted") or b.aborted:
            return {**upd, "judge_rounds": [{"round": rnd, "skipped": b.aborted or state.get("aborted")}]}
        dirs = "\n".join(f"- {d['id']} [{d['category']}] {d['hypothesis']}" for d in state["directions"])
        try:
            out, err = ctx.llm.ask(JUDGE_SYSTEM, JUDGE_USER.format(
                question=state["question"], as_of=state["as_of"], target=dumps(state["plan"]["target"]),
                directions=dirs, table=_table(pts) if pts else "(no verified data points)", methods_spec=METHODS_SPEC,
                extra_rule=EXTRA_RULE_R1 if rnd == 1 else EXTRA_RULE_R2), role=f"judge:r{rnd}", qid=ctx.qid, max_tokens=6000)
        except BudgetExceeded as e:
            return {**upd, "aborted": str(e), "judge_rounds": [{"round": rnd, "skipped": str(e)}]}
        if out is None:
            return {**upd, "judge_rounds": [{"round": rnd, "error": err}]}
        ids = {p["id"] for p in pts}
        dec = {str(x.get("id")): x for x in out.get("decisions") or [] if isinstance(x, dict)}
        for p in pts:
            if p["id"] in dec:
                p["keep"] = bool(dec[p["id"]].get("keep", True))
                p["judge_reason"] = str(dec[p["id"]].get("reason", ""))[:300]
        extra = []
        if rnd == 1:
            raw = [x for x in out.get("extra_directions") or [] if isinstance(x, dict)][: b.extra_directions]
            extra = [{**_clean_direction(x, i + 1, "b"), "category": "base_rates"} for i, x in enumerate(raw)]
        jr = {"round": rnd, "assessment": out.get("assessment") or [], "decisions": list(dec.values()),
              "extra_directions": extra, "methods": [m for m in out.get("methods") or [] if isinstance(m, dict)],
              "unknown_ids_in_decisions": sorted(set(dec) - ids)}
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
        out = C.run(jr.get("methods") or [], pts, state["plan"]["target"])
        out["methods_from_round"] = jr.get("round")
        return {"compute": out}

    def final(state: AgentState):
        comp = state.get("compute") or {}
        r = comp.get("result") or {}
        ph = {"estimate": _fmt_num(r.get("central")), "p10": _fmt_num(r.get("p10")), "p90": _fmt_num(r.get("p90")),
              "interval_basis": str(r.get("basis", "")).replace("_", " "),
              "n_points_kept": str(sum(1 for p in state.get("points") or [] if p.get("keep"))),
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
        summary.insert(0, f"combined estimate {ph['estimate']}, 80% interval {ph['p10']} to {ph['p90']} (basis: {ph['interval_basis']})")
        default = ("Estimate: [[estimate]] (80% interval [[p10]] to [[p90]], basis: [[interval_basis]]), "
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
            # 模型不许写数字：占位符以外的数字（四位年份除外）一律换成 [n]
            parts = PLACEHOLDER.split(model_text)
            for i in range(0, len(parts), 2):
                cleaned, n = re.subn(r"(?<![\w\[])(?!(?:19|20)\d{2}\b)\d[\d,.]*%?", "[n]", parts[i])
                parts[i], digits_removed = cleaned, digits_removed + n
            text = "".join(p if i % 2 == 0 else f"[[{p}]]" for i, p in enumerate(parts))
        rendered = PLACEHOLDER.sub(lambda m: ph.get(m.group(1), "[unknown placeholder]"), text)
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
