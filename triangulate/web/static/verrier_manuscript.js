// Verrier · 手稿版落地页脚本（verrier_manuscript.html）：语言切换、章节高亮、账页结果卡（读 /api/result，失败用 HTML 里的快照）、
// 区间件布局、大数字适配、三张图版（I：圆规和鹅毛笔画出发现过程；II：黄经刻度尺；III：方法的嵌套天球）、IO 触发的一次性动效，
// 以及控制台的焦点管理和给共享 JS 的 window.VERRIER = {play, mission}：mission(m) 驱动控制台工具栏里的 #apProg 分段进度条。
// 不改共享 JS；必须在 verrier_evidence.js / verrier_graph.js / verrier_console.js 之前加载。控制台部分和浅色版（verrier_apple.js）同一套写法。
"use strict";
(() => {
  const R = document.documentElement, B = document.body;
  const $ = id => document.getElementById(id), $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = R.classList.contains("rm"), zh = () => R.dataset.lang === "zh", hasIO = "IntersectionObserver" in window;
  const T = (en, z) => `<span class="en">${en}</span><span class="zh">${z}</span>`;
  const esc = s => String(s).replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  const cl = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const f0 = v => Math.round(v).toLocaleString("en-US");
  const go = el => el && el.classList.add("go");
  function once(el, fn, opt) {   // 进入视口一次就触发；没有 IO 时直接触发
    if (!el) return;
    if (!hasIO) return fn(el);
    const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { io.disconnect(); fn(el); } }, opt);
    io.observe(el);
  }

  // ---------- 语言（<head> 已设好初始值） ----------
  function ariaLang() {
    const z = zh();
    $$("[data-aria-en]").forEach(el => el.setAttribute("aria-label", z ? el.dataset.ariaZh : el.dataset.ariaEn));
  }
  $("lang").addEventListener("click", () => {
    const l = zh() ? "en" : "zh";
    R.dataset.lang = l;
    R.lang = l === "zh" ? "zh-CN" : "en";
    try { localStorage.setItem("verrier-lang", l); } catch (e) { /* 隐私模式 */ }
    ariaLang();
    requestAnimationFrame(relayout);
  });
  ariaLang();

  // ---------- 区间件：比例尺定义域 [p10 − 8%·w, p90 + 8%·w]；估计点和官方刻度相距不到 16px 时，官方标签挪到刻度尺下方 ----------
  function placeRg(rg) {
    const p10 = +rg.dataset.p10, p90 = +rg.dataset.p90, w = p90 - p10, lo = p10 - .08 * w;
    if (!(w > 0)) return;
    const x = v => cl((v - lo) / (1.16 * w)) * 100, c = x(+rg.dataset.c), o = x(+rg.dataset.o);
    rg.style.setProperty("--c", c.toFixed(2) + "%");
    rg.style.setProperty("--o", o.toFixed(2) + "%");
    const tw = rg.firstElementChild.clientWidth;
    if (tw && rg.querySelector(".rg-ol")) rg.classList.toggle("lo", Math.abs(c - o) / 100 * tw < 16);
  }
  // 大数字按所在宽度缩小：只缩不放，最小 32px（控制台 .cx-big 的第一个子节点是数字文本）
  function fit(el) {
    el.style.fontSize = "";
    const w = el.clientWidth, t = el.firstChild;
    if (!w) return;
    let nw = el.scrollWidth;
    if (t && t.nodeType === 3 && t.nodeValue.trim()) { const r = document.createRange(); r.selectNodeContents(t); nw = r.getBoundingClientRect().width; }
    if (nw <= w) return;
    el.style.fontSize = Math.max(32, Math.floor(parseFloat(getComputedStyle(el).fontSize) * w / nw)) + "px";
  }

  // ---------- 账页结果卡：实时读 /api/result，拿不到就保留 HTML 里的快照（2026-10-19 抄录，和浅色版同一份） ----------
  const SNAP = 7395676.450898756, pcard = $("pcard");
  const setK = (k, v, html) => $$(`[data-k="${k}"]`).forEach(el => {
    if (String(html ? el.innerHTML : el.textContent) === String(v)) return;
    if (html) el.innerHTML = v; else el.textContent = v;
    if (!reduce) { el.classList.remove("xf"); void el.offsetWidth; el.classList.add("xf"); }
  });
  async function live() {
    const ac = window.AbortController ? new AbortController() : null, t = setTimeout(() => ac && ac.abort(), 2500);
    try {
      const r = await fetch("/api/result?qid=fc_lhr_pax_2026_09&tag=test1", {cache: "no-store", signal: ac && ac.signal});
      const j = r.ok ? await r.json() : null, e = j && j.estimate, o = j && j.official;
      if (!e || !isFinite(e.central) || !o || !isFinite(o.answer_value)) return;
      const ev = j.evidence || {}, ms = j.methods || [], sh = (j.assumption_share || {}).overall, usd = (j.budget || {}).usd_total_assumed;
      setK("central", f0(e.central));
      if (isFinite(e.p10)) setK("p10", f0(e.p10));
      if (isFinite(e.p90)) setK("p90", f0(e.p90));
      setK("official", f0(o.answer_value));
      if (o.released) setK("released", o.released);
      if (isFinite(o.pct_err)) setK("err", (o.pct_err > 0 ? "+" : "") + (o.pct_err * 100).toFixed(1) + "%");
      if (o.covered_80 === false) setK("cov", T("outside the 80% interval", "没落在 80% 区间内"), true);
      if (typeof sh === "number") {
        setK("ev", Math.round((1 - sh) * 100) + "%");
        setK("as", Math.round(sh * 100) + "%");
        $$(".ea").forEach(el => el.style.setProperty("--ev", (100 * (1 - sh)).toFixed(1) + "%"));
      }
      setK("kept", (ev.kept || []).length);
      setK("disc", (ev.discarded || []).length);
      setK("meth", `${ms.filter(m => m.status === "computed").length}/${ms.length}`);
      if (isFinite(usd)) setK("usd", "$" + Number(usd).toFixed(3));
      $$(".rg[data-live]").forEach(rg => {
        Object.assign(rg.dataset, {c: e.central, o: o.answer_value});
        if (isFinite(e.p10) && isFinite(e.p90)) Object.assign(rg.dataset, {p10: e.p10, p90: e.p90});
        placeRg(rg);
      });
      pcard.classList.add("is-live");
      if (Math.abs(e.central / SNAP - 1) > .001) console.warn("Verrier: live central differs from the snapshot by >0.1% — check the fol. 8 table.", e.central);
    } catch (err) { /* 离线或超时：快照模式 */ } finally { clearTimeout(t); }
  }
  live();

  // ---------- SVG 小工具 ----------
  const NS = "http://www.w3.org/2000/svg";
  const mk = (tag, a, p) => { const e = document.createElementNS(NS, tag); for (const k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; };
  const txt = (p, x, y, s, cls, a = {}) => { const t = mk("text", Object.assign({x, y, class: cls}, a), p); t.textContent = s; return t; };
  const rad = d => d * Math.PI / 180;
  const f1 = v => (+v).toFixed(1);
  const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2, eo = x => 1 - Math.pow(1 - x, 3);
  const seg = (t, a, b) => cl((t - a) / (b - a));

  // ---------- 图版 I：圆规画轨道、鹅毛笔描实测轨迹，推出预测位置（红笔），刻出海王星（约 6.6 秒，↻ 重绘） ----------
  const H = $("hsvg"), CX = 300, CY = 300, RU = 118, RN = 196;
  const TH_N = 326 + 57 / 60, TH_P = 325 + 58 / 60, AMP = 13, SIG = 34;
  const wrapD = d => ((d % 360) + 540) % 360 - 180;
  const bump = d => AMP * Math.exp(-Math.pow(wrapD(d - TH_N) / SIG, 2));
  const ROT = 57;   // 整张图版转 57°，让海王星落在底部正中；刻度上的数字仍是真实黄经
  const P = (r, d) => [CX + r * Math.cos(rad(d - ROT)), CY - r * Math.sin(rad(d - ROT))];
  const arcD = (rf, d0, d1, step = 1.5) => { const n = Math.max(1, Math.ceil(Math.abs(d1 - d0) / step)); let s = ""; for (let i = 0; i <= n; i++) { const d = d0 + (d1 - d0) * i / n, p = P(rf(d), d); s += (i ? "L" : "M") + f1(p[0]) + " " + f1(p[1]); } return s; };
  const plate = {};
  function buildPlate() {
    const g = mk("g", {filter: "url(#rough)"}, H);
    plate.frame = mk("g", {}, g);
    mk("rect", {x: 14, y: 14, width: 572, height: 572, class: "pl-ink"}, plate.frame);
    mk("rect", {x: 21, y: 21, width: 558, height: 558, class: "pl-thin"}, plate.frame);
    [[21, 21, 1, 1], [579, 21, -1, 1], [579, 579, -1, -1], [21, 579, 1, -1]].forEach(([x, y, sx, sy]) => {   // 角花
      mk("path", {d: `M${x + sx * 4} ${y + sy * 30} Q${x + sx * 4} ${y + sy * 4} ${x + sx * 30} ${y + sy * 4}`, class: "pl-thin"}, plate.frame);
      mk("circle", {cx: x + sx * 12, cy: y + sy * 12, r: 2.2, fill: "#2a211a"}, plate.frame);
    });
    txt(plate.frame, 40, 52, "TAB. I.", "pl-sc pl-rt");
    txt(plate.frame, 40, 70, "De inventione Neptuni", "pl-txt", {"font-size": 15});
    txt(plate.frame, 560, 566, "MDCCCXLVI", "pl-sc", {"text-anchor": "end", "font-size": 11, fill: "#5c4b3a"});
    // 黄经刻度环
    plate.ring = mk("g", {}, g);
    mk("circle", {cx: CX, cy: CY, r: 262, class: "pl-thin"}, plate.ring);
    mk("circle", {cx: CX, cy: CY, r: 274, class: "pl-ink"}, plate.ring);
    let ticks = "";
    for (let d = 0; d < 360; d += 2) { const a = P(262, d), b = P(d % 30 ? (d % 10 ? 265 : 268) : 274, d); ticks += `M${f1(a[0])} ${f1(a[1])}L${f1(b[0])} ${f1(b[1])}`; }
    mk("path", {d: ticks, class: "pl-thin"}, plate.ring);
    for (let d = 0; d < 360; d += 30) { const p = P(250, d); txt(plate.ring, f1(p[0]), f1(p[1] + 4), d + "°", "pl-num", {"text-anchor": "middle"}); }
    // 太阳：直线与波纹光芒交替
    plate.sun = mk("g", {}, g);
    let rays = "";
    for (let i = 0; i < 16; i++) {
      const d = i * 22.5, a = P(15, d);
      if (i % 2) { const b = P(25, d); rays += `M${f1(a[0])} ${f1(a[1])}L${f1(b[0])} ${f1(b[1])}`; }
      else { const m1 = P(19, d + 4), m2 = P(23, d - 4), b = P(28, d); rays += `M${f1(a[0])} ${f1(a[1])}Q${f1(m1[0])} ${f1(m1[1])} ${f1((m1[0] + m2[0]) / 2)} ${f1((m1[1] + m2[1]) / 2)}T${f1(b[0])} ${f1(b[1])}`; }
    }
    mk("path", {d: rays, class: "pl-thin"}, plate.sun);
    mk("circle", {cx: CX, cy: CY, r: 11, fill: "#f5eddc", class: "pl-ink"}, plate.sun);
    mk("circle", {cx: CX, cy: CY, r: 2.2, fill: "#2a211a"}, plate.sun);
    txt(plate.sun, CX + 16, CY + 34, "Sol", "pl-txt");
    // 开普勒轨道（点线，用遮罩显出）+ 实测轨迹（实线，用 dashoffset 描出）
    const defs = mk("defs", {}, H);
    const mU = mk("mask", {id: "mU", maskUnits: "userSpaceOnUse"}, defs);
    plate.mUp = mk("path", {d: arcD(() => RU, 150, 510), fill: "none", stroke: "#fff", "stroke-width": 9, pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, mU);
    plate.kep = mk("circle", {cx: CX, cy: CY, r: RU, class: "pl-ink", "stroke-dasharray": "1.6 4.2", mask: "url(#mU)"}, g);
    plate.kepLab = txt(g, 0, 0, "", "pl-txt");
    plate.kepLab.innerHTML = "";
    { const p = P(RU + 14, 168); plate.kepLab.setAttribute("x", f1(p[0])); plate.kepLab.setAttribute("y", f1(p[1])); plate.kepLab.setAttribute("text-anchor", "end"); plate.kepLab.textContent = "Orbita Urani · theoria"; }
    plate.hatch = mk("path", {d: arcD(d => RU + bump(d), 282, 372) + arcD(() => RU, 372, 282).replace("M", "L") + "Z", fill: "url(#hatch)", opacity: 0}, g);
    plate.obs = mk("path", {d: arcD(d => RU + bump(d), 150, 400), class: "pl-ink", "stroke-width": 1.7, pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, g);
    plate.pull = mk("g", {opacity: 0}, g);
    [303, 327, 351].forEach(d => { const a = P(RU + bump(d) + 4, d), b = P(RU + bump(d) + 22, d); mk("path", {d: `M${f1(a[0])} ${f1(a[1])}L${f1(b[0])} ${f1(b[1])}`, class: "pl-ink", "stroke-width": 1, "marker-end": "url(#arw)"}, plate.pull); });
    { const p = P(RU - 20, 318); txt(plate.pull, f1(p[0]), f1(p[1]), "perturbatio", "pl-txt", {"text-anchor": "end", "font-size": 13}); }
    { const p = P(RU + bump(378) + 16, 382); plate.obsLab = txt(g, f1(p[0]), f1(p[1]), "Via observata", "pl-txt", {opacity: 0, "font-size": 13}); }
    // 天王星（1846 年附近的位置，示意）
    plate.ura = mk("g", {opacity: 0}, g);
    { const p = P(RU + bump(40), 40); mk("circle", {cx: f1(p[0]), cy: f1(p[1]), r: 6.5, fill: "url(#hatchL)", class: "pl-ink"}, plate.ura); mk("ellipse", {cx: f1(p[0]), cy: f1(p[1]), rx: 3, ry: 11, class: "pl-thin", transform: `rotate(16 ${f1(p[0])} ${f1(p[1])})`}, plate.ura); txt(plate.ura, f1(p[0] + 12), f1(p[1] - 8), "Uranus", "pl-txt"); }
    // 假想行星的轨道（虚线，遮罩显出）
    const mN = mk("mask", {id: "mN", maskUnits: "userSpaceOnUse"}, defs);
    plate.mNp = mk("path", {d: arcD(() => RN, 290, 362), fill: "none", stroke: "#fff", "stroke-width": 9, pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, mN);
    plate.hyp = mk("circle", {cx: CX, cy: CY, r: RN, class: "pl-ink", "stroke-dasharray": "8 5", mask: "url(#mN)"}, g);
    // 推理线：从三处偏差指向预测位置
    const PP = P(RN, TH_P);
    plate.inf = [300, 327, 354].map(d => { const a = P(RU + bump(d), d); return mk("path", {d: `M${f1(a[0])} ${f1(a[1])}L${f1(PP[0])} ${f1(PP[1])}`, class: "pl-thin", pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, g); });
    // 预测位置：红笔十字 + 圆
    plate.locus = mk("g", {opacity: 0}, H);
    mk("path", {d: `M${f1(PP[0] - 9)} ${f1(PP[1] - 9)}L${f1(PP[0] + 9)} ${f1(PP[1] + 9)}M${f1(PP[0] + 9)} ${f1(PP[1] - 9)}L${f1(PP[0] - 9)} ${f1(PP[1] + 9)}`, class: "pl-red"}, plate.locus);
    plate.locC = mk("circle", {cx: f1(PP[0]), cy: f1(PP[1]), r: 24, class: "pl-red", "stroke-width": 1, pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, plate.locus);
    txt(plate.locus, f1(PP[0] - 32), f1(PP[1] - 4), "Locus praedictus", "pl-txt pl-rt", {"text-anchor": "end"});
    txt(plate.locus, f1(PP[0] - 32), f1(PP[1] + 12), "λ 325° 58′ · 31 Aug.", "pl-num", {"text-anchor": "end", fill: "#a63a24", "font-size": 12.5});
    // 海王星：铜版画排线球体
    const NN = P(RN, TH_N), nr = 14;
    plate.nep = mk("g", {opacity: 0}, H);
    const cp = mk("clipPath", {id: "cNep"}, defs); mk("circle", {cx: f1(NN[0]), cy: f1(NN[1]), r: nr}, cp);
    const wipe = mk("clipPath", {id: "cWipe"}, defs); plate.wipe = mk("rect", {x: f1(NN[0] - nr - 2), y: f1(NN[1] - nr - 2), width: 0, height: nr * 2 + 4}, wipe);
    const body = mk("g", {"clip-path": "url(#cNep)"}, plate.nep);
    const ink = mk("g", {"clip-path": "url(#cWipe)"}, body);
    mk("circle", {cx: f1(NN[0]), cy: f1(NN[1]), r: nr, fill: "#f5eddc"}, ink);
    const sl = Math.hypot(NN[0] - CX, NN[1] - CY), ux = (NN[0] - CX) / sl, uy = (NN[1] - CY) / sl;   // 背光方向 = 背离太阳
    mk("circle", {cx: f1(NN[0] + ux * 6), cy: f1(NN[1] + uy * 6), r: nr * 1.05, fill: "url(#hatch)"}, ink);       // 背光面排线
    mk("circle", {cx: f1(NN[0] + ux * 10), cy: f1(NN[1] + uy * 10), r: nr * .95, fill: "url(#xhatch)"}, ink);     // 最暗处交叉排线
    [-6, 1, 7].forEach((dy, i) => mk("path", {d: `M${f1(NN[0] - nr)} ${f1(NN[1] + dy)}Q${f1(NN[0])} ${f1(NN[1] + dy + (i - 1) * 2 + 3)} ${f1(NN[0] + nr)} ${f1(NN[1] + dy)}`, class: "pl-thin", "stroke-width": i === 1 ? 1.1 : .6}, ink));
    plate.nepO = mk("circle", {cx: f1(NN[0]), cy: f1(NN[1]), r: nr, class: "pl-ink", "stroke-width": 1.4, pathLength: 1, "stroke-dasharray": 1, "stroke-dashoffset": 1}, plate.nep);
    // 标注：拉丁文印刷体 + 手写批注（按语言二选一）
    plate.nepLab = mk("g", {opacity: 0}, H);
    txt(plate.nepLab, f1(NN[0] + 30), f1(NN[1] - 6), "Neptunus", "pl-txt", {"font-size": 16});
    mk("path", {d: `M${f1(NN[0] + 104)} ${f1(NN[1] - 18)}v14M${f1(NN[0] + 99)} ${f1(NN[1] - 16)}v6q5 4 10 0v-6M${f1(NN[0] + 100)} ${f1(NN[1] - 8)}h8`, class: "pl-thin", "stroke-width": 1.1}, plate.nepLab);   // ♆ 三叉戟
    txt(plate.nepLab, f1(NN[0] + 30), f1(NN[1] + 10), "λ 326° 57′ · 23 Sept. 1846", "pl-num", {"font-size": 12.5});
    const hc = mk("clipPath", {id: "cHand"}, defs); plate.handR = mk("rect", {x: f1(CX - 110), y: f1(NN[1] + 24), width: 0, height: 40}, hc);
    const hg = mk("g", {"clip-path": "url(#cHand)"}, H);
    txt(hg, CX, f1(NN[1] + 50), "found within one degree", "pl-hand en", {"text-anchor": "middle"});
    txt(hg, CX, f1(NN[1] + 50), "相差不到一度，寻获", "pl-hand zh", {"text-anchor": "middle"});
    // 仪器：圆规（两脚 + 铰链 + 握柄）、鹅毛笔
    plate.cmp = mk("g", {class: "inst", opacity: 0}, H);
    plate.cmpL = mk("g", {}, plate.cmp);
    plate.quill = mk("g", {class: "inst", opacity: 0}, H);
    const q = mk("g", {transform: "rotate(-38)"}, plate.quill);
    mk("path", {d: "M0 0 L3 -10 L1.4 -46 C 16 -70 30 -104 22 -150 C 12 -118 -6 -88 -1.4 -46 L-3 -10 Z", fill: "#f5eddc", stroke: "#2a211a", "stroke-width": 1}, q);
    mk("path", {d: "M0 -12 C 6 -52 14 -96 22 -150", fill: "none", stroke: "#2a211a", "stroke-width": .8}, q);
    let barbs = "";
    for (let i = 0; i < 16; i++) { const y = -58 - i * 5.6, x = 4 + i * 1.05; barbs += `M${f1(x)} ${f1(y)}l${f1(9 - i * .25)} ${f1(-6)}M${f1(x - 1.5)} ${f1(y + 1)}l${f1(-8 + i * .3)} ${f1(-4)}`; }
    mk("path", {d: barbs, fill: "none", stroke: "#5c4b3a", "stroke-width": .55}, q);
    mk("path", {d: "M0 0 L1.6 -7 L-1.6 -7 Z", fill: "#2a211a"}, q);
  }
  function drawCompass(R0, deg) {   // 一脚钉在圆心，另一脚在轨道上，铰链在两脚上方
    const L = plate.cmpL, h = R0 * .58;
    L.innerHTML = "";
    L.setAttribute("transform", `translate(${CX} ${CY}) rotate(${f1(ROT - deg)})`);
    const hx = R0 / 2, hy = -h;
    mk("path", {d: `M0 0 L${f1(hx - 4)} ${f1(hy + 2)} L${f1(hx + 2)} ${f1(hy + 4)} Z`, fill: "#e6dac2", stroke: "#2a211a", "stroke-width": 1}, L);
    mk("path", {d: `M${R0} 0 L${f1(hx + 4)} ${f1(hy + 2)} L${f1(hx - 2)} ${f1(hy + 4)} Z`, fill: "#e6dac2", stroke: "#2a211a", "stroke-width": 1}, L);
    mk("path", {d: `M${f1(hx * .5)} ${f1(hy * .5)}L${f1(hx * .5 + 3)} ${f1(hy * .5 + 1)}M${f1(R0 - hx * .5)} ${f1(hy * .5)}L${f1(R0 - hx * .5 - 3)} ${f1(hy * .5 + 1)}`, stroke: "#2a211a", "stroke-width": .6, fill: "none"}, L);
    mk("circle", {cx: f1(hx), cy: f1(hy + 3), r: 6, fill: "#e6dac2", stroke: "#2a211a", "stroke-width": 1.1}, L);
    mk("circle", {cx: f1(hx), cy: f1(hy + 3), r: 1.8, fill: "#2a211a"}, L);
    mk("path", {d: `M${f1(hx - 2.4)} ${f1(hy - 2)} L${f1(hx - 1.6)} ${f1(hy - 22)} L${f1(hx + 1.6)} ${f1(hy - 22)} L${f1(hx + 2.4)} ${f1(hy - 2)} Z`, fill: "#5c4b3a", stroke: "#2a211a", "stroke-width": .8}, L);
    mk("circle", {cx: R0, cy: 0, r: 1.6, fill: "#2a211a"}, L);
  }
  const quillAt = (path, p) => { const L = path.getTotalLength(), pt = path.getPointAtLength(L * cl(p)); plate.quill.setAttribute("transform", `translate(${f1(pt.x)} ${f1(pt.y)})`); };
  const quillLine = (a, b, p) => plate.quill.setAttribute("transform", `translate(${f1(a[0] + (b[0] - a[0]) * p)} ${f1(a[1] + (b[1] - a[1]) * p)})`);
  const END = 6.6;
  function render(t) {
    const fr = eo(seg(t, 0, .7));
    plate.frame.setAttribute("opacity", fr); plate.ring.setAttribute("opacity", fr); plate.sun.setAttribute("opacity", eo(seg(t, .2, .8)));
    // 1 圆规：开普勒轨道 0.5–1.7 s
    const k = ease(seg(t, .5, 1.7));
    plate.mUp.setAttribute("stroke-dashoffset", 1 - k);
    plate.kepLab.setAttribute("opacity", seg(t, 1.4, 1.8));
    // 2 鹅毛笔：实测轨迹 1.8–3.1 s
    const o = ease(seg(t, 1.8, 3.1));
    plate.obs.setAttribute("stroke-dashoffset", 1 - o);
    plate.obsLab.setAttribute("opacity", seg(t, 3.0, 3.3));
    plate.ura.setAttribute("opacity", seg(t, 2.9, 3.2));
    plate.hatch.setAttribute("opacity", .85 * eo(seg(t, 2.7, 3.3)));
    plate.pull.setAttribute("opacity", eo(seg(t, 3.0, 3.4)));
    // 3 圆规：假想轨道 3.3–4.0 s
    const hN = ease(seg(t, 3.3, 4.0));
    plate.mNp.setAttribute("stroke-dashoffset", 1 - hN);
    // 4 鹅毛笔：推理线 4.0–4.8 s，红笔标出预测位置 4.8–5.2 s
    plate.inf.forEach((l, i) => l.setAttribute("stroke-dashoffset", 1 - ease(seg(t, 4.0 + i * .25, 4.35 + i * .25))));
    plate.locus.setAttribute("opacity", seg(t, 4.75, 4.85));
    plate.locC.setAttribute("stroke-dashoffset", 1 - ease(seg(t, 4.8, 5.2)));
    // 5 刻出海王星 5.2–5.9 s，写批注 5.6–6.6 s
    plate.nep.setAttribute("opacity", seg(t, 5.15, 5.25));
    plate.nepO.setAttribute("stroke-dashoffset", 1 - ease(seg(t, 5.2, 5.55)));
    plate.wipe.setAttribute("width", f1(32 * ease(seg(t, 5.45, 5.95))));
    plate.nepLab.setAttribute("opacity", seg(t, 5.6, 5.9));
    plate.handR.setAttribute("width", f1(230 * seg(t, 5.8, 6.6)));
    // 仪器：圆规只在画轨道时出现，鹅毛笔跟着笔尖走
    const c1 = t >= .35 && t < 1.85, c2 = t >= 3.15 && t < 4.1;
    plate.cmp.setAttribute("opacity", c1 ? seg(t, .35, .5) * (1 - seg(t, 1.7, 1.85)) : c2 ? seg(t, 3.15, 3.3) * (1 - seg(t, 4.0, 4.1)) : 0);
    if (c1) drawCompass(RU, 150 + 360 * k); else if (c2) drawCompass(RN, 290 + 72 * hN);
    let qa = 0;
    if (t >= 1.75 && t < 3.25) { qa = seg(t, 1.75, 1.85) * (1 - seg(t, 3.1, 3.25)); quillAt(plate.obs, o); }
    else if (t >= 3.95 && t < 5.3) {
      qa = seg(t, 3.95, 4.05) * (1 - seg(t, 5.2, 5.3));
      const i = Math.min(2, Math.floor(cl((t - 4.0) / .25, 0, 2.99))), l = plate.inf[i], d = l.getAttribute("d").match(/-?[\d.]+/g).map(Number);
      if (t < 4.8) quillLine([d[0], d[1]], [d[2], d[3]], ease(seg(t, 4.0 + i * .25, 4.35 + i * .25))); else quillLine([d[2], d[3]], [d[2], d[3]], 1);
    }
    plate.quill.setAttribute("opacity", qa);
  }
  buildPlate();
  let raf0 = 0, t0 = 0;
  function playHero() {
    cancelAnimationFrame(raf0);
    if (reduce) { render(END); return; }
    t0 = performance.now();
    const step = now => { const t = (now - t0) / 1000; render(Math.min(t, END)); if (t < END) raf0 = requestAnimationFrame(step); };
    raf0 = requestAnimationFrame(step);
  }
  render(reduce ? END : 0);
  // 等字体就绪（最多 600ms）、页面在前台时开画；在后台就等切回来
  const startHero = () => {
    if (!document.hidden) return void setTimeout(playHero, 200);
    const h = () => { if (document.hidden) return; document.removeEventListener("visibilitychange", h); setTimeout(playHero, 200); };
    document.addEventListener("visibilitychange", h);
  };
  Promise.race([document.fonts ? document.fonts.ready.catch(() => {}) : 0, new Promise(r => setTimeout(r, 600))]).then(startHero, startHero);
  $$("[data-replay]").forEach(b => b.addEventListener("click", () => {
    const r = H.getBoundingClientRect();
    if (r.bottom < 80 || r.top > innerHeight) $("hplate").scrollIntoView({block: "center"});
    playHero();
  }));

  // ---------- 图版 II：黄经刻度尺 320°–332°（每格 10′） ----------
  (function buildRuler() {
    const S = $("rsvg"), x0 = 30, x1 = 530, d0 = 320, d1 = 332, X = d => x0 + (d - d0) / (d1 - d0) * (x1 - x0), y = 132;
    const g = mk("g", {filter: "url(#roughS)"}, S);
    mk("path", {d: `M${x0 - 10} ${y}H${x1 + 10}M${x0 - 10} ${y + 6}H${x1 + 10}`, class: "pl-ink"}, g);
    let tk = "";
    for (let i = 0; i <= 72; i++) { const d = d0 + i / 6, x = X(d), len = i % 12 === 0 ? 20 : i % 6 === 0 ? 14 : i % 3 === 0 ? 9 : 5; tk += `M${f1(x)} ${y}v${-len}`; }
    mk("path", {d: tk, class: "pl-thin"}, g);
    for (let d = d0; d <= d1; d += 2) txt(g, f1(X(d)), y + 28, d + "°", "pl-num", {"text-anchor": "middle", "font-size": 15});
    txt(g, x1 + 10, y + 52, "longitudo ecliptica", "pl-txt", {"text-anchor": "end", "font-size": 15, fill: "#5c4b3a"});
    const xp = X(TH_P), xo = X(TH_N);
    const mp = mk("g", {class: "r-mk p", style: `--dx:${f1(x0 - xp)}px`}, g);
    mk("path", {d: `M${f1(xp)} ${y}V72`, class: "pl-red"}, mp);
    mk("path", {d: `M${f1(xp - 6)} 64L${f1(xp + 6)} 64L${f1(xp)} 74Z`, fill: "#a63a24"}, mp);
    txt(mp, f1(xp - 10), 90, "praedictus", "pl-txt pl-rt", {"text-anchor": "end", "font-size": 17});
    txt(mp, f1(xp - 10), 109, "325° 58′", "pl-num", {"text-anchor": "end", fill: "#a63a24", "font-size": 16});
    const mo = mk("g", {class: "r-mk o", style: `--dx:${f1(x1 - xo)}px`}, g);
    mk("path", {d: `M${f1(xo)} ${y + 6}V76`, class: "pl-ink"}, mo);
    mk("circle", {cx: f1(xo), cy: 68, r: 6.5, fill: "url(#hatch)", class: "pl-ink"}, mo);
    txt(mo, f1(xo + 12), 90, "observatus", "pl-txt", {"font-size": 17});
    txt(mo, f1(xo + 12), 109, "326° 57′", "pl-num", {"font-size": 16});
    mk("path", {d: `M${f1(xp)} 48V40H${f1(xo)}V48`, class: "pl-ink r-br", pathLength: 1}, g);
    const hd = mk("g", {class: "r-hd"}, S);
    txt(hd, f1((xp + xo) / 2), 30, "Δλ = 0° 59′", "pl-txt", {"text-anchor": "middle", "font-size": 22, fill: "#a63a24"});
  })();

  // ---------- 图版 III：方法的五层天球（问题在中心，交付在最外层），指针缓慢转动 ----------
  const SP = {};
  (function buildSpheres() {
    const S = $("ssvg"), c = 260, bands = [46, 84, 122, 160, 198, 236];
    const LAB = ["I · QVAESTIO", "II · APPROBATIO", "III · COLLECTIO", "IV · COMPVTATIO", "V · TRADITIO"];
    const defs = mk("defs", {}, S), g = mk("g", {filter: "url(#roughS)"}, S);
    mk("circle", {cx: c, cy: c, r: 250, class: "pl-ink"}, g);
    let tk = "";
    for (let d = 0; d < 360; d += 3) { const a = rad(d), r1 = 243, r2 = d % 30 ? 247 : 250; tk += `M${f1(c + r1 * Math.cos(a))} ${f1(c - r1 * Math.sin(a))}L${f1(c + r2 * Math.cos(a))} ${f1(c - r2 * Math.sin(a))}`; }
    mk("path", {d: tk, class: "pl-thin"}, g);
    mk("path", {id: "spTop", d: `M${c - 258} ${c} A258 258 0 0 1 ${c + 258} ${c}`, fill: "none"}, defs);
    const tt = mk("text", {class: "pl-sc", "font-size": 12, "letter-spacing": 3}, g), tp = mk("textPath", {href: "#spTop", startOffset: "50%", "text-anchor": "middle"}, tt);
    tp.textContent = "SPHAERAE METHODI · VERRIER";
    SP.groups = LAB.map((s, i) => {
      const r0 = bands[i], r1 = bands[i + 1], rm = (r0 + r1) / 2 - 4, gi = mk("g", {class: "sp-g", "data-i": i}, g);
      mk("circle", {cx: c, cy: c, r: r1, class: "sp-band sp-ring", pathLength: 1}, gi);
      const rot = -70 + i * 38;
      mk("path", {id: "spA" + i, d: `M${f1(c - rm)} ${c} A${rm} ${rm} 0 0 1 ${f1(c + rm)} ${c}`, fill: "none", transform: `rotate(${rot} ${c} ${c})`}, defs);
      const t = mk("text", {class: "sp-lab"}, gi), p = mk("textPath", {href: "#spA" + i, startOffset: "50%", "text-anchor": "middle"}, t);
      p.textContent = s;
      const orb = mk("g", {class: "sp-orb", style: `--d:${[40, 56, 70, 90, 120][i]}s`}, gi);   // 每层一颗小球，内层转得快
      const a = rad(rot + 160), ox = c + (rm + 4) * Math.cos(a), oy = c - (rm + 4) * Math.sin(a);
      mk("circle", {cx: f1(ox), cy: f1(oy), r: 5, fill: "url(#hatch)", class: "pl-ink", "stroke-width": .9}, orb);
      return gi;
    });
    mk("circle", {cx: c, cy: c, r: bands[0], class: "sp-band sp-ring", pathLength: 1}, g);
    txt(g, c, c + 9, "V", "pl-sc pl-rt", {"text-anchor": "middle", "font-size": 30});
    txt(g, c, c + 26, "VERRIER", "pl-sc", {"text-anchor": "middle", "font-size": 8.5, "letter-spacing": 2});
    const arm = mk("g", {class: "sp-orb sp-arm"}, S);
    mk("path", {d: `M${c} ${c}L${c} ${c - 240}`, class: "pl-thin", "stroke-dasharray": "2 3"}, arm);
    mk("path", {d: `M${c - 5} ${c - 232}L${c} ${c - 244}L${c + 5} ${c - 232}Z`, fill: "#2a211a"}, arm);
  })();
  // 命题和天球同步高亮：区段在视口里时每 2.4 秒换一层；鼠标停在命题上就锁定那一层
  const props = $$("#props li");
  let spI = 0, spT = 0, spHold = -1;
  const spSet = i => { SP.groups.forEach((g, k) => g.classList.toggle("on", k === i)); props.forEach((li, k) => li.classList.toggle("on", k === i)); };
  props.forEach((li, i) => { li.addEventListener("mouseenter", () => { spHold = i; spSet(i); }); li.addEventListener("mouseleave", () => { spHold = -1; }); });
  spSet(0);
  if (hasIO && !reduce) new IntersectionObserver(es => es.forEach(e => {
    clearInterval(spT); spT = 0;
    if (e.isIntersecting) spT = setInterval(() => { if (spHold >= 0 || B.classList.contains("cx-open")) return; spI = (spI + 1) % 5; spSet(spI); }, 2400);
  }), {threshold: .35}).observe($("s2"));

  // ---------- IO 触发的一次性动效：墨迹晾干、贴条、红印、页边批注、图版描线、手写批注、条图、表格 ----------
  if (!reduce) {
    $$(".ink").forEach(el => once(el, e => e.classList.add("in"), {rootMargin: "0px 0px -12% 0px"}));
    $$("[data-st]").forEach(el => once(el, e => e.classList.add("in"), {rootMargin: "0px 0px -18% 0px"}));
    $$(".draw").forEach(el => once(el, go, {threshold: .35}));
    $$(".hand").forEach(el => once(el, go, {threshold: .6}));
    once($("trio"), go, {threshold: .5});
    document.addEventListener("focusin", e => {   // 键盘聚焦到还没出现的内容：立刻显示
      const t = e.target, g = t.closest && t.closest("[data-st],.ink,.draw");
      if (g) g.classList.add("in", "go");
    });
  } else $$(".ink,[data-st],.draw,.hand,#trio").forEach(el => el.classList.add("in", "go"));

  // ---------- 导航：当前章节加 .on；≤860 收进下拉菜单 ----------
  const nav = $("lnav"), mb = $("mnav"), setOpen = o => { nav.classList.toggle("open", o); mb.setAttribute("aria-expanded", String(o)); };
  mb.addEventListener("click", e => { e.stopPropagation(); setOpen(!nav.classList.contains("open")); });
  $$("#nav a").forEach(a => a.addEventListener("click", () => setOpen(false)));
  document.addEventListener("click", e => { if (nav.classList.contains("open") && !nav.contains(e.target)) setOpen(false); });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && nav.classList.contains("open")) { setOpen(false); mb.focus(); } });
  if (hasIO) {
    const links = $$("#nav a"), secs = $$("main .sec");
    const vio = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      const i = secs.indexOf(e.target);
      links.forEach((a, k) => { const on = k + 1 === i; a.classList.toggle("on", on); if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    }), {rootMargin: "-50% 0px -50% 0px"});
    secs.forEach(s => vio.observe(s));
  }

  // ---------- 布局重算：区间件、大数字 ----------
  const cx = $("cx"), card = cx.querySelector(".cx-card"), cxBody = $("cxBody");
  function relayout() {
    $$(".rg").forEach(placeRg);
    $$(".fit").forEach(fit);
    $$(".cx-big", cxBody).forEach(fit);
  }
  let rt = 0;
  addEventListener("resize", () => { cancelAnimationFrame(rt); rt = requestAnimationFrame(relayout); });
  addEventListener("load", relayout);
  if (document.fonts) { document.fonts.ready.then(relayout, () => {}); if (document.fonts.addEventListener) document.fonts.addEventListener("loadingdone", relayout); }
  relayout();

  // ---------- 控制台：焦点进出、共享 JS 生成内容的可访问性补丁、依赖图缩放控件（和浅色版同一套） ----------
  let back = null;
  new MutationObserver(() => {
    if (!cx.hidden) {
      if (!back) back = document.activeElement;
      if (!card.contains(document.activeElement)) card.focus({preventScroll: true});
      requestAnimationFrame(() => $$(".cx-big", cxBody).forEach(fit));
    } else {
      const f = back;
      back = null;
      if (f && f !== B && document.contains(f)) requestAnimationFrame(() => { if (f.getClientRects().length) f.focus({preventScroll: true}); });
    }
  }).observe(cx, {attributes: true, attributeFilter: ["hidden"]});
  function wrapGraph(svg) {   // 1:1 时可横向滚动；click 监听挂在 svg 上，移动节点不会丢
    const host = svg.parentNode, wrap = document.createElement("div"), sg = document.createElement("div");
    wrap.className = "cx-gscroll";
    sg.className = "seg";
    sg.setAttribute("role", "group");
    sg.innerHTML = `<i class="thumb" aria-hidden="true"></i><button type="button" aria-pressed="true">${T("Fit to frame", "缩放到框内")}</button>` +
      `<button type="button" aria-pressed="false">${T("1:1 zoom", "1:1 放大")}</button>`;
    const hint = document.createElement("p");
    hint.className = "g-hint";
    hint.innerHTML = T("Scroll sideways to see the whole graph →", "横向滑动看全图 →");
    host.insertBefore(sg, svg);
    host.insertBefore(hint, svg);
    host.insertBefore(wrap, svg);
    wrap.appendChild(svg);
    const [a, b] = $$("button", sg), set = one => {
      wrap.classList.toggle("one", one);
      sg.classList.toggle("one", one);
      a.setAttribute("aria-pressed", String(!one));
      b.setAttribute("aria-pressed", String(one));
      hint.hidden = !one;
    };
    a.onclick = () => set(false);
    b.onclick = () => set(true);
    set(card.clientWidth >= 734);
  }
  new MutationObserver(ms => {
    for (const m of ms) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      const all = s => (n.matches(s) ? [n] : []).concat($$(s, n));
      all(".cx-think").forEach(t => { t.setAttribute("aria-live", "off"); $$(".cx-tl,.ask-orb,.cx-bits", t).forEach(x => x.setAttribute("aria-hidden", "true")); });
      all(".cx-gsvg > svg").forEach(wrapGraph);
      all(".g-n:not([tabindex])").forEach(g => {
        g.setAttribute("tabindex", "0");
        g.setAttribute("role", "button");
        g.setAttribute("aria-label", (g.querySelector("text") || {}).textContent || g.getAttribute("data-id") || "node");
      });
      all(".cx-big").forEach(fit);
    }
  }).observe(cxBody, {childList: true, subtree: true});
  cxBody.addEventListener("keydown", e => {
    const g = e.target.closest && e.target.closest(".g-n");
    if (!g || (e.key !== "Enter" && e.key !== " ")) return;
    e.preventDefault();
    g.dispatchEvent(new MouseEvent("click", {bubbles: true}));
  });

  // ---------- #apProg：VERRIER.mission(m) 驱动的分段进度条（6 段 = 规划、确认、取证、裁判、计算、交付） ----------
  const pg = $("apProg"), segs = $$(".ap-segs i", pg), apSt = $("apSt"), apClk = $("apClk"), apUsd = $("apUsd");
  const WORD = {"PLANNING ROUTES": ["Planning", "规划中"], "AWAITING APPROVAL": ["Awaiting approval", "等待确认"], "IN FLIGHT": ["In flight", "运行中"],
    "TARGET ACQUIRED": ["Delivered", "已交付"], "MISSION FAILED": ["Failed", "失败"], "MISSION ABORTED": ["Cancelled", "已取消"], "ARCHIVED RESULT": ["Saved result", "已保存的结果"]};
  const TICK = ["PLANNING ROUTES", "IN FLIGHT"];
  let clk = 0, base = 0, at = 0, shown = 0, lastSt = "", lastView = "";
  const mmss = s => { s = Math.max(0, Math.floor(s)); return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); };
  const stopClk = () => { clearInterval(clk); clk = 0; };
  const show = s => { shown = s; apClk.textContent = mmss(s); };
  function mission(m) {
    if (!m || m.status === "AWAITING QUESTION") { pg.hidden = true; stopClk(); lastView = lastSt = ""; return; }
    const first = pg.hidden, st = String(m.status || ""), view = String(m.view || ""), w = WORD[st] || [esc(st), esc(st)];
    pg.hidden = false;
    if (st !== lastSt) { apSt.innerHTML = T(w[0], w[1]); lastSt = st; }
    const dead = !(m.phase >= 0), ph = dead ? -1 : m.done ? 6 : m.phase;
    pg.classList.toggle("dead", dead);
    pg.classList.toggle("wait", st === "AWAITING APPROVAL");
    segs.forEach((s, i) => {
      const c = i < ph ? "p" : i === ph ? "n" : "";
      if (s.dataset.c === c) return;
      s.dataset.c = c;
      s.className = c + (c === "n" && !first && !reduce ? " pop" : "");
    });
    const noClk = /^GRAPH/.test(view) || (!(+m.elapsed) && st === "ARCHIVED RESULT");
    pg.classList.toggle("noclk", noClk);
    if (noClk) stopClk();
    else {
      let sec = +m.elapsed || 0;
      if (view === lastView) sec = Math.max(sec, shown, clk ? base + (performance.now() - at) / 1000 : 0);
      base = sec;
      at = performance.now();
      show(sec);
      if (!TICK.includes(st)) stopClk();
      else if (!clk) clk = setInterval(() => show(Math.max(shown, base + (performance.now() - at) / 1000)), 1000);
    }
    lastView = view;
    const cam = String(m.cam || ""), mu = cam.match(/US\$\s*([\d.]+|—)/), mc = cam.match(/\/\s*([\d.]+)/);
    apUsd.textContent = mu ? (mu[1] === "—" ? "$—" : "$" + (+mu[1]).toFixed(3)) + (mc ? " / $" + (+mc[1]).toFixed(2) : "") : cam;
  }
  window.VERRIER = {play() { if (!B.classList.contains("cx-open")) playHero(); }, mission, render};
  window.__apReady = true;   // 放在最后：前面任何一步抛错，<head> 的 3 秒保险都会撤掉 .enh，内容照常显示
})();
