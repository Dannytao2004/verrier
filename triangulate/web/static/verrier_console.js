// Verrier 控制台：把 agent 的主运行界面（提问 → 人工确认方向 → 进度 → 结果）放进 Verrier 页面（verrier_console.html）。
// 只调用现有 API（/api/runs、/api/result、/api/saved、/api/file），后端逻辑不变；完整的证据表、回测在经典界面（/#/...）。
// 路由：#console（提问）、#console/run/<运行 id>（进度）、#console/result/<题 id>/<tag>（保存的结果）。别的 hash 是页面锚点，控制台关掉。
// 右下角 HUD 由页面里的场景脚本画；这里用 VERRIER.mission({...}) 把它换成任务遥测（用时、阶段、花费），关掉控制台时交还。
"use strict";
(() => {
  const $ = id => document.getElementById(id);
  const cx = $("cx"), body = $("cxBody"), code = $("cxCode");
  let timer = null, token = 0, lastScroll = 0;
  const played = new Set();

  // ---------- 工具（和经典界面 app.js 同一套格式） ----------
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  function fmt(v) {
    if (v === null || v === undefined || typeof v !== "number" || !isFinite(v)) return "—";
    if (Math.abs(v) >= 100) return Math.round(v).toLocaleString("en-US");
    return Number(v.toPrecision(4)).toLocaleString("en-US", {maximumFractionDigits: 6});
  }
  const pct = x => x === null || x === undefined || !isFinite(x) ? "—" : (x > 0 ? "+" : "") + (x * 100).toFixed(1) + "%";
  const share = x => x === null || x === undefined ? "—" : Math.round(x * 100) + "%";
  const prob = x => x === null || x === undefined || !isFinite(x) ? "—" : (x * 100).toFixed(1) + "%";
  const usd = x => x === null || x === undefined ? "—" : "$" + Number(x).toFixed(3);
  const T = (en, zh) => `<span class="en">${en}</span><span class="zh">${zh}</span>`;   // 只传常量或已转义的文字
  const zh = () => document.documentElement.dataset.lang === "zh";
  async function api(path, opts) {
    const r = await fetch(path, opts);
    let b = null;
    try { b = await r.json(); } catch (e) { /* 非 JSON */ }
    if (!r.ok) throw new Error((b && b.detail) || `HTTP ${r.status}`);
    return b;
  }
  const post = (path, data) => api(path, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data || {})});
  const resultHref = (qid, tag) => `/#/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag || "")}`;
  const fileHref = (qid, tag, name) => `/api/file?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag || "")}&name=${name}`;
  const hud = m => window.VERRIER && window.VERRIER.mission && window.VERRIER.mission(m);

  const ST = {planning: ["Planning", "规划中"], awaiting_approval: ["Awaiting approval", "等待确认"], running: ["In flight", "运行中"],
    done: ["Delivered", "已交付"], failed: ["Failed", "失败"], cancelled: ["Cancelled", "已取消"]};
  const badge = st => `<span class="stencil s-${esc(st)}">${T(...(ST[st] || [esc(st), esc(st)]))}</span>`;
  const HUDST = {planning: "PLANNING ROUTES", awaiting_approval: "AWAITING APPROVAL", running: "IN FLIGHT", done: "TARGET ACQUIRED",
    failed: "MISSION FAILED", cancelled: "MISSION ABORTED"};
  const DST = {queued: ["Queued", "排队"], searching: ["Searching", "搜索中"], fetching: ["Fetching", "取页中"], extracting: ["Extracting", "抽取中"],
    done: ["Done", "完成"], stopped: ["Stopped", "中止"]};
  const STAGE = {plan: ["Plan routes", "规划方向"], approve: ["Human gate", "人工确认"], subagents1: ["Gather evidence", "子 agent 取证"],
    subagents2: ["Base-rate routes", "追加的 base-rate 方向"], judge1: ["Judge · round 1", "裁判第 1 轮"], judge2: ["Judge · round 2", "裁判第 2 轮"],
    compute: ["Compute (code)", "代码计算"], final: ["Final answer", "终稿"]};
  const SSTAT = {done: ["done", "完成"], running: ["running", "进行中"], waiting: ["waiting for you", "等你确认"], pending: ["pending", "未开始"]};
  const ACTIVE = ["planning", "awaiting_approval", "running"];
  const EXAMPLES = [
    "How many foreign visitors arrived in Japan in November 2026, as first reported in JNTO's preliminary estimate?",
    "How many live births were registered in South Korea in September 2026, as first reported by Statistics Korea?",
    "How many passengers did London Heathrow handle in October 2026?",
  ];

  // ---------- 打开 / 关闭 / 路由 ----------
  const isConsole = h => h === "#console" || h.startsWith("#console/");
  function stop() { if (timer) { clearTimeout(timer); timer = null; } }
  function open() {
    if (!cx.hidden) return;
    lastScroll = scrollY;
    cx.hidden = false;
    document.body.classList.add("cx-open");
  }
  function close() {
    stop();
    token++;
    if (cx.hidden) return;
    cx.hidden = true;
    document.body.classList.remove("cx-open");
    hud(null);
  }
  function leave() {   // 关掉控制台：回到打开前的位置，不触发锚点跳转
    history.pushState(null, "", location.pathname + location.search);
    close();
    scrollTo(0, lastScroll);
  }
  function route() {
    const h = location.hash || "";
    if (!isConsole(h)) {
      if (!cx.hidden) {
        close();
        const el = h.length > 1 && document.getElementById(h.slice(1));
        if (el) el.scrollIntoView();
      }
      return;
    }
    open();
    stop();
    const tok = ++token, parts = h.slice(1).split("/").map(decodeURIComponent);
    const p = parts[1] === "run" && parts[2] ? viewRun(parts[2], tok)
      : parts[1] === "result" && parts[2] ? viewResult(parts[2], parts[3] || "", tok) : viewHome(tok);
    p.catch(fail(tok));
  }
  const fail = tok => e => { if (tok === token) body.insertAdjacentHTML("afterbegin", `<div class="cx-err">${esc(e.message || e)}</div>`); };
  function schedule(fn, ms, tok) {
    stop();
    timer = setTimeout(() => { if (tok === token) fn().catch(fail(tok)); }, ms);
  }

  // ---------- 提问 ----------
  async function viewHome(tok) {
    code.textContent = "STANDBY";
    hud({view: "MISSION · STANDBY", status: "AWAITING QUESTION", phase: -1, progress: 0, elapsed: 0, cam: "NO ACTIVE MISSION"});
    body.innerHTML = `<div class="cx-grid">
      <div class="cx-ask">
        <div class="eyebrow lbl"><i></i>${T("06 · Mission control", "06 · 控制台")}</div>
        <h2 class="hl">${T("What number<br>do you need?", "你要哪个<br>数字？")}</h2>
        <p class="sub">${T("Verrier pins the target and drafts the routes, then stops for your approval before a single search runs.",
          "Verrier 先钉死目标、列出取证方向，然后停下来等你批准；批准之后才开始搜索。")}</p>
        <div class="cx-row"><label class="lbl" for="cxQ">${T("Question", "问题")}</label></div>
        <textarea id="cxQ" placeholder="How many ... in ...?"></textarea>
        <div class="cx-chips">${EXAMPLES.map((q, i) => `<button type="button" data-ex="${i}" title="${esc(q)}">${esc(q.slice(0, 48))}…</button>`).join("")}</div>
        <div class="cx-row"><label class="lbl" for="cxAsof">AS OF</label><input type="date" id="cxAsof">
          <span class="fine">${T("Empty = today (live pages). An earlier date = backtest: only archived snapshots up to that day.",
            "留空 = 今天（真实使用，读实时网页）；更早的日期 = 回测，只读不晚于那天的存档快照。")}</span></div>
        <div class="cx-row"><button class="btn primary" type="button" id="cxGo">${T("Launch mission", "发射任务")}<span>→</span></button>
          <span id="cxMsg" class="fine"></span></div>
        <p class="fine">${T("Needs the API key file (TRIANGULATE_KEY_FILE) and network. Spending cap per run: US$1.00, including the assumed search fee.",
          "需要 key 文件（TRIANGULATE_KEY_FILE）和网络。每次运行的花费上限 $1.00（含按假设单价记的搜索费）。")}</p>
      </div>
      <div>
        <h3 class="cx-h">${T("Missions this session", "这次服务启动后的任务")}</h3><div id="cxRuns" class="fine">…</div>
        <h3 class="cx-h">${T("Saved runs", "已保存的运行")}</h3><div id="cxSaved" class="fine">…</div>
        <p class="fine"><a href="/#/saved" target="_blank" rel="noopener">${T("All saved runs and backtests in the classic view ↗", "在经典界面看全部运行和回测 ↗")}</a></p>
      </div></div>`;
    body.querySelectorAll("[data-ex]").forEach(b => { b.onclick = () => { $("cxQ").value = EXAMPLES[+b.dataset.ex]; $("cxQ").focus(); }; });
    $("cxGo").onclick = async () => {
      const btn = $("cxGo");
      btn.disabled = true;
      try {
        const r = await post("/api/runs", {question: $("cxQ").value, as_of: $("cxAsof").value || null});
        location.hash = "#console/run/" + encodeURIComponent(r.id);
      } catch (e) { $("cxMsg").innerHTML = `<span class="cx-bad">${esc(e.message)}</span>`; btn.disabled = false; }
    };
    const [runs, saved] = await Promise.all([api("/api/runs"), api("/api/saved").catch(() => ({runs: []}))]);
    if (tok !== token) return;
    $("cxRuns").innerHTML = runs.runs.length ? `<div class="cx-list">${runs.runs.map(r => `<a class="cx-li" href="#console/run/${encodeURIComponent(r.id)}">
      ${badge(r.status)}<span title="${esc(r.question)}">${esc(r.question)}</span><span class="lbl">${esc(r.as_of)}</span></a>`).join("")}</div>
      <p class="fine">${T(`At most ${esc(runs.max_active)} unfinished runs at a time.`, `同时最多 ${esc(runs.max_active)} 个没结束的运行。`)}</p>` : T("None yet.", "还没有。");
    const sv = (saved.runs || []).slice().sort((a, b) => String(b.started_at || "").localeCompare(String(a.started_at || ""))).slice(0, 8);
    $("cxSaved").innerHTML = sv.length ? `<div class="cx-list">${sv.map(r => `<a class="cx-li" href="#console/result/${encodeURIComponent(r.qid)}/${encodeURIComponent(r.tag || "")}">
      <span class="stencil">${esc(r.kind)}</span><span title="${esc(r.qid)} / ${esc(r.tag)}">${esc(r.qid)} <span class="lbl">${esc(r.tag || "")}</span></span>
      <span class="lbl">${r.mode === "discrete" ? esc(r.most_likely ?? "—") : fmt(r.estimate)}</span></a>`).join("")}</div>` : T("None.", "没有。");
  }

  // ---------- 进度 ----------
  function phaseOf(r) {
    if (r.status === "done") return 5;
    const first = (r.stages || []).find(s => s.status !== "done");
    if (!first) return 5;
    const k = first.key || "";
    return k === "plan" ? 0 : k === "approve" ? 1 : k.startsWith("subagents") ? 2 : k.startsWith("judge") ? 3 : 4;
  }
  function missionOf(r) {
    const ph = phaseOf(r), dead = r.status === "failed" || r.status === "cancelled";
    return {view: "MISSION · " + String(r.qid || "").toUpperCase(), status: HUDST[r.status] || String(r.status).toUpperCase(),
      phase: dead ? -1 : ph, progress: ph / 5, elapsed: r.elapsed_s, done: r.status === "done",
      cam: `US$ ${r.usd === null || r.usd === undefined ? "—" : r.usd.toFixed(3)} / ${r.usd_cap ? r.usd_cap.toFixed(2) : "—"}  AS OF ${r.as_of}`};
  }
  function strip(r) {
    const active = ACTIVE.includes(r.status);
    return `<div class="cx-strip">
      <div>${badge(r.status)}${r.cancel_requested ? ` <span class="stencil">${T("cancel requested", "已请求取消")}</span>` : ""}</div>
      <div><span class="lbl">${T("Elapsed", "用时")}</span><b>${fmt(r.elapsed_s)} s</b></div>
      <div><span class="lbl">${T("Spent / cap", "花费 / 上限")}</span><b>${usd(r.usd)}${r.usd_cap ? ` / $${r.usd_cap.toFixed(2)}` : ""}</b></div>
      <div><span class="lbl">AS OF</span><b>${esc(r.as_of)}</b></div>
      <div>${active ? `<button class="btn" type="button" id="cxCancel">${T("Abort", "取消运行")}<span>✕</span></button>`
        : `<a class="btn" href="#console">${T("New mission", "新任务")}<span>+</span></a>`}</div></div>`;
  }
  function targetTable(t) {
    if (!t) return `<p class="fine">${T("Not pinned yet.", "还没有。")}</p>`;
    const rows = [["what", "What", "是什么"], ["unit", "Unit", "单位"], ["period_start", "From", "期间开始"], ["period_end", "To", "期间结束"],
      ["publisher", "Publisher", "谁公布"], ["cadence", "Cadence", "公布节奏"], ["caveats", "Caveats", "注意"]];
    const outs = t.outcome_type === "discrete" ? `<tr><th>${T("Outcomes", "结果")}</th><td>${(t.outcomes || []).map(o => esc(o.label)).join(" · ") || T("defined by the judge after the evidence", "取证后由裁判定义")}</td></tr>` : "";
    return `<table class="cx-t">${rows.filter(([k]) => t[k] !== undefined && t[k] !== null && t[k] !== "")
      .map(([k, en, z]) => `<tr><th>${T(en, z)}</th><td>${esc(t[k])}</td></tr>`).join("")}${outs}</table>`;
  }
  const dots = n => { const k = Math.max(0, Math.min(5, Math.round(+n || 0))); return "●".repeat(k) + "○".repeat(5 - k); };
  function gate(r) {
    return `<div class="cx-gate"><h3 class="cx-h">${T("Human gate · approve the routes", "人工确认 · 批准取证方向")}</h3>
      <p class="sub">${T("Verrier stopped here. Unchecked routes will not run; kept routes are renumbered d1..dK.",
        "agent 停在这里等你确认。不勾的方向不会跑，保留的方向会重新编号 d1..dK。")}</p>
      ${(r.plan_notes || []).length ? `<p class="fine">${r.plan_notes.map(esc).join("<br>")}</p>` : ""}
      <div class="cx-dirs">${(r.directions_proposed || []).map(d => `<label class="cx-dir cx-pick">
        <input type="checkbox" class="cx-keep" value="${esc(d.id)}" checked>
        <span class="cx-dh"><b>${esc(d.id)}</b><span class="stencil">${esc(d.category)}</span>
          <span class="cx-dots" title="expected information ${esc(d.expected_information)}/5">${dots(d.expected_information)}</span></span>
        ${d.perspective ? `<span class="cx-dp">${esc(d.perspective)}</span>` : ""}
        <span><b>${T("Hypothesis", "假设")}:</b> ${esc(d.hypothesis)}</span>
        <span class="fine"><b>${T("Data to find", "要找的数据")}:</b> ${esc(d.data_to_find)}</span></label>`).join("")}</div>
      <div class="cx-row"><button class="btn primary" type="button" id="cxApprove">${T("Approve selected routes", "批准勾选的方向")}<span>→</span></button>
        <button class="btn" type="button" id="cxAll">${T("All", "全选")}</button><button class="btn" type="button" id="cxNone">${T("None", "全不选")}</button>
        <span id="cxGateMsg" class="fine"></span></div></div>`;
  }
  function wireGate(r, tok) {
    const boxes = () => [...body.querySelectorAll("input.cx-keep")];
    const sync = b => b.closest(".cx-dir").classList.toggle("off", !b.checked);
    boxes().forEach(b => { b.onchange = () => sync(b); });
    $("cxAll").onclick = () => boxes().forEach(b => { b.checked = true; sync(b); });
    $("cxNone").onclick = () => boxes().forEach(b => { b.checked = false; sync(b); });
    $("cxApprove").onclick = async () => {
      const ids = boxes().filter(b => b.checked).map(b => b.value);
      if (!ids.length) { $("cxGateMsg").innerHTML = `<span class="cx-bad">${T("Keep at least one route.", "至少保留一个方向。")}</span>`; return; }
      $("cxApprove").disabled = true;
      try {
        await post(`/api/runs/${encodeURIComponent(r.id)}/approve`, ids.length === (r.directions_proposed || []).length ? {} : {keep_direction_ids: ids});
        stop();
        body.innerHTML = "";
        viewRun(r.id, tok).catch(fail(tok));
      } catch (e) { $("cxGateMsg").innerHTML = `<span class="cx-bad">${esc(e.message)}</span>`; $("cxApprove").disabled = false; }
    };
  }
  function stages(ss) {
    return `<div class="cx-steps">${(ss || []).map((s, i) => `<div class="cx-st st-${esc(s.status)}"><span class="n">${String(i + 1).padStart(2, "0")}</span>
      <div><h4>${T(...(STAGE[s.key] || [esc(s.label), esc(s.label)]))}</h4>
      <p><span class="lbl">${T(...(SSTAT[s.status] || [esc(s.status), esc(s.status)]))}</span>${s.detail ? " · " + esc(s.detail) : ""}</p></div></div>`).join("")}</div>`;
  }
  function dirCard(d) {
    const st = DST[d.status] || [esc(d.status), esc(d.status)], busy = ["searching", "fetching", "extracting"].includes(d.status);
    const pg = d.pages || {}, pts = d.n_kept !== null && d.n_kept !== undefined ? d.n_kept : (d.n_points ?? d.n_verified ?? 0);
    const urls = (d.status === "fetching" || d.status === "extracting") ? ` ${esc(d.pages_done ?? 0)}/${esc(d.n_urls ?? "?")}` : "";
    return `<div class="cx-dir${busy ? " busy" : ""}${d.status === "done" ? " ok" : ""}">
      <span class="cx-dh"><b>${esc(d.id)}</b><span class="stencil">${esc(d.category)}</span>${d.round > 1 ? '<span class="lbl">R2</span>' : ""}
        <span class="cx-state">${T(...st)}${urls}</span></span>
      <span>${esc(d.hypothesis)}</span>
      <span class="cx-nums"><span><b>${esc(pg.snapshot ?? 0)}</b> snap</span><span><b>${esc(pg.live_dated ?? 0)}</b> live</span>
        <span><b>${esc(pg.dropped ?? 0)}</b> drop</span><span><b>${esc(d.n_extracted ?? 0)}</b> ${T("read", "抽取")}</span>
        <span><b>${esc(pts)}</b> ${T("points", "个点")}</span></span>
      ${d.stopped ? `<span class="fine">${esc(d.stopped)}</span>` : ""}</div>`;
  }
  function computed(c) {
    if (c.mode === "discrete") return `<h3 class="cx-h">${T("Computed · outcome probabilities", "代码计算 · 各结果的概率")}</h3>
      <div class="cx-big">${esc(c.most_likely ?? "—")}</div><p class="fine">${prob(c.most_likely_prob)} · ${(c.outcomes || []).map(o => `${esc(o.label)} ${prob(o.prob)}`).join(" · ")}</p>`;
    return `<h3 class="cx-h">${T("Computed by code", "代码计算")}</h3><div class="cx-big">${fmt(c.central)}</div>
      <p class="fine">80% model-based [${fmt(c.p10)}, ${fmt(c.p90)}] · ${esc(c.basis)}</p>`;
  }
  function wireCancel(r) {
    const c = $("cxCancel");
    if (!c) return;
    c.onclick = async () => {
      if (!confirm(zh() ? "取消这次运行？已经花掉的钱不会退。" : "Abort this mission? Money already spent is not refunded.")) return;
      try { await post(`/api/runs/${encodeURIComponent(r.id)}/cancel`); } catch (e) { fail(token)(e); return; }
      route();
    };
  }
  async function viewRun(id, tok) {
    const r = await api("/api/runs/" + encodeURIComponent(id));
    if (tok !== token) return;
    code.textContent = String(r.qid || id).toUpperCase();
    hud(missionOf(r));
    if (r.status === "done" && !played.has(id)) { played.add(id); window.VERRIER && window.VERRIER.play(); }
    const active = ACTIVE.includes(r.status), picking = r.status === "awaiting_approval";
    if (picking && $("cxApprove")) {   // 正在勾选方向：只刷新状态条，不重画勾选框
      $("cxStrip").innerHTML = strip(r);
      wireCancel(r);
      return schedule(() => viewRun(id, tok), 3000, tok);
    }
    const keep = body.scrollTop;
    body.innerHTML = `<div id="cxStrip">${strip(r)}</div>
      ${r.error ? `<div class="cx-err">${esc(r.error)}</div>` : ""}
      <p class="cx-q">${esc(r.question)}</p><p class="fine">${T("question id", "题 id")} ${esc(r.qid)} · tag ${esc(r.tag)}</p>
      ${picking ? gate(r) : ""}
      <div class="cx-grid"><div>
        <h3 class="cx-h">${T("Pipeline", "流程")}</h3>${stages(r.stages)}
        ${(r.directions || []).length ? `<h3 class="cx-h">${T("Field agents", "子 agent（各取证方向）")}</h3><div class="cx-dirs">${r.directions.map(dirCard).join("")}</div>` : ""}
        ${r.markets ? `<p class="fine">${T("Prediction markets", "预测市场")}: ${esc(r.markets.n_markets)} · ${esc(r.markets.n_points)} pts. ${esc(r.markets.note || "")}</p>` : ""}
      </div><div>
        <h3 class="cx-h">${T("Pinned target", "钉死的目标")}</h3>${targetTable(r.target)}
        ${r.compute ? computed(r.compute) : ""}
      </div></div>
      <div id="cxDelivered"></div>`;
    body.scrollTop = keep;
    if (picking) wireGate(r, tok);
    wireCancel(r);
    if (r.result) loadDelivered(r.result.qid, r.result.tag, tok, false);
    if (active) schedule(() => viewRun(id, tok), picking ? 3000 : 2000, tok);
  }

  // ---------- 结果 ----------
  function delivered(r, qid, tag) {
    const e = r.estimate || {}, o = r.official, sh = (r.assumption_share || {}).overall, ev = r.evidence || {}, b = r.budget || {};
    const ms = r.methods || [], d = r.discrete;
    const main = d ? `<div class="lbl">${T("Most likely outcome", "最可能的结果")}</div><div class="cx-big">${esc(d.most_likely ?? "—")}</div>
        <p class="fine">${prob(d.most_likely_prob)} · ${(d.outcomes || []).map(x => `${esc(x.label)} ${prob(x.prob)}`).join(" · ")}</p>`
      : `<div class="lbl">${T("Estimate", "估计")}</div><div class="cx-big">${fmt(e.central)}</div>
        <p class="fine">80% model-based [${fmt(e.p10)}, ${fmt(e.p90)}]${e.basis_text ? " · " + esc(e.basis_text) : ""}</p>`;
    return `<div class="cx-deliv"><div class="bh"><span>R-01 · ${T("Delivered", "已交付")}</span><i class="hz"></i><span class="sp"></span><span>${esc(qid)} / ${esc(tag || "—")}</span></div>
      <div class="bd"><div class="cx-grid"><div>${main}
        ${o && !d ? `<p class="fine">OFFICIAL ${fmt(o.answer_value)} · ${T("error", "误差")} <b>${pct(o.pct_err)}</b></p>` : ""}
        ${sh === null || sh === undefined ? "" : `<div class="cx-bar"><i style="width:${(100 * (1 - sh)).toFixed(1)}%"></i></div>
          <p class="fine">${T("Evidence", "证据")} ${share(1 - sh)} · ${T("Assumptions", "假设")} ${share(sh)}</p>`}
        ${r.aborted ? `<div class="cx-err">${esc(r.aborted)}</div>` : ""}
      </div><div class="cx-meta">
        <div><span class="lbl">${T("Kept points", "保留的点")}</span><b>${(ev.kept || []).length}</b></div>
        <div><span class="lbl">${T("Discarded", "丢弃的点")}</span><b>${(ev.discarded || []).length}</b></div>
        <div><span class="lbl">${T("Methods computed", "算出的方法")}</span><b>${ms.filter(m => m.status === "computed").length}/${ms.length}</b></div>
        <div><span class="lbl">${T("Cost", "花费")}</span><b>${usd(b.usd_total_assumed)}</b></div>
      </div></div>
      <h3 class="cx-h">${T("Final answer", "最终答案")}</h3><pre class="cx-answer">${esc(r.final_text || "—")}</pre>
      <div class="cx-row">
        <a class="btn primary" href="${resultHref(qid, tag)}" target="_blank" rel="noopener">${T("Evidence, methods, assumptions", "证据、方法和假设")}<span>↗</span></a>
        <a class="btn" href="${fileHref(qid, tag, "graph.html")}" target="_blank" rel="noopener">${T("Dependency graph", "依赖图")}<span>↗</span></a>
        <a class="btn" href="${fileHref(qid, tag, "ledger.md")}" target="_blank" rel="noopener">ledger.md<span>↗</span></a>
      </div></div></div>`;
  }
  async function loadDelivered(qid, tag, tok, withQuestion) {
    let r;
    try { r = await api(`/api/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`); } catch (e) { r = {error: e.message}; }
    const el = $("cxDelivered");
    if (tok !== token || !el) return r;
    el.innerHTML = r.error ? `<div class="cx-err">${esc(r.error)}</div>` : delivered(r, qid, tag);
    return r;
  }
  async function viewResult(qid, tag, tok) {
    code.textContent = String(qid).toUpperCase();
    body.innerHTML = `<div class="cx-row"><a class="btn" href="#console"><span>←</span>${T("Mission control", "控制台")}</a></div>
      <p class="cx-q" id="cxRq">…</p><p class="fine" id="cxRm"></p><div id="cxDelivered"></div>`;
    const r = await loadDelivered(qid, tag, tok, true);
    if (tok !== token || !r || r.error) return;
    $("cxRq").textContent = r.question || qid;
    $("cxRm").innerHTML = `AS OF ${esc(r.as_of)} · ${esc(r.kind)} · ${esc(r.model)} · ${esc(r.started_at)}${r.wall_s ? ` · ${fmt(r.wall_s)} s` : ""}`;
    hud({view: "MISSION · " + String(qid).toUpperCase(), status: r.aborted ? "MISSION FAILED" : "ARCHIVED RESULT", phase: r.aborted ? -1 : 5, progress: 1,
      elapsed: r.wall_s || 0, done: !r.aborted, cam: `US$ ${(r.budget || {}).usd_total_assumed?.toFixed?.(3) ?? "—"}  AS OF ${r.as_of}`});
  }

  // ---------- 接线 ----------
  $("cxClose").onclick = leave;
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !cx.hidden) leave(); });
  addEventListener("hashchange", route);
  route();
})();
