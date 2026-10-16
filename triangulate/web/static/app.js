// triangulate-agent 本地网页：原生 JS，没有构建步骤。路由用 location.hash。
"use strict";

const $app = document.getElementById("app");
let pollTimer = null;

// ---------- 工具 ----------
function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
}
function fmt(v) {
  if (v === null || v === undefined || typeof v !== "number" || !isFinite(v)) return "—";
  if (Math.abs(v) >= 100) return Math.round(v).toLocaleString("en-US");
  return Number(v.toPrecision(4)).toLocaleString("en-US", {maximumFractionDigits: 6});
}
function pct(x, signed = true) {
  if (x === null || x === undefined || !isFinite(x)) return "—";
  const s = (x * 100).toFixed(1) + "%";
  return signed && x > 0 ? "+" + s : s;
}
function share(x) { return x === null || x === undefined ? "—" : Math.round(x * 100) + "%"; }
function prob(x) { return x === null || x === undefined || !isFinite(x) ? "—" : (x * 100).toFixed(1) + "%"; }
function yesno(b) { return b === true ? '<span class="good">是</span>' : b === false ? '<span class="bad">否</span>' : "—"; }
function resultHref(qid, tag) { return `#/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag || "")}`; }
function fileHref(qid, tag, name) {
  return `/api/file?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag || "")}&name=${name}`;
}
function link(url, text) { return url ? `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(text || url)}</a>` : "—"; }
const STATUS = {planning: "规划中", awaiting_approval: "等待确认方向", running: "运行中", done: "完成", failed: "失败", cancelled: "已取消"};
function badge(st) { return `<span class="badge b-${esc(st)}">${esc(STATUS[st] || st)}</span>`; }
const KIND = {backtest: "回测", web: "网页运行", ask: "命令行 --ask"};

async function api(path, opts) {
  const r = await fetch(path, opts);
  let body = null;
  try { body = await r.json(); } catch (e) { /* 非 JSON */ }
  if (!r.ok) throw new Error((body && body.detail) || `HTTP ${r.status}`);
  return body;
}
function post(path, data) {
  return api(path, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data || {})});
}
function showError(e) { $app.insertAdjacentHTML("afterbegin", `<div class="err">${esc(e.message || e)}</div>`); }

// ---------- 路由 ----------
function route() {
  if (pollTimer) { clearTimeout(pollTimer); pollTimer = null; }
  const h = location.hash || "#/";
  const [path, qs] = h.slice(1).split("?");
  const params = new URLSearchParams(qs || "");
  document.querySelectorAll("header nav a").forEach(a => a.classList.toggle("on",
    (a.dataset.nav === "home" && (path === "/" || path.startsWith("/run/"))) ||
    (a.dataset.nav === "saved" && (path === "/saved" || path === "/result")) || (a.dataset.nav === "backtests" && path === "/backtests")));
  const page = path === "/saved" ? pageSaved() : path === "/backtests" ? pageBacktests() :
    path === "/result" ? pageResult(params.get("qid"), params.get("tag") || "") :
    path.startsWith("/run/") ? pageRun(decodeURIComponent(path.slice(5))) : pageHome();
  page.catch(e => { $app.innerHTML = ""; showError(e); });
}
window.addEventListener("hashchange", route);
window.addEventListener("load", route);

// ---------- 首页：发起运行 ----------
async function pageHome() {
  $app.innerHTML = `<h1>问一个拿不到的数</h1>
  <div class="card">
    <p class="muted">agent 先钉死目标、列出取证方向，然后停下来等你确认；确认后并行取证、裁判、代码计算、给出估计。
    需要 key 文件（环境变量 TRIANGULATE_KEY_FILE）和网络。每次运行的花费上限是 $1.00（含按假设单价记的搜索费）。</p>
    <label>问题<br><textarea id="q" placeholder="How many ... in ...?"></textarea></label>
    <p><label>as_of（站在哪一天）：<input type="date" id="asof"></label>
    <span class="muted">留空 = 今天（真实使用，可以用今天的网页）；更早的日期 = 回测模式，只用不晚于 as_of 的存档快照。</span></p>
    <button id="go">开始</button> <span id="msg" class="muted"></span>
  </div>
  <h2>这次服务启动后的网页运行</h2><div id="runs" class="muted">加载中…</div>`;
  document.getElementById("go").onclick = async () => {
    const btn = document.getElementById("go");
    btn.disabled = true;
    try {
      const r = await post("/api/runs", {question: document.getElementById("q").value, as_of: document.getElementById("asof").value || null});
      location.hash = "#/run/" + r.id;
    } catch (e) { document.getElementById("msg").innerHTML = `<span class="bad">${esc(e.message)}</span>`; btn.disabled = false; }
  };
  const d = await api("/api/runs");
  document.getElementById("runs").innerHTML = d.runs.length ? `<table><tr><th>开始时间</th><th>问题</th><th>as_of</th><th>状态</th><th></th></tr>
    ${d.runs.map(r => `<tr><td>${esc(r.created_at)}</td><td>${esc(r.question)}</td><td>${esc(r.as_of)}</td><td>${badge(r.status)}</td>
    <td><a href="#/run/${esc(r.id)}">进度</a>${r.result ? ` · <a href="${resultHref(r.result.qid, r.result.tag)}">结果</a>` : ""}</td></tr>`).join("")}</table>
    <p class="muted small">同时最多 ${d.max_active} 个没结束的运行。</p>` : "还没有。";
}

