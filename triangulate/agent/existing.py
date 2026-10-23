"""v2.11f 现成数据前置步骤（计划 C）。plan 之后、人工确认之前搜一次目标本身（官方值、第三方估计、一致预期、预测）；取页、抽取、
核对复用子 agent 的流水线（pipeline._live_pages / _process_page，引文、数值、倍数、日期规则同任何一个点）。哪些点就是目标本身：
官方值原样复用 published.candidates / prompt / resolve（同 EarlyWatch）；其余的点问 EXISTING_CHECK_*（只回标签，不写数字；
期间差一点算不算由模型判断）。页面日期补出期间的点、区间不算；读数先过 value_check。候选进同一个人工确认：选用 -> accept；
批准路线 = 排除，原流程里同值、期间重叠的点由 _process_page 丢掉（excluded_by），终稿列出（excluded_note）。
只在真实使用、有人确认、连续值目标、目标期末 <= as_of 时跑，否则不发任何调用；点只存在 state["existing"]，页数名额全部退回。"""
import json

from ..config import MAX_TOKENS
from ..llm import BalanceExhausted
from . import compute as C
from . import discrete as D
from . import evidence as ev
from . import pipeline as P
from . import published as PB
from . import value_check as VC
from .evidence import parse_date, period_text
from .prompts import (EXISTING_CHECK_SYSTEM, EXISTING_CHECK_USER, EXISTING_DATA_TO_FIND, EXISTING_HYPOTHESIS,
                      EXISTING_SEARCH_USER)

MAX_USES, URLS = 6, 8   # 决定 14：一个方向的两倍（max_uses 3、4 个 URL）
CHECK_MAX_TOKENS = 4000   # existing:check 的输出上限：模块常数，不进 config.MAX_TOKENS（否则所有运行的 settings 都变）
DIRECTION = {"id": "existing", "hypothesis": EXISTING_HYPOTHESIS, "data_to_find": EXISTING_DATA_TO_FIND}
TYPES = {"official": "official figure", "estimate": "third-party estimate"}
EXCLUDED = "excluded by the user: same value and an overlapping period as existing figure"
SAME_TOL = 1e-9   # 排除时「同一个数」的相对容差：只吸收浮点误差（不用 published.REL_TOL 0.5%：会把相近的官方值当成被排除的一致预期丢掉）
NOT_CHECKED = ("not checked: the existing-figure step runs only in live use with a human at the approval step "
               "(not in backtests, scored, --auto-approve or ablation runs)")


def run(ctx, state: dict) -> dict:
    """前置步骤，返回 state["existing"]：status = found / none / not_checked / not_applicable / skipped（预算）/ error。"""
    target = (state.get("plan") or {}).get("target") or {}
    if (state.get("aborted") or not getattr(ctx, "human", False) or not getattr(ctx, "check_published", False)
            or getattr(ctx, "ablate_own_history", False)):
        return {"status": "not_checked", "note": NOT_CHECKED}
    tpe = parse_date(target.get("period_end"), end=True)
    if D.is_discrete(target) or tpe is None or tpe > ctx.as_of:
        return {"status": "not_applicable", "note": "discrete target" if D.is_discrete(target) else
                "target period_end unparseable" if tpe is None else f"target period ends {tpe}, after as_of"}
    b = ctx.budget
    rec = {"status": "none", "search": {}, "pages": [], "points": [], "dropped_points": []}
    n0, a0 = b.pages_used, b.aborted
    try:
        prompt = EXISTING_SEARCH_USER.format(cap=URLS, as_of=ctx.as_of_s, **{k: target.get(k, "") for k in (
            "what", "unit", "period_start", "period_end", "publisher")})
        with b.sem, b.hold(b.search_reserve(MAX_USES)):
            try:
                rec["search"] = ctx.searcher.search(prompt, role="existing:search", qid=ctx.qid, max_uses=MAX_USES, cap=URLS)
            except BalanceExhausted as e:   # 余额不足 -> 整次运行停下（同 run_direction）
                raise P.BudgetExceeded(b.halt(str(e))) from None
        P._live_pages(ctx, target, DIRECTION, 1, rec["search"].get("urls", [])[:URLS], rec, watch=False)
        for i, p in enumerate(rec["points"], start=1):
            p["id"] = f"x{i}"
        rec.update(check(ctx, target, rec["points"]))
        rec["status"] = "found" if rec["candidates"] else "none"
    except P.BudgetExceeded as e:
        rec.update(status="skipped", note=str(e))
        if " would be exceeded " in b.aborted:   # 只是前置步骤自己的预扣放不下（不是余额不足、取消、真超支）：不中止整次运行
            b.aborted = a0
    except Exception as e:  # noqa: BLE001  前置步骤出任何意外都不拖垮整题：照今天的流程进人工确认
        rec.update(status="error", error=P.redact(ctx, f"{type(e).__name__}: {e}")[:300])
    finally:
        for _ in range(b.pages_used - n0):   # 页数名额全部退回：原流程的页数上限和以前一样
            b.release_page()
    return rec


