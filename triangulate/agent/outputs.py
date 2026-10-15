"""输出：state.json（全过程）、evidence ledger（Markdown）、依赖图 HTML（target <- methods <- data points / assumptions <- sources）。"""
import html
import json
import urllib.parse

from ..viewer import VIS

COL = {"snapshot": "#1b7a3a", "live_dated": "#8fd19e", "discarded": "#bdbdbd", "leak": "#d93b3b",
       "base_rate": "#4a7fd6", "method": "#4a7fd6", "method_failed": "#9e9e9e", "target": "#1f2d4d", "api": "#1b7a3a",
       "assumption": "#f28e2b"}
LEGEND = [("snapshot", "verified in archived snapshot <= as_of"), ("live_dated", "live page dated <= as_of"),
          ("discarded", "discarded by judge"), ("leak", "page excluded: leak sentinel hit"),
          ("base_rate", "base-rate direction (kept)"), ("assumption", "assumption proposed by the judge (not observed)"),
          ("method_failed", "method failed"), ("target", "target")]


def _num(v):
    return "n/a" if v is None else (f"{v:,.0f}" if abs(v) >= 100 else f"{v:.4g}")


def dep_graph(state: dict) -> dict:
    dirs = {d["id"]: d for d in state.get("directions") or []}
    comp = state.get("compute") or {}
    res = comp.get("result") or {}
    nodes = [{"id": "target", "kind": "target", "label": f"target\n{_num(res.get('central'))}", "colour": COL["target"],
              "detail": {"target": (state.get("plan") or {}).get("target"), "result": res}}]
    edges = []
    used = {}
    for m in comp.get("methods") or []:
        ok = m.get("estimate") is not None
        nodes.append({"id": f"M:{m['id']}", "kind": "method", "label": f"{m['id']} {m['method']}\n{_num(m.get('estimate'))}",
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
                srcs[pg["url"]] = {"id": f"S:{len(srcs) + 1}", "kind": "source", "colour": COL["leak" if leak else pg["status"]],
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
                L.append(f"Queries issued by the searcher: {'; '.join(_md(q) for q in s.get('queries', [])) or '(none)'}")
                L.append("")
            if res.get("markets"):
                mk = res["markets"]
                L += [f"Market keywords {mk.get('keywords')}: {mk.get('note') or ''} markets={len(mk.get('markets', []))}", ""]
            if res.get("error") or res.get("aborted"):
                L += [f"Sub-agent stopped: {_md(res.get('error') or res.get('aborted'))}", ""]
            for pg in res.get("pages") or []:
                via = pg.get("status")
                extra = f"snapshot {pg.get('snapshot_ts')}" if via == "snapshot" else f"page date {pg.get('page_date')}" if via == "live_dated" else _md(pg.get("reason"))
                leak = f" **LEAK SENTINEL HIT {pg.get('leak_hits')} (excluded)**" if pg.get("leak_hits") else ""
                L.append(f"- `{pg['url'][:150]}` -> **{via}** ({extra}){leak}; points raw/verified "
                         f"{pg.get('n_points_raw', '-')}/{pg.get('n_points_verified', '-')}")
                for p in pts_by_url.get((d["id"], pg["url"]), []):
                    k = "EXCLUDED (ablation)" if p.get("ablation_excluded") else "keep" if p.get("keep") else "DISCARD"
                    L.append(f"  - {p['id']} {_md(p['name'])[:80]} = **{_num(p['value'])}** {_md(p.get('unit'))} "
                             f"({p.get('period_start')}..{p.get('period_end')}) [{k}: {_md(p.get('judge_reason'))[:120]}] "
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
    w = r.get("weights") or {}
    wb = r.get("weight_basis") or {}
    for m in comp.get("methods") or []:
        e = m.get("backtest_mean_abs_log_err")
        es = "" if e is None else f"{e:.3f}"
        inp = f"{m.get('used_ids') or []} / {m.get('used_assumptions') or []}" if m.get("inputs_detail") else ""
        L.append(f"| {m['id']} | {m['method']} | {_num(m.get('estimate'))} | {_md(inp)} | "
                 f"{[b['year'] for b in m.get('backtest') or []]} | {es} | {w.get(m['id'], 0):.2f} | {wb.get(m['id'], '')} | "
                 f"{_md(m.get('error') or '; '.join(m.get('notes') or []))[:200]} |")
    share = r.get("assumption_weight_share")
    tail = "" if share is None else f", weight on methods that use assumptions {share:.2f}"
    L += ["", f"Result: central **{_num(r.get('central'))}**, 80% interval [{_num(r.get('p10'))}, {_num(r.get('p90'))}], "
              f"basis {r.get('basis')}, weight rule {r.get('weight_rule')}{tail}", "", "## Final answer", "",
          (state.get("final") or {}).get("text", ""), ""]
    return "\n".join(L)


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
        L.append(f"  - {x['id']} {_md(x['name'])[:90]} = {_num(x['value'])} ({x.get('period_end')}): {_md(x['reason'])}")
    return L + [""]
