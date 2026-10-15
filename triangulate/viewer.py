"""静态 HTML 查看器：每题一页 + 索引页。图用 vis-network（CDN，版本钉死）。
颜色 = 状态（仿 Lean blueprint：颜色表示证明状态），输入节点大小 = 敏感度 |Δlog10(最终估计)|。"""
import html
import json

VIS = "https://cdn.jsdelivr.net/npm/vis-network@9.1.9/standalone/umd/vis-network.min.js"

COLOURS = {
    "sourced_verified": "#1b7a3a", "sourced_unverified": "#8fd19e", "assumption": "#f2b134",
    "missing": "#bdbdbd", "contradicted": "#d93b3b",
    "valid": "#4a7fd6", "outlier": "#b04ad6", "invalid": "#9e9e9e",
    "estimated": "#1f2d4d", "failed": "#d93b3b",
}
LEGEND = [("sourced_verified", "sourced, verified (needs retrieval; not used yet)"),
          ("sourced_unverified", "sourced, unverified (model-cited)"), ("assumption", "assumption (model knowledge)"),
          ("missing", "missing / invalid"), ("contradicted", "contradicted (needs retrieval; not used yet)"),
          ("valid", "path: valid"), ("outlier", "path: >1 OOM from aggregate"), ("invalid", "path: invalid"),
          ("estimated", "target")]

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>__TITLE__</title>
<script src="__VIS__"></script>
<style>
body{font-family:system-ui,Segoe UI,Arial,sans-serif;margin:0;color:#222}
header{padding:12px 18px;border-bottom:1px solid #ddd}
h1{font-size:17px;margin:0 0 6px} .meta{font-size:13px;color:#444} .meta b{color:#000}
main{display:flex;height:calc(100vh - 150px);min-height:480px}
#graph{flex:1;border-right:1px solid #ddd}
#side{width:390px;overflow:auto;padding:10px 14px;font-size:13px}
#side pre{white-space:pre-wrap;word-break:break-word;background:#f6f6f6;padding:8px;border-radius:4px}
.legend{display:flex;flex-wrap:wrap;gap:10px;font-size:12px;margin-top:6px}
.legend span{display:inline-flex;align-items:center;gap:4px}
.sw{width:12px;height:12px;border-radius:50%;display:inline-block;border:1px solid #888}
a{color:#2457b3}
</style></head><body>
<header><h1>__H1__</h1><div class="meta">__META__</div><div class="legend">__LEGEND__</div></header>
<main><div id="graph"></div><div id="side"><p>Click a node to see its details. Input node size = sensitivity
|&Delta;log10(final estimate)| when the input moves from low to high with all others at their medians,
scaled relative to the most sensitive input on this page (largest here: <b id="maxs"></b>).
<code>sensitivity_path_max</code> is the same change measured on the input's own path.</p>
<pre id="detail"></pre></div></main>
<script>
const G = __GRAPH__;
const COL = __COLOURS__;
const LEVEL = {input:0, path:1, target:2};
const maxS = Math.max(0, ...G.nodes.filter(n => n.kind === 'input').map(n => Math.abs(n.sensitivity || 0)));
const nodes = G.nodes.map(n => {
  const s = n.kind === 'input' ? 8 + (maxS > 0 ? 30 * Math.abs(n.sensitivity || 0) / maxS : 0) : (n.kind === 'path' ? 18 : 26);
  return {id:n.id, label:n.label, level:LEVEL[n.kind], size:s,
          shape: n.kind === 'input' ? 'dot' : (n.kind === 'path' ? 'box' : 'star'),
          color:{background:COL[n.status] || '#ccc', border:'#555'},
          font:{color: n.kind === 'path' || n.kind === 'target' ? '#fff' : '#222', size: 13},
          borderWidth: n.status === 'missing' ? 3 : 1, shapeProperties:{borderDashes: n.status === 'missing' ? [4,3] : false}};
});
nodes.forEach(n => { if (n.shape === 'star') n.font = {color:'#222', size:14}; });
const edges = G.edges.map(e => ({from:e.source, to:e.target, arrows:'to',
  dashes: e.kind === 'aggregated_into' && !e.included, color:{color: e.kind === 'used_by' ? '#999' : '#555'}}));
const net = new vis.Network(document.getElementById('graph'), {nodes:new vis.DataSet(nodes), edges:new vis.DataSet(edges)},
  {layout:{hierarchical:{direction:'LR', sortMethod:'directed', levelSeparation:280, nodeSpacing:115}},
   physics:false, interaction:{hover:true}});
const byId = Object.fromEntries(G.nodes.map(n => [n.id, n]));
function show(id){ const n = byId[id]; if(!n) return;
  const clean = Object.fromEntries(Object.entries(n).filter(([k,v]) => v !== null && v !== undefined && !(Array.isArray(v) && !v.length)));
  document.getElementById('detail').textContent = JSON.stringify(clean, null, 2); }
net.on('click', p => { if (p.nodes.length) show(p.nodes[0]); });
document.getElementById('maxs').textContent = maxS.toFixed(3) + ' in log10';
show('target');
</script></body></html>"""


def _fmt(x):
    if x is None:
        return "n/a"
    return f"{x:.3g}"


def legend_html():
    return "".join(f'<span><i class="sw" style="background:{COLOURS[k]}"></i>{html.escape(v)}</span>' for k, v in LEGEND)


def render_page(state: dict, title: str, extra_meta: str = "", back_link: str = "") -> str:
    r = state["result"]
    unit = state["target"]["unit"] or "(pure number)"
    meta = (f"Target unit: <b>{html.escape(unit)}</b> &middot; central estimate <b>{_fmt(r.get('central'))}</b> "
            f"&middot; 80% interval [{_fmt(r.get('p10'))}, {_fmt(r.get('p90'))}] &middot; valid paths {r.get('n_valid_paths', 0)}"
            f"{' &middot; outliers ' + ', '.join(r['outliers']) if r.get('outliers') else ''}")
    if extra_meta:
        meta += "<br>" + extra_meta
    if state["target"].get("definition"):
        meta += "<br>Target definition (model): " + html.escape(state["target"]["definition"])
    if back_link:
        meta += f'<br><a href="{back_link}">&larr; index</a>'
    return (PAGE.replace("__TITLE__", html.escape(title)).replace("__VIS__", VIS)
            .replace("__H1__", html.escape(title)).replace("__META__", meta).replace("__LEGEND__", legend_html())
            .replace("__COLOURS__", json.dumps(COLOURS))
            .replace("__GRAPH__", json.dumps(state["graph"], ensure_ascii=False).replace("</", "<\\/")))


INDEX = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>triangulate graphs</title>
<style>body{font-family:system-ui,Segoe UI,Arial,sans-serif;margin:24px;color:#222}
table{border-collapse:collapse;font-size:13px}td,th{border:1px solid #ccc;padding:4px 8px;text-align:right}
td:first-child,th:first-child{text-align:left}a{color:#2457b3}.note{font-size:13px;color:#555;max-width:900px}</style>
</head><body><h1>triangulate: dependency graphs</h1>
<p class="note">__NOTE__</p>
<h2>Finance demo (not scored)</h2><ul>__DEMO__</ul>
<h2>realFP backtest (20 questions)</h2>
<p class="note">Question pages live in <code>realfp/</code> and are local only (realFP has no licence, so question text is not committed).
Run <code>python -m triangulate report</code> to (re)build them.</p>
<table><tr><th>id</th><th>target unit</th><th>naive |log10 err|</th><th>structured |log10 err|</th><th>structured 80% covers</th><th>valid paths</th><th>outliers</th></tr>
__ROWS__</table></body></html>"""


def render_index(rows: list, demo_links: list, note: str) -> str:
    def cell(x):
        return "fail" if x is None else (f"{x:.2f}" if isinstance(x, float) else html.escape(str(x)))
    body = "".join(
        f'<tr><td><a href="realfp/{r["file"]}">{html.escape(r["id"])}</a></td><td>{html.escape(r["unit"] or "(pure number)")}</td>'
        f'<td>{cell(r["naive_err"])}</td><td>{cell(r["structured_err"])}</td><td>{cell(r["covered"])}</td>'
        f'<td>{r["n_valid_paths"]}</td><td>{html.escape(", ".join(r["outliers"]))}</td></tr>' for r in rows)
    demo = "".join(f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label in demo_links)
    return INDEX.replace("__ROWS__", body).replace("__DEMO__", demo).replace("__NOTE__", note)
