// Verrier 控制台的依赖图（路由 #console/graph/<题 id>/<tag>，由 verrier_console.js 取数、接线）：把 /api/graph 的 {nodes, edges}
// （outputs.dep_graph，和 graph.html 里的是同一份）画成分层的技术图纸 SVG，不用 CDN 上的库。四列从左到右：来源 → 数据点和假设 → 方法 → 目标。
// 细墨线；没连到目标的方法（失败或不进合并）和裁判丢弃的点用虚线；已公布的值（直接连到目标的数据点）、它连到目标的线和目标用红色。
// 列内顺序：从目标往左扫一遍，每个节点按它右边邻居的平均 y 排（稳定排序；右边没有邻居的排在最后，保持原顺序）。
// 纯函数 window.VERRIER_GRAPH = {draw(g), detail(g, id)}：返回 HTML 字符串，不发请求、不碰 DOM。graph.html 仍由 outputs.render_graph 生成，这里不碰。
"use strict";
(() => {
  // ---------- 工具（和 verrier_console.js 同一套 esc、T） ----------
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  const T = (en, zh) => `<span class="en">${en}</span><span class="zh">${zh}</span>`;   // 只传常量或已转义的文字
  // 详情里的数：≥ 100 取整加千分位（< 10000 的整数照写，年份不加逗号），更小的保留 4 位有效数字（1e-6 这类系数不会变成 0）
  const num = v => Math.abs(v) >= 100 ? (Number.isInteger(v) && Math.abs(v) < 1e4 ? String(v) : Math.round(v).toLocaleString("en-US"))
    : String(Number(v.toPrecision(4)));

  const COL = {source: 0, point: 1, assumption: 1, method: 2, target: 3};
  const HEAD = [["SOURCES", "来源"], ["DATA POINTS · ASSUMPTIONS", "数据点 · 假设"], ["METHODS", "方法"], ["TARGET", "目标"]];
  const KIND = {source: ["Source", "来源"], point: ["Data point", "数据点"], assumption: ["Assumption", "假设"], method: ["Method", "方法"],
    target: ["Target", "目标"]};
  const W = 212, GAP = 64, PAD = 12, TOP = 40, LINE = 13, VGAP = 7;   // 节点宽、列间距、边距、表头高、行高、节点间距（px）

  // 虚线 / 红色：dep_graph 只给算出估计的方法连到目标的边；已公布的值是直接连到目标的数据点
  function flags(g) {
    const kind = new Map(g.nodes.map(n => [n.id, n.kind]));
    const toTarget = new Set(g.edges.filter(e => e.to === "target").map(e => e.from));
    const pub = [...toTarget].filter(id => kind.get(id) === "point");
    return {dash: n => (n.kind === "method" && !toTarget.has(n.id)) || (n.kind === "point" && !n.detail.keep),
      red: n => pub.includes(n.id) || (n.kind === "target" && pub.length > 0)};
  }

  function layout(g) {
    const F = flags(g);
    const ns = g.nodes.map(n => ({id: n.id, kind: n.kind, col: COL[n.kind], lines: n.label.split("\n"), dash: F.dash(n), red: F.red(n)}));
    const by = new Map(ns.map(n => [n.id, n]));
    const es = g.edges.filter(e => by.has(e.from) && by.has(e.to)).map(e => [by.get(e.from), by.get(e.to)]);   // 两端都在图里才画
    const right = new Map(ns.map(n => [n.id, []]));
    es.forEach(([a, b]) => right.get(a.id).push(b));   // 边都是从左列指向右列
    const cols = [[], [], [], []];
    ns.forEach(n => cols[n.col].push(n));
    const mid = n => n.y + n.h / 2;
    const place = (col, c) => { let y = TOP; col.forEach(n => { n.x = PAD + c * (W + GAP); n.y = y; n.h = 12 + LINE * n.lines.length; y += n.h + VGAP; }); };
    place(cols[3], 3);
    for (let c = 2; c >= 0; c--) {
      const key = new Map(cols[c].map(n => { const r = right.get(n.id); return [n.id, r.length ? r.reduce((s, m) => s + mid(m), 0) / r.length : Infinity]; }));
      cols[c].sort((a, b) => { const ka = key.get(a.id), kb = key.get(b.id); return ka === kb ? 0 : ka - kb; });
      place(cols[c], c);
    }
    const height = Math.max(...cols.map(col => col.length ? col[col.length - 1].y + col[col.length - 1].h : TOP)) + PAD;
    return {ns, es, cols, mid, width: 2 * PAD + 4 * W + 3 * GAP, height};
  }

  function draw(g) {
    const L = layout(g);
    const head = HEAD.map(([en, zh], c) => { const x = PAD + c * (W + GAP), n = String(c + 1).padStart(2, "0");
      return `<text class="g-h" x="${x}" y="16"><tspan class="en">${n} · ${en}</tspan><tspan class="zh">${n} · ${zh}</tspan> (${L.cols[c].length})</text>
        <path class="g-rule" d="M${x} 25H${x + W}"/>`; }).join("");
    const edge = ([a, b]) => { const x1 = a.x + W, y1 = L.mid(a), x2 = b.x, y2 = L.mid(b), mx = (x1 + x2) / 2;
      return `<path class="g-e${a.dash || b.dash ? " dash" : ""}${a.red && b.red ? " red" : ""}" d="M${x1} ${y1}C${mx} ${y1} ${mx} ${y2} ${x2} ${y2}"/>`; };
    const node = n => `<g class="g-n g-${n.kind}${n.dash ? " dash" : ""}${n.red ? " red" : ""}" data-id="${esc(n.id)}"><rect x="${n.x}" y="${n.y}" width="${W}" height="${n.h}"/>${
      n.lines.map((s, i) => `<text x="${n.x + 8}" y="${n.y + 16 + LINE * i}"${i ? "" : ' class="b"'}>${esc(s)}</text>`).join("")}</g>`;
    return `<div class="cx-gw"><div class="cx-gsvg"><svg viewBox="0 0 ${L.width} ${L.height}" width="${L.width}" height="${L.height}" role="img" aria-label="Dependency graph">
      ${head}${L.es.map(edge).join("")}${L.ns.map(node).join("")}</svg>
      <p class="fine">${T("Lines show what feeds what. Dashed: a method that is not in the combined estimate (failed or covers only part of the target), or a point the judge discarded. Red: a published value. Click a node to see its details.",
        "连线表示谁用了谁。虚线：没有进入合并估计的方法（失败或只覆盖目标的一部分），或裁判丢弃的数据点。红色：已公布的值。点一个节点看它的详情。")}</p></div>
      <aside class="cx-gside" id="cxGside"></aside></div>`;
  }

  // ---------- 侧栏：一个节点的详情（dep_graph 的 detail，按键排成表，嵌套的字典和列表画成内嵌的表；不是原样的 JSON） ----------
  function value(v) {
    if (v === null || v === undefined || v === "") return "—";
    if (typeof v === "number") return num(v);
    if (typeof v === "boolean") return v ? "true" : "false";
    if (typeof v === "string") return /^https?:\/\//.test(v) ? `<a href="${esc(v)}" target="_blank" rel="noopener noreferrer">${esc(v)}</a>` : esc(v);
    if (Array.isArray(v)) return !v.length ? "—" : v.every(x => x === null || typeof x !== "object") ? v.map(value).join(", ") : v.map(value).join("");
    const ks = Object.keys(v);
    return ks.length ? `<table class="cx-t cx-gd">${ks.map(k => `<tr><th>${esc(k)}</th><td>${value(v[k])}</td></tr>`).join("")}</table>` : "—";
  }
  function detail(g, id) {
    const n = g.nodes.find(x => x.id === id);
    const F = flags(g), red = F.red(n), dash = F.dash(n);
    const st = red ? T("Published value", "已公布的值") : dash && n.kind === "method" ? T("Not in the combined estimate", "没有进入合并估计")
      : dash ? T("Discarded by the judge", "裁判丢弃") : "";
    return `<div class="lbl">${T(...KIND[n.kind])} · ${esc(n.id)}</div>
      <div class="cx-gl">${esc(n.label)}</div>${st ? `<p class="${red ? "cx-bad" : "fine"}">${st}</p>` : ""}${value(n.detail)}`;
  }

  window.VERRIER_GRAPH = {draw, detail};
})();
