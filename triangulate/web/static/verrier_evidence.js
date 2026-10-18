// Verrier 控制台的证据页（路由 #console/evidence/<题 id>/<tag>，由 verrier_console.js 取数、接线）：把 /api/result 的同一份 JSON
// 用 Verrier 的版式画出来（黑色标题条、带螺丝的面板、等宽标签、墨色 / 红色，沿用 .cx-* 样式）。
// 纯函数 window.VERRIER_EVIDENCE(r, qid, tag)：输入 /api/result 的 JSON，返回 HTML 字符串；不发请求、不碰 DOM。经典界面的结果页（/#/result）不变。
"use strict";
(() => {
  // ---------- 工具（和 verrier_console.js 同一套格式） ----------
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
  const factor = x => typeof x === "number" && isFinite(x) ? String(Number(x.toPrecision(4))) : "—";   // 单位换算系数（1e-6 这类小数）
  const link = (url, text) => url ? `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(text || url)}</a>` : "—";
  const period = x => `${esc(x.period_start || "?")}..${esc(x.period_end || "?")}`;
  const seen = p => p.snapshot_url ? link(p.snapshot_url, "snapshot " + p.snapshot_date) : esc([p.via, p.page_date].filter(Boolean).join(" ")) || "—";
  const bigUnit = u => u ? ` <span style="font-size:.4em;font-stretch:100%;letter-spacing:0">${esc(u)}</span>` : "";
  const panel = (code, title, right, inner) => `<section class="card cx-ev"><div class="bh"><span>${code} · ${title}</span><i class="hz"></i>
    <span class="sp"></span><span>${right}</span></div><div class="bd">${inner}</div></section>`;
  const none = () => `<p class="fine">${T("None.", "没有。")}</p>`;

  // ---------- E-01 估计、终稿 ----------
  function estimate(r, qid, tag) {
    const e = r.estimate || {}, o = r.official, d = r.discrete, sh = (r.assumption_share || {}).overall, ev = r.evidence || {}, b = r.budget || {};
    const ms = r.methods || [];
    const main = d ? `<div class="lbl">${T("Most likely outcome", "最可能的结果")}</div><div class="cx-big">${esc(d.most_likely ?? "—")}</div>
        <p class="fine">${prob(d.most_likely_prob)} · ${(d.outcomes || []).map(x => `${esc(x.label)} ${prob(x.prob)}`).join(" · ")}</p>`
      : `<div class="lbl">${T("Estimate", "估计")}</div><div class="cx-big">${fmt(e.central)}${bigUnit(e.unit)}</div>
        <p>80% model-based [${fmt(e.p10)}, ${fmt(e.p90)}]${e.unit ? " " + esc(e.unit) : ""}</p>
        <p class="fine">${T("Interval basis", "区间依据")} <b>${esc(e.basis || "—")}</b>${e.basis_text ? ": " + esc(e.basis_text) : ""}
          · ${T("weights", "加权规则")} ${esc(e.weight_rule || "—")}</p>`;
    const off = !o ? "" : d ? `<p class="fine">${T("True outcome", "真实结果")} <b>${esc(o.true_outcome ?? fmt(o.answer_value))}</b> · ${T("its probability", "它的概率")}
        ${prob(o.prob_true)} · Brier ${fmt(o.brier)}</p>`
      : `<p class="fine">OFFICIAL <b>${fmt(o.answer_value)}</b> · ${T("error", "误差")} <b>${pct(o.pct_err)}</b> · ${T("80% interval covers it", "80% 区间盖住")}
        ${o.covered_80 === true ? T("yes", "是") : o.covered_80 === false ? `<span class="cx-bad">${T("no", "否")}</span>` : "—"}
        · ${T("released", "公布")} ${esc(o.released || "—")} · ${link(o.source, "source")}</p>`;
    const inner = `<div class="cx-grid"><div>${main}${off}
        ${sh === null || sh === undefined ? "" : `<div class="cx-bar"><i style="width:${(100 * (1 - sh)).toFixed(1)}%"></i></div>
          <p class="fine">${T("Evidence", "证据")} ${share(1 - sh)} · ${T("Assumptions", "假设")} ${share(sh)}${(r.assumption_share || {}).warning
            ? ` · <span class="cx-bad">${T("uncertainty comes mainly from assumptions", "不确定性主要来自假设")}</span>` : ""}</p>`}
        ${r.aborted ? `<div class="cx-err">${esc(r.aborted)}</div>` : ""}
      </div><div class="cx-meta">
        <div><span class="lbl">${T("Kept points", "保留的点")}</span><b>${(ev.kept || []).length}</b></div>
        <div><span class="lbl">${T("Discarded", "丢弃的点")}</span><b>${(ev.discarded || []).length}</b></div>
        <div><span class="lbl">${T("Methods computed", "算出的方法")}</span><b>${ms.filter(m => m.status === "computed").length}/${ms.length}</b></div>
        <div><span class="lbl">${T("Cost", "花费")}</span><b>${usd(b.usd_total_assumed)}</b></div>
      </div></div>
      <h3 class="cx-h">${T("Final answer", "最终答案")}</h3><pre class="cx-answer">${esc(r.final_text || "—")}</pre>`;
    return panel("E-01", T("Estimate", "估计"), `${esc(qid)} / ${esc(tag || "—")}`, inner);
  }

  // ---------- E-02 钉死的目标 ----------
  function target(t) {
    const rows = [["what", "What", "是什么"], ["unit", "Unit", "单位"], ["unit_canonical", "Pinned unit", "钉死的单位"],
      ["period_start", "From", "期间开始"], ["period_end", "To", "期间结束"], ["publisher", "Publisher", "谁公布"], ["cadence", "Cadence", "公布节奏"],
      ["caveats", "Caveats", "注意"], ["outcome_type", "Outcome type", "结果类型"]];
    const have = rows.filter(([k]) => t[k] !== undefined && t[k] !== null && t[k] !== "");
    const outs = (t.outcomes || []).length ? `<tr><th>${T("Outcomes", "结果")}</th><td>${t.outcomes.map(o => esc(o.label)).join(" · ")}</td></tr>` : "";
    return panel("E-02", T("Pinned target", "钉死的目标"), t.unit_canonical ? esc(t.unit_canonical) : T("unit not pinned", "没有钉死单位"),
      have.length || outs ? `<table class="cx-t">${have.map(([k, en, z]) => `<tr><th>${T(en, z)}</th><td>${esc(t[k])}</td></tr>`).join("")}${outs}</table>` : none());
  }

  // ---------- E-03 方法 ----------
  const MST = {computed: ["Computed", "已算出"], failed: ["Failed", "失败"],
    excluded_by_input_audit: ["Failed the input audit, not computed", "输入核对不通过，未计算"],
    excluded_by_coverage: ["Covers part of the target, not combined", "只覆盖目标的一部分，不进合并"]};
  function coverage(c) {
    const list = xs => (xs || []).map(esc).join(", ");
    if (c.kind === "full") return T("the whole target", "整个目标");
    if (c.kind === "part") return T(`only ${esc(c.part)} of ${esc(c.dimension)} (siblings: ${list(c.siblings)})`,
      `只有 ${esc(c.dimension)} 的 ${esc(c.part)}（同级：${list(c.siblings)}）`);
    const miss = (c.missing || []).length ? T(`; missing ${list(c.missing)}`, `；缺 ${list(c.missing)}`) : "";
    return T(`sum over ${esc(c.dimension)}: ${(c.parts || []).map(esc).join(" + ")}`, `${esc(c.dimension)} 各部分之和：${(c.parts || []).map(esc).join(" + ")}`) + miss;
  }
  function evidenceOf(e) {
    if (!e) return "—";
    if (e.kind === "assumption") return `<span class="stencil">${T("assumption", "假设")}</span> <b>${esc(e.id)}</b> ${esc(e.name)} = ${fmt(e.value)}${e.unit === "%" ? "%" : " " + esc(e.unit)}`;
    if (e.kind === "constant") return `<span class="stencil">${T("constant", "常数")}</span> <b>${esc(e.id)}</b> ${T("calendar or unit constant (code)", "日历或单位常数（代码给）")}`;
    if (e.kind === "unknown") return `<span class="cx-bad"><b>${esc(e.id)}</b> ${T("unknown id", "未知 id")}</span>`;
    return `<span class="stencil">${T("point", "数据点")}</span> <b>${esc(e.id)}</b> ${esc(e.name)} = ${fmt(e.value)} ${esc(e.unit)}
      <div class="fine">${period(e)} · ${link(e.source_url, e.domain)} · ${seen(e)}</div>${e.quote ? `<div class="cx-qt">“${esc(e.quote)}”</div>` : ""}`;
  }
  function inputs(m) {
    if (!(m.inputs || []).length) return "";
    return `<div class="cx-scroll"><table class="cx-t cx-w"><tr><th>${T("Input", "输入")}</th><th>${T("Role", "role")}</th><th>${T("Evidence it points to", "指向的证据")}</th>
      <th>${m.method === "outcome_probs" ? T("Probability", "概率") : T("Sampled P10..P90", "采样 P10..P90")}</th></tr>
      ${m.inputs.map(i => `<tr><td><b>${esc(i.name)}</b> = ${esc(i.id)}</td><td>${esc(i.role) || `<span class="cx-bad">${T("(not given)", "（没写）")}</span>`}</td>
        <td>${evidenceOf(i.evidence)}</td><td>${i.prob !== undefined && i.prob !== null ? prob(i.prob)
          : i.p10 !== undefined && i.p10 !== null ? `${fmt(i.p10)}..${fmt(i.p90)}` : "—"}</td></tr>`).join("")}</table></div>`;
  }
  function method(m) {
    const st = MST[m.status] || [esc(m.status), esc(m.status)], ok = m.status === "computed", u = m.unit_check, c = m.coverage_excluded;
    const val = m.distribution ? Object.entries(m.distribution).map(([k, v]) => `${esc(k)} ${prob(v)}`).join(" · ") : fmt(m.estimate);
    const series = (lbl, s) => s ? `<span class="fine">${lbl}: ${Object.entries(s).map(([y, v]) => `${esc(y)} ${fmt(v)}`).join(" · ")}</span>` : "";
    return `<div class="cx-dir${ok ? " ok" : " bad"}">
      <span class="cx-dh"><b>${esc(m.id)}</b>${m.label && m.label !== m.id ? `<span class="lbl">${T("judge id", "裁判 id")} ${esc(m.label)}</span>` : ""}
        <span class="stencil">${esc(m.method)}</span><span class="cx-state${ok ? "" : " cx-bad"}">${T(...st)}</span></span>
      <code class="cx-f">${esc(m.formula) || "—"}</code>
      <span class="cx-nums"><span>${T("estimate", "估计")} <b>${val}</b></span>${m.mc ? `<span>MC P10..P90 <b>${fmt(m.mc.p10)}..${fmt(m.mc.p90)}</b></span>` : ""}
        <span>${T("weight", "权重")} <b>${ok ? Math.round(100 * (m.weight || 0)) + "%" : "—"}</b>${m.weight_basis ? " " + esc(m.weight_basis) : ""}</span>
        <span>${T("assumption share", "假设占比")} <b>${ok ? share(m.assumption_share) : "—"}</b></span></span>
      ${u ? `<span><span class="lbl">${T("Unit check", "单位检查")}</span> ${esc(u.unit)} → ${esc(u.target_unit)} × ${factor(u.factor)}</span>` : ""}
      ${m.coverage ? `<span><span class="lbl">${T("Coverage", "覆盖范围")}</span> ${coverage(m.coverage)}</span>` : ""}
      ${c ? `<span class="fine">${T("Its own estimate (reference only)", "它自己的估计（只作参考）")} ${fmt(c.estimate)}${c.mc ? ` · P10..P90 ${fmt(c.mc.p10)}..${fmt(c.mc.p90)}` : ""}</span>` : ""}
      ${series(T("target series", "目标序列"), m.target_series)}${series(T("signal series", "信号序列"), m.signal_series)}
      ${(m.backtest || []).length ? `<span class="fine">${T("backtest", "回测")}: ${m.backtest.map(x => `${esc(x.year)} ${pct(Math.exp(x.log_err) - 1)}`).join(" · ")}</span>` : ""}
      ${m.error ? `<span class="cx-bad">${esc(m.error)}</span>` : ""}
      ${(m.notes || []).length ? `<span class="fine">${m.notes.map(esc).join("<br>")}</span>` : ""}
      ${m.rationale ? `<span class="fine"><b>${T("Rationale", "理由")}:</b> ${esc(m.rationale)}</span>` : ""}
      ${m.remainder ? `<span class="fine">${T(`remaining outcome ${esc(m.remainder)} = 1 minus the others (code)`, `余下的结果 ${esc(m.remainder)} = 1 − 其余之和（代码算）`)}</span>` : ""}
      ${inputs(m)}</div>`;
  }
  function methods(r) {
    const ms = r.methods || [];
    const inner = `<p class="fine">${T(`Methods from judge round ${esc(r.methods_from_round ?? "?")}. Methods with weight 0 are not in the combined estimate.`,
        `裁判第 ${esc(r.methods_from_round ?? "?")} 轮给出的方法。权重为 0 的方法没有进入合并。`)}</p>
      ${(r.audit_errors || []).length ? `<div class="cx-err">${T("Input audit itself failed (no method was blocked)", "输入核对本身出错（没有拦方法）")}: ${r.audit_errors.map(esc).join("; ")}</div>` : ""}
      ${ms.length ? `<div class="cx-ms">${ms.map(method).join("")}</div>` : none()}`;
    return panel("E-03", T("Methods", "方法"), `${ms.filter(m => m.status === "computed").length}/${ms.length} ${T("computed", "算出")}`, inner);
  }

  // ---------- E-04 修正轮 ----------
  function repairs(r) {
    const rs = r.repairs || [];
    const li = xs => `<ul>${xs.map(x => `<li>${esc(x)}</li>`).join("")}</ul>`;
    const inner = rs.length ? `<div class="cx-ms">${rs.map(p => `<div class="cx-dir">
      <span class="cx-dh"><b>${T(`Judge round ${esc(p.round)}`, `裁判第 ${esc(p.round)} 轮`)}</b><span class="stencil">${T("repair", "修正轮")}</span></span>
      <span class="lbl">${T("Sent back to the judge", "交回裁判的问题")}</span>${li(p.errors || [])}
      ${(p.previous_methods || []).length ? `<span class="lbl">${T("Methods before the repair", "修正前的方法")}</span>${li(p.previous_methods)}` : ""}
      ${p.error ? `<span class="cx-bad">${T("Repair call failed", "修正调用失败")}: ${esc(p.error)}</span>` : ""}
      ${p.errors_after ? `<span class="lbl">${T("Still open after the repair", "修正后仍有的问题")}</span>${p.errors_after.length ? li(p.errors_after) : `<span class="fine">${T("None.", "无。")}</span>`}` : ""}
      ${p.reverted ? `<span class="cx-bad">${esc(p.reverted)}</span>` : ""}</div>`).join("")}</div>` : `<p class="fine">${T("No repair round.", "没有修正轮。")}</p>`;
    return panel("E-04", T("Repair rounds", "修正轮"), String(rs.length), inner);
  }

  // ---------- E-05 假设 ----------
  function assumptions(r) {
    const as = r.assumptions || [], rej = r.assumptions_rejected || [];
    const p = a => a.is_pct ? "%" : "";
    const table = as.length ? `<div class="cx-scroll"><table class="cx-t cx-w"><tr><th>id</th><th>${T("Name", "名称")}</th><th>${T("Value", "值")}</th>
      <th>${T("Judge range", "裁判给的范围")}</th><th>${T("Sampled range", "代码采样范围")}</th><th>${T("Unit", "单位")}</th><th>${T("Rationale", "理由")}</th>
      <th>${T("Applies when", "适用条件")}</th><th>${T("Falsified by", "什么会推翻它")}</th><th>${T("Used by", "被谁用")}</th></tr>
      ${as.map(a => `<tr><td><b>${esc(a.id)}</b></td><td>${esc(a.name)}</td><td>${fmt(a.value)}${p(a)}</td><td>${fmt(a.low)}..${fmt(a.high)}</td>
        <td>${fmt(a.p10_used)}..${fmt(a.p90_used)}${p(a)}${a.widened_by_floor ? `<div class="lbl">${T("widened", "已放宽")}</div>` : ""}</td>
        <td>${esc(a.unit)}</td><td>${esc(a.rationale)}</td><td>${esc(a.applies_when)}</td><td>${esc(a.falsified_by)}</td>
        <td>${(a.used_by || []).length ? a.used_by.map(esc).join(", ") : T("not used", "没用上")}</td></tr>`).join("")}</table></div>`
      : `<p class="fine">${T("No kept assumptions.", "没有保留的假设。")}</p>`;
    const rejected = rej.length ? `<h3 class="cx-h">${T("Rejected by code", "被代码拒绝的假设")} (${rej.length})</h3>
      <ul>${rej.map(a => `<li>${esc(a.id || a.raw)} ${esc(a.name || "")}: ${esc(a.reason)}</li>`).join("")}</ul>` : "";
    return panel("E-05", T("Assumptions", "假设"), `${as.length} ${T("kept", "保留")} · ${rej.length} ${T("rejected", "拒绝")}`, table + rejected);
  }

  // ---------- E-06 数据点 ----------
  function points(ps, kept) {
    if (!ps.length) return none();
    return `<div class="cx-scroll"><table class="cx-t cx-w"><tr><th>id</th><th>${T("Route", "方向")}</th><th>${T("Name", "名称")}</th><th>${T("Value", "值")}</th>
      <th>${T("Unit", "单位")}</th><th>${T("Period", "期间")}</th><th>${T("Source", "来源")}</th><th>${T("Snapshot / page date", "快照 / 页面日期")}</th>
      <th>${kept ? T("Used by", "被哪些方法用") : T("Judge's reason", "裁判的理由")}</th><th>${T("Quote", "原文")}</th></tr>
      ${ps.map(x => `<tr><td><b>${esc(x.id)}</b></td><td>${esc(x.direction_id)}</td><td>${esc(x.name)}</td><td>${fmt(x.value)}</td><td>${esc(x.unit)}</td>
        <td>${period(x)}</td><td>${link(x.source_url, x.domain)}</td><td>${seen(x)}</td>
        <td>${kept ? esc((x.used_by || []).join(", ")) : esc(x.judge_reason || x.ablation_excluded || "")}</td><td class="cx-qt">${esc(x.quote)}</td></tr>`).join("")}</table></div>`;
  }
  function evidence(r) {
    const ev = r.evidence || {}, pg = ev.pages || {}, kept = ev.kept || [], disc = ev.discarded || [], abl = ev.ablation_excluded || [];
    const drop = Object.entries(ev.dropped_by_code || {}).map(([k, v]) => `${esc(k)} ×${esc(v)}`).join("; ");
    const inner = `<p class="fine">${T("Pages", "页面")}: snapshot ${esc(pg.snapshot || 0)} · live ${esc(pg.live_dated || 0)} · ${T("dropped", "丢弃")} ${esc(pg.dropped || 0)}.
        ${T("Points dropped by code checks", "代码核对丢掉的点")}: ${drop || T("none", "无")}</p>
      <h3 class="cx-h">${T("Kept points", "保留的点")} (${kept.length})</h3>${points(kept, true)}
      <h3 class="cx-h">${T("Discarded by the judge", "裁判丢弃的点")} (${disc.length})</h3>${points(disc, false)}
      ${abl.length ? `<h3 class="cx-h">${T("Excluded by ablation", "消融排除的点")} (${abl.length})</h3>${points(abl, false)}` : ""}`;
    return panel("E-06", T("Evidence points", "数据点"), `${kept.length} ${T("kept", "保留")} · ${disc.length} ${T("discarded", "丢弃")}`, inner);
  }

  // ---------- E-07 泄漏审计、E-08 方向 ----------
  function leakage(l) {
    l = l || {};
    const v = x => esc(x ?? "—");
    const rows = [[T("Pages (snapshot / live / dropped)", "页面（快照 / live / 丢弃）"), `${v(l.pages_total)} (${v(l.pages_snapshot)} / ${v(l.pages_live_dated)} / ${v(l.pages_dropped)})`],
      [T("Sentinel hits (page excluded)", "哨兵命中（整页排除）"), v(l.sentinel_hits)],
      [T("Points dated after as_of", "期间或页面日期晚于 as_of 的数据点"), v(l.points_dated_after_as_of)],
      [T("Snapshots after as_of", "时间戳晚于 as_of 的快照"), v(l.snapshots_after_as_of)],
      [T("Searcher queries containing registered values", "searcher 查询词里出现登记值"), v(l.searcher_queries_containing_registered_values)],
      [T("Assumptions containing registered values", "假设里出现登记值"), v(l.assumptions_containing_registered_values)],
      [T("Pages sent with dates after as_of", "送给 extractor 的正文里晚于 as_of 的日期（页数）"), v(l.late_dates_in_text_sent)]];
    const risks = [...(l.residual_risks || []), ...(l.by_construction || [])];
    const inner = `<table class="cx-t cx-w">${rows.map(([k, x]) => `<tr><th>${k}</th><td>${x}</td></tr>`).join("")}</table>
      <p class="fine">${T("Registered values = the true value of a backtest question and known official values published after as_of; web runs have none, so these counts are always 0 there.",
        "登记值 = 回测题的真值和 as_of 之后公布的已知官方值；网页运行没有登记值，这几项恒为 0，不说明什么。")}</p>
      ${risks.length ? `<h3 class="cx-h">${T("Residual risks", "残余风险")} (${risks.length})</h3><ul>${risks.map(x => `<li>${esc(x)}</li>`).join("")}</ul>` : ""}`;
    return panel("E-07", T("Leakage audit", "泄漏审计"), `${v(l.sentinel_hits)} ${T("sentinel hits", "次哨兵命中")}`, inner);
  }
  function directions(ds) {
    const inner = ds.length ? `<div class="cx-dirs">${ds.map(d => `<div class="cx-dir"><span class="cx-dh"><b>${esc(d.id)}</b><span class="stencil">${esc(d.category)}</span></span>
      ${d.perspective ? `<span class="cx-dp">${esc(d.perspective)}</span>` : ""}<span>${esc(d.hypothesis)}</span></div>`).join("")}</div>` : none();
    return panel("E-08", T("Directions", "取证方向"), String(ds.length), inner);
  }

  window.VERRIER_EVIDENCE = (r, qid, tag) => `<p class="cx-q">${esc(r.question || qid)}</p>
    <p class="fine">AS OF ${esc(r.as_of)} · ${esc(r.kind)} · ${esc(r.model)} · ${esc(r.started_at)}${r.wall_s ? ` · ${fmt(r.wall_s)} s` : ""}</p>
    ${estimate(r, qid, tag)}${target(r.target || {})}${methods(r)}${repairs(r)}${assumptions(r)}${evidence(r)}${leakage(r.leakage)}${directions(r.directions || [])}`;
})();