// ---------- 运行进度 ----------
const DSTATUS = {queued: "排队", searching: "搜索中", fetching: "取页中", extracting: "抽取中", done: "完成", stopped: "中止"};
function dirStatus(d) {
  let s = DSTATUS[d.status] || d.status;
  if (d.status === "fetching" || d.status === "extracting") s += `：${d.pages_done}/${d.n_urls ?? "?"} 个网址`;
  if (d.status === "done" || d.status === "stopped") {
    s += d.n_kept !== null && d.n_kept !== undefined ? `：保留 ${d.n_kept} 个点` : `：${d.n_points ?? d.n_verified} 个点通过代码核对`;
    if (d.stopped) s += `（${esc(d.stopped)}）`;
  }
  return s;
}
function targetTable(t) {
  if (!t) return '<p class="muted">还没有。</p>';
  const rows = [["what", "是什么"], ["unit", "单位"], ["period_start", "期间开始"], ["period_end", "期间结束"], ["publisher", "谁公布"],
    ["cadence", "公布节奏"], ["caveats", "注意"]];
  const outs = t.outcome_type === "discrete" ? `<tr><th>结果类型</th><td>离散：${(t.outcomes || []).map(o =>
    `${esc(o.label)}${o.value === null || o.value === undefined ? "" : `（${fmt(o.value)}）`}`).join("；")}</td></tr>` : "";
  return `<table>${rows.map(([k, l]) => `<tr><th style="width:110px">${l}</th><td>${esc(t[k])}</td></tr>`).join("")}${outs}</table>`;
}

function schedule(id, ms) {
  if (pollTimer) clearTimeout(pollTimer);
  pollTimer = setTimeout(() => pageRun(id).catch(showError), ms);
}
function wireCancel(id) {
  const c = document.getElementById("cancel");
  if (c) c.onclick = async () => {
    if (!confirm("取消这次运行？已经花掉的钱不会退。")) return;
    try { await post(`/api/runs/${encodeURIComponent(id)}/cancel`); pageRun(id).catch(showError); } catch (e) { showError(e); }
  };
}

