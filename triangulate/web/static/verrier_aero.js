// Verrier · Aero 落地页脚本（verrier_aero.html）：语言切换、照片加载、hero 几何（地球准星、月球边缘对齐）、入场动效、
// 章节高亮、领域墙像素显影，以及给共享 JS 的 window.VERRIER = {play, mission}：mission(m) 画 #aeroHud 遥测条。
// 不改共享 JS；必须在 verrier_evidence.js / verrier_graph.js / verrier_console.js 之前加载。动效全部交给 CSS，这里只负责触发。
"use strict";
(() => {
  window.__aeroReady = true;
  const root = document.documentElement, body = document.body;
  const $ = id => document.getElementById(id);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = s => String(s).replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  const pad = n => String(n).padStart(2, "0");
  const mq = matchMedia("(prefers-reduced-motion: reduce)");
  let reduce = mq.matches;
  if (mq.addEventListener) mq.addEventListener("change", e => { reduce = e.matches; });
  const zh = () => root.dataset.lang === "zh";
  const hasIO = "IntersectionObserver" in window;
  const supportsView = !!(window.CSS && CSS.supports && CSS.supports("animation-timeline: view()"));
  // 进入视口一次就触发（阈值按规格）；没有 IO 时直接触发
  function once(el, threshold, fn, rootMargin) {
    if (!el) return;
    if (!hasIO) return fn(el);
    const io = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting && en.intersectionRatio >= threshold) { io.disconnect(); fn(el); }
    }), {threshold: [0, threshold], rootMargin: rootMargin || "0px"});
    io.observe(el);
  }

  // ---------- 语言（head 里的内联脚本已经设好初始值） ----------
  function ariaLang() { $$("[data-aria-en]").forEach(el => el.setAttribute("aria-label", zh() ? el.dataset.ariaZh : el.dataset.ariaEn)); }
  function setLang(l) {
    root.dataset.lang = l;
    root.lang = l === "zh" ? "zh-CN" : "en";
    try { localStorage.setItem("verrier-lang", l); } catch (e) { /* 隐私模式 */ }
    ariaLang();
    requestAnimationFrame(heroGeom);
  }
  $("lang").addEventListener("click", () => setLang(zh() ? "en" : "zh"));
  ariaLang();

  // ---------- 照片：加载完淡入、LQIP 淡出；失败时只留 LQIP 和回退色 ----------
  function wireImg(fig) {
    const img = fig.querySelector("img");
    if (!img) return;
    const ok = () => { if (img.naturalWidth) { fig.classList.add("is-loaded"); fig.classList.remove("is-missing"); } };
    const bad = () => fig.classList.add("is-missing");
    if (img.complete) (img.naturalWidth ? ok : bad)();
    img.addEventListener("load", ok);
    img.addEventListener("error", bad);
  }
  $$(".ph").forEach(wireImg);
  // 大照片：离视口 1.5 屏以内提前 decode（避免开窗那一刻卡顿）；不加 will-change（审计：常驻 will-change 违反性能预算）；不支持滚动驱动时用 IO 开窗
  const bigFigs = $$("main .sec:not(.hero) .stage > .ph");
  if (hasIO) {
    const dio = new IntersectionObserver(es => es.forEach(en => {
      if (!en.isIntersecting) return;
      const img = en.target.querySelector("img");
      if (img && img.decode) img.decode().catch(() => {});
      dio.unobserve(en.target);
    }), {rootMargin: "150% 0px"});
    bigFigs.forEach(f => dio.observe(f));
    if (!supportsView) {
      const sio = new IntersectionObserver(es => es.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add("open"); sio.unobserve(en.target); }
      }), {threshold: .12});
      bigFigs.forEach(f => sio.observe(f));
    }
  } else bigFigs.forEach(f => f.classList.add("open"));

  // ---------- M3 读数锁定：把数字拆成 span.dg > span.dv（读屏读 .sr 里的完整值）。每位先显示一条「未点亮」底线，锁定时换成数字，中间不出现别的数 ----------
  function split(el) {
    if (reduce || el.dataset.split) return;
    const txt = el.textContent, chars = [...txt], n = chars.filter(c => /\d/.test(c)).length;
    let k = 0;
    el.dataset.split = "1";
    el.innerHTML = `<span class="sr">${esc(txt)}</span><span class="rd" aria-hidden="true">${chars.map(c => /\d/.test(c)
      ? `<span class="dg" style="--k:${k++}"><span class="dv">${c}</span></span>` : `<span class="nd" style="--n:${n}">${esc(c)}</span>`).join("")}</span>`;
  }
  $$("[data-num]").forEach(split);

  // ---------- s0 hero：几何（按 object-fit / object-position 算出地球和月球边缘的屏幕坐标） ----------
  const hero = $("s0"), heroFig = hero.querySelector(".ph"), heroImg = heroFig.querySelector("img");
  const ret = $("reticle"), lead = $("lead"), fig1 = $("fig1"), rtL = $("rtLabel");
  const RT_FULL = "EARTH · ARTEMIS II · 6 APR 2026", RT_SHORT = "EARTH · 6 APR 2026";
  const EARTH = [.929, .48], LIMB = .142;   // 实测：地球亮部质心 (92.9%, 48.0%)，月球边缘 x = 14.2%
  const frac = v => /%$/.test(v) ? parseFloat(v) / 100 : null;
  const hit = (a, b) => a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;
  function heroGeom() {
    const r = heroFig.getBoundingClientRect();
    if (!r.width || !r.height) return;
    const W = r.width, H = r.height, iw = heroImg.naturalWidth || 1920, ih = heroImg.naturalHeight || 1280;
    const s = Math.max(W / iw, H / ih), dw = iw * s, dh = ih * s;
    const pos = getComputedStyle(heroImg).objectPosition.split(/\s+/);
    const px = frac(pos[0]) ?? .5, py = frac(pos[1] || "50%") ?? .5;
    const ox = (W - dw) * px, oy = (H - dh) * py;
    const ex = ox + EARTH[0] * dw, ey = oy + EARTH[1] * dh, limb = ox + LIMB * dw;
    const g = parseFloat(getComputedStyle(root).getPropertyValue("--g")) || 20;
    hero.style.setProperty("--hero-x", Math.round(Math.max(g, limb + 24)) + "px");
    heroFig.style.setProperty("--ox", ex.toFixed(1) + "px");
    heroFig.style.setProperty("--oy", ey.toFixed(1) + "px");
    [ret, lead].forEach(el => { el.style.setProperty("--ex", ex.toFixed(1) + "px"); el.style.setProperty("--ey", ey.toFixed(1) + "px"); });
    const over = ex + 60 - (W - 8), shift = over > 0 ? -over : 0;
    ret.style.setProperty("--rshift", shift.toFixed(1) + "px");
    // 准星落在画面里、且不压到文字时才显示（它只是装饰）
    const blockers = $$(".lock-a, .lock-b, .stats", hero).map(el => el.getBoundingClientRect());
    const box = {left: r.left + ex - 60, right: r.left + ex + 60, top: r.top + ey - 60, bottom: r.top + ey + 60};
    const blocked = blockers.some(b => hit(box, b));
    // 标签框按布局尺寸算（不读 getBoundingClientRect：准星入场时有 scale），四周留 16px
    const labelHits = txt => {
      if (rtL.textContent !== txt) rtL.textContent = txt;
      const w = rtL.offsetWidth, h = rtL.offsetHeight, right = r.left + ex + 60 + shift, bottom = r.top + ey - 66;
      const lb = {left: right - w - 16, right: right + 16, top: bottom - h - 16, bottom: bottom + 16};
      return blockers.some(b => hit(lb, b));
    };
    const noLabel = labelHits(RT_FULL) && labelHits(RT_SHORT);
    ret.classList.toggle("nolabel", noLabel);
    const inside = ex > 0 && ex < W && ey > 0 && ey < H;
    ret.classList.toggle("placed", inside && !blocked);
    // 引线：从准星下方接到右下角的图注
    const fr = fig1.getBoundingClientRect(), top = fr.top - r.top - 12, len = top - (ey + 64);
    const ok = inside && !blocked && len > 24 && r.left + ex >= fr.left - 4 && r.left + ex <= fr.right + 4;
    lead.style.setProperty("--lead-h", Math.max(0, len).toFixed(1) + "px");
    lead.classList.toggle("placed", ok);
  }
  let geomRaf = 0;
  const geomSoon = () => { cancelAnimationFrame(geomRaf); geomRaf = requestAnimationFrame(heroGeom); };
  addEventListener("resize", geomSoon);
  heroImg.addEventListener("load", geomSoon);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(geomSoon, () => {});
  heroGeom();

  // ---------- M1 + hero 编排：图片就绪（decode）或 1500 ms 后曝光；文字在 min(就绪, 800 ms) 后开始 ----------
  let heroLit = false, heroGo = false;
  const lit = () => { if (heroLit) return; heroLit = true; heroFig.classList.add("lit"); };
  const go = () => { if (heroGo) return; heroGo = true; heroGeom(); hero.classList.add("go"); };
  if (heroImg.decode) heroImg.decode().then(() => { lit(); go(); }, () => {});
  setTimeout(go, 800);
  setTimeout(lit, 1500);
  heroImg.addEventListener("animationend", e => { if (e.animationName === "aeroPush") heroFig.classList.add("settled"); });
  if (hasIO) new IntersectionObserver(es => es.forEach(en => hero.classList.toggle("off", !en.isIntersecting))).observe(hero);
  function replayHero() {
    const r = hero.getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) hero.scrollIntoView();
    if (reduce) return;
    hero.classList.remove("go");
    void hero.offsetWidth;   // 重排后再加回 .go，CSS 动画从头播；缓推挂在 .ph.lit 上，不受影响
    heroGo = true;
    hero.classList.add("go");
  }
  $$("[data-replay]").forEach(b => b.addEventListener("click", replayHero));

  // ---------- M2 各节入场（阈值 .25，只播一次；离开视口时把没播完的直接播完） ----------
  const finish = el => {
    if (!el.getAnimations) return;
    el.getAnimations({subtree: true}).forEach(a => { if (a.timeline === document.timeline) { try { a.finish(); } catch (e) { /* 无限循环等 */ } } });
  };
  const groups = $$("[data-rv]");
  if (hasIO && !reduce) {
    const rio = new IntersectionObserver(es => es.forEach(en => {
      const g = en.target;
      if (en.intersectionRatio >= .25 || (en.isIntersecting && en.intersectionRect.height >= innerHeight * .6)) g.classList.add("in");
      else if (!en.isIntersecting && g.classList.contains("in")) finish(g);
    }), {threshold: [0, .25, .5]});
    groups.forEach(g => rio.observe(g));
  } else groups.forEach(g => g.classList.add("in"));

  // M5 区间收拢（s1 刻度尺）→ 之后三个角度逐位锁定
  const lock = el => el.classList.add("lock");
  const ruler = $("ruler"), tl3 = $("tl3");
  const rulerGo = () => { ruler.classList.add("go"); $$("[data-lock]", tl3).forEach(lock); };
  // M6 流程进度（s2 竖线 + 编号点亮；s3 勾形描线）
  const steps = $("steps"), pillars = $("pillars"), trio = $("trio");
  const stepsGo = () => steps.classList.add("go");
  const pillarsGo = () => pillars.classList.add("go");
  // M7 误差条（s4）→ 之后数值逐位锁定
  const trioGo = () => { trio.classList.add("go"); $$("[data-lock]", trio).forEach(lock); };
  if (reduce || !hasIO) { rulerGo(); stepsGo(); pillarsGo(); trioGo(); $$("li", steps).forEach(li => li.classList.add("lit")); }
  else {
    once(ruler, .5, rulerGo);
    once(trio, .4, trioGo);
    once(pillars, .3, pillarsGo);
    if (!supportsView) once(steps, .2, stepsGo); else stepsGo();
    const lio = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add("lit"); lio.unobserve(en.target); } }),
      {rootMargin: "0px 0px -50% 0px"});
    $$("li", steps).forEach(li => lio.observe(li));
  }
  // 键盘聚焦到还没显示的内容：立刻显示终态
  document.addEventListener("focusin", e => {
    const t = e.target;
    if (!t.closest) return;
    if (t.closest(".hero") && !heroGo) go();
    const g = t.closest("[data-rv]");
    if (!g || g.classList.contains("done")) return;
    g.classList.add("in", "done");
    if (g.contains(ruler)) rulerGo();
    if (g.contains(steps)) { stepsGo(); $$("li", steps).forEach(li => li.classList.add("lit")); }
    if (g.contains(pillars)) pillarsGo();
    if (g.contains(trio)) trioGo();
    requestAnimationFrame(() => finish(g));
  });

  // ---------- 章节高亮：视口中线落在哪一节 ----------
  const secs = $$("main .sec"), navA = $$("#nav a"), idxA = $$("#idx a"), secNow = $("secNow");
  let cur = 0, mission = null;
  function setView(v) {
    cur = v;
    if (!mission) body.dataset.view = String(v);
    navA.forEach((a, i) => a.classList.toggle("on", i + 1 === v));
    idxA.forEach((a, i) => { a.classList.toggle("on", i === v); if (i === v) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    if (secNow) secNow.textContent = `${pad(v)} / 05`;
  }
  if (hasIO) {
    const vio = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) setView(secs.indexOf(en.target)); }),
      {rootMargin: "-50% 0px -50% 0px", threshold: 0});
    secs.forEach(s => vio.observe(s));
  }
  setView(0);
  // 顶栏：只在页面最上方、hero 文字还没碰到顶栏时透明；之后一律实心（审计：窄屏和 s4 的正文会从品牌字和导航底下滚过）。
  // 用滚动阈值而不是 IO：点导航直接跳过去时 IO 不会触发。滚动回调里只比较一个数，不读布局
  {
    const lockA = hero.querySelector(".lock-a");
    let solidAt = 0;
    const upd = () => body.classList.toggle("top-solid", scrollY > solidAt);
    const calc = () => {
      const top = parseFloat(getComputedStyle(root).getPropertyValue("--top")) || 64;
      solidAt = lockA.getBoundingClientRect().top + scrollY - top - 8;
      upd();
    };
    addEventListener("scroll", upd, {passive: true});
    let bt = 0;
    addEventListener("resize", () => { clearTimeout(bt); bt = setTimeout(calc, 150); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(calc, () => {});
    calc();
  }

  // ---------- M8 领域墙像素显影：进入视口且 decode 完成后，32×21 → 64×43 → 128×85 三级，每级 80 ms；同时最多 3 格，相隔 60 ms。显影前格子是 s2 纯色 ----------
  const STEPS = [[32, 21], [64, 43], [128, 85]];
  const queue = [];
  let active = 0, nextAt = 0;
  function pump() {
    while (active < 3 && queue.length) {
      const job = queue.shift(), now = performance.now(), wait = Math.max(0, nextAt - now);
      active++;
      nextAt = now + wait + 60;
      setTimeout(() => job(() => { active--; pump(); }), wait);
    }
  }
  function pixelate(fig, done) {
    const img = fig.querySelector("img"), cv = document.createElement("canvas"), ctx = cv.getContext && cv.getContext("2d");
    if (!ctx || !img.naturalWidth) { wireImg(fig); return done(); }
    cv.setAttribute("aria-hidden", "true");
    fig.appendChild(cv);
    let k = 0;
    const step = () => {
      const [w, h] = STEPS[k];
      cv.width = w; cv.height = h;
      ctx.imageSmoothingEnabled = true;   // 缩小时取平均色；放大靠 CSS image-rendering:pixelated 出方块
      ctx.drawImage(img, 0, 0, w, h);
      if (k === 0) fig.classList.add("is-loaded");   // 真图在 canvas 下面先显示好
      if (++k < STEPS.length) return void setTimeout(step, 80);
      setTimeout(() => { cv.classList.add("fade"); setTimeout(() => { cv.remove(); done(); }, 260); }, 80);
    };
    step();
  }
  const tiles = $$("[data-tile] .tph");
  if (reduce || !hasIO) tiles.forEach(wireImg);
  else {
    tiles.forEach(f => f.querySelector("img").addEventListener("error", () => f.classList.add("is-missing")));
    const tio = new IntersectionObserver(es => es.forEach(en => {
      if (!en.isIntersecting) return;
      tio.unobserve(en.target);
      const f = en.target, img = f.querySelector("img");
      const enqueue = () => { queue.push(done => pixelate(f, done)); pump(); };
      (img.decode ? img.decode() : Promise.resolve()).then(enqueue, () => { if (img.naturalWidth) enqueue(); else f.classList.add("is-missing"); });
    }), {rootMargin: "0px 0px -10% 0px"});
    tiles.forEach(f => tio.observe(f));
  }

  // ---------- 控制台：背景照片（第一次打开才插入）、焦点管理 ----------
  const cx = $("cx"), card = cx.querySelector(".cx-card"), cxBg = $("cxBgAero"), cxBody = $("cxBody");
  let bgDone = false, lastFocus = null;
  const P = "/static/aero_assets/img/aerospace-08";
  new MutationObserver(() => {
    if (!cx.hidden) {
      if (!bgDone) {
        bgDone = true;
        cxBg.innerHTML = `<picture><source type="image/avif" srcset="${P}-1920.avif 1920w, ${P}-2560.avif 2560w, ${P}-3840.avif 3840w" sizes="100vw">
          <img src="${P}-1920.jpg" width="1920" height="1280" alt="" decoding="async"></picture>`;
        const img = cxBg.querySelector("img");
        img.addEventListener("load", () => cxBg.classList.add("is-loaded"));
      }
      if (!lastFocus) lastFocus = document.activeElement;
      if (!card.contains(document.activeElement)) card.focus({preventScroll: true});
    } else {
      const f = lastFocus;
      lastFocus = null;
      if (f && f !== body && document.contains(f) && f.getClientRects().length) f.focus({preventScroll: true});
    }
  }).observe(cx, {attributes: true, attributeFilter: ["hidden"]});
  // 共享 JS 生成内容的两处可访问性补丁（只加属性，不改它的结构）：打字机不进 aria-live；依赖图节点可以用键盘选
  new MutationObserver(ms => {
    for (const m of ms) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      const th = n.classList && n.classList.contains("cx-think") ? [n] : $$(".cx-think", n);
      th.forEach(t => { t.setAttribute("aria-live", "off"); $$(".cx-tl, .cx-bits, .ask-orb", t).forEach(x => x.setAttribute("aria-hidden", "true")); });
      // 依赖图 SVG 包进横向滚动层，按 1:1 显示（click 监听挂在 svg 上，移动节点不会丢）
      // 窄屏（CSS 容器查询）默认缩放到框内看全貌，按钮切到 1:1 横滑
      $$(".cx-gsvg > svg", n).forEach(svg => {
        const wrap = document.createElement("div"), tool = document.createElement("div");
        wrap.className = "cx-gscroll";
        tool.className = "cx-gtool";
        const label = one => one ? '<span class="en">Fit to frame</span><span class="zh">缩放到框内</span>' : '<span class="en">1:1 zoom</span><span class="zh">1:1 放大</span>';
        tool.innerHTML = `<button type="button" aria-pressed="false">${label(false)}</button><span class="hint" aria-hidden="true">⟷ <span class="en">SCROLL</span><span class="zh">左右滑动</span></span>`;
        svg.parentNode.insertBefore(tool, svg);
        svg.parentNode.insertBefore(wrap, svg);
        wrap.appendChild(svg);
        const b = tool.querySelector("button");
        b.addEventListener("click", () => { const one = wrap.classList.toggle("one"); b.setAttribute("aria-pressed", String(one)); b.innerHTML = label(one); });
      });
      $$(".g-n:not([tabindex])", n).forEach(gn => {
        gn.setAttribute("tabindex", "0");
        gn.setAttribute("role", "button");
        gn.setAttribute("aria-label", (gn.querySelector("text") || {}).textContent || gn.getAttribute("data-id") || "node");
      });
      (n.classList.contains("cx-big") ? [n] : $$(".cx-big", n)).forEach(fitBig);
    }
  }).observe(cxBody, {childList: true, subtree: true});
  // 大数字按所在列宽缩小：13 位的韩元金额在 128px 下会被截断。只缩不放，最小 32px；换列宽、字体加载完、控制台打开时重算
  function fitBig(el) {
    el.style.fontSize = "";
    const w = el.clientWidth;
    if (!w || el.scrollWidth <= w) return;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    el.style.fontSize = Math.max(32, Math.floor(fs * w / el.scrollWidth)) + "px";
  }
  const refitBig = () => $$(".cx-big", cxBody).forEach(fitBig);
  let fitRaf = 0;
  addEventListener("resize", () => { cancelAnimationFrame(fitRaf); fitRaf = requestAnimationFrame(refitBig); });
  // 大数字的字重可能在它第一次出现时才开始下载：插入时量到的是回退字体的宽度，所以字体每加载完一批都重算
  if (document.fonts) { document.fonts.ready.then(refitBig); document.fonts.addEventListener("loadingdone", refitBig); }
  new MutationObserver(() => { if (!cx.hidden) requestAnimationFrame(refitBig); }).observe(cx, {attributes: true, attributeFilter: ["hidden"]});
  cxBody.addEventListener("keydown", e => {
    const gn = e.target.closest && e.target.closest(".g-n");
    if (!gn || (e.key !== "Enter" && e.key !== " ")) return;
    e.preventDefault();
    gn.dispatchEvent(new MouseEvent("click", {bubbles: true}));
  });

  // ---------- #aeroHud：VERRIER.mission(m) 驱动的任务遥测条 ----------
  const hud = $("aeroHud"), hSt = $("hudSt"), hStatus = $("hudStatus"), hView = $("hudView"), hPh = $("hudPh"), hOl = hPh.querySelector("ol");
  const hLis = $$("li", hPh), hClock = $("hudClock"), hCost = $("hudCost"), hArc = $("hudArc"), hUsd = $("hudUsd"), hCap = $("hudCap"), hAsof = $("hudAsof");
  const LIVE = ["PLANNING ROUTES", "IN FLIGHT", "AWAITING APPROVAL"], TICK = ["PLANNING ROUTES", "IN FLIGHT"], DEAD = ["MISSION FAILED", "MISSION ABORTED"];
  let clk = null, base = 0, baseAt = 0, shown = false, lastView = "";
  const fmtT = sec => { const s = Math.max(0, Math.floor(+sec || 0)); return `T+${pad(Math.floor(s / 3600))}:${pad(Math.floor(s % 3600 / 60))}:${pad(s % 60)}`; };
  const stopClock = () => { if (clk) { clearInterval(clk); clk = null; } };
  const startClock = () => { if (!clk) clk = setInterval(() => { hClock.textContent = fmtT(base + (performance.now() - baseAt) / 1000); }, 1000); };
  const setText = (el, s) => { if (el.textContent !== s) el.textContent = s; };
  function setMission(m) {
    mission = m || null;
    if (!m || m.status === "AWAITING QUESTION") {
      hud.hidden = true;
      shown = false;
      stopClock();
      body.dataset.view = m ? "m" : String(cur);
      if (!m) mission = null;
      return;
    }
    body.dataset.view = "m";
    const first = !shown;
    hud.hidden = false;
    shown = true;
    hSt.dataset.k = LIVE.includes(m.status) ? "live" : DEAD.includes(m.status) ? "dead" : "ok";
    setText(hStatus, String(m.status || ""));
    setText(hView, String(m.view || ""));
    // 阶段轨道：小于 phase 实心，等于 phase 红环，大于 phase 空心；phase = -1（失败 / 取消）全部变暗；done 全部实心
    const ph = typeof m.phase === "number" ? m.phase : -1;
    hPh.toggleAttribute("data-dead", ph < 0);
    hLis.forEach((li, i) => {
      const cls = ph < 0 ? "next" : m.done || i < ph ? "past" : i === ph ? "now" : "next";
      if (li.classList.contains(cls)) return;
      li.classList.remove("past", "now", "next", "pop");
      li.classList.add(cls);
      if (!first && !reduce && cls !== "next") { void li.offsetWidth; li.classList.add("pop"); }   // 只在状态真的变化时动一次
    });
    hOl.style.setProperty("--ph", String(ph < 0 ? 0 : m.done ? 1 : ph / 5));
    // T+ 时钟：服务端值校准，运行中本地每秒 +1，且同一个任务里只增不减。依赖图页共享 JS 传的是 elapsed:0（不是真值），显示「T+ —」
    const noClock = /^GRAPH/.test(String(m.view || "")) || (!(+m.elapsed) && m.status === "ARCHIVED RESULT");
    hClock.parentNode.classList.toggle("noclk", noClock);
    if (noClock) { stopClock(); setText(hClock, "T+ —"); }
    else {
      let sec = +m.elapsed || 0;
      if (clk && TICK.includes(m.status) && m.view === lastView) sec = Math.max(sec, base + (performance.now() - baseAt) / 1000);
      base = sec;
      baseAt = performance.now();
      setText(hClock, fmtT(base));
      if (TICK.includes(m.status)) startClock(); else stopClock();
    }
    lastView = String(m.view || "");
    // 成本表：运行页 "US$ x / cap  AS OF d"；归档页 "US$ x  AS OF d"（只显示数字）；依赖图 "N NODES · M EDGES"（原样）
    const cam = String(m.cam || ""), mu = cam.match(/US\$\s*([\d.]+|—)/), mc = cam.match(/\/\s*([\d.]+)/), ma = cam.match(/AS OF\s+(\S+)/);
    if (mu) {
      const usd = mu[1] === "—" ? null : +mu[1], cap = mc ? +mc[1] : null;
      setText(hUsd, usd === null ? "$—" : "$" + usd.toFixed(3));
      setText(hCap, cap ? `/ $${cap.toFixed(2)} CAP` : "");
      setText(hAsof, ma ? "AS OF " + ma[1] : "");
      hCost.classList.toggle("noarc", !cap);
      if (cap) {
        const f = Math.max(0, Math.min(1, (usd || 0) / cap));
        hArc.style.strokeDashoffset = String(75 - 75 * f);
        hArc.classList.toggle("hot", f >= .8);
      }
    } else {
      hCost.classList.add("noarc");
      setText(hUsd, cam);
      setText(hCap, "");
      setText(hAsof, "");
    }
  }
  function play() {
    if (body.classList.contains("cx-open")) {
      if (reduce) return;
      hud.classList.remove("sweep");
      void hud.offsetWidth;
      hud.classList.add("sweep");
      return;
    }
    replayHero();
  }
  window.VERRIER = {play, mission: setMission};
})();
