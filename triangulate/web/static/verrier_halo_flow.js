// Verrier HALO：从提问到结果的整套流程，画面用 verrier_halo.html（HALOFLUX by Ryder191 的非商业派生版，见那个文件开头的声明）。
// 这个文件是 Verrier 自己的代码，不是 HALOFLUX 的一部分：只通过页面里已有的名字（V、CODE、CHECKS、HEAD、KEYS、CODE_T、slots、
// ROUTES、COLSR、rState、renderRoutes、agEl、segs、feed、drawAdv / drawDiff / drawVal / drawIdx / agentsTick、flashSlotAt、
// cLine / cChar / cNum / typed、cAdv / cDiff / cVal / cIdx、FONT、T、TAU、rnd、rr、gauss）读写画面。
// 只调用现有接口（同 verrier_console.js）：/api/providers、/api/key/check、POST /api/runs、/api/runs/{id}（轮询）、/approve、/cancel、
// /api/saved、/api/result。路由：#ask（默认）、#run/<运行 id>、#result/<题 id>/<tag>（旧的 #<题 id>/<tag> 也认）。
// 显示的每个数都来自接口；流水只在状态真的变了时写一行；光环、光束是装饰。
"use strict";
(() => {
  const $ = id => document.getElementById(id);
  const esc = t => String(t == null ? "" : t).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const plain = t => String(t == null ? "" : t).replace(/[<>&]/g, " ");
  function fmtN(v) {
    if (v == null || typeof v !== "number" || !isFinite(v)) return "—";
    return Math.abs(v) >= 1e4 ? Math.round(v).toLocaleString("en-US") : (+v.toPrecision(4)).toLocaleString("en-US", { maximumFractionDigits: 6 });
  }
  function short(v) {
    if (v == null || typeof v !== "number" || !isFinite(v)) return "—";
    const a = Math.abs(v);
    return a >= 1e12 ? (v / 1e12).toFixed(2) + "T" : a >= 1e9 ? (v / 1e9).toFixed(2) + "B" : a >= 1e6 ? (v / 1e6).toFixed(2) + "M"
      : a >= 1e4 ? (v / 1e3).toFixed(1) + "K" : String(+v.toPrecision(3));
  }
  const money = x => x == null ? "—" : "$" + Number(x).toFixed(2);
  const setArr = (a, items) => { a.length = 0; items.forEach(v => a.push(v)); };
  async function api(path, opts) {
    const r = await fetch(path, opts);
    let b = null;
    try { b = await r.json(); } catch (e) { /* 非 JSON */ }
    if (!r.ok) throw new Error((b && b.detail) || `HTTP ${r.status}`);
    return b;
  }
  const post = (path, data) => api(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data || {}) });
  const CAT = { related_series: "rel", own_history: "own", capacity_consumption: "cap", base_rates: "base", physical_flow: "flow",
    forecasts_markets: "fcst", persona: "pers", shocks: "shck", administrative: "adm", attention: "attn" };
  const flash = () => { try { flashSlotAt(rnd() * TAU); } catch (e) { /* 光环还没建好 */ } };

  // ---------- 样式（Verrier 自己的浮层和表单，配色沿用页面的变量） ----------
  const css = document.createElement("style");
  css.textContent = `
.hx{position:absolute;z-index:4;pointer-events:auto;background:rgba(8,9,11,.95);border:1px solid var(--line2);font-size:10px;color:var(--text)}
.hx h2{margin:2px 0 8px;font-size:clamp(20px,2.6vw,34px);font-weight:800;color:var(--white);letter-spacing:1px}
.hx .eyb{font-size:8px;color:var(--dim);letter-spacing:1.4px}
.hx-ask{left:8px;top:6px;width:min(56%,760px);padding:12px 14px}
.hx textarea{width:100%;min-height:64px;resize:vertical;background:#050607;color:var(--white);border:1px solid var(--line2);padding:8px;
  font:12px "JetBrains Mono",Consolas,monospace}
.hx input,.hx select{background:#050607;color:var(--text);border:1px solid var(--line2);font:10px "JetBrains Mono",Consolas,monospace;padding:3px 5px}
.hx-row{display:flex;align-items:center;gap:8px;margin-top:8px;flex-wrap:wrap}
.hx-chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}
.hx-chips button{background:transparent;color:var(--dim);border:1px solid var(--line2);font:9px "JetBrains Mono",Consolas,monospace;padding:2px 6px;cursor:pointer}
.hx-chips button:hover{color:var(--white);border-color:var(--text)}
.hx-btn{background:transparent;color:var(--text);border:1px solid var(--line2);font:800 10px "JetBrains Mono",Consolas,monospace;
  letter-spacing:1.2px;padding:5px 12px;cursor:pointer}
.hx-btn:hover{border-color:var(--white);color:var(--white)}
.hx-btn.primary{background:#d6d8dd;color:#000;border-color:#d6d8dd}
.hx-btn.primary:hover{background:#fff}
.hx-btn:disabled{opacity:.45;cursor:default}
.hx .fine{font-size:8px;color:var(--dim)}
.hx .bad{color:var(--pink)} .hx .ok{color:var(--teal)}
.hx-gate{right:14px;top:40px;bottom:44px;width:min(48%,680px);padding:10px 12px;overflow:auto}
.hx-gate h3,.askp h3{margin:0 0 6px;font-size:9px;font-weight:800;letter-spacing:1.3px;color:var(--white)}
.hx-tgt{display:grid;grid-template-columns:96px 1fr;gap:2px 8px;font-size:9px;margin-bottom:8px}
.hx-tgt b{color:var(--dim);font-weight:600}
.hx-dir{display:block;border:1px solid var(--line);padding:5px 7px;margin:5px 0;font-size:9px;line-height:1.4;cursor:pointer}
.hx-dir.off{opacity:.4}
.hx-dir .hd{display:flex;gap:8px;align-items:center;color:var(--white);font-weight:800}
.hx-dir .cat{color:var(--teal);font-weight:600}
.hx-dir .dots{color:var(--pink);letter-spacing:1px}
.hx-x{border:1px solid rgba(240,166,198,.5);padding:6px 8px;margin:6px 0;font-size:9px}
.hx-x b{color:var(--white);font-size:12px}
.runsel{display:flex;gap:6px;align-items:center}
.hx-new{padding:2px 8px;font-size:9px;background:rgba(8,9,11,.85)}
.est .hx-btn{pointer-events:auto;margin-top:8px}
.est .num.stage{font-size:clamp(20px,2.4vw,32px)}
body.mode-ask .panels > .p.data{display:none}
body.mode-ask .est,body.mode-ask .hx-new{display:none}
.askp{border:1px solid var(--line);background:var(--panel);padding:7px 10px 8px;min-width:0;overflow:auto;max-height:30vh;font-size:9px}
.askp.w2{grid-column:span 2}
.askp dl{display:grid;grid-template-columns:86px 1fr;gap:4px 8px;margin:0;align-items:center}
.askp dt{color:var(--dim)} .askp dd{margin:0}
.askp .li{display:block;color:var(--text);text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:1px 0}
.askp .li:hover{color:var(--white)}
.askp .li i{font-style:normal;color:var(--dim)}
.askp .big{font-size:18px;font-weight:800;color:var(--white)}
`;
  document.head.appendChild(css);
  document.querySelectorAll(".panels > .p").forEach(p => p.classList.add("data"));

  // 流水：一行一条真实记录（页面里的 feedPush 在结果画面轮放 V.feed，也走这里）
  const VERB = { seek: "read", keep: "keep", drop: "drop", calc: "calc" };
  let feedN = 1;
  V.push = (v, t) => {
    const d = document.createElement("div"), n = document.createElement("span"), b = document.createElement("span");
    n.className = "n"; n.textContent = String(feedN++).padStart(3, "0");
    b.className = "vb " + v; b.textContent = VERB[v] || v;
    d.append(n, b, document.createTextNode(String(t)));
    feed.appendChild(d);
    while (feed.children.length > 14) feed.removeChild(feed.firstChild);
    flash();
  };
  const kpi = (i, v, f) => { $("k" + i).textContent = v; segs[i].style.width = Math.round(100 * Math.max(0, Math.min(1, f))) + "%"; };
  const placeholder = (ctxBox, text) => {
    const x = ctxBox.x, w = ctxBox.w, h = ctxBox.h;
    x.clearRect(0, 0, w, h);
    x.fillStyle = "#6b6f78"; x.font = `600 8px ${FONT}`; x.textBaseline = "middle"; x.fillText(text, 6, h / 2);
  };

  // =========================================================
  // 结果（一次已保存的运行）
  // =========================================================
  function mres(m, f) { return m.error ? "rejected" : m.estimate != null ? f(m.estimate) : m.distribution ? "distribution" : "rejected"; }
  function drawCloud(est, label) {   // 按 P10、P90 拟合的对数正态，实时抽样画点（点不是计算时的蒙特卡洛样本）
    const lp10 = Math.log(est.p10), lp90 = Math.log(est.p90), mu = (lp10 + lp90) / 2, sg = (lp90 - lp10) / (2 * 1.2816);
    const dist = isFinite(mu) && sg > 0 ? { mu, sg } : null;
    let samples = [];
    return function (dt) {
      const x = cAdv.x, w = cAdv.w, h = cAdv.h;
      if (!dist) { placeholder(cAdv, label); return; }
      x.fillStyle = "rgba(14,15,18,0.35)"; x.fillRect(0, 0, w, h);
      const lo = dist.mu - 2.6 * dist.sg, hi = dist.mu + 2.6 * dist.sg, X = l => (l - lo) / (hi - lo) * w;
      x.strokeStyle = "rgba(235,238,244,.8)"; x.lineWidth = 1; x.beginPath();
      for (let i = 0; i <= 80; i++) {
        const l = lo + (hi - lo) * i / 80, z = (l - dist.mu) / dist.sg, y = h - 12 - Math.exp(-z * z / 2) * (h - 26);
        i ? x.lineTo(X(l), y) : x.moveTo(X(l), y);
      }
      x.stroke();
      for (let k = 0; k < 3; k++) samples.push({ l: dist.mu + gauss() * 1.5 * dist.sg, y: 0, v: rr(20, 60) });
      x.fillStyle = "rgba(240,166,198,.85)";
      samples.forEach(s => { s.y += s.v * dt; x.fillRect(X(s.l), s.y, 1.5, 1.5); });
      samples = samples.filter(s => s.y < h - 12);
      x.font = `600 7px ${FONT}`; x.textBaseline = "alphabetic";
      [[lp10, "P10"], [Math.log(est.central), "EST"], [lp90, "P90"]].forEach(([l, t]) => {
        const xx = X(l);
        x.strokeStyle = t === "EST" ? "#fff" : "rgba(152,224,207,.8)"; x.beginPath(); x.moveTo(xx, 8); x.lineTo(xx, h - 12); x.stroke();
        x.fillStyle = "#9a9ea7"; x.fillText(`${t} ${short(Math.exp(l))}`, Math.min(w - 52, xx + 2), t === "EST" ? 8 : h - 2);
      });
    };
  }

  function vBind(d, pick) {
    const est = d.estimate || {}, comb = est.combination || {}, blocks = comb.blocks || [];
    const ev = d.evidence || {}, kept = ev.kept || [], disc = ev.discarded || [], pages = ev.pages || {};
    const ms = d.methods || [], dirs = d.directions || [];
    const okm = ms.filter(m => (m.estimate != null || m.distribution) && !m.error);   // 离散题的方法给的是概率分布
    const discrete = d.mode === "discrete", xfig = d.existing;                          // xfig：选用的现成数据（没有区间、没有方法）
    const nb = blocks.length || (okm.length ? 1 : 0);                                  // v2.12 之前的运行没有块的结构：算出来就当一块
    const unit = est.unit || (d.target || {}).unit_canonical || "";
    const read = (pages.snapshot || 0) + (pages.live_dated || 0), dropped = pages.dropped || 0;
    const per = x => ({ k: kept.filter(p => p.direction_id === x.id).length, d: disc.filter(p => p.direction_id === x.id).length });

    $("estQ").textContent = d.question || pick.qid;
    const numEl = $("estNum");
    numEl.classList.remove("stage");
    if (xfig) {
      numEl.innerHTML = fmtN(xfig.value) + `<small>${esc(xfig.unit || unit)}</small>`;
      $("estIv").textContent = `existing figure (${xfig.type || "figure"}) · ${xfig.domain || ""}`;
    } else if (est.central == null && pick.most_likely == null && !discrete) {   // 中途取消 / 失败：只有已经取到的证据，没有估计
      numEl.textContent = pick.status === "cancelled" ? "ABORTED" : pick.status === "failed" ? "FAILED" : "NO ESTIMATE";
      $("estIv").textContent = pick.why || "no estimate in this run";
    } else {
      numEl.innerHTML = (est.central != null ? fmtN(est.central) : esc(pick.most_likely != null ? pick.most_likely : "—"))
        + `<small>${esc(discrete ? "most likely outcome" : unit)}</small>`;
      $("estIv").textContent = est.p10 != null && est.p90 != null ? `80% interval ${fmtN(est.p10)} – ${fmtN(est.p90)} ${unit}`
        : discrete && pick.most_likely_prob != null ? `probability ${(100 * pick.most_likely_prob).toFixed(1)}% · ${unit}` : "";
    }
    const usd = (d.budget || {}).usd_total_assumed;
    $("estMeta").textContent = `as of ${d.as_of || "—"} · ${d.model || ""} · ${usd != null ? "$" + usd.toFixed(2) : ""} · ${pick.qid}/${pick.tag}`;

    [[dirs.length, 1], [read, read / Math.max(1, read + dropped)], [kept.length, kept.length / Math.max(1, kept.length + disc.length)],
      [`${okm.length}/${ms.length}`, okm.length / Math.max(1, ms.length)], [nb, 1]].forEach(([v, f], i) => kpi(i, v, f));
    $("stBig").textContent = xfig ? "EXISTING FIGURE · NO ROUTE RUN" : `${okm.length} / ${ms.length} METHODS · ${nb} BLOCK${nb === 1 ? "" : "S"}`;
    $("stSm").textContent = `${kept.length} points kept · ${disc.length} discarded · ${read} pages read · ${dropped} dropped`;

    const F = [];
    dirs.forEach(x => {
      F.push(["seek", `${x.id} ${x.category} · ${x.perspective || ""}`]);
      kept.filter(p => p.direction_id === x.id).slice(0, 6).forEach(p => F.push(["keep", `${p.id} ${p.value_as_written} · ${p.name} · ${p.domain || ""}`]));
      disc.filter(p => p.direction_id === x.id).slice(0, 2).forEach(p => F.push(["drop", `${p.id} ${p.value_as_written} · ${p.name}`]));
    });
    ms.forEach(m => F.push(["calc", `${m.label || m.id} ${m.formula || m.method} = ${mres(m, short)}`]));
    if (est.central != null) F.push(["calc", `estimate ${short(est.central)} ${unit}`]);
    feed.innerHTML = "";
    V.feed = F;

    const C2 = ms.map(m => [plain(m.label || m.id), plain(m.formula || m.method), `   → ${mres(m, fmtN)}`]);
    (d.assumptions || []).forEach(a => C2.push([plain(a.id), plain(String(a.name || "").slice(0, 46)), ` = ${a.value} [${a.low}, ${a.high}] ${plain(a.unit || "")}`]));
    blocks.forEach(b => C2.push([plain(b.id), b.members.join(" + "), `   → ${fmtN(b.value)}`]));
    if (est.central != null) C2.push(["estimate", plain(comb.rule_across_blocks || est.weight_rule || "combine"), `   → ${fmtN(est.central)} ${plain(unit)}`]);
    if (C2.length) { setArr(CODE, C2); cLine = 0; cChar = 0; cNum = 1; typed = []; }

    const CK = ms.filter(m => m.formula).map(m => [`${String(m.label || m.id).toUpperCase()} · ${String(m.method).toUpperCase()}`, `${m.formula} = ${mres(m, short)}`]);
    blocks.forEach(b => CK.push([`BLOCK ${b.id}`, `${b.members.join(" + ")} → ${short(b.value)}`]));
    if (est.central != null) CK.push(["ESTIMATE", `${short(est.central)} ${unit}`]);
    if (xfig) CK.push(["EXISTING FIGURE", `${fmtN(xfig.value)} ${xfig.unit || ""}`]);
    if (CK.length) setArr(CHECKS, CK);

    const pts = kept.slice(0, 80);
    if (pts.length) {
      setArr(HEAD, pts.map(p => `${String(p.id).toUpperCase()} ${String(p.domain || "").replace(/^www\./, "").toUpperCase().slice(0, 14)}`));
      setArr(KEYS, [...new Set(pts.map(p => String(p.unit || "").slice(0, 10)).filter(Boolean))].slice(0, 20));
      setArr(CODE_T, pts.map(p => String(p.value_as_written || "").slice(0, 12)).filter(Boolean));
      slots.forEach(s => s.c = null);
    }

    const top = dirs.slice(0, 6);
    setArr(ROUTES, top.map(x => `${x.id} ${CAT[x.category] || x.category}`));
    setArr(COLSR, ["search", "read", "keep"]);
    setArr(rState, top.map(x => { const c = per(x); return c.k ? 3 : c.d ? 2 : 1; }));
    V.routePink = top.map(x => per(x).k === 0);
    renderRoutes();

    const agDirs = dirs.slice(0, 12);
    agEl.innerHTML = agDirs.map(x => `<div class="ag"><span class="id">${esc(x.id)}</span><span class="rl">${esc(CAT[x.category] || x.category)}</span>`
      + `<span class="cells">${"<i></i>".repeat(6)}</span><span class="st"></span></div>`).join("");
    const rows = [...agEl.children], ag = agDirs.map((x, i) => ({ ...per(x), row: rows[i], p: 0 }));
    agentsTick = function (dt) {
      ag.forEach(a => {
        a.p = Math.min(6, a.p + dt * 2.5);
        const tot = a.k + a.d, nk = tot ? Math.round(6 * a.k / tot) : 0, fill = Math.floor(a.p);
        const cells = a.row.children[2].children;
        for (let c = 0; c < 6; c++) cells[c].style.background = c >= fill || !tot ? "#1d1f24" : c < nk ? "#98e0cf" : "#f0a6c6";
        const st = tot ? `${a.k} kept · ${a.d} out` : "no points", se = a.row.children[3];
        if (se.textContent !== st) { se.textContent = st; se.className = "st" + (a.k ? " w" : ""); }
      });
    };

    drawAdv = drawCloud(est, discrete ? "discrete target: outcome probabilities, no interval" : xfig ? "existing figure: no interval" : "no interval for this run");

    const items = blocks.length ? blocks.map(b => ({ id: b.id, v: b.value, lab: b.members.join("+") }))
      : okm.filter(m => m.estimate != null).map(m => ({ id: m.label || m.id, v: m.estimate, lab: m.method }));
    const lp10 = Math.log(est.p10), lp90 = Math.log(est.p90), hasIv = isFinite(lp10) && isFinite(lp90);
    drawDiff = function () {
      const x = cDiff.x, w = cDiff.w, h = cDiff.h;
      if (!items.length || est.central == null) { placeholder(cDiff, "no blocks for this run"); return; }
      x.clearRect(0, 0, w, h);
      const ls = items.map(i => Math.log(i.v)).concat(hasIv ? [lp10, lp90] : []);
      const lo = Math.min(...ls) - 0.15, hi = Math.max(...ls) + 0.15, X = l => 64 + (l - lo) / (hi - lo) * (w - 74);
      x.font = `600 7px ${FONT}`; x.textBaseline = "middle";
      if (hasIv) { x.fillStyle = "rgba(152,224,207,.12)"; x.fillRect(X(lp10), 0, X(lp90) - X(lp10), h); }
      const rh = Math.min(18, (h - 8) / items.length);
      items.forEach((it, i) => {
        const y = 6 + i * rh + rh / 2, xx = X(Math.log(it.v));
        x.fillStyle = "#9a9ea7"; x.fillText(`${it.id} ${it.lab}`.slice(0, 13), 0, y);
        x.fillStyle = "#2b2e34"; x.fillRect(64, y - 1, w - 74, 2);
        x.fillStyle = "#f0a6c6"; x.fillRect(xx - 2, y - 4, 4, 8);
        x.fillStyle = "#cfd2d8"; x.fillText(short(it.v), Math.min(w - 34, xx + 5), y);
      });
      const xc = X(Math.log(est.central));
      x.strokeStyle = "#fff"; x.beginPath(); x.moveTo(xc, 0); x.lineTo(xc, h); x.stroke();
    };

    // 单位核对只算真走到这一步的：被别的检查拒掉的方法没有核对过单位，不算失败
    const unitOK = ms.filter(m => m.unit_check && m.unit_check.unit).length, unitBad = ms.filter(m => /unit check/i.test(m.error || "")).length;
    const nAudit = (d.audit_errors || []).length, hits = (d.leakage || {}).sentinel_hits || 0;
    drawVal = checksDrawer([["UNIT CHECK", `${unitOK} passed · ${unitBad} failed`, unitBad > 0],
      ["INPUT AUDIT", nAudit ? `${nAudit} methods rejected` : "no rejections", nAudit > 0],
      ["LEAK SENTINEL", `${hits} hits`, hits > 0], ["PAGES DROPPED", `${dropped} of ${read + dropped}`, false]]);

    const cols = [];
    ms.forEach(m => (m.inputs || []).forEach(i => {
      if (!cols.find(c => c.id === i.id)) cols.push({ id: i.id, kind: (i.evidence || {}).kind || (String(i.id).startsWith("a") ? "assumption" : "point") });
    }));
    const idxCols = cols.slice(0, 28);
    const idxRows = ms.slice(0, 11).map(m => ({ id: m.label || m.id, r: mres(m, short), ok: !m.error && (m.estimate != null || !!m.distribution),
      used: new Set((m.inputs || []).map(i => i.id)) }));
    drawIdx = function () {
      const x = cIdx.x, w = cIdx.w, h = cIdx.h;
      if (!idxRows.length || !idxCols.length) { placeholder(cIdx, "no methods with inputs"); return; }
      x.clearRect(0, 0, w, h);
      x.font = `600 6.5px ${FONT}`; x.textBaseline = "middle";
      const lx = 26, rx = 40, cw = (w - lx - rx) / idxCols.length, ch = Math.min(14, h / idxRows.length), scan = Math.floor((T * 4) % idxCols.length);
      idxRows.forEach((m, j) => {
        const y = j * ch;
        x.fillStyle = "#6b6f78"; x.fillText(String(m.id).toUpperCase(), 0, y + ch / 2);
        idxCols.forEach((c, i) => {
          const used = m.used.has(c.id);
          let col = used ? (c.kind === "assumption" ? "#f0a6c6" : c.kind === "constant" ? "#98e0cf" : "#e6e8ec") : "#1c1e23";
          if (i === scan) col = used ? "#ffffff" : "#2a2d33";
          x.fillStyle = col; x.fillRect(lx + i * cw, y + 1, Math.max(1, cw - 1), ch - 2);
        });
        x.fillStyle = m.ok ? "#9a9ea7" : "#f0a6c6"; x.fillText(m.r, w - rx + 4, y + ch / 2);
      });
    };
    V.ready = true;
  }
  function checksDrawer(rows) {
    return function () {
      const x = cVal.x, w = cVal.w, h = cVal.h;
      x.clearRect(0, 0, w, h);
      const rh = h / rows.length, scan = (T * 0.35 % 1) * w;
      x.textBaseline = "middle";
      rows.forEach(([k, v, bad], i) => {
        const yc = rh * i + rh / 2;
        x.font = `800 7px ${FONT}`; x.fillStyle = "#9a9ea7"; x.fillText(k, 0, yc);
        x.strokeStyle = "#1f2227"; x.lineWidth = 1; x.beginPath(); x.moveTo(86, yc + 6); x.lineTo(w, yc + 6); x.stroke();
        x.font = `600 8px ${FONT}`; x.fillStyle = bad ? "#f0a6c6" : "#e6e8ec"; x.fillText(v, 92, yc);
      });
      x.strokeStyle = "rgba(240,166,198,.45)"; x.beginPath(); x.moveTo(scan, 0); x.lineTo(scan, h); x.stroke();
    };
  }

  // =========================================================
  // 顶部工具：已保存的运行、新问题
  // =========================================================
  async function savedRuns() {
    let runs = [];
    try { runs = (await api("/api/saved")).runs || []; } catch (e) { /* 没有服务时留空 */ }
    return runs.filter(r => r.estimate != null || r.most_likely != null)
      .sort((a, b) => String(b.started_at || "").localeCompare(String(a.started_at || "")));
  }
  function tools(runs, current) {
    const sel = $("runSel"), list = runs.slice(0, 80), cur = current && runs.find(r => r.qid === current.qid && r.tag === current.tag);
    if (cur && !list.includes(cur)) list.unshift(cur);   // 正在看的运行不在最近 80 个里也要列出来
    sel.innerHTML = `<option value="">saved runs…</option>` + list.map(r =>
      `<option value="${esc(r.qid)}/${esc(r.tag)}"${current && r.qid === current.qid && r.tag === current.tag ? " selected" : ""}>`
      + `${esc(String(r.question || r.qid).slice(0, 42))} · ${esc(r.tag)}</option>`).join("");
    sel.onchange = () => { if (sel.value) location.hash = "result/" + sel.value; };
    const b = document.createElement("button");
    b.className = "hx-btn hx-new"; b.type = "button"; b.textContent = "+ NEW QUESTION";
    b.onclick = () => { location.hash = "ask"; };
    sel.parentElement.prepend(b);
  }

  // =========================================================
  // 提问（模型 · key · 上限：和 verrier_console.js 同一套存储，填过的 key 两边通用）
  // =========================================================
  const CFG_STORE = "verrier-run-cfg", keyName = (p, r) => `verrier-key:${p}:${r}`;
  const stor = k => { try { return k === "local" ? localStorage : sessionStorage; } catch (e) { return null; } };
  const sget = (k, n) => { try { const s = stor(k); return s ? s.getItem(n) : null; } catch (e) { return null; } };
  const sset = (k, n, v) => { try { const s = stor(k); if (s) { if (v === null) s.removeItem(n); else s.setItem(n, v); } } catch (e) { /* 存不了就不存 */ } };
  const EXAMPLES = [
    "How many foreign visitors arrived in Japan in November 2026, as first reported in JNTO's preliminary estimate?",
    "How many live births were registered in South Korea in September 2026, as first reported by Statistics Korea?",
    "How many passengers did London Heathrow handle in October 2026?",
  ];
  const bi = n => n ? esc(n.en) : "";

  async function viewAsk(runs) {
    document.body.classList.add("mode-ask");
    setArr(CHECKS, [["VERRIER", "awaiting a question"], ["ROUTES", "drafted after you ask"], ["HUMAN GATE", "you approve before any search runs"]]);
    $("stBig").textContent = "STANDBY · AWAITING QUESTION";
    $("stSm").textContent = "plan → human gate → field agents → judge → code compute";
    [0, 1, 2, 3, 4].forEach(i => kpi(i, "—", 0));
    // 提问页把数据面板藏起来了（画布宽 0）：原作的 drawVal 遇到宽 0 会死循环，所以换成什么都不画
    drawAdv = drawDiff = drawVal = drawIdx = agentsTick = function () {};
    V.ready = true;

    const ask = document.createElement("div");
    ask.className = "ov hx hx-ask";
    ask.innerHTML = `<div class="eyb">MISSION CONTROL · ASK</div><h2>WHAT NUMBER DO YOU NEED?</h2>
      <textarea id="hxQ" placeholder="How many … in …?"></textarea>
      <div class="hx-chips">${EXAMPLES.map((q, i) => `<button type="button" data-ex="${i}" title="${esc(q)}">${esc(q.slice(0, 46))}…</button>`).join("")}</div>
      <div class="hx-row"><span class="eyb">AS OF</span><input type="date" id="hxAsof">
        <span class="fine">empty = today (live pages) · earlier = backtest (archived snapshots only)</span></div>
      <div class="hx-row"><button class="hx-btn primary" type="button" id="hxGo">LAUNCH →</button><span id="hxMsg" class="fine"></span></div>`;
    $("stageWrap").appendChild(ask);
    const q = $("hxQ");
    ask.querySelectorAll("[data-ex]").forEach(b => { b.onclick = () => { q.value = EXAMPLES[+b.dataset.ex]; q.dispatchEvent(new Event("input")); q.focus(); }; });
    q.addEventListener("input", () => {   // 光环卡片上的字：你正在打的问题
      const words = q.value.trim().split(/\s+/).filter(w => w.length > 2).slice(0, 40);
      if (words.length) { setArr(HEAD, words.map(w => w.toUpperCase().slice(0, 14))); setArr(CODE_T, words.map(w => w.slice(0, 12))); slots.forEach(s => s.c = null); }
      if (rnd() < 0.5) flash();
    });

    // 底部：模型 · key · 上限、估计花费、这次服务启动后的任务、已保存的运行
    const grid = document.querySelector(".panels"), credit = grid.querySelector(".credit");
    const panel = (cls, html) => { const p = document.createElement("div"); p.className = "p askp " + cls; p.innerHTML = html; grid.insertBefore(p, credit); return p; };
    panel("w2", `<h3>MODEL · KEY · LIMITS</h3><dl>
      <dt>Provider</dt><dd><select id="hxProv"></select> <span class="fine" id="hxProvNote"></span></dd>
      <dt class="hx-reg">Region</dt><dd class="hx-reg"><select id="hxReg"></select></dd>
      <dt>Model</dt><dd><select id="hxModel"></select></dd>
      <dt>API key</dt><dd><input type="password" id="hxKey" autocomplete="off" spellcheck="false" placeholder="sk-…" style="width:58%">
        <button class="hx-btn" type="button" id="hxCheck">CHECK</button>
        <label class="fine"><input type="checkbox" id="hxRemember"> remember on this device</label> <span id="hxKeyMsg" class="fine"></span></dd>
      <dt>Thinking</dt><dd><select id="hxThink"></select></dd>
      <dt>Spending cap</dt><dd>US$ <input type="number" id="hxCap" min="0.1" step="0.5" value="2.00" style="width:70px"> <span class="fine">per run</span></dd>
      </dl><p class="fine">Bring your own key: web runs only use the key entered here, never a key file on the server. It stays in this browser
      (session only unless you tick “remember”) and in the server's memory for this one run.</p>`);
    panel("", `<h3>ESTIMATED COST</h3><div id="hxEst" class="fine">loading models…</div>`);
    panel("", `<h3>MISSIONS THIS SESSION</h3><div id="hxRuns" class="fine">…</div>`);
    panel("w2", `<h3>SAVED RUNS</h3><div>${runs.slice(0, 10).map(r => `<a class="li" href="#result/${encodeURIComponent(r.qid)}/${encodeURIComponent(r.tag)}">`
      + `<i>${esc(r.tag)}</i> ${esc(String(r.question || r.qid).slice(0, 70))} · <b>${r.mode === "discrete" ? esc(r.most_likely ?? "—") : fmtN(r.estimate)}</b></a>`).join("") || "none"}</div>`);
    panel("w2", `<h3>HOW A MISSION RUNS</h3><p class="fine">The planner pins the exact target and drafts evidence routes, then stops for your
      approval. Field agents search, fetch and extract quoted numbers; code checks every quote, date and unit. A judge proposes methods,
      code computes them and combines independent blocks. Every number on the result screen traces to a quote.</p>`);

    const cfg = { provider: null, region: null, model: null, thinking: null, cap: 2 };
    try { Object.assign(cfg, JSON.parse(sget("local", CFG_STORE) || "{}")); } catch (e) { /* 用默认 */ }
    let cat = null, capT = null;
    const provOf = () => cat.providers.find(p => p.id === cfg.provider), modelOf = () => provOf().models.find(m => m.id === cfg.model);
    const regionOf = m => m.by_region[cfg.region] || Object.values(m.by_region)[0];
    function normalize() {
      if (!cat.providers.some(p => p.id === cfg.provider)) cfg.provider = cat.default_provider;
      const p = provOf();
      if (!p.regions.some(r => r.id === cfg.region)) cfg.region = p.default_region;
      if (!p.models.some(m => m.id === cfg.model)) cfg.model = p.default_model;
      const m = modelOf();
      if (!m.thinking.levels.includes(cfg.thinking)) cfg.thinking = m.thinking.default;
      if (!(Number(cfg.cap) > 0)) cfg.cap = cat.default_usd_cap;
    }
    function render() {
      normalize();
      sset("local", CFG_STORE, JSON.stringify(cfg));
      const p = provOf(), m = modelOf();
      $("hxProv").innerHTML = cat.providers.map(x => `<option value="${esc(x.id)}"${x.id === cfg.provider ? " selected" : ""}>${esc(x.label)}</option>`).join("");
      $("hxReg").innerHTML = p.regions.map(r => `<option value="${esc(r.id)}"${r.id === cfg.region ? " selected" : ""}>${esc(r.label)}</option>`).join("");
      document.querySelectorAll(".hx-reg").forEach(el => { el.hidden = !p.region_choice; });
      $("hxModel").innerHTML = p.models.map(x => {
        const lv = x.thinking.levels.includes(cfg.thinking) ? cfg.thinking : x.thinking.default, e = regionOf(x).by_thinking[lv];
        return `<option value="${esc(x.id)}"${x.id === cfg.model ? " selected" : ""}>${esc(x.label)} · ≈ ${money(e.est_usd)}/run${e.stops_early ? " ⚠" : ""}</option>`;
      }).join("");
      $("hxThink").innerHTML = cat.thinking_levels.map(lv => { const ok = m.thinking.levels.includes(lv);
        return `<option value="${esc(lv)}"${lv === cfg.thinking ? " selected" : ""}${ok ? "" : " disabled"}>${esc(lv)}${ok ? "" : " — n/a"}</option>`; }).join("");
      if (document.activeElement !== $("hxCap")) $("hxCap").value = Number(cfg.cap).toFixed(2);
      const e = regionOf(m).by_thinking[cfg.thinking];
      $("hxProvNote").innerHTML = (p.notes || []).map(bi).join(" · ");
      $("hxEst").innerHTML = `<div class="big">≈ ${money(e.est_usd)}</div><div>cap ${money(cfg.cap)} · ${esc(e.directions)} first-round routes</div>`
        + (e.over_cap ? `<div class="bad">the estimate is above the cap: the run stops at ${money(cfg.cap)}</div>` : "")
        + (e.stops_early ? `<div class="bad">this cap cannot cover a minimal run (${money(e.run_floor_usd)}): the server will refuse it</div>` : "")
        + `<div>${bi(cat.estimate_note)}</div>`;
    }
    function keyLoad() {
      const n = keyName(cfg.provider, cfg.region), loc = sget("local", n);
      $("hxKey").value = loc ?? sget("session", n) ?? "";
      $("hxRemember").checked = loc !== null;
      $("hxKeyMsg").textContent = "";
    }
    function keyStore() {
      const n = keyName(cfg.provider, cfg.region), v = $("hxKey").value.trim(), keep = $("hxRemember").checked;
      sset("local", n, v && keep ? v : null);
      sset("session", n, v && !keep ? v : null);
    }
    async function loadCat() { cat = await api("/api/providers?usd_cap=" + encodeURIComponent(Number(cfg.cap) > 0 ? Number(cfg.cap) : 2)); render(); }
    try { await loadCat(); keyLoad(); } catch (e) { $("hxEst").innerHTML = `<span class="bad">${esc(e.message)}</span>`; }
    const changed = (k, keyToo) => ev => { cfg[k] = ev.target.value; render(); if (keyToo) keyLoad(); };
    $("hxProv").onchange = changed("provider", true);
    $("hxReg").onchange = changed("region", true);
    $("hxModel").onchange = changed("model");
    $("hxThink").onchange = changed("thinking");
    $("hxCap").oninput = () => { const v = Number($("hxCap").value); if (!(v > 0)) return; cfg.cap = v; clearTimeout(capT); capT = setTimeout(() => loadCat().catch(() => {}), 350); };
    $("hxKey").oninput = keyStore;
    $("hxRemember").onchange = keyStore;
    $("hxCheck").onclick = async () => {
      const key = $("hxKey").value;
      if (!key.trim()) { $("hxKeyMsg").innerHTML = `<span class="bad">enter a key first</span>`; return; }
      $("hxCheck").disabled = true; $("hxKeyMsg").textContent = "…";
      try {
        const r = await post("/api/key/check", { provider: cfg.provider, region: cfg.region, model: cfg.model, api_key: key });
        $("hxKeyMsg").innerHTML = r.ok ? `<span class="ok">✓ ${esc(r.message)}</span>` : `<span class="bad">✕ ${esc(r.message || r.error)}</span>`;
      } catch (err) { $("hxKeyMsg").innerHTML = `<span class="bad">✕ ${esc(err.message)}</span>`; }
      $("hxCheck").disabled = false;
    };
    $("hxGo").onclick = async () => {
      const key = $("hxKey").value || "";
      if (!cat) { $("hxMsg").innerHTML = `<span class="bad">the model list has not loaded yet</span>`; return; }
      if (!key.trim()) { $("hxMsg").innerHTML = `<span class="bad">enter your own API key first (web runs never use a key file on the server)</span>`; $("hxKey").focus(); return; }
      const capIn = $("hxCap").value.trim(), cap = capIn !== "" ? Number(capIn) : Number(cfg.cap);
      $("hxGo").disabled = true; $("hxMsg").textContent = "ignition…";
      for (let i = 0; i < 12; i++) setTimeout(flash, i * 60);
      try {
        const r = await post("/api/runs", { question: q.value, as_of: $("hxAsof").value || null, provider: cfg.provider, model: cfg.model,
          region: cfg.region, thinking: cfg.thinking, usd_cap: isFinite(cap) ? cap : capIn, api_key: key });
        location.hash = "run/" + encodeURIComponent(r.id);
      } catch (e) { $("hxMsg").innerHTML = `<span class="bad">${esc(e.message)}</span>`; $("hxGo").disabled = false; }
    };
    try {
      const rs = await api("/api/runs");
      $("hxRuns").innerHTML = rs.runs.length ? rs.runs.map(r => `<a class="li" href="#run/${encodeURIComponent(r.id)}"><i>${esc(r.status)}</i> ${esc(String(r.question).slice(0, 60))}</a>`).join("")
        + `<p class="fine">at most ${esc(rs.max_active)} unfinished runs at a time</p>` : "none yet";
    } catch (e) { $("hxRuns").textContent = "—"; }
  }

  // =========================================================
  // 运行（轮询 /api/runs/{id}）：8 站流程、人工确认、子 agent、裁判、计算
  // =========================================================
  const STATIONS = [["plan", "PLAN · LOCK TARGET", ["plan"]], ["approve", "HUMAN GATE", ["approve"]], ["field", "FIELD AGENTS", ["subagents1", "subagents2"]],
    ["judge", "JUDGE", ["judge1", "judge2"]], ["units", "UNIT REVIEW", []], ["audit", "INPUT AUDIT · REPAIR", []], ["compute", "COMPUTE (CODE)", ["compute"]],
    ["final", "PUBLISHED CHECK · FINAL", ["final"]]];
  function stations(r) {   // 同 verrier_console.js：由 stages（服务端阶段）和 calls（按角色计的调用次数）推出来
    const by = new Map((r.stages || []).map(s => [s.key, s])), calls = Object.entries(r.calls || {});
    const count = f => calls.reduce((n, [k, v]) => n + (f(k) ? v : 0), 0);
    const nChk = count(k => k.startsWith("unit_check")), nArb = count(k => k.startsWith("unit_arbiter"));
    const nAud = count(k => k === "audit"), nRep = count(k => k.endsWith(":repair"));
    const computed = (by.get("compute") || {}).status === "done";
    const plainSt = keys => { const ss = keys.map(k => by.get(k)).filter(Boolean), sts = ss.map(s => s.status);
      return { status: !sts.length ? "pending" : sts.every(s => s === "done") ? "done" : sts.includes("waiting") ? "waiting"
        : sts.includes("running") ? "running" : "pending", detail: ss.map(s => s.detail || "").filter(Boolean).join(" · ") }; };
    const judging = plainSt(["judge1", "judge2"]).status === "running";
    const st = STATIONS.map(([key, label, keys]) => {
      if (key === "units") return { key, label, status: computed ? "done" : judging && nChk + nArb ? "running" : "pending", detail: nChk + nArb ? `checks ${nChk} · arbiter ${nArb}` : "" };
      if (key === "audit") return { key, label, status: computed ? "done" : judging && nAud + nRep ? "running" : "pending", detail: nAud + nRep ? `audits ${nAud}${nRep ? ` · repairs ${nRep}` : ""}` : "" };
      return { key, label, ...plainSt(keys) };
    });
    const last = st.map(s => s.status).lastIndexOf("running");
    st.forEach((s, i) => { if (i < last && s.status !== "done") s.status = "done"; });
    return { st, nChk, nArb, nAud, nRep };
  }
  const DST = { queued: "queued", searching: "searching", fetching: "fetching", extracting: "extracting", done: "done", stopped: "stopped" };
  const dots = n => { const k = Math.max(0, Math.min(5, Math.round(+n || 0))); return "●".repeat(k) + "○".repeat(5 - k); };
  const nPts = d => d.n_kept != null ? d.n_kept : (d.n_points ?? d.n_verified ?? 0);

  async function viewRun(id) {
    document.body.classList.remove("mode-ask");
    V.ready = true;
    const est = $("est");
    est.querySelector(".num").classList.add("stage");
    const ctl = document.createElement("div");
    est.appendChild(ctl);
    let prev = null, gateShown = false, delivered = false, lastStations = "";
    drawAdv = function () { placeholder(cAdv, "estimate appears after code compute"); };
    drawDiff = function () { placeholder(cDiff, "blocks appear after code compute"); };
    drawIdx = function () { placeholder(cIdx, "methods and inputs appear after the judge"); };
    drawVal = function () { placeholder(cVal, "code checks appear as the run goes"); };
    agentsTick = function () {};

    async function tick() {
      let r;
      try { r = await api("/api/runs/" + encodeURIComponent(id)); }
      catch (e) { $("estQ").textContent = `run ${id}: ${e.message}`; $("estNum").textContent = "NOT FOUND"; return; }
      const { st, nChk, nArb, nAud, nRep } = stations(r);
      const cur = st.findIndex(s => s.status !== "done"), curS = st[cur];
      const active = ["planning", "awaiting_approval", "running"].includes(r.status);
      const dirs = r.directions || [];

      // 舞台左上：问题、阶段（算出估计以后是大号数字）、用时和花费
      $("estQ").textContent = r.question;
      const c = r.compute;
      if (c && c.mode !== "discrete" && c.central != null) {
        $("estNum").classList.remove("stage");
        $("estNum").innerHTML = fmtN(c.central) + `<small>${esc(String((r.target || {}).unit_canonical || (r.target || {}).unit || ""))}</small>`;
        $("estIv").textContent = c.p10 != null ? `80% interval ${fmtN(c.p10)} – ${fmtN(c.p90)} · computed by code, final check running` : "computed by code";
      } else if (c && c.mode === "discrete") {
        $("estNum").classList.remove("stage");
        $("estNum").innerHTML = esc(c.most_likely ?? "—") + `<small>most likely outcome</small>`;
        $("estIv").textContent = c.most_likely_prob != null ? `probability ${(100 * c.most_likely_prob).toFixed(1)}%` : "";
      } else {
        $("estNum").textContent = r.status === "done" ? "DELIVERED" : r.status === "failed" ? "FAILED" : r.status === "cancelled" ? "ABORTED"
          : curS ? `${String(cur + 1).padStart(2, "0")} / 08 · ${curS.label}` : r.status.toUpperCase();
        $("estIv").textContent = r.error ? r.error : r.stopped ? `stopped early: ${r.stopped}` : curS && curS.detail ? curS.detail : "";
      }
      const spec = r.run_spec || {};
      $("estMeta").textContent = `${r.status} · ${Math.round(r.elapsed_s || 0)} s · ${r.usd == null ? "—" : "$" + r.usd.toFixed(3)} / ${r.usd_cap ? money(r.usd_cap) : "—"}`
        + ` · as of ${r.as_of}${spec.model ? " · " + spec.model : ""}`;
      ctl.innerHTML = active ? `<button class="hx-btn" type="button" id="hxAbort">ABORT ✕</button>` : "";
      if ($("hxAbort")) $("hxAbort").onclick = async () => {
        if (!confirm("Abort this run? Money already spent is not refunded.")) return;
        try { await post(`/api/runs/${encodeURIComponent(id)}/cancel`); } catch (e) { alert(e.message); }
      };

      // 页头和状态行
      const pg = dirs.reduce((a, d) => ({ s: a.s + ((d.pages || {}).snapshot || 0) + ((d.pages || {}).live_dated || 0), x: a.x + ((d.pages || {}).dropped || 0) }), { s: 0, x: 0 });
      const pts = dirs.reduce((a, d) => a + nPts(d), 0);
      kpi(0, dirs.length || (r.directions_proposed || []).length || "—", 1);
      kpi(1, pg.s, pg.s / Math.max(1, pg.s + pg.x));
      kpi(2, pts, 1);
      kpi(3, r.compute ? "✓" : "—", r.compute ? 1 : 0);
      kpi(4, "—", 0);
      $("stBig").textContent = curS ? `STAGE ${cur + 1} / 8 · ${curS.label}` : r.status === "done" ? "8 / 8 · DELIVERED" : r.status.toUpperCase();
      $("stSm").textContent = `${Math.round(r.elapsed_s || 0)} s · ${r.usd == null ? "—" : "$" + r.usd.toFixed(3)} spent · ${pg.s} pages read · ${pg.x} dropped`;

      // 方法工作区：8 站流程（真实状态）；浮标：当前这一站
      const stLines = st.map((s, i) => [String(i + 1).padStart(2, "0"), s.label.toLowerCase(), ` · ${s.status}${s.detail ? " · " + plain(s.detail).slice(0, 60) : ""}`]);
      const sig = stLines.map(l => l.join("")).join("|");
      if (sig !== lastStations) { lastStations = sig; setArr(CODE, stLines); cLine = 0; cChar = 0; cNum = 1; typed = []; }
      const ck = [`STAGE ${Math.max(1, cur + 1)} / 8`, curS ? `${curS.label.toLowerCase()} · ${curS.status}` : r.status];
      if (CHECKS[0][1] !== ck[1]) { $("chkK").textContent = ck[0]; $("chkV").textContent = ck[1]; }   // 换站时马上换字，不等原作的轮换
      setArr(CHECKS, [ck]);

      // 光环卡片：这次运行的方向
      const dsrc = dirs.length ? dirs : (r.directions_proposed || []);
      if (dsrc.length && HEAD[0] === "VERRIER") {
        setArr(HEAD, dsrc.map(d => `${String(d.id).toUpperCase()} ${String(d.category || "").toUpperCase()}`));
        setArr(KEYS, [...new Set(dsrc.map(d => CAT[d.category] || d.category))]);
        setArr(CODE_T, dsrc.flatMap(d => String(d.hypothesis || "").split(/\s+/).filter(w => w.length > 3).slice(0, 4)).slice(0, 60));
        slots.forEach(s => s.c = null);
      }

      // 流水：和上一次轮询比，真的变了才写
      if (!prev) V.push("seek", `mission ${r.qid} · ${r.status}`);
      else {
        const ps = new Map((prev.directions || []).map(d => [d.id, d]));
        dirs.forEach(d => {
          const p = ps.get(d.id);
          if (!p) { V.push("seek", `${d.id} ${d.category} · ${d.perspective || d.hypothesis || ""}`.slice(0, 160)); return; }
          if (p.status !== d.status) V.push(d.status === "done" ? "keep" : d.status === "stopped" ? "drop" : "seek",
            `${d.id} ${DST[d.status] || d.status}${d.status === "done" ? ` · ${nPts(d)} points kept` : ""}${d.stopped ? " · " + d.stopped : ""}`);
          const dp = ((d.pages || {}).dropped || 0) - ((p.pages || {}).dropped || 0), rp = (((d.pages || {}).snapshot || 0) + ((d.pages || {}).live_dated || 0))
            - (((p.pages || {}).snapshot || 0) + ((p.pages || {}).live_dated || 0));
          if (rp > 0) V.push("seek", `${d.id} read ${rp} page${rp > 1 ? "s" : ""}`);
          if (dp > 0) V.push("drop", `${d.id} dropped ${dp} page${dp > 1 ? "s" : ""}`);
          const dk = nPts(d) - nPts(p);
          if (dk > 0) V.push("keep", `${d.id} +${dk} code-checked point${dk > 1 ? "s" : ""}`);
        });
        Object.entries(r.judge || {}).forEach(([k, j]) => { if (!(prev.judge || {})[k]) V.push("calc", `judge round ${k} · ${j.text || ""}`.slice(0, 200)); });
        if (r.compute && !prev.compute) V.push("calc", r.compute.mode === "discrete" ? `compute · most likely ${r.compute.most_likely}` : `compute · ${short(r.compute.central)} [${short(r.compute.p10)}, ${short(r.compute.p90)}]`);
        if (r.status !== prev.status) V.push(r.status === "failed" || r.status === "cancelled" ? "drop" : "seek", `mission ${r.status}${r.error ? " · " + r.error : ""}`.slice(0, 200));
      }

      // 方向表和子 agent：真实状态和页数
      const top = dirs.slice(0, 6);
      setArr(ROUTES, top.map(d => `${d.id} ${CAT[d.category] || d.category}`));
      setArr(COLSR, ["search", "read", "keep"]);
      setArr(rState, top.map(d => d.status === "queued" ? 0 : d.status === "searching" ? 0 : ["fetching", "extracting"].includes(d.status) ? 1 : nPts(d) ? 3 : 2));
      V.routePink = top.map(d => d.status === "done" || d.status === "stopped");
      renderRoutes();
      agEl.innerHTML = dirs.slice(0, 12).map(d => {
        const n = Math.max(1, d.n_urls || 4), done = d.status === "done" ? n : Math.min(n, d.pages_done || 0), k = Math.round(6 * done / n);
        const cells = Array.from({ length: 6 }, (_, i) => `<i style="background:${i < k ? (nPts(d) ? "#98e0cf" : "#5a5e66") : "#1d1f24"}"></i>`).join("");
        const label = `${DST[d.status] || d.status}${["fetching", "extracting"].includes(d.status) ? ` ${d.pages_done ?? 0}/${d.n_urls ?? "?"}` : ""} · ${nPts(d)} pts`;
        return `<div class="ag"><span class="id">${esc(d.id)}</span><span class="rl">${esc(CAT[d.category] || d.category)}</span><span class="cells">${cells}</span>`
          + `<span class="st${["searching", "fetching", "extracting"].includes(d.status) ? " w" : ""}">${esc(label)}</span></div>`;
      }).join("");
      drawVal = checksDrawer([["UNIT CHECK", `checks ${nChk} · arbiter ${nArb}`, false], ["INPUT AUDIT", `audits ${nAud} · repairs ${nRep}`, false],
        ["PAGES DROPPED", `${pg.x} of ${pg.s + pg.x}`, false], ["SPENT", `${r.usd == null ? "—" : "$" + r.usd.toFixed(3)} of ${money(r.usd_cap)}`, r.usd_cap && r.usd > r.usd_cap * 0.9]]);
      if (c && c.mode !== "discrete" && c.central != null) drawAdv = drawCloud(c, "");

      // 人工确认：只画一次（勾选时轮询不重画）
      if (r.status === "awaiting_approval" && !gateShown) { gateShown = true; showGate(r); }
      if (r.status !== "awaiting_approval" && $("hxGate")) $("hxGate").remove();

      // 结果：跑完就接上结果画面（不刷新页面）
      if (r.result && !delivered) {
        delivered = true;
        try {
          const d = await api(`/api/result?qid=${encodeURIComponent(r.result.qid)}&tag=${encodeURIComponent(r.result.tag)}`);
          V.push("calc", "delivered · result loaded");
          vBind(d, { qid: r.result.qid, tag: r.result.tag, most_likely: c && c.most_likely, most_likely_prob: c && c.most_likely_prob,
            status: r.status, why: r.error || r.stopped });
          ctl.innerHTML = "";   // 新问题用右上角的按钮
        } catch (e) { V.push("drop", `result not loaded: ${e.message}`); }
      }
      prev = r;
      if (active) setTimeout(tick, r.status === "awaiting_approval" ? 3000 : 2000);
    }
    tick();
  }

  function showGate(r) {
    const g = document.createElement("div");
    g.className = "ov hx hx-gate";
    g.id = "hxGate";
    const t = r.target || {};
    const row = (k, v) => v ? `<b>${esc(k)}</b><span>${esc(v)}</span>` : "";
    g.innerHTML = `<div class="eyb">HUMAN GATE · APPROVE THE ROUTES</div><h3>Verrier stopped here. Unchecked routes will not run.</h3>
      <div class="hx-tgt">${row("target", t.what)}${row("unit", t.unit)}${row("unit (code)", t.unit_canonical)}
        ${row("period", [t.period_start, t.period_end].filter(Boolean).join(" – "))}${row("publisher", t.publisher)}${row("caveats", String(t.caveats || "").slice(0, 300))}</div>
      ${(r.plan_notes || []).length ? `<p class="fine">${r.plan_notes.map(esc).join("<br>")}</p>` : ""}
      ${(r.existing || []).length ? `<p class="fine">Existing figures for this exact target: use one to stop here without running any route,
        or approve the routes below (approving excludes these figures from the evidence).</p>` + r.existing.map(x => `<div class="hx-x">
        <span class="eyb">${esc(x.id)} · ${esc(x.type)}</span><br><b>${fmtN(x.value)}</b> ${esc(x.unit)} · ${esc([x.period_start, x.period_end].filter(Boolean).join(" – "))}
        <div class="fine">${esc(x.domain)} · “${esc(x.quote)}”</div><button class="hx-btn" type="button" data-use="${esc(x.id)}">USE THIS FIGURE →</button></div>`).join("") : ""}
      ${(r.directions_proposed || []).map(d => `<label class="hx-dir"><span class="hd"><input type="checkbox" class="hx-keep" value="${esc(d.id)}" checked>
        ${esc(d.id)} <span class="cat">${esc(d.category)}</span> <span class="dots" title="expected information">${dots(d.expected_information)}</span></span>
        ${d.perspective ? `<div>${esc(d.perspective)}</div>` : ""}<div><b>hypothesis:</b> ${esc(d.hypothesis)}</div>
        <div class="fine"><b>data to find:</b> ${esc(d.data_to_find)}</div></label>`).join("")}
      <div class="hx-row"><button class="hx-btn primary" type="button" id="hxApprove">APPROVE SELECTED →</button>
        <button class="hx-btn" type="button" id="hxAll">ALL</button><button class="hx-btn" type="button" id="hxNone">NONE</button>
        <span id="hxGateMsg" class="fine"></span></div>`;
    $("stageWrap").appendChild(g);
    const boxes = () => [...g.querySelectorAll("input.hx-keep")];
    const sync = b => b.closest(".hx-dir").classList.toggle("off", !b.checked);
    boxes().forEach(b => { b.onchange = () => sync(b); });
    $("hxAll").onclick = () => boxes().forEach(b => { b.checked = true; sync(b); });
    $("hxNone").onclick = () => boxes().forEach(b => { b.checked = false; sync(b); });
    g.querySelectorAll("button[data-use]").forEach(b => { b.onclick = async () => {
      b.disabled = true;
      try { await post(`/api/runs/${encodeURIComponent(r.id)}/approve`, { use_existing: b.dataset.use }); g.remove(); V.push("keep", `existing figure ${b.dataset.use} chosen`); }
      catch (e) { $("hxGateMsg").innerHTML = `<span class="bad">${esc(e.message)}</span>`; b.disabled = false; }
    }; });
    $("hxApprove").onclick = async () => {
      const ids = boxes().filter(b => b.checked).map(b => b.value);
      if (!ids.length) { $("hxGateMsg").innerHTML = `<span class="bad">keep at least one route</span>`; return; }
      $("hxApprove").disabled = true;
      try {
        await post(`/api/runs/${encodeURIComponent(r.id)}/approve`, ids.length === (r.directions_proposed || []).length ? {} : { keep_direction_ids: ids });
        g.remove();
        V.push("keep", `routes approved · ${ids.join(", ")}`);
      } catch (e) { $("hxGateMsg").innerHTML = `<span class="bad">${esc(e.message)}</span>`; $("hxApprove").disabled = false; }
    };
  }

  // =========================================================
  // 路由
  // =========================================================
  async function viewResult(qid, tag, runs) {
    document.body.classList.remove("mode-ask");
    const pick = runs.find(r => r.qid === qid && r.tag === tag) || { qid, tag };
    try { vBind(await api(`/api/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`), pick); }
    catch (e) { $("estQ").textContent = `could not load ${qid}/${tag}: ${e.message}`; }
  }
  async function route() {
    const h = decodeURIComponent(location.hash.replace(/^#/, "")), parts = h.split("/");
    const runs = await savedRuns();
    let mode = parts[0] || "ask";
    if (!["ask", "run", "result"].includes(mode) && parts.length === 2) { parts.unshift("result"); mode = "result"; }   // 旧链接 #<题 id>/<tag>
    tools(runs, mode === "result" ? { qid: parts[1], tag: parts[2] || "" } : null);
    if (mode === "run" && parts[1]) return viewRun(parts[1]);
    if (mode === "result" && parts[1]) return viewResult(parts[1], parts[2] || "", runs);
    return viewAsk(runs);
  }
  window.addEventListener("hashchange", () => location.reload());
  route();
})();