async function pageRun(id) {
  const r = await api("/api/runs/" + encodeURIComponent(id));
  if (location.hash !== "#/run/" + encodeURIComponent(id) && location.hash !== "#/run/" + id) return;  // 已经换页了
  const active = ["planning", "awaiting_approval", "running"].includes(r.status);
  const picking = r.status === "awaiting_approval";
  if (picking && document.getElementById("approve")) {
    // 正在勾选方向：只刷新上面的状态行，不重画勾选框
    document.getElementById("hdr").innerHTML = runHeader(r);
    wireCancel(id);
    schedule(id, 3000);
    return;
  }
  $app.innerHTML = `<h1>运行进度</h1><div id="hdr">${runHeader(r)}</div>
  ${r.error ? `<div class="err">${esc(r.error)}</div>` : ""}
  ${r.result ? `<div class="card"><b>已写盘：</b><a href="${resultHref(r.result.qid, r.result.tag)}">查看结果</a>
     <span class="muted">（results/agent/${esc(r.result.qid)}/${esc(r.result.tag)}/）</span></div>` : ""}
  <h2>钉死的目标</h2>${targetTable(r.target)}
  ${picking ? approvalBlock(r) : ""}
  <h2>阶段</h2><table><tr><th>阶段</th><th>状态</th><th>说明</th></tr>
  ${r.stages.map(s => `<tr><td>${esc(s.label)}</td><td class="st-${esc(s.status)}">${{done: "完成", running: "进行中", waiting: "等待", pending: "未开始"}[s.status] || esc(s.status)}</td>
  <td>${esc(s.detail)}</td></tr>`).join("")}</table>
  ${r.directions.length ? `<h2>各方向（子 agent）</h2><table><tr><th>方向</th><th>轮</th><th>类别</th><th>假设</th><th>状态</th>
  <th class="num">快照 / live / 丢弃</th><th class="num">抽取页</th><th class="num">核对通过的点</th></tr>
  ${r.directions.map(d => `<tr><td>${esc(d.id)}</td><td>${d.round}</td><td>${esc(d.category)}</td><td class="small">${esc(d.hypothesis)}</td>
  <td style="white-space:nowrap">${dirStatus(d)}</td><td class="num">${d.pages.snapshot} / ${d.pages.live_dated} / ${d.pages.dropped}</td>
  <td class="num">${d.n_extracted}</td><td class="num">${d.n_points ?? d.n_verified}</td></tr>`).join("")}</table>
  ${r.markets ? `<p class="muted">预测市场工具：${r.markets.n_markets} 个市场，${r.markets.n_points} 个点。${esc(r.markets.note || "")}</p>` : ""}` : ""}
  ${r.compute ? (r.compute.mode === "discrete" ? `<h2>计算结果（离散目标）</h2><p>最可能的结果 <b>${esc(r.compute.most_likely ?? "—")}</b>（${prob(r.compute.most_likely_prob)}）：
     ${(r.compute.outcomes || []).map(o => `${esc(o.label)} ${prob(o.prob)}`).join("；")}</p>` :
    `<h2>计算结果</h2><p>估计 <b>${fmt(r.compute.central)}</b>，80% 区间 [${fmt(r.compute.p10)}, ${fmt(r.compute.p90)}]（${esc(r.compute.basis)}）</p>`) : ""}
  ${r.calls && Object.keys(r.calls).length ? `<details><summary>calls.jsonl 里的调用（按 role）</summary><p class="small">
     ${Object.entries(r.calls).map(([k, v]) => `${esc(k)} × ${v}`).join("；")}</p></details>` : ""}`;
  if (picking) wireApproval(r);
  wireCancel(id);
  if (active) schedule(id, picking ? 3000 : 2000);
}
function runHeader(r) {
  const active = ["planning", "awaiting_approval", "running"].includes(r.status);
  return `<div class="card"><div>${badge(r.status)} ${r.cancel_requested ? '<span class="badge">已请求取消</span>' : ""}
  &nbsp; 已用时 <b>${fmt(r.elapsed_s)}</b> 秒 · 已花 <b>$${r.usd === null ? "—" : r.usd.toFixed(3)}</b>
  ${r.usd_cap ? ` / 上限 $${r.usd_cap.toFixed(2)}` : ""}（含按假设单价记的搜索费） · as_of ${esc(r.as_of)}
  ${active ? ' &nbsp; <button class="secondary" id="cancel">取消运行</button>' : ""}</div>
  <p>${esc(r.question)}</p><p class="muted small">题 id ${esc(r.qid)} · tag ${esc(r.tag)}</p></div>`;
}
function approvalBlock(r) {
  return `<h2>确认方向</h2><div class="card warn"><p>agent 停在这里等你确认。不勾的方向不会跑（走图里已有的「改方向列表」路径，保留的方向会重新编号 d1..dK）。</p>
  ${r.directions_proposed.map(d => `<div class="dirpick"><input type="checkbox" class="keep" value="${esc(d.id)}" checked>
    <div><b>${esc(d.id)}</b> <span class="badge">${esc(d.category)}</span> <span class="muted">预期信息量 ${esc(d.expected_information)}/5</span>
    <div>${esc(d.perspective)}</div><div><b>假设：</b>${esc(d.hypothesis)}</div><div class="muted small"><b>要找的数据：</b>${esc(d.data_to_find)}</div></div></div>`).join("")}
  <p><button id="approve">批准勾选的方向</button></p></div>`;
}
function wireApproval(r) {
  document.getElementById("approve").onclick = async () => {
    const ids = [...document.querySelectorAll("input.keep")].filter(x => x.checked).map(x => x.value);
    const all = ids.length === r.directions_proposed.length;
    try {
      await post(`/api/runs/${encodeURIComponent(r.id)}/approve`, all ? {} : {keep_direction_ids: ids});
      if (pollTimer) clearTimeout(pollTimer);
      $app.innerHTML = "";
      pageRun(r.id).catch(showError);
    } catch (e) { showError(e); }
  };
}

// ---------- 已保存的运行 ----------
async function pageSaved() {
  const d = await api("/api/saved");
  $app.innerHTML = `<h1>已保存的运行</h1><p class="muted">results/agent/ 下所有带 state.json 的运行（回测、命令行 --ask、网页运行），按题 id 和 tag 排列。离线可看。</p>
  <table><tr><th>题 id</th><th>tag</th><th>类型</th><th>as_of</th><th class="num">估计</th><th class="num">80% 区间</th><th class="num">假设占比</th>
  <th class="num">花费</th><th class="num">用时</th><th>开始（UTC）</th><th></th></tr>
  ${d.runs.map(r => `<tr><td>${esc(r.qid)}</td><td>${esc(r.tag || "(无)")}</td><td>${esc(KIND[r.kind] || r.kind)}</td><td>${esc(r.as_of)}</td>
  ${r.mode === "discrete" ? `<td class="num">${esc(r.most_likely ?? "—")}<div class="muted small">离散：最可能 ${prob(r.most_likely_prob)}</div></td><td class="num">—</td>` :
  `<td class="num">${fmt(r.estimate)}</td><td class="num">${r.estimate === null ? "—" : `[${fmt(r.p10)}, ${fmt(r.p90)}]`}</td>`}
  <td class="num">${share(r.share)}${r.share > 0.5 ? ' <span class="badge b-warn">假设为主</span>' : ""}</td>
  <td class="num">${r.usd === null || r.usd === undefined ? "—" : "$" + r.usd.toFixed(3)}</td><td class="num">${r.wall_s ? Math.round(r.wall_s / 60) + " 分钟" : "—"}</td>
  <td class="small">${esc(r.started_at)}</td><td><a href="${resultHref(r.qid, r.tag)}">查看</a></td></tr>`).join("")}</table>`;
}

