"""输出：state.json（全过程）、evidence ledger（Markdown）、依赖图 HTML（target <- methods <- data points / assumptions <- sources）。"""
import html
import json
import math
import re
import urllib.parse

from ..mc import Z90
from ..viewer import VIS
from .evidence import PAGE_DATE, period_text

COL = {"snapshot": "#1b7a3a", "live_dated": "#8fd19e", "discarded": "#bdbdbd", "leak": "#d93b3b",
       "base_rate": "#4a7fd6", "method": "#4a7fd6", "method_failed": "#9e9e9e", "target": "#1f2d4d", "api": "#1b7a3a",
       "assumption": "#f28e2b"}
LEGEND = [("snapshot", "verified in archived snapshot <= as_of"), ("live_dated", "live page dated <= as_of"),
          ("discarded", "discarded by judge"), ("leak", "page excluded: leak sentinel hit"),
          ("base_rate", "base-rate direction (kept)"), ("assumption", "assumption proposed by the judge (not observed)"),
          ("method_failed", "method failed"), ("target", "target")]
# v2.6d（F2，D4）：区间依据（methods.combine / published.result 给的 basis）-> 一句给读者看的英文说明。终稿的 [[interval_basis]]
# 占位符、ledger、graph.html 页头（run.save_run）、网页结果页（web/results.py 的 basis_text）共用这一张表。
# 终稿模板常把它嵌在句中（括号里、「basis:」后面），所以小写开头、不带句号、不用括号；不写数字（数字只从代码字段出来）。
BASIS_TEXT = {
    "historical_errors": "interval width set from the methods' backtest errors on earlier years of the target",
    "method_spread": "interval width set from the disagreement between the methods' estimates",
    "monte_carlo": "too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs "
                   "and reflects input uncertainty only",
    "no_basis": "too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, "
                "so code used its fixed default width",
    "no_method": "no method produced an estimate, so there is no interval",
    "published": "the value is already published, so there is no interval",
    # v2.12（决定 5）：分块合并后的区间依据（methods.combine）；上面的旧键留给已存的运行
    "series_calibration": "interval from the series method's measured errors on offline benchmark series with the same "
                          "history length and horizon, not from this target's own errors",
    "backtest_t": "interval width set from the method's backtest errors on earlier years of the target, widened for the "
                  "small number of backtest years",
    "blocks": "several routes with separate inputs: the width is the typical width of the routes' own intervals, "
              "not narrowed for their number",
    "blocks_disagree": "several routes with separate inputs that disagree more than their own intervals allow, so code "
                       "widened the interval in proportion to the disagreement",
}


def basis_text(basis) -> str:
    """basis -> BASIS_TEXT 里的说明；表里没有的值（离散目标的 outcome_probabilities 等）照旧把下划线换成空格，None 返回空串。"""
    return BASIS_TEXT.get(basis) or str(basis or "").replace("_", " ")


def unit_text(target) -> str:
    """v2.7e：估计值和区间后面显示的单位：钉死的 target.unit_canonical，没有就用 target.unit（已存的运行都没有 unit_canonical）。
    终稿的 [[unit]]、ledger、graph.html 页头、网页结果 JSON 的 estimate.unit 共用。"""
    t = target or {}
    return str(t.get("unit_canonical") or t.get("unit") or "").strip()


def unit_full(target) -> str:
    """v2.13a（用户 10-26：「答案的单位也要写清楚」）：答案的单位写全：代码换算用的单位、它数的是什么、哪段期间。
    单位里带时间（t/day）：这段期间里的平均速率；不带时间：这段期间的总数；期初期末是同一天：那一天的量。"""
    t = target or {}
    u, desc = unit_text(t), str(t.get("unit") or "").strip()
    if not u:
        return ""
    s, e = str(t.get("period_start") or ""), str(t.get("period_end") or "")
    from . import qty as Q   # 这里才 import：outputs 被很多模块引用，单位解析只在这一处用
    q, _ = Q.parse_unit(str(t.get("unit_canonical") or ""))
    rate = q is not None and bool(q.dimensionality.get("[time]", 0))
    when = ("" if not e else f"on {e}" if s in ("", e) else f"for {s} to {e}" if q is None else
            f"average over {s} to {e}" if rate else f"total for {s} to {e}")   # 单位没钉住（解析不了）时不说总数还是平均
    what = "; ".join(x for x in (desc if desc and desc != u else "", when) if x)
    return f"{u} ({what})" if what else u


def _num(v):
    return "n/a" if v is None else (f"{v:,.0f}" if abs(v) >= 100 else f"{v:.4g}")


def _pct(p):
    return "n/a" if p is None else f"{100 * p:.1f}%"


def coverage_text(m: dict) -> str:
    """v2.7d：方法的 coverage（compute 规范化过的）-> 一句英文；不进合并的方法附上它自己的估计（只作诊断）。"""
    c = m.get("coverage") or {}
    s = {"full": "the whole target",
         "part": f"only {c.get('part')} of {c.get('dimension')} (siblings {', '.join(c.get('siblings') or [])})",
         "sum": f"sum over {c.get('dimension')} of {', '.join(c.get('parts') or [])}" +
                (f", missing {', '.join(c.get('missing'))}" if c.get("missing") else "")}.get(c.get("kind"), str(c))
    x = m.get("coverage_excluded")
    return s + (f"; not combined (its own estimate {_num(x.get('estimate'))})" if x else "")


def _fx(sigma) -> str:
    """ln 空间的 sigma -> 80% 区间的倍数写法（x/÷1.29）。"""
    return "n/a" if sigma is None else f"x/÷{math.exp(Z90 * sigma):.2f}"


def _mi(x: str) -> int:
    return int(x[:4]) * 12 + int(x[5:7]) - 1