def check(ctx, target: dict, pts: list) -> dict:
    """前置步骤核对过的点 -> {candidates, published_check, check}。数字一律取自点，不取自模型的回复。"""
    pool = [p for p in pts if p.get("period_source") != ev.PAGE_DATE and p.get("value_low") is None]
    found, out = {}, {}
    cands, note = PB.candidates(pool, target, ctx.as_of, judged_only=False)
    out["published_check"] = {"status": "no_candidates", "note": note}
    if cands:   # 官方值：同 EarlyWatch（PUBLISHED_* 不改）
        system, user = PB.prompt(target, ctx.as_of_s, cands)
        reply, err = ctx.llm.ask(system, user, role="existing:published", qid=ctx.qid, max_tokens=MAX_TOKENS["published"])
        pub = {**PB.resolve(reply, cands, target), "note": note} if reply is not None else {"status": "error", "error": err}
        out["published_check"] = pub
        why = {c["id"]: c.get("reason", "") for c in pub.get("candidates") or []}
        found.update({p["id"]: (p, "official", why.get(p["id"], "")) for p in cands if p["id"] in (pub.get("confirmed_ids") or [])})
    rest = [p for p in pool if p["id"] not in found]
    if rest:   # 其余的点（第三方估计、一致预期、预测；期间差一点的官方值）：模型只回标签
        reply, err = ctx.llm.ask(EXISTING_CHECK_SYSTEM, EXISTING_CHECK_USER.format(
            target=json.dumps(target, ensure_ascii=False, default=str), as_of=ctx.as_of_s,
            candidates="\n".join(PB.candidate_line(p) for p in rest)), role="existing:check", qid=ctx.qid,
            max_tokens=CHECK_MAX_TOKENS)
        by_id, raw = {p["id"]: p for p in rest}, (reply or {}).get("matches")
        for x in raw if isinstance(raw, list) else []:
            i, lab = (str(x.get("id")), str(x.get("label", "")).strip().lower()) if isinstance(x, dict) else ("", "")
            if i in by_id and i not in found and lab in TYPES:
                found[i] = (by_id[i], lab, str(x.get("reason", ""))[:300])
        out["check"] = {"n_sent": len(rest), "error": err, "matched": [i for i in found if i in by_id]}
    for p, _, _ in found.values():   # 读数（单词、分数写的数）先核对（同裁判方法用到的点），没过的不算
        if p.get("value_check") == "pending":
            VC._apply(p, VC.check_point(ctx.llm, ctx.qid, p))
    out["candidates"] = [PB._summary(p) | {"type": t, "reason": r} for p, t, r in
                         sorted(found.values(), key=lambda f: PB._order(f[0])) if p.get("value_check") != "failed"]
    return out


def excluded_by(p: dict, shown: list) -> str:
    """原流程的一个点和用户排除的某个现成数据是同一个数（相对差 <= SAME_TOL，只吸收浮点误差）、期间重叠（含相同）：返回那个候选的 id。"""
    v, (ps, pe) = p.get("value"), C._span(p)
    for x in shown:
        w, (xs, xe) = x.get("value"), C._span(x)
        if pe is None or xe is None or not isinstance(v, (int, float)) or not isinstance(w, (int, float)):
            continue
        if abs(v - w) <= SAME_TOL * max(abs(v), abs(w)) and ps <= xe and xs <= pe:
            return x["id"]
    return ""


def accept(state: dict) -> dict:
    """用户选用了一个现成数据（graph 的 use_existing 节点）：compute.result 换成它（没有区间、没有方法），终稿全部由代码写。"""
    x = (state.get("existing") or {})["accepted"]
    res = {"central": x.get("value"), "p10": None, "p90": None, "weights": {}, "weight_basis": {}, "basis": "existing",
           "assumption_weight_share": 0, "existing": {k: x.get(k) for k in ("id", "value", "unit", "type", "source_url", "domain")},
           "weight_rule": "none: existing figure accepted by the user (no estimate was made)"}
    pub = f", publication date {x['published_at_if_visible']}" if x.get("published_at_if_visible") else ""
    text = "\n\n".join([
        f"Existing figure: {PB._with_unit(x.get('value'), x.get('unit', ''))} ({TYPES.get(x.get('type'), x.get('type'))}). "
        "It was found before any estimation and you chose to use it: it is not an estimate by this agent, and no estimate was made.",
        f"Source: data point {x.get('id')} \"{x.get('name')}\" (period {period_text(x, blank='')}), from {x.get('domain')} "
        f"({PB._via(x)}{pub}), quoting: \"{x.get('quote')}\"",
        "A separate model check judged that this figure has the pinned target's quantity, scope and period; the number is "
        "taken from the data point by code."])
    return {"compute": {"result": res, "methods": [], "estimate_result": None,
                        "skipped": "existing figure accepted by the user; no estimate was made"},
            "final": {"template": text, "text": text, "placeholders": {}, "digits_removed": 0, "model_error": None,
                      "used_model_text": False, "written_by": "code (existing figure)"}}


def excluded_note(state: dict) -> str:
    """排除了现成数据时终稿末尾的一段（代码写）：被排除的值，和原流程里因此丢掉的点。没排除时返回空串（终稿和以前相同）。"""
    ex = state.get("existing") or {}
    shown = [x for x in ex.get("candidates") or [] if x.get("id") in (ex.get("excluded") or [])]
    if not shown:
        return ""
    drops = [d for r in state.get("results") or [] for d in r.get("dropped_points") or []
             if str(d.get("reason", "")).startswith(EXCLUDED)]
    head = ("Existing figures you excluded (not used as evidence): " + "; ".join(
        f"{x['id']} {PB._with_unit(x.get('value'), x.get('unit', ''))} ({TYPES.get(x.get('type'), x.get('type'))}, "
        f"{x.get('domain')})" for x in shown) + ".")
    tail = (f" Code dropped {len(drops)} data point(s) found by the routes with the same value (exact match, relative "
            f"tolerance {SAME_TOL:g}) and an overlapping period" + (": " + "; ".join(
                f"\"{d.get('name')}\" = {d.get('value_as_written')} ({d.get('source_url')})" for d in drops) if drops else "") + ".")
    return "\n\n" + head + tail