// ---------- 结果页 ----------
function evidenceText(e) {
  if (!e) return "";
  if (e.kind === "assumption") return `<span class="k-assumption">假设 ${esc(e.id)}</span>：${esc(e.name)} = ${fmt(e.value)}${e.unit === "%" ? "%" : " " + esc(e.unit)}`;
  if (e.kind === "constant") return `<span class="k-constant">常数 ${esc(e.id)}（代码给）</span>`;
  if (e.kind === "unknown") return `<span class="bad">${esc(e.id)}：未知 id</span>`;
  return `<span class="k-point">数据点 ${esc(e.id)}</span>：${esc(e.name)} = ${fmt(e.value)} ${esc(e.unit)}，期间 ${esc(e.period_start || "?")}..${esc(e.period_end || "?")}，
    来源 ${link(e.source_url, e.domain)}${e.snapshot_url ? `（${link(e.snapshot_url, "快照 " + e.snapshot_date)}）` : e.page_date ? `（${esc(e.via)} ${esc(e.page_date)}）` : ""}`;
}
function methodRows(ms) {
  const ST = {computed: "", failed: '<span class="bad">失败</span>', excluded_by_input_audit: '<span class="bad">输入核对不通过，未计算</span>'};
  return ms.map(m => `<tr><td><b>${esc(m.id)}</b>${m.label && m.label !== m.id ? `<div class="muted small">裁判 id ${esc(m.label)}</div>` : ""}</td>
  <td>${esc(m.method)}<div>${ST[m.status] || ""}</div></td><td><code>${esc(m.formula)}</code>
  ${m.target_series ? `<div class="small muted">目标序列：${Object.entries(m.target_series).map(([y, v]) => `${y}: ${fmt(v)}`).join("，")}</div>` : ""}
  ${m.signal_series ? `<div class="small muted">信号序列：${Object.entries(m.signal_series).map(([y, v]) => `${y}: ${fmt(v)}`).join("，")}</div>` : ""}</td>
  <td><ul class="inputs">${(m.inputs || []).map(i => `<li><b>${esc(i.name)}</b> = ${esc(i.id)}${i.p10 !== undefined && i.p10 !== null && i.p10 !== i.p90 ? `
    <span class="muted small">采样 P10..P90 ${fmt(i.p10)}..${fmt(i.p90)}</span>` : ""}${i.prob !== undefined && i.prob !== null ? ` <span class="muted small">概率 ${prob(i.prob)}</span>` : ""}
    <div class="small">role：${esc(i.role) || '<span class="bad">（没写）</span>'}</div>
    <div class="small">证据：${evidenceText(i.evidence)}</div></li>`).join("")}${m.remainder ? `<li class="small">余下的结果 <b>${esc(m.remainder)}</b> = 1 − 其余之和（代码算）</li>` : ""}</ul></td>
  <td class="num">${m.distribution ? Object.entries(m.distribution).map(([k, v]) => `<div class="small">${esc(k)}：${prob(v)}</div>`).join("") : fmt(m.estimate)}</td>
  <td class="num">${m.status === "computed" ? Math.round(100 * (m.weight || 0)) + "%" : "—"}
  ${m.weight_basis ? `<div class="muted small">${esc(m.weight_basis)}</div>` : ""}</td>
  <td class="num">${m.status === "computed" ? share(m.assumption_share) : "—"}</td>
  <td class="small">${(m.backtest || []).length ? "回测 " + m.backtest.map(b => `${b.year}: ${pct(Math.exp(b.log_err) - 1)}`).join("，") + "<br>" : ""}
  ${m.error ? `<span class="bad">${esc(m.error)}</span>` : ""}${(m.notes || []).length ? `<div class="muted">${m.notes.map(esc).join("<br>")}</div>` : ""}</td></tr>`).join("");
}
function pointTable(ps, withReason) {
  if (!ps.length) return '<p class="muted">没有。</p>';
  return `<table><tr><th>id</th><th>方向</th><th>名称</th><th class="num">值</th><th>单位</th><th>期间</th><th>来源</th><th>快照 / 页面日期</th>
  ${withReason ? "<th>裁判的理由</th>" : "<th>被哪些方法用</th>"}<th>原文</th></tr>
  ${ps.map(p => `<tr><td>${esc(p.id)}</td><td>${esc(p.direction_id)}</td><td>${esc(p.name)}</td><td class="num">${fmt(p.value)}</td><td>${esc(p.unit)}</td>
  <td class="small">${esc(p.period_start || "?")}..${esc(p.period_end || "?")}</td><td>${link(p.source_url, p.domain)}</td>
  <td class="small">${p.snapshot_url ? link(p.snapshot_url, p.snapshot_date) : esc((p.via || "") + " " + (p.page_date || ""))}</td>
  <td class="small">${withReason ? esc(p.judge_reason || p.ablation_excluded || "") : esc((p.used_by || []).join(", "))}</td>
  <td class="quote" title="${esc(p.quote)}">${esc((p.quote || "").slice(0, 160))}</td></tr>`).join("")}</table>`;
}

