// Verrier · 浅色版落地页脚本（verrier_apple.html）：语言切换、导航状态、hero 产品卡（读 /api/result，失败用 HTML 里的快照）、
// 区间件布局、大数字适配、一个约 60 行的滚动场景驱动（M4 / M5 / M6 / M10）、IO 触发的一次性动效，以及控制台的焦点管理和
// 给共享 JS 的 window.VERRIER = {play, mission}：mission(m) 驱动 sheet 工具栏里的 #apProg 分段进度条。
// 不改共享 JS；必须在 verrier_evidence.js / verrier_graph.js / verrier_console.js 之前加载。动效都在 CSS 里，这里只写类名和 --p。
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
    $$("img[data-alt-en]").forEach(el => { el.alt = z ? el.dataset.altZh : el.dataset.altEn; });
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

  // ---------- 区间件：比例尺定义域 [p10 − 8%·w, p90 + 8%·w]；估计点和官方刻度相距不到 16px 时，官方标签挪到轨道下方 ----------
  function placeRg(rg) {
    const p10 = +rg.dataset.p10, p90 = +rg.dataset.p90, w = p90 - p10, lo = p10 - .08 * w;
    if (!(w > 0)) return;
    const x = v => cl((v - lo) / (1.16 * w)) * 100, c = x(+rg.dataset.c), o = x(+rg.dataset.o);
    rg.style.setProperty("--c", c.toFixed(2) + "%");
    rg.style.setProperty("--o", o.toFixed(2) + "%");
    const tw = rg.firstElementChild.clientWidth;
    if (tw && rg.querySelector(".rg-ol")) rg.classList.toggle("lo", Math.abs(c - o) / 100 * tw < 16);
  }
  // 大数字按所在宽度缩小（13 位的韩元金额在 80px 下会溢出）：只缩不放，最小 32px。只量数字：
  // 控制台 .cx-big 的第一个子节点是数字文本，后面的单位 span 由 CSS 排成单独一行、固定 17px，不参与缩放
  function fit(el) {
    el.style.fontSize = "";
    const w = el.clientWidth, t = el.firstChild;
    if (!w) return;
    let nw = el.scrollWidth;
    if (t && t.nodeType === 3 && t.nodeValue.trim()) { const r = document.createRange(); r.selectNodeContents(t); nw = r.getBoundingClientRect().width; }
    if (nw <= w) return;
    el.style.fontSize = Math.max(32, Math.floor(parseFloat(getComputedStyle(el).fontSize) * w / nw)) + "px";
  }

  // ---------- hero 产品卡：实时读 /api/result，拿不到就保留 HTML 里的快照（2026-10-19 抄录） ----------
  const SNAP = 7395676.450898756, pcard = $("pcard"), hst = $("hstage");
  let xf = false;   // M1 已开播且实时值和快照差 >0.1% 时，换掉的数字做 200ms 交叉淡入；相同的值不动
  const setK = (k, v, html) => $$(`[data-k="${k}"]`).forEach(el => {
    if (String(html ? el.innerHTML : el.textContent) === String(v)) return;
    if (html) el.innerHTML = v; else el.textContent = v;
    if (xf) { el.classList.remove("xf"); void el.offsetWidth; el.classList.add("xf"); }
  });
  async function live() {
    const ac = window.AbortController ? new AbortController() : null, t = setTimeout(() => ac && ac.abort(), 2500);
    try {
      const r = await fetch("/api/result?qid=fc_lhr_pax_2026_09&tag=test1", {cache: "no-store", signal: ac && ac.signal});
      const j = r.ok ? await r.json() : null, e = j && j.estimate, o = j && j.official;
      if (!e || !isFinite(e.central) || !o || !isFinite(o.answer_value)) return;
      const ev = j.evidence || {}, ms = j.methods || [], sh = (j.assumption_share || {}).overall, usd = (j.budget || {}).usd_total_assumed;
      xf = started && !reduce && Math.abs(e.central / SNAP - 1) > .001;
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
      if (Math.abs(e.central / SNAP - 1) > .001) console.warn("Verrier: live central differs from the snapshot by >0.1% — check the s4 copy.", e.central);
    } catch (err) { /* 离线或超时：快照模式 */ } finally { clearTimeout(t); }
  }
  // M1：字体就绪（最多等 300ms）就用 HTML 里的快照开播，不等接口；实时数据到了只静默替换 [data-k]。↻ 重放
  const heroParts = () => [hst, ...$$(".rg.m7", hst)];
  let started = false;
  function startHero() {
    if (started) return;
    started = true;
    relayout();
    heroParts().forEach(go);
  }
  function playHero() {
    if (reduce) return;
    heroParts().forEach(el => el.classList.remove("go"));
    void hst.offsetWidth;
    heroParts().forEach(go);
  }
  Promise.race([document.fonts ? document.fonts.ready.catch(() => {}) : 0, new Promise(r => setTimeout(r, 300))]).then(startHero, startHero);
  live();
  $$("[data-replay]").forEach(b => b.addEventListener("click", () => {
    const r = $("s0").getBoundingClientRect();
    if (r.bottom < 120 || r.top > innerHeight) $("s0").scrollIntoView();
    playHero();
  }));

  // ---------- IO 触发的一次性动效：M3 错峰、刻度尺、M7（s4 卡片）、M8（T-01）、M9（误差柱） ----------
  if (!reduce) {
    $$("[data-st]").forEach(el => once(el, e => e.classList.add("in"), {rootMargin: "0px 0px -20% 0px"}));   // 组的顶边过视口 80%（手机上便当格很高，按比例 .2 永远达不到）
    once($("ruler"), go, {threshold: .5});
    $$(".qrows.m8").forEach(el => once(el, go, {threshold: .3}));
    $$(".qc .rg.m7").forEach(el => once(el, go, {threshold: .6}));
    once($("trio"), go, {rootMargin: "0px 0px -50% 0px"});
    // 键盘聚焦到还没出现的内容：立刻显示；焦点落进钉住的流水线卡时，把页面滚到这个部件已经出现的进度
    document.addEventListener("focusin", e => {
      const t = e.target, g = t.closest && t.closest("[data-st]");
      if (g) g.classList.add("in");
      const pan = t.closest && t.closest("#pin2 .pp-pan"), sc = scenes.find(x => x.el.id === "pin2");
      if (!pan || !sc) return;
      measure();
      if (!sc.pin) return;
      const w = t.closest(".pw"), cs = v => parseFloat(getComputedStyle(v).getPropertyValue("--s"));
      const p = w && isFinite(cs(w)) ? cs(w) + .07 : Math.max(0, parseFloat(getComputedStyle(pan).getPropertyValue("--a")) + .05);
      requestAnimationFrame(() => scrollTo(0, Math.round(sc.top + cl(p) * (sc.h - innerHeight))));   // 等浏览器自己的聚焦滚动做完再滚
    });
  }

  // ---------- 导航：hero 文字滚到导航下面时换玻璃底；进入暗场景换暗色；当前节加 .on ----------
  const nav = $("lnav"), s0 = $("s0");
  let glassAt = 0;
  const navUpd = () => nav.classList.toggle("glass", scrollY > glassAt);
  const navCalc = () => { glassAt = s0.firstElementChild.getBoundingClientRect().top + scrollY - 62; navUpd(); };   // hero 文字一碰到导航就换玻璃底
  addEventListener("scroll", navUpd, {passive: true});
  // ≤734：#nav 收进品牌右侧的 chevron 下拉菜单
  const mb = $("mnav"), setOpen = o => { nav.classList.toggle("open", o); mb.setAttribute("aria-expanded", String(o)); };
  mb.addEventListener("click", e => { e.stopPropagation(); setOpen(!nav.classList.contains("open")); });
  $$("#nav a").forEach(a => a.addEventListener("click", () => setOpen(false)));
  document.addEventListener("click", e => { if (nav.classList.contains("open") && !nav.contains(e.target)) setOpen(false); });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && nav.classList.contains("open")) { setOpen(false); mb.focus(); } });
  if (hasIO) {
    const dk = new Set();
    const dio = new IntersectionObserver(es => {
      es.forEach(e => e.isIntersecting ? dk.add(e.target) : dk.delete(e.target));
      nav.classList.toggle("dark", dk.size > 0);
    }, {rootMargin: "-52px 0px -90% 0px"});
    $$("main [data-theme=dark]").forEach(s => dio.observe(s));
    const links = $$("#nav a"), secs = $$("main .sec");
    const vio = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      const i = secs.indexOf(e.target);
      links.forEach((a, k) => { const on = k + 1 === i; a.classList.toggle("on", on); if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    }), {rootMargin: "-50% 0px -50% 0px"});
    secs.forEach(s => vio.observe(s));
  }

  // ---------- 滚动场景驱动：IO 判断场景在视口附近才算；p = clamp((scrollY − top) / (height − innerHeight))，|Δp| > .0005 才写回 --p ----------
  const scenes = [];
  const addScene = (el, upd, stick) => { if (el) scenes.push({el, upd, stick: stick && el.querySelector(stick), top: 0, h: 0, on: !hasIO, p: -1, pin: true}); };
  function measure() {
    scenes.forEach(s => {
      const r = s.el.getBoundingClientRect();
      s.top = r.top + scrollY;
      s.h = r.height;
      s.pin = !s.stick || getComputedStyle(s.stick).position === "sticky";   // ≤1068 或减少动态时不钉住：什么都不写
    });
  }
  const prog = (s, H) => cl((scrollY - s.top) / Math.max(1, s.h - H));
  function writeP(s, p) {
    if (Math.abs(p - s.p) <= .0005 && !((p === 0 || p === 1) && p !== s.p)) return false;
    s.p = p;
    s.el.style.setProperty("--p", p.toFixed(4));
    return true;
  }
  let raf = 0;
  const frame = () => { raf = 0; const H = innerHeight; scenes.forEach(s => { if (s.on && s.pin) s.upd(s, H); }); };
  const kick = () => { if (!raf) raf = requestAnimationFrame(frame); };
  if (!reduce) {
    addScene($("pin1"), (s, H) => writeP(s, prog(s, H)), ".p1-stage");                                   // M4
    addScene($("pin2"), (s, H) => {                                                                       // M6
      const p = prog(s, H);
      if (!writeP(s, p)) return;
      const st = String(p < .16 ? 0 : p < .33 ? 1 : p < .58 ? 2 : p < .8 ? 3 : 4);
      if (s.el.dataset.step !== st) s.el.dataset.step = st;
    }, ".p2-stage");
    addScene($("narr"), (s, H) => $$(".ln", s.el).forEach(l => {                                          // M5：句子中线从 75% 移到 45%
      const r = l.getBoundingClientRect();
      if (!r.height) return;
      const v = cl((.75 * H - (r.top + r.height / 2)) / (.3 * H)).toFixed(3);
      if (l._o !== v) { l._o = v; l.style.setProperty("--o", v); }
    }));
    addScene(document.querySelector(".uses"), (s, H) => $$(".uph", s.el).forEach(f => {                   // M10：tile 顶边 70vh → −5vh
      const t = cl((.7 * H - f.getBoundingClientRect().top) / (.75 * H)), v = (30 * (1 - t)).toFixed(1) + "px";
      if (f._v !== v) { f._v = v; f.style.setProperty("--py", v); }
    }));
    if (hasIO) {
      const sio = new IntersectionObserver(es => { es.forEach(e => { const s = scenes.find(x => x.el === e.target); if (s) s.on = e.isIntersecting; }); kick(); },
        {rootMargin: "200px 0px"});
      scenes.forEach(s => sio.observe(s.el));
    }
    addEventListener("scroll", kick, {passive: true});
  }

  // ---------- 布局重算：区间件、大数字、场景位置、导航阈值 ----------
  const cx = $("cx"), card = cx.querySelector(".cx-card"), cxBody = $("cxBody");
  function relayout() {
    $$(".rg").forEach(placeRg);
    $$(".fit").forEach(fit);
    $$(".cx-big", cxBody).forEach(fit);
    measure();
    navCalc();
    kick();
  }
  let rt = 0;
  addEventListener("resize", () => { cancelAnimationFrame(rt); rt = requestAnimationFrame(relayout); });
  addEventListener("load", relayout);
  // 大数字的字重可能在它第一次出现时才开始下载：字体每加载完一批都重算
  if (document.fonts) { document.fonts.ready.then(relayout, () => {}); if (document.fonts.addEventListener) document.fonts.addEventListener("loadingdone", relayout); }
  relayout();

  // ---------- 控制台：焦点进出、共享 JS 生成内容的可访问性补丁、依赖图缩放控件 ----------
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
    const host = svg.parentNode, wrap = document.createElement("div"), seg = document.createElement("div");
    wrap.className = "cx-gscroll";
    seg.className = "seg";
    seg.setAttribute("role", "group");
    seg.innerHTML = `<i class="thumb" aria-hidden="true"></i><button type="button" aria-pressed="true">${T("Fit to frame", "缩放到框内")}</button>` +
      `<button type="button" aria-pressed="false">${T("1:1 zoom", "1:1 放大")}</button>`;
    const hint = document.createElement("p");
    hint.className = "g-hint";
    hint.innerHTML = T("Scroll sideways to see the whole graph →", "横向滑动看全图 →");
    host.insertBefore(seg, svg);
    host.insertBefore(hint, svg);
    host.insertBefore(wrap, svg);
    wrap.appendChild(svg);
    const [a, b] = $$("button", seg), set = one => {
      wrap.classList.toggle("one", one);
      seg.classList.toggle("one", one);
      a.setAttribute("aria-pressed", String(!one));
      b.setAttribute("aria-pressed", String(one));
      hint.hidden = !one;
    };
    a.onclick = () => set(false);
    b.onclick = () => set(true);
    set(card.clientWidth >= 734);   // 宽 sheet 默认 1:1（缩进栏里标签只剩约 7px），窄屏默认缩放到框内
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
  // 状态词和共享 JS 的 strip 徽章同一套（verrier_console.js 的 ST 表），同一屏不出现两种说法
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
    pg.classList.toggle("wait", st === "AWAITING APPROVAL");   // 等待确认时当前段用橙色，和 gate、时间轴一致
    segs.forEach((s, i) => {   // 已过 = 墨色，当前 = 蓝（M12：phase 真的变了才从左展开），未到 = 灰
      const c = i < ph ? "p" : i === ph ? "n" : "";
      if (s.dataset.c === c) return;
      s.dataset.c = c;
      s.className = c + (c === "n" && !first && !reduce ? " pop" : "");
    });
    // 计时：服务端值校准，运行中本地每秒插值，同一视图里只增不减；依赖图页共享 JS 传的是 elapsed:0，隐藏
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
    // 花费：运行页 "US$ x / cap  AS OF d"；归档页 "US$ x  AS OF d"；依赖图 "N NODES · M EDGES"（原样）
    const cam = String(m.cam || ""), mu = cam.match(/US\$\s*([\d.]+|—)/), mc = cam.match(/\/\s*([\d.]+)/);
    apUsd.textContent = mu ? (mu[1] === "—" ? "$—" : "$" + (+mu[1]).toFixed(3)) + (mc ? " / $" + (+mc[1]).toFixed(2) : "") : cam;
  }
  window.VERRIER = {play() { if (!B.classList.contains("cx-open")) playHero(); }, mission};
  window.__apReady = true;   // 放在最后：前面任何一步抛错，<head> 的 3 秒保险都会撤掉 .enh，内容照常显示
})();
