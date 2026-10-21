// Verrier 控制台：把 agent 的主运行界面（提问 → 人工确认方向 → 进度 → 结果）放进 Verrier 页面（verrier_console.html）。
// 只调用现有 API（/api/runs、/api/result、/api/saved、/api/file、/api/graph），后端逻辑不变；回测表在经典界面（/#/...）。
// web-v0.9：提问页多了「模型 · key · 上限」：provider、区域（只有 Kimi / GLM）、模型（带每次运行的估计花费，/api/providers）、
// 你自己的 API key（默认存在这个标签页的 sessionStorage；勾「在这台设备上记住」才放 localStorage，明文）、校验 key（/api/key/check）、
// 思考档位、花费上限（默认 $2.00）。发起运行时 key 随 POST /api/runs 发给本机服务，只留在这次运行的内存里。
// 路由：#console（提问）、#console/run/<运行 id>（进度）、#console/result/<题 id>/<tag>（保存的结果）、
// #console/evidence/<题 id>/<tag>（证据、方法和假设；面板由 verrier_evidence.js 画）、#console/graph/<题 id>/<tag>（依赖图；
// 图纸由 verrier_graph.js 画）。别的 hash 是页面锚点，控制台关掉。
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
  const fileHref = (qid, tag, name) => `/api/file?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag || "")}&name=${name}`;
  const hud = m => window.VERRIER && window.VERRIER.mission && window.VERRIER.mission(m);

  const ST = {planning: ["Planning", "规划中"], awaiting_approval: ["Awaiting approval", "等待确认"], running: ["In flight", "运行中"],
    done: ["Delivered", "已交付"], failed: ["Failed", "失败"], cancelled: ["Cancelled", "已取消"]};
  const badge = st => `<span class="stencil s-${esc(st)}">${T(...(ST[st] || [esc(st), esc(st)]))}</span>`;
  const HUDST = {planning: "PLANNING ROUTES", awaiting_approval: "AWAITING APPROVAL", running: "IN FLIGHT", done: "TARGET ACQUIRED",
    failed: "MISSION FAILED", cancelled: "MISSION ABORTED"};
  const DST = {queued: ["Queued", "排队"], searching: ["Searching", "搜索中"], fetching: ["Fetching", "取页中"], extracting: ["Extracting", "抽取中"],
    done: ["Done", "完成"], stopped: ["Stopped", "中止"]};
  const SSTAT = {done: ["done", "完成"], running: ["running", "进行中"], waiting: ["waiting for you", "等你确认"], pending: ["pending", "未开始"]};
  // 运行页的流程时间轴：8 站，由 /api/runs 的 stages（服务端的阶段）和 calls（按角色计的调用次数）推出来，只是大致反映 agent 在做什么：
  // 单位核对、输入核对和修正都在裁判节点里，服务端没有单独的阶段，按调用次数亮灯
  const STATIONS = [["plan", ["Plan · lock target", "规划 · 锁定目标"], ["plan"]], ["approve", ["Human gate", "人工确认"], ["approve"]],
    ["field", ["Field agents", "子 agent 取证"], ["subagents1", "subagents2"]], ["judge", ["Judge", "裁判评估"], ["judge1", "judge2"]],
    ["units", ["Unit review", "单位核对"], []], ["audit", ["Input audit · repair", "输入核对 · 修正"], []],
    ["compute", ["Compute (code)", "代码计算"], ["compute"]], ["final", ["Published check · final", "已公布检查 · 终稿"], ["final"]]];
  function stations(r) {
    const by = new Map((r.stages || []).map(s => [s.key, s])), calls = Object.entries(r.calls || {});
    const count = f => calls.reduce((n, [k, v]) => n + (f(k) ? v : 0), 0);
    const nChk = count(k => k.startsWith("unit_check")), nArb = count(k => k.startsWith("unit_arbiter"));
    const nAud = count(k => k === "audit"), nRep = count(k => k.endsWith(":repair"));
    const computed = (by.get("compute") || {}).status === "done";
    const plain = keys => { const ss = keys.map(k => by.get(k)).filter(Boolean), sts = ss.map(s => s.status);
      return {status: !sts.length ? "pending" : sts.every(s => s === "done") ? "done" : sts.includes("waiting") ? "waiting"
        : sts.includes("running") ? "running" : "pending", detail: ss.map(s => esc(s.detail || "")).filter(Boolean).join(" · ")}; };
    const judging = plain(["judge1", "judge2"]).status === "running";   // 单位核对、输入核对都在裁判节点里：裁判站在跑时才按调用次数亮
    const st = STATIONS.map(([key, label, keys]) => {
      if (key === "units") return {key, label, status: computed ? "done" : judging && nChk + nArb ? "running" : "pending",
        detail: nChk + nArb ? `${T("checks", "核对")} ${nChk} · ${T("arbiter", "裁定")} ${nArb}` : ""};
      if (key === "audit") return {key, label, status: computed ? "done" : judging && nAud + nRep ? "running" : "pending",
        detail: nAud + nRep ? `${T("audits", "输入核对")} ${nAud}${nRep ? ` · ${T("repairs", "修正")} ${nRep}` : ""}` : ""};
      return {key, label, ...plain(keys)};
    });
    // 后一站已经开始时，前面没完成的站都显示成完成（裁判节点要等单位核对、输入核对做完才结束；没做单位核对时那一站算跳过）
    const last = st.map(s => s.status).lastIndexOf("running");
    st.forEach((s, i) => { if (i < last && s.status !== "done") s.status = "done"; });
    return st;
  }
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
      : parts[1] === "result" && parts[2] ? viewResult(parts[2], parts[3] || "", tok)
      : parts[1] === "evidence" && parts[2] ? viewEvidence(parts[2], parts[3] || "", tok)
      : parts[1] === "graph" && parts[2] ? viewGraph(parts[2], parts[3] || "", tok) : viewHome(tok);
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
        ${cfgForm()}
        <div class="cx-row"><button class="btn primary" type="button" id="cxGo">${T("Launch mission", "发射任务")}<span>→</span></button>
          <span id="cxMsg" class="fine"></span></div>
        <p class="fine">${T("Bring your own key: web runs only use the key you enter here, never a key file on the server. The key stays in this browser and in the server's memory for this one run; it is cleared when the run ends and never written to disk. The spending cap includes the assumed search fee.",
          "自带 key：网页运行只用你在这里填的 key，从不使用服务器上的 key 文件。key 只留在这个浏览器和这次运行的服务器内存里，运行结束就清掉，不写进任何文件。花费上限含按假设单价记的搜索费。")}</p>
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
      const btn = $("cxGo"), key = ($("cxKey") || {}).value || "";
      if (!cat) {   // 模型清单没取到：不发（否则会按服务端默认的 DeepSeek 发出去，而 key 可能是别家的）
        $("cxMsg").innerHTML = `<span class="cx-bad">${T("The model list has not loaded yet.", "模型清单还没取到。")}</span>`;
        return;
      }
      if (!key.trim()) {
        $("cxMsg").innerHTML = `<span class="cx-bad">${T("Enter your own API key first (web runs never use a key file on the server).",
          "先填你自己的 API key（网页运行从不使用服务器上的 key 文件）。")}</span>`;
        if ($("cxKey")) $("cxKey").focus();
        return;
      }
      btn.disabled = true;
      btn.classList.add("ignite");
      $("cxScopeTxt").innerHTML = T("Ignition", "点火");
      try {
        const [r] = await Promise.all([post("/api/runs", {question: $("cxQ").value, as_of: $("cxAsof").value || null, ...runCfg(), api_key: key}),
          new Promise(ok => setTimeout(ok, 900))]);   // 点火动画至少放完一段
        location.hash = "#console/run/" + encodeURIComponent(r.id);
      } catch (e) {
        $("cxMsg").innerHTML = `<span class="cx-bad">${esc(e.message)}</span>`;
        btn.disabled = false;
        btn.classList.remove("ignite");
      }
    };
    scope(tok);
    cfgInit(tok).catch(fail(tok));
    const [runs, saved] = await Promise.all([api("/api/runs"), api("/api/saved").catch(() => ({runs: []}))]);
    if (tok !== token) return;
    $("cxRuns").innerHTML = runs.runs.length ? `<div class="cx-list">${runs.runs.map(r => `<a class="cx-li" href="#console/run/${encodeURIComponent(r.id)}">
      ${badge(r.status)}<span title="${esc(r.question)}">${esc(r.question)}</span><span class="lbl">${r.run_spec ? esc(r.run_spec.model) + " · " : ""}${esc(r.as_of)}</span></a>`).join("")}</div>
      <p class="fine">${T(`At most ${esc(runs.max_active)} unfinished runs at a time.`, `同时最多 ${esc(runs.max_active)} 个没结束的运行。`)}</p>` : T("None yet.", "还没有。");
    const sv = (saved.runs || []).slice().sort((a, b) => String(b.started_at || "").localeCompare(String(a.started_at || ""))).slice(0, 8);
    $("cxSaved").innerHTML = sv.length ? `<div class="cx-list">${sv.map(r => `<a class="cx-li" href="#console/result/${encodeURIComponent(r.qid)}/${encodeURIComponent(r.tag || "")}">
      <span class="stencil">${esc(r.kind)}</span><span title="${esc(r.qid)} / ${esc(r.tag)}">${esc(r.qid)} <span class="lbl">${esc(r.tag || "")}</span></span>
      <span class="lbl">${r.mode === "discrete" ? esc(r.most_likely ?? "—") : fmt(r.estimate)}</span></a>`).join("")}</div>` : T("None.", "没有。");
  }

  // ---------- 模型 · key · 上限（web-v0.9：自带 key） ----------
  // 非秘密的选择（provider、区域、模型、档位、上限）存 localStorage；key 按「provider + 区域」分开存：默认 sessionStorage
  // （关掉标签页就没了），勾了「在这台设备上记住」才放 localStorage（明文）。key 只在发起运行和校验 key 时发给本机服务
  const CFG_STORE = "verrier-run-cfg", keyName = (p, r) => `verrier-key:${p}:${r}`;
  const LV = {off: ["off", "关"], low: ["low", "低"], medium: ["medium", "中"], high: ["high", "高"]};
  const REG_ZH = {global: "国际站", cn: "国内站"};
  const bi = n => n ? T(esc(n.en), esc(n.zh)) : "";
  const money = x => x === null || x === undefined ? "—" : "$" + Number(x).toFixed(2);
  const stor = kind => { try { return kind === "local" ? localStorage : sessionStorage; } catch (e) { return null; } };
  const sget = (kind, k) => { try { const s = stor(kind); return s ? s.getItem(k) : null; } catch (e) { return null; } };
  const sset = (kind, k, v) => { try { const s = stor(kind); if (s) { if (v === null) s.removeItem(k); else s.setItem(k, v); } } catch (e) { /* 存不了就不存 */ } };
  let cat = null, capTimer = null;
  const cfg = {provider: null, region: null, model: null, thinking: null, cap: 2};
  try { Object.assign(cfg, JSON.parse(sget("local", CFG_STORE) || "{}")); } catch (e) { /* 坏的就用默认 */ }
  const cfgSave = () => sset("local", CFG_STORE, JSON.stringify(cfg));
  const provOf = () => cat.providers.find(p => p.id === cfg.provider);
  const modelOf = () => provOf().models.find(m => m.id === cfg.model);
  const regionOf = m => m.by_region[cfg.region] || Object.values(m.by_region)[0];
  function normalize() {   // 让选择总是合法的：不认识的 provider / 区域 / 模型 / 档位换成默认值
    if (!cat.providers.some(p => p.id === cfg.provider)) cfg.provider = cat.default_provider;
    const p = provOf();
    if (!p.regions.some(r => r.id === cfg.region)) cfg.region = p.default_region;
    if (!p.models.some(m => m.id === cfg.model)) cfg.model = p.default_model;
    const m = modelOf();
    if (!m.thinking.levels.includes(cfg.thinking)) cfg.thinking = m.thinking.default;
    if (!(Number(cfg.cap) > 0)) cfg.cap = cat.default_usd_cap;
  }
  function runCfg() {   // 上限取输入框里的值（不合法时由服务端回 400 说明，不悄悄用上一次的值）
    const capIn = $("cxCap"), cap = capIn && capIn.value.trim() !== "" ? Number(capIn.value) : Number(cfg.cap);
    return {provider: cfg.provider, model: cfg.model, region: cfg.region, thinking: cfg.thinking, usd_cap: isFinite(cap) ? cap : String(capIn.value)};
  }
  function cfgForm() {
    return `<div class="cx-cfg" id="cxCfg">
      <div class="cx-cfg-h"><span>${T("Model · key · limits", "模型 · key · 上限")}</span><i class="hz"></i><span class="sp"></span><span>BYOK</span></div>
      <dl class="cx-cfg-g">
        <dt><label for="cxProv">${T("Provider", "模型厂商")}</label></dt><dd><select id="cxProv"><option>…</option></select><div class="fine" id="cxProvNote"></div></dd>
        <dt class="cx-reg"><label for="cxReg">${T("Region", "区域")}</label></dt><dd class="cx-reg"><select id="cxReg"></select>
          <div class="fine">${T("The international and China platforms have separate keys and balances: pick the one where the key was created.",
            "国际站和国内站的 key、余额互不通用：选建 key 的那一站。")}</div></dd>
        <dt><label for="cxModel">${T("Model", "模型")}</label></dt><dd><select id="cxModel"></select><div class="fine" id="cxModelNote"></div></dd>
        <dt><label for="cxKey">API key</label></dt><dd>
          <div class="cx-keyrow"><input type="password" id="cxKey" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="sk-…">
            <button class="btn" type="button" id="cxCheck">${T("Check key", "校验 key")}</button></div>
          <label class="cx-chk"><input type="checkbox" id="cxRemember"> ${T("Remember on this device", "在这台设备上记住")}</label>
          <div class="fine" id="cxKeyMsg"></div>
          <div class="fine" id="cxKeyNote"></div></dd>
        <dt><label for="cxThink">${T("Thinking", "思考深度")}</label></dt><dd><select id="cxThink"></select><div class="fine" id="cxThinkNote"></div></dd>
        <dt><label for="cxCap">${T("Spending cap", "花费上限")}</label></dt><dd><span class="cx-capin"><span class="lbl">US$</span>
          <input type="number" id="cxCap" min="0.1" step="0.5" value="2.00" inputmode="decimal"></span>
          <span class="fine">${T("per run, default $2.00", "每次运行，默认 $2.00")}</span></dd>
      </dl>
      <div class="cx-est" id="cxEst"></div></div>`;
  }
  function keyNote() {
    $("cxKeyNote").innerHTML = $("cxRemember").checked
      ? `<span class="cx-bad">${T("Stored in this browser's localStorage in plain text: anyone who can use this browser profile can read it. Untick to forget it.",
          "以明文存在这个浏览器的 localStorage 里：能用这个浏览器配置的人都读得到。取消勾选就会删掉。")}</span>`
      : T("Kept in this tab's sessionStorage only (gone when the tab is closed).", "只存在这个标签页的 sessionStorage 里（关掉标签页就没了）。");
  }
  function keyLoad() {   // 换 provider / 区域时填上这个组合存过的 key
    const n = keyName(cfg.provider, cfg.region), loc = sget("local", n);
    $("cxKey").value = loc ?? sget("session", n) ?? "";
    $("cxRemember").checked = loc !== null;
    $("cxKeyMsg").innerHTML = "";
    keyNote();
  }
  function keyStore() {
    const n = keyName(cfg.provider, cfg.region), v = $("cxKey").value.trim(), keep = $("cxRemember").checked;
    sset("local", n, v && keep ? v : null);
    sset("session", n, v && !keep ? v : null);
    keyNote();
  }
  function fillSelects() {
    const p = provOf(), m = modelOf();
    $("cxProv").innerHTML = cat.providers.map(x => `<option value="${esc(x.id)}"${x.id === cfg.provider ? " selected" : ""}>${esc(x.label)}</option>`).join("");
    $("cxReg").innerHTML = p.regions.map(r => `<option value="${esc(r.id)}"${r.id === cfg.region ? " selected" : ""}>${esc(r.label)}${REG_ZH[r.id] ? " · " + REG_ZH[r.id] : ""}</option>`).join("");
    body.querySelectorAll(".cx-reg").forEach(el => { el.hidden = !p.region_choice; });
    $("cxModel").innerHTML = p.models.map(x => {
      const lv = x.thinking.levels.includes(cfg.thinking) ? cfg.thinking : x.thinking.default, e = regionOf(x).by_thinking[lv];
      return `<option value="${esc(x.id)}"${x.id === cfg.model ? " selected" : ""}>${esc(x.label)} · ≈ ${money(e.est_usd)}/run${e.stops_early ? " ⚠" : ""}</option>`;
    }).join("");
    $("cxThink").innerHTML = cat.thinking_levels.map(lv => { const ok = m.thinking.levels.includes(lv);
      return `<option value="${esc(lv)}"${lv === cfg.thinking ? " selected" : ""}${ok ? "" : " disabled"}>${LV[lv] ? LV[lv].join(" · ") : esc(lv)}${ok ? "" : " — n/a"}</option>`; }).join("");
    if (document.activeElement !== $("cxCap")) $("cxCap").value = Number(cfg.cap).toFixed(2);
  }
  function priceLine(pr) {
    const u = pr.usd_per_mtok, cny = pr.currency !== "USD" && pr.listed;
    return `${T("Price, US$ per 1M tokens", "价格（美元 / 百万 token）")}: ${T("input", "输入")} ${esc(u.input.toFixed(3))} · ${T("output", "输出")} ${esc(u.output.toFixed(3))} · ${T("cache hit", "缓存命中")} ${esc(u.cache_hit.toFixed(3))}` +
      (cny ? ` · ${T(`listed in ${esc(pr.currency)}`, `原价 ${esc(pr.currency)}`)} ${esc(pr.listed.miss)} / ${esc(pr.listed.out)}${pr.fx ? `, ${T("converted at", "按汇率")} ${esc(pr.fx.cny_per_usd)} (${esc(pr.fx.date)})` : ""}` : "") +
      (pr.peak_offpeak ? ` · ${T("peak-hour price", "峰时价")}` : "") +
      (pr.source ? ` · <a href="${esc(pr.source)}" target="_blank" rel="noopener noreferrer">${T("source", "来源")}</a> ${esc(pr.checked || "")}` : "");
  }
  function cfgNotes() {
    const p = provOf(), m = modelOf(), r = regionOf(m), e = r.by_thinking[cfg.thinking], th = m.thinking, cap = Number(cfg.cap);
    const page = p.key_pages && p.key_pages[cfg.region];
    $("cxProvNote").innerHTML = (p.notes || []).map(bi).join("<br>") +
      (page ? `<br>${T("Create the key at", "在这里建 key")}: <a href="${esc(page)}" target="_blank" rel="noopener noreferrer">${esc(page)}</a>` : "");
    $("cxModelNote").innerHTML = priceLine(r.price) + ((m.notes || []).length ? "<br>" + m.notes.map(bi).join("<br>") : "");
    $("cxThinkNote").innerHTML = `${T("Applies to plan, judge and repair; they send", "作用于 plan、judge、repair，发")} <code>${esc(JSON.stringify(th.sends[cfg.thinking] || {}))}</code>;
      ${T("the other roles send", "其余角色发")} <code>${esc(JSON.stringify(th.sends_other_roles || {}))}</code>.
      ${T("Thinking tokens are billed as output.", "思考 token 按输出计费。")}`;   // 关不掉思考的说明在模型说明里（catalog.NOTE_NO_OFF）
    $("cxEst").innerHTML = `<div class="cx-est-n"><span class="lbl">${T("Estimated cost per run", "每次运行的估计花费")}</span><b>≈ ${money(e.est_usd)}</b></div>
      <div class="cx-est-n"><span class="lbl">${T("Cap", "上限")}</span><b>${money(cap)}</b></div>
      <div class="cx-est-n"><span class="lbl">${T("First-round routes", "第一轮方向数")}</span><b>${esc(e.directions)}</b></div>
      <div class="cx-est-t">
        ${e.over_cap ? `<p class="cx-bad">${T(`The estimate is above the cap: the run stops when it reaches ${money(cap)}.`, `估计超过上限：花到 ${money(cap)} 时运行就会停下。`)}</p>` : ""}
        ${e.stops_early ? `<p class="cx-bad">${T(`At this cap the first round's worst-case holds (searches in flight ${money(e.round1_search_hold_usd)}, one page extraction ${money(e.extract_hold_usd)}) do not fit, so the run will likely stop in round 1.`,
          `这个上限下，第一轮最坏情况的预扣（同时在途的搜索 ${money(e.round1_search_hold_usd)}、抽取一页 ${money(e.extract_hold_usd)}）放不下，运行很可能在第一轮就停下。`)}
          ${e.min_cap_usd ? T(`Raise the cap to at least ${money(e.min_cap_usd)} or pick a cheaper model.`, `把上限调到至少 ${money(e.min_cap_usd)}，或者换便宜的模型。`) : T("Pick a cheaper model.", "换便宜的模型。")}</p>` : ""}
        <p class="fine">${bi(cat.estimate_note)}</p></div>`;
  }
  function cfgRender() { normalize(); cfgSave(); fillSelects(); cfgNotes(); }
  async function loadCatalog(tok) {
    const c = await api("/api/providers?usd_cap=" + encodeURIComponent(Number(cfg.cap) > 0 ? Number(cfg.cap) : 2));
    if (tok !== token || !$("cxCfg")) return false;
    cat = c;
    cfgRender();
    return true;
  }
  async function cfgInit(tok) {
    if (!(await loadCatalog(tok))) return;
    keyLoad();
    const changed = (k, keyToo) => ev => { cfg[k] = ev.target.value; cfgRender(); if (keyToo) keyLoad(); };
    $("cxProv").onchange = changed("provider", true);
    $("cxReg").onchange = changed("region", true);
    $("cxModel").onchange = changed("model");
    $("cxThink").onchange = changed("thinking");
    $("cxCap").oninput = () => {   // 上限变了：方向数和估计跟着变，重新取一次目录（本机接口）
      const v = Number($("cxCap").value);
      if (!(v > 0)) return;
      cfg.cap = v;
      clearTimeout(capTimer);
      capTimer = setTimeout(() => loadCatalog(tok).catch(fail(tok)), 350);
    };
    $("cxKey").oninput = keyStore;
    $("cxRemember").onchange = keyStore;
    $("cxCheck").onclick = async () => {
      const btn = $("cxCheck"), key = $("cxKey").value;
      if (!key.trim()) { $("cxKeyMsg").innerHTML = `<span class="cx-bad">${T("Enter a key first.", "先填 key。")}</span>`; return; }
      btn.disabled = true;
      $("cxKeyMsg").textContent = "…";
      try {
        const r = await post("/api/key/check", {provider: cfg.provider, region: cfg.region, model: cfg.model, api_key: key});
        $("cxKeyMsg").innerHTML = r.ok ? `<span class="cx-ok">✓ ${esc(r.message)}</span>` : `<span class="cx-bad">✕ ${esc(r.message || r.error)}</span>`;
      } catch (err) { $("cxKeyMsg").innerHTML = `<span class="cx-bad">✕ ${esc(err.message)}</span>`; }
      btn.disabled = false;
    };
  }
  function specLine(r) {   // 运行页：这次运行用的模型，和 key 还在不在服务器内存里
    const s = r.run_spec;
    if (!s) return "";
    return ` · ${esc(s.provider)} / ${esc(s.model)}${s.region && s.region !== "global" ? " / " + esc(s.region) : ""} · ${T("thinking", "思考")} ${esc(s.thinking)} · ` +
      (r.key_in_memory ? T("key held in server memory for this run", "key 在服务器内存里（只用于这次运行）") : T("key cleared from server memory", "key 已从服务器内存清掉"));
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
    units: [["Three checkers derive each input's unit", "三位核对员各自推导单位"], ["The arbiter settles the result unit", "裁定员定下结果单位"],
      ["Checking the unit fits the target", "检查单位和目标是否同类"]],
    audit: [["Matching every formula input to its evidence", "逐个比对公式输入和证据"], ["Sending failed routes back for repair", "把没过的路线交回修正"]],
    final: [["Checking whether the number is already published", "检查这个数是否已经公布"], ["Writing the answer", "撰写答案"],
      ["Attaching the evidence ledger", "附上证据账本"]],
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
    const cur = stations(r).find(s => s.status !== "done");
    if (!cur || cur.key === "approve") return r.status === "planning" ? "plan" : null;
    return cur.key === "field" ? "subagents" : cur.key;
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
    if (!t) return `<p class="fine">${T("Not locked yet.", "尚未锁定。")}</p>`;
    const outs = t.outcome_type === "discrete" ? [[T("Outcomes", "结果集合"), (t.outcomes || []).map(o => esc(o.label)).join(" · ")
      || T("defined by the judge after the evidence", "取证后由裁判定义")]] : [];
    return window.VERRIER_SPEC(t, outs);
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
  function timeline(ss, live) {
    const cur = live ? ss.findIndex(s => s.status !== "done") : -1, done = ss.filter(s => s.status === "done").length;
    return `<div class="cx-tl8" style="--p:${(100 * done / ss.length).toFixed(1)}%">${ss.map((s, i) => `<div class="cx-sta st-${s.status}${i === cur ? " cur" : ""}">
      <span class="n">${String(i + 1).padStart(2, "0")}</span><h4>${T(...s.label)}</h4>
      <p><span class="lbl">${T(...(SSTAT[s.status] || [esc(s.status), esc(s.status)]))}</span>${s.detail ? `<br>${s.detail}` : ""}</p></div>`).join("")}</div>`;
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
  // v2.7e：估计值和区间后面的单位（钉死的 unit_canonical，没有就用 target.unit；结果用 API 的 estimate.unit）；空串不显示
  const unitOf = t => t ? String(t.unit_canonical || t.unit || "") : "";
  const bigUnit = u => u ? ` <span style="font-size:.4em;font-stretch:100%;letter-spacing:0">${esc(u)}</span>` : "";
  function computed(c, u) {
    if (c.mode === "discrete") return `<h3 class="cx-h">${T("Computed · outcome probabilities", "代码计算 · 各结果的概率")}</h3>
      <div class="cx-big">${esc(c.most_likely ?? "—")}</div><p class="fine">${prob(c.most_likely_prob)} · ${(c.outcomes || []).map(o => `${esc(o.label)} ${prob(o.prob)}`).join(" · ")}</p>`;
    return `<h3 class="cx-h">${T("Computed by code", "代码计算")}</h3><div class="cx-big">${fmt(c.central)}${bigUnit(u)}</div>
      <p class="fine">80% model-based [${fmt(c.p10)}, ${fmt(c.p90)}]${u ? " " + esc(u) : ""} · ${esc(c.basis)}</p>`;
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
    const keep = body.scrollTop, key = stageKey(r), cur = stations(r).find(s => s.status !== "done");
    $("cxRunTop").innerHTML = `<div id="cxStrip">${strip(r)}</div>
      ${r.error ? `<div class="cx-err">${esc(r.error)}</div>` : ""}
      <p class="cx-q">${esc(r.question)}</p><p class="fine">${T("question id", "题 id")} ${esc(r.qid)} · tag ${esc(r.tag)}${specLine(r)}</p>`;
    thinkSet($("cxThink"), key, cur ? T(...cur.label) : "");
    $("cxRunMain").innerHTML = `${picking ? gate(r) : ""}
      <h3 class="cx-h">${T("Mission timeline", "任务流程")}</h3>${timeline(stations(r), active)}
      <div class="cx-grid"><div>
        ${(r.directions || []).length ? `<h3 class="cx-h">${T("Field agents", "子 agent（各取证方向）")}</h3><div class="cx-dirs">${r.directions.map(dirCard).join("")}</div>` : ""}
        ${r.markets ? `<p class="fine">${T("Prediction markets", "预测市场")}: ${esc(r.markets.n_markets)} · ${esc(r.markets.n_points)} pts. ${esc(r.markets.note || "")}</p>` : ""}
      </div><div>
        <h3 class="cx-h">${T("Target lock", "目标锁定")}</h3>${targetTable(r.target)}
        ${r.compute ? computed(r.compute, unitOf(r.target)) : ""}
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
      : `<div class="lbl">${T("Estimate", "估计")}</div><div class="cx-big">${fmt(e.central)}${bigUnit(e.unit)}</div>
        <p class="fine">80% model-based [${fmt(e.p10)}, ${fmt(e.p90)}]${e.unit ? " " + esc(e.unit) : ""}${e.basis_text ? " · " + esc(e.basis_text) : ""}</p>`;
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
        <a class="btn primary" href="#console/evidence/${encodeURIComponent(qid)}/${encodeURIComponent(tag || "")}">${T("Evidence, methods, assumptions", "证据、方法和假设")}<span>→</span></a>
        <a class="btn" href="#console/graph/${encodeURIComponent(qid)}/${encodeURIComponent(tag || "")}">${T("Dependency graph", "依赖图")}<span>→</span></a>
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
  // 证据、方法和假设：同一份 /api/result，面板由 verrier_evidence.js 画；返回按钮回到交付页（#console/result/...）
  async function viewEvidence(qid, tag, tok) {
    code.textContent = String(qid).toUpperCase() + " · EVIDENCE";
    body.dataset.run = "";
    body.innerHTML = `<div class="cx-row"><a class="btn" href="#console/result/${encodeURIComponent(qid)}/${encodeURIComponent(tag)}"><span>←</span>${T("Back to delivered", "返回交付页")}</a></div>
      <div id="cxEv"><p class="fine">…</p></div>`;
    body.scrollTop = 0;
    const r = await api(`/api/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`);
    if (tok !== token) return;
    $("cxEv").innerHTML = window.VERRIER_EVIDENCE(r, qid, tag);
    hud({view: "EVIDENCE · " + String(qid).toUpperCase(), status: r.aborted ? "MISSION FAILED" : "ARCHIVED RESULT", phase: r.aborted ? -1 : 5, progress: 1,
      elapsed: r.wall_s || 0, done: !r.aborted, cam: `US$ ${(r.budget || {}).usd_total_assumed?.toFixed?.(3) ?? "—"}  AS OF ${r.as_of}`});
  }

  // 依赖图：/api/graph（outputs.dep_graph，和 graph.html 同一份数据），图纸由 verrier_graph.js 画；点一个节点，右栏显示它的详情
  async function viewGraph(qid, tag, tok) {
    code.textContent = String(qid).toUpperCase() + " · GRAPH";
    body.dataset.run = "";
    body.innerHTML = `<div class="cx-row"><a class="btn" href="#console/result/${encodeURIComponent(qid)}/${encodeURIComponent(tag)}"><span>←</span>${T("Back to delivered", "返回交付页")}</a>
      <span class="lbl">${esc(qid)} / ${esc(tag || "—")}</span></div><div id="cxGr"><p class="fine">…</p></div>`;
    body.scrollTop = 0;
    const g = await api(`/api/graph?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`);
    if (tok !== token) return;
    const el = $("cxGr");
    el.innerHTML = window.VERRIER_GRAPH.draw(g);
    const pick = id => {
      el.querySelectorAll(".g-n").forEach(x => x.classList.toggle("on", x.getAttribute("data-id") === id));
      $("cxGside").innerHTML = window.VERRIER_GRAPH.detail(g, id);
    };
    el.querySelector("svg").addEventListener("click", e => { const n = e.target.closest(".g-n"); if (n) pick(n.getAttribute("data-id")); });
    pick("target");
    hud({view: "GRAPH · " + String(qid).toUpperCase(), status: "ARCHIVED RESULT", phase: 5, progress: 1, elapsed: 0, done: true,
      cam: `${g.nodes.length} NODES · ${g.edges.length} EDGES`});
  }

  // ---------- 接线 ----------
  $("cxClose").onclick = leave;
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !cx.hidden) leave(); });
  addEventListener("hashchange", route);
  route();
})();