def _consecutive(ms: list) -> bool:
    return all(_mi(b) - _mi(a) == 1 for a, b in zip(ms, ms[1:]))


def _span(ms, ids=None) -> str:
    """用到的月份（YYYY-MM）。连续的一段（5 个月以上）写首尾；不连续的逐个列出，ids（{月: [点 id]}）给了就在每个月后面
    写用了哪些点（v2.12d 审查：以前多于 4 个就写首尾，yoy 路径不连续的 5-7 个月看着像连续的一段，也看不出用了哪些点）。"""
    ms = sorted(ms or [])
    if not ms:
        return "none"
    if len(ms) > 4 and _consecutive(ms):
        return f"{ms[0]}..{ms[-1]}"
    return ", ".join(f"{x} ({', '.join(ids[x])})" if ids and ids.get(x) else x for x in ms)


def _plain(key, text):
    return text


SIGMA_SOURCE = {"series_calibration": "benchmark calibration", "backtest_t": "t-corrected backtest errors",
                "monte_carlo": "Monte Carlo of the formula inputs", "no_basis": "no error evidence, code's default width",
                "method_spread": "disagreement inside the block"}


def _sigma_text(ms: dict, put, mid: str) -> str:
    """一个方法自己的区间宽度和它的来源（methods.combine 的 member_sigma）。"""
    if not ms:
        return ""
    src = ms.get("source")
    extra = (f", {put(mid + '_folds', str(ms['n_folds']))} backtest years, t {put(mid + '_t90', f'{ms['t90']:.3f}')}"
             if src == "backtest_t" else
             f", row {put(mid + '_row', str(ms.get('calibration_row')))} of table {put(mid + '_table', str(ms.get('table')))}"
             if src == "series_calibration" else "")
    return f"; own 80% width {put(mid + '_width', _fx(ms.get('sigma_ln')))} ({SIGMA_SOURCE.get(src, src)}{extra})"


def _bt_text(m: dict, put, mid: str) -> str:
    bt = m.get("backtest") or []
    if not bt:
        return "; no backtest year"
    return f"; backtest years {put(mid + '_bt_years', ', '.join(str(b['year']) for b in bt))}"


def _pairs_text(pairs: list) -> str:
    """yoy 的同比对：「月份: 值 / 一年前的值」。"""
    return "; ".join(f"{x['month']}: {_num(x.get('value'))} / {_num(x.get('year_earlier'))}" for x in pairs or [])


def _member(k: str, est, p: dict, put, mid: str) -> str:
    """series_auto 的一个成员：名字、估计、参数（v2.12d 审查：Theta 的模型、LightGBM 的模型文件和 sha、yoy 的每个同比对）。"""
    key = re.sub(r"[^a-z0-9]", "", k.lower())
    if k in ("AutoETS", "Theta"):
        tag = put(f"{mid}_{key}_model", str(p.get("model") or "")) if p.get("model") else ""
    elif k == "LightGBM":
        sha = str(p.get("point_model_text_sha256") or "")
        tag = (f"config {put(f'{mid}_{key}_cfg', str(p.get('cfg_key')))}"
               + (f", model {put(f'{mid}_{key}_file', str(p['point_model']))} (text sha256 "
                  f"{put(f'{mid}_{key}_sha', sha[:12])})" if p.get("point_model") and sha else ""))
    elif k.startswith("yoy") and p.get("growth"):
        base = (f" = {put(f'{mid}_{key}_base_value', _num(p['base_value']))}" if p.get("base_value") is not None else "")
        tag = (f"base month {put(f'{mid}_{key}_base', str(p.get('base_month')))}{base} x growth "
               f"{put(f'{mid}_{key}_growth', f'{p['growth']:.4f}')} over {put(f'{mid}_{key}_pairs', str(p.get('n_pairs')))} "
               f"year-on-year pair(s)"
               + (f": sum of these months / sum of the same months a year earlier, "
                  f"{put(f'{mid}_{key}_pair_values', _pairs_text(p['pairs']))}" if p.get("pairs") else ""))
    else:
        tag = ""
    return f"{k} {put(f'{mid}_{key}', _num(est))}" + (f" ({tag})" if tag else "")