async function pageResult(qid, tag) {
  const r = await api(`/api/result?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`);
  const e = r.estimate || {}, sh = r.assumption_share || {}, o = r.official, b = r.budget || {};
  const ov = sh.overall;
  const evid = r.evidence;
  $app.innerHTML = `<h1>${esc(r.qid)} <span class="muted">/ ${esc(r.tag || "(无 tag)")}</span> <span class="badge">${esc(KIND[r.kind] || r.kind)}</span></h1>
  <p>${esc(r.question)}</p>
  <p class="muted">as_of ${esc(r.as_of)} · 模型 ${esc(r.model)} · 开始 ${esc(r.started_at)} · 用时 ${r.wall_s ? (r.wall_s / 60).toFixed(1) + " 分钟" : "—"}
   · 花费 ${b.usd_total_assumed !== undefined ? "$" + b.usd_total_assumed.toFixed(3) : "—"}（token $${(b.usd_tokens || 0).toFixed(3)} + 假设的搜索费 $${(b.usd_search_fee_assumed || 0).toFixed(3)}）
   · <a href="${fileHref(r.qid, r.tag, "graph.html")}" target="_blank">依赖图 graph.html</a>（需要联网加载 vis-network）
   · <a href="${fileHref(r.qid, r.tag, "ledger.md")}" target="_blank">证据账本 ledger.md</a></p>
  ${r.aborted ? `<div class="err">中止：${esc(r.aborted)}</div>` : ""}
  ${r.discrete ? discreteBlock(r.discrete, o) : `<div class="row">
    <div class="card"><div class="muted">估计</div><div class="big">${fmt(e.central)}</div>
      <div>80% 区间 [${fmt(e.p10)}, ${fmt(e.p90)}]</div><div class="muted small">区间依据 ${esc(e.basis)}${e.basis_text ? "：" + esc(e.basis_text) : ""} · 加权规则 ${esc(e.weight_rule)}</div></div>
    ${o ? `<div class="card"><div class="muted">官方值（只用于打分，agent 看不到）</div><div class="big">${fmt(o.answer_value)}</div>
      <div>误差 <b>${pct(o.pct_err)}</b> · 80% 区间盖住：${yesno(o.covered_80)}</div>
      <div class="muted small">公布 ${esc(o.released)} · ${link(o.source, "来源")}</div></div>` : ""}
    <div class="card ${sh.warning ? "warn" : ""}"><div class="muted">证据 vs 假设</div>
      ${ov === null || ov === undefined ? '<div class="big">—</div><div class="muted">没有算出估计</div>' : `
      <div class="big">证据 ${share(1 - ov)} · 假设 ${share(ov)}</div>
      <div class="bar"><div class="ev" style="width:${100 * (1 - ov)}%"></div><div class="as" style="width:${100 * ov}%"></div></div>
      ${sh.warning ? `<div class="bad"><b>注意：这个估计的不确定性主要来自假设（超过 ${share(sh.threshold)}），不是观测证据。</b></div>` : ""}
      <div class="small">各方法：${Object.entries(sh.per_method || {}).map(([k, v]) => `${esc(k)} ${share(v.share)}（权重 ${Math.round(100 * v.weight)}%）`).join("，")}</div>`}
      <details><summary class="small">怎么算的</summary><p class="small">${esc(sh.definition)}</p></details></div>
  </div>`}
  <h2>最终答案</h2><pre class="answer">${esc(r.final_text || "（没有）")}</pre>
  <h2>钉死的目标</h2>${targetTable(r.target)}
  <h2>方法（代码计算）</h2><p class="muted small">裁判从第 ${esc(r.methods_from_round ?? "?")} 轮给出的方法。权重为 0 的方法没有进入合并。</p>
  <table><tr><th>id</th><th>方法</th><th>公式</th><th>输入（role 和它指向的证据）</th><th class="num">估计</th><th class="num">权重</th><th class="num">假设占比</th><th>回测 / 错误</th></tr>
  ${methodRows(r.methods)}</table>
  ${r.audit_errors.length ? `<p class="bad">输入核对本身出错（没有拦方法）：${r.audit_errors.map(esc).join("；")}</p>` : ""}
  ${r.repairs.map(p => `<h3>裁判第 ${esc(p.round)} 轮的修正轮</h3><div class="card"><b>交回裁判的问题：</b><ul>${p.errors.map(x => `<li class="small">${esc(x)}</li>`).join("")}</ul>
    ${p.previous_methods.length ? `<div class="small"><b>修正前的方法：</b>${p.previous_methods.map(esc).join("；")}</div>` : ""}
    ${p.error ? `<div class="bad">修正调用失败：${esc(p.error)}</div>` : ""}
    ${p.errors_after ? `<div class="small"><b>修正后仍有的问题：</b>${p.errors_after.length ? p.errors_after.map(esc).join("；") : "无"}</div>` : ""}
    ${p.reverted ? `<div class="bad small">${esc(p.reverted)}</div>` : ""}</div>`).join("")}
  <h2>假设</h2>
  ${r.assumptions.length ? `<table><tr><th>id</th><th>名称</th><th class="num">值</th><th class="num">裁判给的范围</th><th class="num">代码采样范围（放宽后）</th><th>单位</th>
  <th>理由</th><th>适用条件</th><th>什么会推翻它</th><th>被谁用</th></tr>
  ${r.assumptions.map(a => `<tr><td>${esc(a.id)}</td><td>${esc(a.name)}</td><td class="num">${fmt(a.value)}${a.is_pct ? "%" : ""}</td>
  <td class="num">${fmt(a.low)}..${fmt(a.high)}</td><td class="num">${fmt(a.p10_used)}..${fmt(a.p90_used)}${a.is_pct ? "%" : ""}${a.widened_by_floor ? '<div class="muted small">已放宽</div>' : ""}</td>
  <td>${esc(a.unit)}</td><td class="small">${esc(a.rationale)}</td><td class="small">${esc(a.applies_when)}</td><td class="small">${esc(a.falsified_by)}</td>
  <td>${esc((a.used_by || []).join(", ") || "没用上")}</td></tr>`).join("")}</table>` : '<p class="muted">没有保留的假设。</p>'}
  ${r.assumptions_rejected.length ? `<details><summary>被代码拒绝的假设（${r.assumptions_rejected.length}）</summary><ul>${r.assumptions_rejected.map(a =>
    `<li class="small">${esc(a.id || a.raw)} ${esc(a.name || "")}：${esc(a.reason)}</li>`).join("")}</ul></details>` : ""}
  <h2>证据</h2>
  <p class="muted">页面：快照 ${evid.pages.snapshot || 0} · live ${evid.pages.live_dated || 0} · 丢弃 ${evid.pages.dropped || 0}。
  代码核对丢掉的点：${Object.entries(evid.dropped_by_code).map(([k, v]) => `${esc(k)} ×${v}`).join("；") || "无"}</p>
  <h3>保留的点（${evid.kept.length}）</h3>${pointTable(evid.kept, false)}
  <details><summary>裁判丢弃的点（${evid.discarded.length}）</summary>${pointTable(evid.discarded, true)}</details>
  ${evid.ablation_excluded.length ? `<details><summary>消融排除的点（${evid.ablation_excluded.length}）</summary>${pointTable(evid.ablation_excluded, true)}</details>` : ""}
  <h2>泄漏审计</h2>${leakTable(r.leakage)}
  <details><summary>方向（${r.directions.length}）</summary><table>${r.directions.map(d => `<tr><td>${esc(d.id)}</td><td>${esc(d.category)}</td>
    <td>${esc(d.perspective)}</td><td class="small">${esc(d.hypothesis)}</td></tr>`).join("")}</table></details>`;
}
function discreteBlock(d, o) {
  // 离散目标：结果概率表（agent 的等权平均 + 每个方法 + Jev 对照臂，Jev 不并入 agent 的答案）
  const j = d.jev, jok = j && j.status === "ok";
  const jnote = !j ? "没有运行" : jok ? `${esc(j.model)} · 选择 ${esc(j.choice)} · confidence ${fmt(j.confidence)} · 输入 token ${esc((j.usage || {}).input_tokens)}
     · 输出 token ${esc((j.usage || {}).output_tokens)}${j.usd_estimated !== null && j.usd_estimated !== undefined ? ` · 估算费用 $${j.usd_estimated.toFixed(6)}` : ""}
     · 简报 ${esc(j.n_points_in_brief)} 个保留的点` : `${esc(j.status === "not_configured" ? "未配置（没设 TYPESAFE_KEY_FILE）" : j.status)}${j.error ? "：" + esc(j.error) : ""}`;
  return `<div class="row"><div class="card"><div class="muted">离散目标：最可能的结果</div><div class="big">${esc(d.most_likely ?? "—")}</div>
    <div>概率 ${prob(d.most_likely_prob)} · ${esc(d.methods.length)} 个方法等权平均（${esc(d.weight_rule)}）</div>
    <div class="muted small">用到假设的方法的权重 ${share(d.assumption_weight_share)}</div></div>
    ${o ? `<div class="card"><div class="muted">真实结果（只用于打分，agent 看不到）</div><div class="big">${esc(o.true_outcome ?? fmt(o.answer_value))}</div>
      <div>真实结果得到的概率 <b>${prob(o.prob_true)}</b> · Brier ${fmt(o.brier)} · 最可能的结果对不对：${yesno(o.most_likely_correct)}</div></div>` : ""}</div>
  <table><tr><th>结果</th><th class="num">数值</th><th class="num">agent（等权平均）</th>${d.methods.map(m => `<th class="num">${esc(m)}</th>`).join("")}<th class="num">Jev（对照，不并入）</th></tr>
  ${d.outcomes.map(x => `<tr><td>${esc(x.label)}</td><td class="num">${fmt(x.value)}</td><td class="num"><b>${prob(x.prob)}</b></td>
    ${d.methods.map(m => `<td class="num">${prob((x.per_method || {})[m])}</td>`).join("")}<td class="num">${prob(x.jev)}</td></tr>`).join("")}</table>
  <p class="muted small">Jev 对照臂（TypeSafe 官方端点，代码把保留的数据点写成简报、问一次）：${jnote}</p>
  ${d.jev_brief ? `<details><summary class="small">发给 Jev 的简报</summary><pre class="answer small">${esc(d.jev_brief)}</pre></details>` : ""}`;
}
function leakTable(l) {
  const rows = [["页面（快照 / live / 丢弃）", `${l.pages_total ?? "—"}（${l.pages_snapshot ?? "—"} / ${l.pages_live_dated ?? "—"} / ${l.pages_dropped ?? "—"}）`],
    ["哨兵命中（整页排除）", l.sentinel_hits ?? "—"], ["期间或页面日期晚于 as_of 的数据点", l.points_dated_after_as_of ?? "—"],
    ["时间戳晚于 as_of 的快照", l.snapshots_after_as_of ?? "—"], ["searcher 查询词里出现登记值", l.searcher_queries_containing_registered_values ?? "—"],
    ["假设里出现登记值", l.assumptions_containing_registered_values ?? "—"], ["送给 extractor 的正文里晚于 as_of 的日期（页数）", l.late_dates_in_text_sent ?? "—"]];
  return `<table>${rows.map(([k, v]) => `<tr><th style="width:360px">${k}</th><td>${esc(v)}</td></tr>`).join("")}</table>
  <p class="muted small">登记值 = 回测题的真值和 as_of 之后公布的已知官方值；网页运行没有登记值，这几项恒为 0，不说明什么。</p>
  ${l.residual_risks.length ? `<details><summary>残余风险（${l.residual_risks.length}）</summary><ul>${l.residual_risks.map(x => `<li class="small">${esc(x)}</li>`).join("")}
  ${l.by_construction.map(x => `<li class="small">${esc(x)}</li>`).join("")}</ul></details>` : ""}`;
}

