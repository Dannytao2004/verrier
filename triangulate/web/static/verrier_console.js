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
  // 装饰动效（雷达、声波、打字机）的定时器：换页或关掉控制台时清掉；和轮询的 timer 分开，轮询重画不打断它们
  const fxTimers = [];
  const fxEvery = (fn, ms) => fxTimers.push(setInterval(fn, ms));
  function fxClear() { while (fxTimers.length) clearInterval(fxTimers.pop()); thinkStop(); }

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
    fxClear();
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
    fxClear();
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
        <div class="cx-wave" id="cxWave" aria-hidden="true">${"<i></i>".repeat(48)}</div>
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
        <h3 class="cx-h">${T("Signal scope", "信号扫描")}</h3>
        <div class="cx-scope" aria-hidden="true"><div class="cx-radar" id="cxRadar"><i class="ring a"></i><i class="ring b"></i><i class="ring c"></i>
          <i class="ax h"></i><i class="ax v"></i><i class="sweep"></i></div>
          <div class="cx-scope-read"><span class="lbl">DU-2 · SCOPE</span><b id="cxScopeTxt"></b><span class="lbl" id="cxScopeSub">SWEEP 0000</span></div></div>
        <h3 class="cx-h">${T("Missions this session", "这次服务启动后的任务")}</h3><div id="cxRuns" class="fine">…</div>
        <h3 class="cx-h">${T("Saved runs", "已保存的运行")}</h3><div id="cxSaved" class="fine">…</div>
        <p class="fine"><a href="/#/saved" target="_blank" rel="noopener">${T("All saved runs and backtests in the classic view ↗", "在经典界面看全部运行和回测 ↗")}</a></p>
      </div></div>`;
    body.dataset.run = "";
    body.querySelectorAll("[data-ex]").forEach(b => { b.onclick = () => {
      $("cxQ").value = EXAMPLES[+b.dataset.ex]; $("cxQ").dispatchEvent(new Event("input")); $("cxQ").focus(); }; });
    $("cxGo").onclick = async () => {
      const btn = $("cxGo");
      btn.disabled = true;
      btn.classList.add("ignite");
      $("cxScopeTxt").innerHTML = T("Ignition", "点火");
      try {
        const [r] = await Promise.all([post("/api/runs", {question: $("cxQ").value, as_of: $("cxAsof").value || null}),
          new Promise(ok => setTimeout(ok, 900))]);   // 点火动画至少放完一段
        location.hash = "#console/run/" + encodeURIComponent(r.id);
      } catch (e) {
        $("cxMsg").innerHTML = `<span class="cx-bad">${esc(e.message)}</span>`;
        btn.disabled = false;
        btn.classList.remove("ignite");
      }
    };
    scope(tok);
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

  // ---------- 装饰动效：雷达扫描、按键声波、「思考中」打字机 ----------
  // 只是动效：显示的文字是固定的短语或真实的阶段名、字数，不编造证据或数字。
  const IDLE = [["Listening for a question", "等待你的问题"], ["Scanning the public record", "扫描公开记录"],
    ["Release calendars on file", "发布日历已就绪"], ["Field agents on standby", "子 agent 待命"]];
  function scope(tok) {
    const radar = $("cxRadar"), txt = $("cxScopeTxt"), sub = $("cxScopeSub"), wave = $("cxWave"), q = $("cxQ");
    if (!radar || !wave || !q) return;
    const bars = [...wave.children];
    let k = 0, typing = 0;
    txt.innerHTML = T(...IDLE[0]);
    const blip = () => {
      const a = Math.random() * 2 * Math.PI, r = 8 + Math.random() * 48, b = document.createElement("span");
      b.className = "blip" + (Math.random() < .3 ? " r" : "");
      b.style.left = (60 + r * Math.cos(a)).toFixed(1) + "px";
      b.style.top = (60 + r * Math.sin(a)).toFixed(1) + "px";
      radar.appendChild(b);
      setTimeout(() => b.remove(), 2500);
    };
    q.addEventListener("input", () => {
      typing = 3;
      radar.classList.add("fast");
      wave.classList.add("live");
      const s = q.value.trim(), words = s ? s.split(/\s+/).length : 0;
      txt.innerHTML = T("Parsing the question", "正在解析问题");
      sub.textContent = `${s.length} CHARS · ${words} WORDS`;
      bars.forEach(i => { i.style.height = (18 + Math.random() * 82).toFixed(0) + "%"; });
      if (Math.random() < .5) blip();
    });
    fxEvery(() => {
      if (tok !== token || !document.body.contains(radar)) return;
      blip();
      if (typing > 0) typing--;
      else {
        radar.classList.remove("fast");
        wave.classList.remove("live");
        if (!$("cxGo") || !$("cxGo").disabled) { txt.innerHTML = T(...IDLE[++k % IDLE.length]); sub.textContent = "SWEEP " + String(k).padStart(4, "0"); }
      }
    }, 1400);
    fxEvery(() => { if (!typing) bars.forEach(i => { i.style.height = (5 + Math.random() * 16).toFixed(0) + "%"; }); }, 220);
  }
  const orb = p => `<svg class="ask-orb" viewBox="0 0 80 80" aria-hidden="true"><circle class="o-ring" cx="40" cy="40" r="37"/>
    <g class="o-ticks"><path d="M40 0v6M40 74v6M0 40h6M74 40h6"/></g><path class="o-sweep" d="M40 40 L40 3 A37 37 0 0 1 66.2 13.8 Z"/>
    <g class="o-sys"><path id="${p}A" class="o-orbit" d="M10 40 a30 11 0 1 0 60 0 a30 11 0 1 0 -60 0"/>
    <circle class="o-pl" r="3.4"><animateMotion dur="2.6s" repeatCount="indefinite"><mpath href="#${p}A"/></animateMotion></circle>
    <g transform="rotate(58 40 40)"><path id="${p}B" class="o-orbit dim" d="M40 13 a10 27 0 1 0 0 54 a10 27 0 1 0 0 -54"/>
    <circle class="o-pl" r="2.3"><animateMotion dur="1.7s" repeatCount="indefinite"><mpath href="#${p}B"/></animateMotion></circle></g></g>
    <circle class="o-halo" cx="40" cy="40" r="8"/><circle class="o-core" cx="40" cy="40" r="4.4"/></svg>`;
  // 每个阶段的短语：描述这个阶段真实在做的事
  const PHRASES = {
    plan: [["Reading the question", "正在读题"], ["Pinning the exact target", "锁定要估的那个数"], ["Drafting estimation routes", "起草推算路线"],
      ["Working out where the evidence might hide", "推测证据可能藏在哪里"]],
    subagents: [["Field agents are reading the public record", "子 agent 正在翻公开记录"], ["Checking every quote against the page", "逐字核对每条引文"],
      ["Dropping pages without a usable date", "丢掉读不出日期的网页"], ["Collecting numbers with their sources", "收集带出处的数字"]],
    judge: [["Weighing the evidence", "权衡证据"], ["Cross-checking the routes", "交叉核对各条路线"], ["Flagging every assumption", "标出每一个假设"],
      ["Auditing each formula input", "逐个核对公式输入"]],
    compute: [["Running the formulas in code", "用代码跑公式"], ["Drawing 20,000 Monte Carlo samples", "抽 20,000 个 Monte Carlo 样本"],
      ["Combining the routes", "合并各条路线"]],
    final: [["Writing the answer", "撰写答案"], ["Attaching the evidence ledger", "附上证据账本"]],
  };
  const GLYPHS = "▮▯▮▯··0123456789ABCDEF";
  let think = null;
  function thinkStop() { if (think) { clearInterval(think.timer); think = null; } }
  function thinkSet(host, key, stageHtml) {
    if (!host) return thinkStop();
    if (!key) { thinkStop(); host.innerHTML = ""; return; }
    if (think && think.host === host && think.key === key) { $("cxThinkStage").innerHTML = stageHtml; return; }
    thinkStop();
    host.innerHTML = `<div class="cx-think" aria-live="polite">${orb("cxOrb")}<div>
      <span class="lbl">${T("Verrier is thinking", "Verrier 正在思考")} · <span id="cxThinkStage">${stageHtml}</span></span>
      <div class="cx-tl"><b class="cx-type" id="cxType"></b><span class="cx-cursor">▌</span></div>
      <div class="cx-scan"><i></i></div><div class="cx-bits" id="cxBits"></div></div></div>`;
    const list = PHRASES[key] || PHRASES.plan, st = {host, key, p: 0, c: 0, dir: 1, hold: 0, n: 0};
    st.timer = setInterval(() => {
      const el = $("cxType"), bits = $("cxBits");
      if (!el || !document.body.contains(host)) return thinkStop();
      const s = list[st.p][zh() ? 1 : 0];
      if (st.hold > 0) { if (--st.hold === 0) st.dir = -1; }
      else if (st.dir === 1) { st.c = Math.min(s.length, st.c + 1); if (st.c >= s.length) { st.dir = 0; st.hold = 40; } }
      else if (st.dir === -1) { st.c = Math.max(0, st.c - 2); if (st.c === 0) { st.p = (st.p + 1) % list.length; st.dir = 1; } }
      el.textContent = s.slice(0, st.c);
      if (bits && ++st.n % 3 === 0) bits.textContent = Array.from({length: 56}, () => GLYPHS[Math.floor(Math.random() * GLYPHS.length)]).join("");
    }, 45);
    think = st;
  }
  function stageKey(r) {
    if (!["planning", "running"].includes(r.status)) return null;
    const first = (r.stages || []).find(s => s.status !== "done");
    if (!first || first.key === "approve") return r.status === "planning" ? "plan" : null;
    const k = first.key || "";
    return k.startsWith("subagents") ? "subagents" : k.startsWith("judge") ? "judge" : ["plan", "compute", "final"].includes(k) ? k : "plan";
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
        viewRun(r.id, tok).catch(fail(tok));   // 骨架（cxRunTop / cxThink / cxRunMain）留着，只重画里面
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
    // 同一个运行只搭一次骨架：「思考中」面板放在 cxThink 里，轮询只重画 cxRunTop 和 cxRunMain，打字机动画不会被打断
    if (body.dataset.run !== id) {
      body.dataset.run = id;
      body.innerHTML = `<div id="cxRunTop"></div><div id="cxThink"></div><div id="cxRunMain"></div>`;
    }
    const keep = body.scrollTop, key = stageKey(r), cur = (r.stages || []).find(s => s.status !== "done");
    $("cxRunTop").innerHTML = `<div id="cxStrip">${strip(r)}</div>
      ${r.error ? `<div class="cx-err">${esc(r.error)}</div>` : ""}
      <p class="cx-q">${esc(r.question)}</p><p class="fine">${T("question id", "题 id")} ${esc(r.qid)} · tag ${esc(r.tag)}</p>`;
    thinkSet($("cxThink"), key, cur ? T(...(STAGE[cur.key] || [esc(cur.label), esc(cur.label)])) : "");
    $("cxRunMain").innerHTML = `${picking ? gate(r) : ""}
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
    body.dataset.run = "";
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