def method_details(m: dict, res: dict, put=_plain) -> str:
    """v2.12（决定 8）：一个方法的细节，一行英文：算子、成员和各自的估计、用到的数据窗口（月份 / 年份）、参数、校准行、
    它自己的区间宽度。put(key, 文字) 决定数字怎么出现：ledger 直接写，终稿换成占位符（graph.final_estimate）。
    没算出估计、也不是对照基线的方法返回空串（它的错误在方法表里）；v2.12 以前的结果（没有 combination）也返回空串。"""
    if "combination" not in (res or {}):
        return ""
    mid = re.sub(r"[^a-z0-9]", "", str(m.get("id", "")).lower()) or "m"
    ms = (res.get("member_sigma") or {}).get(m.get("id"))
    meth = m.get("method")

    def n(v, k):
        return put(f"{mid}_{k}", _num(v))
    if m.get("baseline_only"):
        b = m["baseline_only"]
        return (f"{m['id']} series_naive: baseline only, not combined: {n(b.get('estimate'), 'baseline')} "
                f"(year {put(mid + '_baseline_year', str((b.get('years_used') or ['?'])[-1]))})")
    if m.get("estimate") is None:
        return ""
    if meth == "series_auto":
        sa = m.get("series_auto") or {}
        prm = sa.get("member_params") or {}
        iv = sa.get("interval") or {}
        win = sa.get("window") or []
        members = ", ".join(_member(k, v, prm.get(k) or {}, put, mid) for k, v in (sa.get("members") or {}).items())
        # v2.12d（审查）：模型路径没走成（模型文件缺、成员不是有限正数）时写明原因，不然「yoy path」和 13 个月以上的连续月对不上
        failed = (f" Models path not used: {put(mid + '_models_failed', str(sa['models_path_failed']))}."
                  if sa.get("models_path_failed") else "")
        shape = "consecutive" if _consecutive(sorted(win)) else "not consecutive"
        return (f"{m['id']} series_auto, {sa.get('path')} path: {sa.get('rule')}.{failed} Members: {members}. "
                f"Data window {put(mid + '_window', _span(win, sa.get('window_month_ids')))} "
                f"({put(mid + '_n_months', str(len(win)))} months used, {shape}; "
                f"last month {put(mid + '_last_month', str(sa.get('last_month')))}, {put(mid + '_h', str(sa.get('h')))} month(s) "
                f"before the target; the run of consecutive months ending there is "
                f"{put(mid + '_consecutive', str(sa.get('consecutive_months')))} long). Calibrated 80% "
                f"interval {n(iv.get('p10'), 'p10')} to {n(iv.get('p90'), 'p90')}" + _sigma_text(ms, put, mid))
    if meth == "yoy_scaling" and m.get("detail"):
        d = m["detail"]
        return (f"{m['id']} yoy_scaling: target {put(mid + '_base_year', str(d['base_year']))} {n(d['target_base'], 'target_base')} "
                f"x signal {n(d['signal_now'], 'signal_now')} / {n(d['signal_base'], 'signal_base')} (growth "
                f"{put(mid + '_growth', f'{d['growth']:.4f}')})" + _bt_text(m, put, mid) + _sigma_text(ms, put, mid))
    if meth == "ratio" and m.get("detail"):
        d = m["detail"]
        return (f"{m['id']} ratio: signal {n(d['signal_now'], 'signal_now')} x sum of target / sum of signal over "
                f"{put(mid + '_years', ', '.join(str(y) for y in d['years']))} ({n(d['sum_target'], 'sum_target')} / "
                f"{n(d['sum_signal'], 'sum_signal')} = {put(mid + '_ratio', f'{d['ratio']:.4g}')}, ratio of means)"
                + _bt_text(m, put, mid) + _sigma_text(ms, put, mid))
    if meth == "partial_period" and m.get("partial_period"):
        d = m["partial_period"]
        pt = d.get("partial_this") or {}
        # v2.12d（审查）：每个往年的部分 / 全期都写 id 和值，覆盖率能照着重算
        pairs = "; ".join(f"{x['year']}: partial {x['partial_id']} = {_num(x['partial'])} / full {x['full_id']} = "
                          f"{_num(x['full'])}" for x in d.get("pairs") or [])
        return (f"{m['id']} partial_period: partial_this {pt.get('id')} ({put(mid + '_partial_span', str(pt.get('period')))}) "
                f"{n(pt.get('value'), 'partial_this')} / coverage {put(mid + '_coverage', f'{d['coverage_ratio']:.4f}')} "
                f"(sum of partial / sum of full, ratio of means, over {put(mid + '_pairs', pairs)})"
                + _bt_text(m, put, mid) + _sigma_text(ms, put, mid))
    if meth == "formula_mc":
        mc = m.get("mc") or {}
        uc = m.get("unit_check")
        return (f"{m['id']} formula_mc: {(m.get('params') or {}).get('formula')}; Monte Carlo P10 to P90 "
                f"{n(mc.get('p10'), 'mc_p10')} to {n(mc.get('p90'), 'mc_p90')}"
                + (f"; result unit {uc['unit']} converted to {uc['target_unit']}" if uc else "") + _sigma_text(ms, put, mid))
    return f"{m['id']} {meth}" + _sigma_text(ms, put, mid)


ACROSS_TEXT = {"single": "the only block", "geometric_mean": "the geometric mean of the two blocks",
               "median": "the median of the blocks", "inverse_backtest_error": "the blocks weighted by inverse backtest error"}


def combination_details(res: dict, put=_plain) -> list:
    """v2.12（决定 8）：合并的块结构、中心规则、区间规则和季节朴素对照，几行英文（put 同 method_details）。"""
    cb = res.get("combination")
    if not cb:
        return []
    parts = []
    for b in cb.get("blocks") or []:
        bid = "block" + b["id"][1:]   # 占位符名 block1_value：b1 是追加方向的 id，别混
        inner = ("" if len(b["members"]) == 1 else
                 f", {'median' if b['rule'] == 'median' else 'geometric mean'} of methods sharing "
                 f"{put(bid + '_shared', ', '.join(b.get('shared_inputs') or []) or 'most inputs')}")
        parts.append(f"{b['id']} = {' + '.join(b['members'])}{inner}: {put(bid + '_value', _num(b['value']))} "
                     f"(width {put(bid + '_width', _fx(b['sigma_ln']))}, {SIGMA_SOURCE.get(b['sigma_source'], b['sigma_source'])})")
    lines = [f"Combination: {put('n_blocks', str(cb['n_blocks']))} block(s), equal weight per block (methods whose inputs "
             f"overlap by at least half form one block; backtest errors set widths, not weights): {'; '.join(parts)}. "
             f"Estimate = {ACROSS_TEXT.get(cb.get('rule_across_blocks'), cb.get('rule_across_blocks'))}."]
    iv = res.get("interval") or {}
    if cb["n_blocks"] >= 2:
        flags = iv.get("flags") or []
        br = iv.get("birge_ratio", 0)
        lines.append(f"Interval: root mean square of the block widths {put('blocks_rms_width', _fx(iv.get('sigma_blocks_rms')))}; "
                     f"Birge ratio {put('birge_ratio', f'{br:.2f}')} "
                     + ("(above one, so the width is multiplied by it)" if br > 1 else "(not above one, so no widening)")
                     + f"; final width {put('final_width', _fx(iv.get('sigma_ln')))}"
                     + ("; the blocks are more than a factor of two apart" if "blocks_disagree_x2" in flags else "")
                     + ("; widened to cover every block" if iv.get("widened_to_cover_blocks") else "") + ".")
    else:
        lines.append(f"Interval: {iv.get('rule')} ({put('final_width', _fx(iv.get('sigma_ln')))}).")
    b = res.get("baseline")
    if b:
        d = b.get("estimate_vs_baseline")
        lines.append(f"Seasonal naive baseline (not combined): {put('baseline', _num(b['estimate']))} "
                     f"({put('baseline_period', str(b.get('period')))}" + (f", point{'s' if len(b['ids']) > 1 else ''} {', '.join(b['ids'])}" if b.get("ids") else "")
                     + f", from {b.get('from')})"
                     + ("" if d is None else f"; the estimate is {put('baseline_diff', f'{round(100 * d, 1) + 0.0:+.1f}%')} against it")
                     + ".")
    return lines