// ---------- 回测 ----------
function btTable(rows) {
  const arm = a => a ? `${fmt(a.estimate)}<div class="small ${Math.abs(a.pct_err) > 0.2 ? "bad" : ""}">${pct(a.pct_err)}</div>` : "—";
  return `<table><tr><th>题</th><th>tag</th><th>as_of</th><th class="num">官方值</th><th class="num">agent 估计</th><th class="num">误差</th>
  <th class="num">80% 区间</th><th>盖住</th><th class="num">假设占比</th><th class="num">直接问（naive）</th><th class="num">不联网结构化</th><th></th></tr>
  ${rows.map(r => !r.found ? `<tr><td>${esc(r.qid)}</td><td>${esc(r.tag)}</td><td colspan="10" class="bad">summary_${esc(r.tag)}.json 里没有这题</td></tr>` :
  `<tr><td>${esc(r.qid)}</td><td>${esc(r.tag)}</td><td>${esc(r.as_of)}</td><td class="num">${fmt(r.answer_value)}</td>
  <td class="num"><b>${fmt(r.estimate)}</b></td><td class="num ${Math.abs(r.pct_err) > 0.2 ? "bad" : ""}">${pct(r.pct_err)}</td>
  <td class="num small">${r.estimate === null ? "—" : `[${fmt(r.p10)}, ${fmt(r.p90)}]`}</td><td>${yesno(r.covered_80)}</td>
  <td class="num">${share(r.share)}${r.share_warning ? '<div><span class="badge b-warn">注意：估计主要靠假设</span></div>' : ""}</td>
  <td class="num">${arm(r.naive)}</td><td class="num">${arm(r.structured)}</td>
  <td><a href="${resultHref(r.qid, r.tag)}">详情</a></td></tr>`).join("")}</table>`;
}
// ---------- 展示集（EVAL_SHOWCASE_PLAN.md） ----------
function scArm(a, scored) {
  if (!a) return "—";
  if (a.estimate === null || a.estimate === undefined) return `<span class="bad">没有估计</span>${a.status ? `<div class="small muted">${esc(a.status)}</div>` : ""}`;
  return `${fmt(a.estimate)}${scored ? `<div class="small ${Math.abs(a.pct_err) > 0.2 ? "bad" : ""}">${pct(a.pct_err)}</div>` : ""}`;
}
function scMarket(m) {
  if (!m) return "—";
  return m.price_points && m.price_points.length ? m.price_points.map(x => `${esc(x.name)}：${prob(x.value)}`).join("<br>")
    : `<span class="muted small">无匹配市场${m.note ? "（" + esc(m.note) + "）" : ""}</span>`;
}
function scInterval(a) { return !a || a.estimate === null || a.estimate === undefined ? "—" : `[${fmt(a.p10)}, ${fmt(a.p90)}]`; }
function scMed(x) { return x === "inf" ? "∞（过半没有估计）" : x === null || x === undefined ? "—" : Number(x).toFixed(4); }
function scBlock(s) {
  if (!s) return '<p class="muted">还没有展示集汇总（.venv/Scripts/python.exe -m triangulate showcase）。</p>';
  const pub = s.rows.filter(r => r.kind === "published"), un = s.rows.filter(r => r.kind === "unpublished"), c = s.criteria || {};
  const tf = b => b === true ? '<span class="good">满足</span>' : b === false ? '<span class="bad">不满足</span>' : "待定";
  return `<h3>已公布题（回测：只用 as_of 之前的 Wayback 快照）</h3>
  <table><tr><th>题</th><th>as_of</th><th class="num">官方值</th><th class="num">agent 估计</th><th class="num">80% 区间</th><th>盖住</th>
  <th class="num">直接问（naive）</th><th class="num">不联网结构化</th><th>结构化区间盖住</th><th>预测市场</th><th class="num">agent 成本 / 用时</th><th></th></tr>
  ${pub.map(r => `<tr><td>${esc(r.qid)}</td><td>${esc(r.as_of)}</td><td class="num">${fmt(r.answer_value)}<div class="muted small">公布 ${esc(r.released)}</div></td>
  <td class="num"><b>${scArm(r.agent, true)}</b></td><td class="num small">${scInterval(r.agent)}</td><td>${yesno(r.agent && r.agent.covered_80)}</td>
  <td class="num">${scArm(r.naive, true)}</td><td class="num">${scArm(r.structured, true)}</td><td>${yesno(r.structured && r.structured.covered_80)}</td>
  <td class="small">${scMarket(r.agent && r.agent.markets)}</td>
  <td class="num small">${r.agent ? `$${fmt(r.agent.usd_total_assumed)} / ${fmt(r.agent.wall_s)} s` : "—"}</td>
  <td>${r.agent ? `<a href="${resultHref(r.qid, r.tag)}">详情</a>` : ""}</td></tr>`).join("")}</table>
  <h3>未公布题（真实使用：as_of = 运行当天，公布后再打分）</h3>
  <table><tr><th>题</th><th>as_of</th><th>预计公布</th><th class="num">agent 估计</th><th class="num">80% 区间</th><th class="num">直接问（naive）</th>
  <th class="num">不联网结构化</th><th class="num">联网直接答（预注册）</th><th class="num">联网直接答（补充，不计分）</th><th>预测市场</th><th class="num">agent 成本 / 用时</th><th></th></tr>
  ${un.map(r => `<tr><td>${esc(r.qid)}</td><td>${esc(r.as_of)}</td><td>${esc(r.expected_release)}</td>
  <td class="num"><b>${scArm(r.agent, false)}</b></td><td class="num small">${scInterval(r.agent)}</td><td class="num">${scArm(r.naive, false)}</td>
  <td class="num">${scArm(r.structured, false)}<div class="muted small">${scInterval(r.structured)}</div></td>
  <td class="num">${scArm(r.search_direct, false)}</td><td class="num">${scArm(r.search_direct_supp, false)}</td>
  <td class="small">${scMarket(r.agent && r.agent.markets)}</td>
  <td class="num small">${r.agent ? `$${fmt(r.agent.usd_total_assumed)} / ${fmt(r.agent.wall_s)} s` : "—"}</td>
  <td>${r.agent ? `<a href="${resultHref(r.qid, r.tag)}">详情</a>` : ""}</td></tr>`).join("")}</table>
  <div class="card small"><b>预注册的成功标准（${c.final ? "最终" : `中期：${esc(c.n_scored)} / ${esc(c.n_questions)} 题已打分`}）</b><br>
  ${c.final ? "" : "标准按全部 4 题定义；下面的数只算已打分的题，判定要等未公布题公布。<br>"}
  1. agent 中位百分比误差绝对值 ≤ 20%：${c.c1_agent_median_abs_pct_err === "inf" ? "∞" : pct(c.c1_agent_median_abs_pct_err, false)} → ${tf(c.c1_pass)}<br>
  2. agent 的中位 |log10 误差| 低于直接问和结构化：agent ${scMed((c.median_abs_log10 || {}).agent)} · 直接问 ${scMed((c.median_abs_log10 || {}).naive)}
   · 结构化 ${scMed((c.median_abs_log10 || {}).structured)} → ${tf(c.c2_vs_naive_structured_pass)}；未公布题上低于联网直接答（预注册那次）：${tf(c.c2_vs_search_direct_pass)}<br>
  两条都满足 = 达标：${c.final ? tf(c.met) : "待定（未公布题公布后才能判定）"}。n = 4，只能说明方向，不是统计结论。</div>
  <p class="muted small">联网直接答（同一模型 + 服务端 web_search，一次调用）预注册那次两题都在 max_tokens = 4096 处截断、没有给出数字，按规则记为失败；
  补充运行只把 max_tokens 提到 32000，不在预注册里、不进成功标准。「去年同月」不再是对照，不显示。详见 SHOWCASE.md。</p>`;
}
async function pageBacktests() {
  const d = await api("/api/backtests");
  $app.innerHTML = `<h1>回测</h1>
  <h2>开发集（4 题，每题取最新的 agent 版本）</h2>
  <p class="muted">v2.1 的几处修正是看着这 4 题的失败做出来的，所以这里的成绩是开发数据，不能当测试成绩（EVAL_TEST_PLAN.md）。</p>${btTable(d.dev)}
  <h2>留出测试（test1，3 题）</h2>
  <p class="muted">代码在跑之前定型（v2.1c），每题一次，跑完不为这三题改代码。n = 3，只能说明方向，不是统计结论。</p>${btTable(d.test)}
  <h2>展示集（${esc((d.showcase || {}).tag || "showcase1")}，4 题，2026-10-16 预注册）</h2>
  <p class="muted">题目、arm、成功标准在任何模型调用之前提交（tag showcase-prereg）；每题每个 arm 只跑一次，全部报告。</p>${scBlock(d.showcase)}
  <div class="card small"><b>假设占比</b>：${esc(d.share_definition)} 超过 ${share(d.share_threshold)} 的行标「注意：估计主要靠假设」：
  这次估计的不确定性主要来自裁判提出的假设输入，而不是观测到的证据。</div>
  <p class="muted small">数字来自 results/agent/summary_&lt;tag&gt;.json（agent 和两个基线：直接问、不联网结构化；基线来自 results/forecast/summary.json）；假设占比由同一次运行的 state.json 算出。
  展示集的数字来自 results/showcase/summary.json。</p>`;
}