def _top(dist: dict):
    """一个方法的分布里概率最大的结果（并列取先出现的）。"""
    return max(dist.items(), key=lambda kv: kv[1]) if dist else (None, None)


def dep_graph(state: dict) -> dict:
    dirs = {d["id"]: d for d in state.get("directions") or []}
    comp = state.get("compute") or {}
    res = comp.get("result") or {}
    pub = res.get("published") if res.get("basis") == "published" else None   # v2.4：结果是已公布的值（published.py）
    if res.get("mode") == "discrete":   # 离散目标：目标节点显示最可能的结果和它的概率；Jev 对照臂放在详情里
        tlabel = (f"target\n{str(res.get('most_likely') or 'n/a')[:28]}\nresolved (published)" if pub else
                  f"target\n{str(res.get('most_likely') or 'n/a')[:28]}\n{_pct(res.get('most_likely_prob'))}")
    else:
        tlabel = f"target\n{_num(res.get('central'))}" + ("\npublished" if pub else "")
    tdetail = {"target": (state.get("plan") or {}).get("target"), "result": res}
    if state.get("jev"):
        tdetail["jev_arm_not_pooled"] = state["jev"]
    nodes = [{"id": "target", "kind": "target", "label": tlabel, "colour": COL["target"], "detail": tdetail}]
    edges = []
    used = {}
    for m in comp.get("methods") or []:
        ok = m.get("estimate") is not None or bool(m.get("distribution"))
        if m.get("distribution"):
            lab, pr = _top(m["distribution"])
            mlabel = f"{m['id']} {m['method']}\n{str(lab)[:24]} {_pct(pr)}"
        else:
            mlabel = f"{m['id']} {m['method']}\n{_num(m.get('estimate'))}"
        nodes.append({"id": f"M:{m['id']}", "kind": "method", "label": mlabel,
                      "colour": COL["method" if ok else "method_failed"], "detail": m})
        if ok:
            edges.append({"from": f"M:{m['id']}", "to": "target"})
        for i in m.get("used_ids") or []:
            used.setdefault(i, []).append(f"M:{m['id']}")
        for a in m.get("used_assumptions") or []:
            edges.append({"from": f"A:{a}", "to": f"M:{m['id']}"})
    for a in (state.get("assumptions") or {}).get("kept") or []:
        pct = "%" if a.get("is_pct") else ""
        nodes.append({"id": f"A:{a['id']}", "kind": "assumption", "colour": COL["assumption"],
                      "label": f"{a['id']} {_num(a['value'])}{pct}\n{a['name'][:28]}", "detail": a})
    srcs = {}
    for res_d in state.get("results") or []:
        for pg in res_d.get("pages") or []:
            if pg.get("status") in ("snapshot", "live_dated"):
                leak = bool(pg.get("leak_hits"))
                # 同一个网址被别的方向又取了一次：沿用它第一次的编号（P2 前会拿到 S:{n+1}，和下一个新网址撞号，边就分不清连的是谁）
                sid = srcs[pg["url"]]["id"] if pg["url"] in srcs else f"S:{len(srcs) + 1}"
                srcs[pg["url"]] = {"id": sid, "kind": "source", "colour": COL["leak" if leak else pg["status"]],
                                   "label": urllib.parse.urlsplit(pg["url"]).netloc[:28], "detail": pg}
    for p in state.get("points") or []:
        cat = (dirs.get(p["direction_id"]) or {}).get("category")
        c = COL["discarded"] if not p.get("keep") else COL["base_rate"] if cat == "base_rates" else \
            COL["api"] if p.get("via") == "api" else COL[p.get("via", "snapshot")] if p.get("via") in COL else COL["snapshot"]
        nodes.append({"id": f"P:{p['id']}", "kind": "point", "label": f"{p['id']} {_num(p['value'])}", "colour": c,
                      "detail": {k: p.get(k) for k in ("id", "direction_id", "name", "value", "value_as_written", "scale_word",
                                                       "unit", "period_start", "period_end", "quote", "source_url", "via",
                                                       "page_date", "keep", "judge_reason")}})
        s = srcs.get(p.get("source_url"))
        if s is None and p.get("via") == "api":
            s = srcs.setdefault(p["source_url"], {"id": f"S:{len(srcs) + 1}", "kind": "source", "colour": COL["api"],
                                                   "label": "prediction market api", "detail": {"url": p["source_url"]}})
        if s is not None:
            edges.append({"from": s["id"], "to": f"P:{p['id']}"})
        for mid in used.get(p["id"], []):
            edges.append({"from": f"P:{p['id']}", "to": mid})
        if pub and pub.get("id") == p["id"]:   # 已公布的值直接连到目标（方法只作参考）
            edges.append({"from": f"P:{p['id']}", "to": "target"})
    nodes += list(srcs.values())
    return {"nodes": nodes, "edges": edges}


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>__TITLE__</title>
<script src="__VIS__"></script>
<style>
body{font-family:system-ui,Segoe UI,Arial,sans-serif;margin:0;color:#222}
header{padding:12px 18px;border-bottom:1px solid #ddd}
h1{font-size:17px;margin:0 0 6px} .meta{font-size:13px;color:#444} .meta b{color:#000}
main{display:flex;height:calc(100vh - 150px);min-height:480px}
#graph{flex:1;border-right:1px solid #ddd}
#side{width:420px;overflow:auto;padding:10px 14px;font-size:13px}
#side pre{white-space:pre-wrap;word-break:break-word;background:#f6f6f6;padding:8px;border-radius:4px}
.legend{display:flex;flex-wrap:wrap;gap:10px;font-size:12px;margin-top:6px}
.legend span{display:inline-flex;align-items:center;gap:4px}
.sw{width:12px;height:12px;border-radius:50%;display:inline-block;border:1px solid #888}
</style></head><body>
<header><h1>__TITLE__</h1><div class="meta">__META__</div><div class="legend">__LEGEND__</div></header>
<main><div id="graph"></div><div id="side"><p>Click a node to see its details. Levels: sources &rarr; data points and assumptions &rarr; methods &rarr; target.</p>
<pre id="detail"></pre></div></main>
<script>
const G = __GRAPH__;
const LEVEL = {source:0, point:1, assumption:1, method:2, target:3};
const SHAPE = {source:'square', point:'dot', assumption:'diamond', method:'box', target:'star'};
const nodes = G.nodes.map(n => ({id:n.id, label:n.label, level:LEVEL[n.kind], shape:SHAPE[n.kind],
  size: n.kind === 'target' ? 26 : 12, color:{background:n.colour, border:'#555'},
  font:{color: n.kind === 'method' ? '#fff' : '#222', size:12}}));
const net = new vis.Network(document.getElementById('graph'), {nodes:new vis.DataSet(nodes),
  edges:new vis.DataSet(G.edges.map(e => ({from:e.from, to:e.to, arrows:'to', color:{color:'#888'}})))},
  {layout:{hierarchical:{direction:'LR', sortMethod:'directed', levelSeparation:300, nodeSpacing:40}},
   physics:false, interaction:{hover:true}});
const byId = Object.fromEntries(G.nodes.map(n => [n.id, n]));
function show(id){ const n = byId[id]; if (n) document.getElementById('detail').textContent = JSON.stringify(n.detail, null, 2); }
net.on('click', p => { if (p.nodes.length) show(p.nodes[0]); });
show('target');
</script></body></html>"""


def render_graph(state: dict, title: str, meta: str) -> str:
    leg = "".join(f'<span><i class="sw" style="background:{COL[k]}"></i>{html.escape(v)}</span>' for k, v in LEGEND)
    g = json.dumps(dep_graph(state), ensure_ascii=False, default=str).replace("</", "<\\/")
    return (PAGE.replace("__TITLE__", html.escape(title)).replace("__VIS__", VIS).replace("__META__", meta)
            .replace("__LEGEND__", leg).replace("__GRAPH__", g))


def _md(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def ledger(state: dict, score: dict | None = None) -> str:
    plan = state.get("plan") or {}
    t = plan.get("target") or {}
    comp = state.get("compute") or {}
    r = comp.get("result") or {}
    L = [f"# Evidence ledger: {state['qid']}", "", f"- Question: {state['question']}", f"- as_of: {state['as_of']}",
         f"- Pinned target: {_md(t.get('what'))} | unit {_md(t.get('unit'))} | period {t.get('period_start')}..{t.get('period_end')}"
         f" | publisher {_md(t.get('publisher'))}", ""]
    if score and score.get("answer_value") is not None:
        L += [f"- Official value (scoring only, never shown to the agent): {score.get('answer_value'):,}", ""]
    L += ["## Directions and pages", ""]
    by_dir = {}
    for res in state.get("results") or []:
        by_dir.setdefault(res["direction_id"], []).append(res)
    pts_by_url = {}
    for p in state.get("points") or []:
        pts_by_url.setdefault((p["direction_id"], p.get("source_url")), []).append(p)
    for d in (state.get("directions") or []) + [{"id": "markets", "category": "forecasts_markets", "hypothesis": "prediction-market tool (code)"}]:
        L += [f"### {d['id']} [{d['category']}] {_md(d.get('perspective', ''))}", "", f"Hypothesis: {_md(d.get('hypothesis'))}", ""]
        for res in by_dir.get(d["id"], []):
            s = res.get("search") or {}
            if s:
                # v2.10i：provider 的回复里本来就没有查询词（GLM，queries_reported False）时不写「(none)」：看起来像根本没搜
                none = "(not reported by the provider)" if s.get("queries_reported") is False else "(none)"
                L.append(f"Queries issued by the searcher: {'; '.join(_md(q) for q in s.get('queries', [])) or none}")
                L.append("")
            if s.get("voided"):   # v2.6c 回测泄漏护栏（pipeline.run_direction）
                L += [f"**DIRECTION VOIDED: a searcher query contains a registered value {s['voided']}; no pages fetched**", ""]
            if res.get("markets"):
                mk = res["markets"]
                L += [f"Market keywords {mk.get('keywords')}: {mk.get('note') or ''} markets={len(mk.get('markets', []))}", ""]
            if res.get("error") or res.get("aborted") or res.get("stopped"):
                L += [f"Sub-agent stopped: {_md(res.get('error') or res.get('aborted') or res.get('stopped'))}", ""]
            for pg in res.get("pages") or []:
                via = pg.get("status")
                extra = f"snapshot {pg.get('snapshot_ts')}" if via == "snapshot" else f"page date {pg.get('page_date')}" if via == "live_dated" else _md(pg.get("reason"))
                leak = f" **LEAK SENTINEL HIT {pg.get('leak_hits')} (excluded)**" if pg.get("leak_hits") else ""
                L.append(f"- `{pg['url'][:150]}` -> **{via}** ({extra}){leak}; points raw/verified "
                         f"{pg.get('n_points_raw', '-')}/{pg.get('n_points_verified', '-')}")
                for p in pts_by_url.get((d["id"], pg["url"]), []):
                    k = "EXCLUDED (ablation)" if p.get("ablation_excluded") else "keep" if p.get("keep") else "DISCARD"
                    # v2.8o：抽取员读的数（number / 区间）写出原文写法和核对结果
                    rd = (f" (range {_num(p['value_low'])}..{_num(p['value_high'])})" if p.get("value_low") is not None else "") + \
                         (f" as written \"{_md(p.get('value_as_written'))}\", value check {p.get('value_check')}" if p.get("reading") else "")
                    L.append(f"  - {p['id']} {_md(p['name'])[:80]} = **{_num(p['value'])}**{rd} {_md(p.get('unit'))} "
                             f"({period_text(p, blank='')}) [{k}: {_md(p.get('judge_reason'))[:120]}] "
                             f"quote: \"{_md(p.get('quote'))[:200]}\"")
            n_drop = len(res.get("dropped_points") or [])
            if n_drop:
                reasons = {}
                for x in res["dropped_points"]:
                    reasons[x["reason"]] = reasons.get(x["reason"], 0) + 1
                L.append(f"- dropped by code checks: {n_drop} ({'; '.join(f'{k}: {v}' for k, v in reasons.items())})")
            L.append("")
    L += ["## Judge", ""]
    for jr in state.get("judge_rounds") or []:
        L.append(f"### round {jr.get('round')}")
        for a in jr.get("assessment") or []:
            if isinstance(a, dict):
                L.append(f"- {a.get('relation')}: {a.get('ids')} {_md(a.get('note'))[:200]}")
        if jr.get("extra_directions"):
            L.append(f"- extra base-rate directions requested: {[x['id'] for x in jr['extra_directions']]}")
        L.append("")
    L += assumptions_md(state)
    L += ablation_md(state)
    L += ["## Methods (computed by code)", "",
          "| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | "
          "notes / error |", "|---|---|---|---|---|---|---|---|---|"]
    est = comp.get("estimate_result") or {} if r.get("basis") == "published" else r   # v2.4：已公布时估计只作参考
    w = est.get("weights") or {}
    wb = est.get("weight_basis") or {}
    for m in comp.get("methods") or []:
        e = m.get("backtest_mean_abs_log_err")
        es = "" if e is None else f"{e:.3f}"
        # v2.12d（审查）：每个算子都写输入（以前只有 formula_mc），series_auto / partial_period 的输入照样能对上点
        inp = (f"{m.get('used_ids') or []} / {m.get('used_assumptions') or []}"
               if m.get("inputs_detail") or m.get("used_ids") or m.get("used_assumptions") else "")
        L.append(f"| {m['id']} | {m['method']} | {_num(m.get('estimate'))} | {_md(inp)} | "
                 f"{[b['year'] for b in m.get('backtest') or []]} | {es} | {w.get(m['id'], 0):.2f} | {wb.get(m['id'], '')} | "
                 f"{_md(m.get('error') or '; '.join(m.get('notes') or []))[:200]} |")
    cov = [m for m in comp.get("methods") or [] if m.get("coverage")]   # v2.7d：只有声明了 coverage 的方法才多这几行
    if cov:
        L.append("")
        L += [f"- {m['id']} coverage: {_md(coverage_text(m))}" for m in cov]
    # v2.12（决定 8）：每个方法的算子、成员、数据窗口、参数、校准行，合并的块结构和季节朴素对照（旧运行没有这些字段时不写）
    det = [x for x in (method_details(m, est) for m in comp.get("methods") or []) if x] + combination_details(est)
    if det and r.get("mode") != "discrete":
        L += ["", "Method details (computed by code):", ""] + [f"- {_md(x)}" for x in det]
    share = r.get("assumption_weight_share")
    tail = "" if share is None else f", weight on methods that use assumptions {share:.2f}"
    if r.get("mode") == "discrete":
        L += [""] + outcomes_md(state, score)
    elif r.get("basis") == "published" and (state.get("published") or {}).get("early_stop"):   # v2.5 提前停
        L += ["", f"Result: **published value {_num(r.get('central'))}** (data point {(r.get('published') or {}).get('id')}), "
                  f"confirmed while the sub-agents were running. No estimate was made: the judge and the estimation methods "
                  f"were skipped."]
    elif r.get("basis") == "published":
        bt = basis_text(est.get("basis"))
        L += ["", f"Result: **published value {_num(r.get('central'))}** (data point {(r.get('published') or {}).get('id')}). "
                  f"Estimation methods for reference only, not blended (weights above are theirs): central "
                  f"{_num(est.get('central'))}, 80% interval [{_num(est.get('p10'))}, {_num(est.get('p90'))}], basis "
                  f"{est.get('basis')}" + (f" ({bt})" if bt else "") + f", weight rule {est.get('weight_rule')}"]
    else:   # v2.6d：basis 后面附 BASIS_TEXT 的说明（没有 basis 时说明是空串，不加括号）；v2.7e：中心和区间后面跟单位
        bt = basis_text(r.get("basis"))
        u = f" {_md(unit_text(t))}" if unit_text(t) else ""
        L += ["", f"Result: central **{_num(r.get('central'))}**{u}, 80% interval [{_num(r.get('p10'))}, {_num(r.get('p90'))}]{u}, "
                  f"basis {r.get('basis')}" + (f" ({bt})" if bt else "") + f", weight rule {r.get('weight_rule')}{tail}"]
        if unit_full(t):   # v2.13a：单位写全（数的是什么、哪段期间）
            L += ["", f"Unit of the estimate: {_md(unit_full(t))}"]
    L += [""] + published_md(state)
    L += ["", "## Final answer", "", (state.get("final") or {}).get("text", ""), ""]
    return "\n".join(L)


def published_md(state: dict) -> list:
    """账本里「答案已公布」检查（v2.4，published.py）一节：状态、候选点和模型的判定。旧运行没有这条记录，不写。"""
    pub = state.get("published")
    if not pub:
        return []
    L = ["## Published-value check (live use only)", "", f"Status: **{pub.get('status')}**. {_md(pub.get('note'))}"]
    pe = state.get("published_early") or {}
    if pe:   # v2.5：子 agent 运行中的提前检查
        by = pe.get("by_status") or {}   # v2.5.2：有检查出错时写出每种状态的次数
        L.append(f"Early checks while the sub-agents were running: {pe.get('n_checks')} ({pe.get('status')}"
                 + (f"; {_md(pe.get('off'))}" if pe.get("off") else "")
                 + (f"; by status: {', '.join(f'{k} {v}' for k, v in sorted(by.items()))}; candidates of a failed check "
                    f"are re-sent with the next check" if pe.get("n_error") else "")
                 + "); details in state.json -> published_early.")
    if pub.get("error"):
        L.append(f"Error: {_md(pub['error'])}")
    if pub.get("status") == "published":
        pt = pub.get("point") or {}
        L.append(f"Published value: **{_num(pub.get('value'))}** {_md(pub.get('unit'))} = data point {pub.get('id')} from "
                 f"{_md(pt.get('domain'))} ({pt.get('via')}, dated {pub.get('date')}); confirmed ids {pub.get('confirmed_ids')}"
                 + (f"; resolves to outcome **{_md(pub.get('outcome'))}**" if pub.get("outcome") else ""))
    if pub.get("status") == "conflict":
        L.append(f"Confirmed values disagree: {pub.get('values')}; the estimate is reported instead.")
    if pub.get("candidates"):
        L += ["", "| id | name | value | unit | period | source | verdict | reason |", "|---|---|---|---|---|---|---|---|"]
        for c in pub["candidates"]:
            L.append(f"| {c.get('id')} | {_md(c.get('name'))[:90]} | {_num(c.get('value'))} | {_md(c.get('unit'))[:30]} | "
                     f"{period_text(c, blank='')} | {_md(c.get('domain'))} | {_md(c.get('verdict', ''))} | "
                     f"{_md(c.get('reason', ''))[:160]} |")
    return L + [""]


def outcome_rows(state: dict) -> tuple:
    """离散目标的结果表：([(label, value, agent 概率, {方法 id: 概率}, Jev 概率)], 算出分布的方法 id, Jev 记录)。"""
    comp = state.get("compute") or {}
    r = comp.get("result") or {}
    ms = [m for m in comp.get("methods") or [] if m.get("distribution")]
    jv = state.get("jev") or {}
    jp = jv.get("probabilities") if jv.get("status") == "ok" else None
    rows = [(o["label"], o.get("value"), o.get("prob"), {m["id"]: m["distribution"].get(o["label"]) for m in ms},
             None if not jp else jp.get(o["label"])) for o in r.get("outcomes") or []]
    return rows, [m["id"] for m in ms], jv


def jev_note(jv: dict) -> str:
    if not jv:
        return "Jev arm: not run."
    if jv.get("status") != "ok":
        return f"Jev arm (TypeSafe, not pooled): {jv.get('status')}: {jv.get('error') or jv.get('note') or ''}"
    u = jv.get("usage") or {}
    usd = jv.get("usd_estimated")
    return (f"Jev arm (TypeSafe {jv.get('model')}, asked once with a code-built brief of {jv.get('n_points_in_brief')} kept "
            f"points; not pooled into the agent's answer): choice {jv.get('choice')}, confidence {jv.get('confidence')}, "
            f"input tokens {u.get('input_tokens')}, output tokens {u.get('output_tokens')}"
            + ("" if usd is None else f", estimated cost ${usd:.6f}") + ".")


def outcomes_md(state: dict, score: dict | None = None) -> list:
    """账本里离散目标的「结果概率」表（agent 的等权平均、每个方法、Jev 对照臂）。"""
    r = (state.get("compute") or {}).get("result") or {}
    rows, mids, jv = outcome_rows(state)
    L = ["## Outcome probabilities (computed by code)", "",
         f"Most likely: **{_md(r.get('most_likely') or 'none (no method computed)')}** ({_pct(r.get('most_likely_prob'))}); "
         f"pooling {r.get('weight_rule')} "
         f"over {len(mids)} method(s); weight on methods that use assumptions {r.get('assumption_weight_share') or 0:.2f}.", "",
         "| outcome | value | agent (pooled) | " + "".join(f"{m} | " for m in mids) + "Jev (not pooled) |",
         "|---|---|---|" + "---|" * len(mids) + "---|"]
    if r.get("resolved"):   # v2.4：已公布的结果（published.py）；方法的列是估计，只作参考
        ref = ((state.get("compute") or {}).get("estimate_result") or {}).get("outcomes") or []
        ref_txt = "; ".join(f"{_md(o.get('label'))} {_pct(o.get('prob'))}" for o in ref) or "none"
        L[2] = (f"Resolved by a published value: **{_md(r.get('most_likely'))}** (data point "
                f"{(r.get('published') or {}).get('id')}). The agent column shows the resolved outcome; the method columns are "
                f"the estimation methods, for reference only (pooled estimate: {ref_txt}).")
    orec = state.get("outcomes") or {}
    if orec.get("list"):   # v2.3：结果列表由裁判根据证据定义（可能修订过一次）
        rev = (f"; revised in round {orec['revised_round']} ({_md(orec.get('revision_reason'))[:200]})"
               if orec.get("revised_round") else "")
        L[2:2] = [f"Outcome list defined by the judge in round {orec.get('defined_round')}{rev}, from kept points "
                  f"{(orec.get('basis') or {}).get('ids')}: {_md((orec.get('basis') or {}).get('note'))[:300]}", ""]
    for lab, v, p, per, jp in rows:
        L.append(f"| {_md(lab)} | {_num(v)} | **{_pct(p)}** | " + "".join(f"{_pct(per.get(m))} | " for m in mids)
                 + f"{_pct(jp)} |")
    L += ["", jev_note(jv)]
    if score and score.get("prob_true") is not None:
        L += ["", f"Scoring: true outcome {score.get('true_outcome')}, probability on it {_pct(score.get('prob_true'))}, "
                  f"Brier {score.get('brier'):.3f}, most likely correct {score.get('most_likely_correct')}"]
    return L


def outcome_table_html(state: dict) -> str:
    """graph.html 页头里离散目标的结果表（代码算的概率 + Jev 对照臂）。"""
    r = (state.get("compute") or {}).get("result") or {}
    rows, mids, jv = outcome_rows(state)
    e = html.escape
    head = "".join(f"<th>{e(m)}</th>" for m in mids)
    body = "".join(f"<tr><td>{e(str(lab))}</td><td>{e(_num(v))}</td><td><b>{e(_pct(p))}</b></td>"
                   + "".join(f"<td>{e(_pct(per.get(m)))}</td>" for m in mids) + f"<td>{e(_pct(jp))}</td></tr>"
                   for lab, v, p, per, jp in rows)
    top = (f"resolved <b>{e(str(r.get('most_likely') or 'n/a'))}</b> (published value, data point "
           f"{e(str((r.get('published') or {}).get('id')))}; method columns are estimates for reference)" if r.get("resolved") else
           f"most likely <b>{e(str(r.get('most_likely') or 'n/a'))}</b> ({e(_pct(r.get('most_likely_prob')))})")
    return (top +
            f'<table style="font-size:12px;border-collapse:collapse;margin-top:4px" border="1" cellpadding="3">'
            f"<tr><th>outcome</th><th>value</th><th>agent (pooled)</th>{head}<th>Jev (not pooled)</th></tr>{body}</table>"
            f'<div style="font-size:12px">{e(jev_note(jv))}</div>')


def assumptions_md(state: dict) -> list:
    """账本里的假设一节：保留的（值、裁判给的范围、代码实际采样的范围、理由、适用条件、推翻条件、被哪个方法用）和被拒的。"""
    av = state.get("assumptions") or {}
    kept, rej = av.get("kept") or [], av.get("rejected") or []
    L = ["## Assumptions (proposed by the judge, validated by code)", ""]
    if not kept and not rej:
        return L + ["None proposed.", ""]
    L += [f"Rules: ids a1..a{av.get('max_per_run', 8)}, at most {av.get('max_per_method', 3)} per method, every formula needs "
          f"an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= "
          f"{av.get('min_width')}. From judge round {av.get('from_round')}.", "",
          "| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for a in kept:
        f = 100.0 if a.get("is_pct") else 1.0
        used = ", ".join(f"{m} ({lab})" for m, lab in zip(a.get("used_by") or [], a.get("used_by_labels") or [])) or "unused"
        wid = " (widened)" if a.get("widened_by_floor") else ""
        L.append(f"| {a['id']} | {_md(a['name'])} | {_num(a['value'])} | {_num(a['low'])}..{_num(a['high'])} | "
                 f"{_num(a['p10_used'] * f)}..{_num(a['p90_used'] * f)}{wid} | {_md(a['unit'])} | {used} | "
                 f"{_md(a['rationale'])} | {_md(a.get('applies_when'))} | {_md(a.get('falsified_by'))} |")
    if rej:
        L += ["", "Rejected by code:", ""]
        for a in rej:
            L.append(f"- {_md(a.get('id') or a.get('raw'))} {_md(a.get('name', ''))[:80]}: {_md(a.get('reason'))}")
    return L + [""]


def ablation_md(state: dict) -> list:
    ab = state.get("ablation")
    if not ab:
        return []
    L = ["## Ablation: no own history (--ablate-own-history)", "",
         f"- own_history candidate directions dropped: {ab.get('dropped_candidate_directions')}",
         f"- own_history extra directions dropped: {ab.get('dropped_extra_directions')}",
         f"- entity anchors from the pinned target: {ab.get('entity_anchors')}; quantity stems: {ab.get('quantity_stems')}",
         f"- points excluded before the judge: {ab.get('n_points_excluded')} of {ab.get('n_points_total')}",
         f"- methods allowed: {ab.get('methods_allowed')}", ""]
    for x in ab.get("excluded_points") or []:
        per = period_text(x) if x.get("period_source") == PAGE_DATE else x.get("period_end")
        L.append(f"  - {x['id']} {_md(x['name'])[:90]} = {_num(x['value'])} ({per}): {_md(x['reason'])}")
    return L + [""]
