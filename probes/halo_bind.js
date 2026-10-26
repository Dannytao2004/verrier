
/* =========================================================
   VERRIER — bind one saved run (GET /api/saved, /api/result) to this layout.
   Every number on the page comes from that run; the ring, beams and web stay decorative.
   (Added for Verrier HALO; the rest of this file is HALOFLUX by Ryder191, see the notice at the top.)
   ========================================================= */
function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function plain(t) { return String(t == null ? '' : t).replace(/[<>&]/g, ' '); }
function fmtN(v) {
  if (v == null || !isFinite(v)) return '—';
  return Math.abs(v) >= 1e4 ? Math.round(v).toLocaleString('en-US') : (+(+v).toPrecision(4)).toLocaleString('en-US', { maximumFractionDigits: 6 });
}
function short(v) {
  if (v == null || !isFinite(v)) return '—';
  const a = Math.abs(v);
  return a >= 1e12 ? (v / 1e12).toFixed(2) + 'T' : a >= 1e9 ? (v / 1e9).toFixed(2) + 'B' : a >= 1e6 ? (v / 1e6).toFixed(2) + 'M'
    : a >= 1e4 ? (v / 1e3).toFixed(1) + 'K' : String(+(+v).toPrecision(3));
}
const CAT = { related_series: 'rel', own_history: 'own', capacity_consumption: 'cap', base_rates: 'base', physical_flow: 'flow',
  forecasts_markets: 'fcst', persona: 'pers', shocks: 'shck', administrative: 'adm', attention: 'attn' };
function setArr(a, items) { a.length = 0; items.forEach(v => a.push(v)); }
function mres(m, f) { return m.error ? 'rejected' : m.estimate != null ? f(m.estimate) : m.distribution ? 'distribution' : 'rejected'; }

async function vLoad() {
  let runs = [];
  try { runs = (await (await fetch('/api/saved')).json()).runs || []; } catch (e) { /* 没有服务时页面留在占位 */ }
  runs = runs.filter(r => r.estimate != null || r.most_likely != null)
    .sort((a, b) => String(b.started_at || '').localeCompare(String(a.started_at || '')));
  const [hq, ht] = decodeURIComponent(location.hash.slice(1)).split('/');
  const pick = runs.find(r => r.qid === hq && r.tag === (ht || '')) || runs[0];
  const sel = document.getElementById('runSel');
  sel.innerHTML = runs.slice(0, 80).map(r => `<option value="${esc(r.qid)}/${esc(r.tag)}"${r === pick ? ' selected' : ''}>`
    + `${esc(String(r.question || r.qid).slice(0, 42))} · ${esc(r.tag)}</option>`).join('');
  sel.onchange = () => { location.hash = sel.value; location.reload(); };
  if (!pick) { document.getElementById('estQ').textContent = 'no saved run with an estimate'; return; }
  let d;
  try {
    d = await (await fetch(`/api/result?qid=${encodeURIComponent(pick.qid)}&tag=${encodeURIComponent(pick.tag)}`)).json();
  } catch (e) { document.getElementById('estQ').textContent = 'could not load the run'; return; }
  vBind(d, pick);
}

function vBind(d, pick) {
  const est = d.estimate || {}, comb = est.combination || {}, blocks = comb.blocks || [];
  const ev = d.evidence || {}, kept = ev.kept || [], disc = ev.discarded || [], pages = ev.pages || {};
  const ms = d.methods || [], dirs = d.directions || [];
  const okm = ms.filter(m => (m.estimate != null || m.distribution) && !m.error);   // 离散题的方法给的是概率分布
  const disc1 = d.mode === 'discrete';   // 离散题：central 是最可能那个结果的值，显示它和它的概率，不是区间
  const nb = blocks.length || (okm.length ? 1 : 0);                                // v2.12 之前的运行没有块的结构：算出来就当一块
  const unit = est.unit || (d.target || {}).unit_canonical || '';
  const read = (pages.snapshot || 0) + (pages.live_dated || 0), dropped = pages.dropped || 0;
  const per = x => ({ k: kept.filter(p => p.direction_id === x.id).length, d: disc.filter(p => p.direction_id === x.id).length });

  // 估计值浮层（舞台左上角，大号数字）
  document.getElementById('estQ').textContent = d.question || pick.qid;
  document.getElementById('estNum').innerHTML = (est.central != null ? fmtN(est.central)
    : esc(pick.most_likely != null ? pick.most_likely : '—')) + `<small>${esc(disc1 ? 'most likely outcome' : unit)}</small>`;
  document.getElementById('estIv').textContent = est.p10 != null && est.p90 != null
    ? `80% interval ${fmtN(est.p10)} – ${fmtN(est.p90)} ${unit}`
    : disc1 && pick.most_likely_prob != null ? `probability ${(100 * pick.most_likely_prob).toFixed(1)}% · ${unit}` : '';
  const usd = (d.budget || {}).usd_total_assumed;
  document.getElementById('estMeta').textContent = `as of ${d.as_of || '—'} · ${d.model || ''} · `
    + `${usd != null ? '$' + usd.toFixed(2) : ''} · ${pick.qid}/${pick.tag}`;

  // 页头 5 个统计和状态行
  const kv = [[dirs.length, 1], [read, read / Math.max(1, read + dropped)], [kept.length, kept.length / Math.max(1, kept.length + disc.length)],
    [`${okm.length}/${ms.length}`, okm.length / Math.max(1, ms.length)], [nb, 1]];
  kv.forEach(([v, f], i) => { document.getElementById('k' + i).textContent = v; segs[i].style.width = Math.round(100 * f) + '%'; });
  document.getElementById('stBig').textContent = `${okm.length} / ${ms.length} METHODS · ${nb} BLOCK${nb === 1 ? '' : 'S'}`;
  document.getElementById('stSm').textContent = `${kept.length} points kept · ${disc.length} discarded · ${read} pages read · ${dropped} dropped`;

  // 调查流水：每个方向读了什么、留下了哪些点、丢了哪些点，最后是方法和估计
  const F = [];
  dirs.forEach(x => {
    F.push(['seek', `${x.id} ${x.category} · ${x.perspective || ''}`]);
    kept.filter(p => p.direction_id === x.id).slice(0, 6).forEach(p =>
      F.push(['keep', `${p.id} ${p.value_as_written} · ${p.name} · ${p.domain || ''}`]));
    disc.filter(p => p.direction_id === x.id).slice(0, 2).forEach(p => F.push(['drop', `${p.id} ${p.value_as_written} · ${p.name}`]));
  });
  ms.forEach(m => F.push(['calc', `${m.label || m.id} ${m.formula || m.method} = ${mres(m, short)}`]));
  if (est.central != null) F.push(['calc', `estimate ${short(est.central)} ${unit}`]);
  feed.innerHTML = '';
  V.feed = F;

  // 方法工作区（打字机）：方法公式、假设、合并块
  const C2 = ms.map(m => [plain(m.label || m.id), plain(m.formula || m.method),
    `   → ${mres(m, fmtN)}`]);
  (d.assumptions || []).forEach(a => C2.push([plain(a.id), plain(String(a.name || '').slice(0, 46)),
    ` = ${a.value} [${a.low}, ${a.high}] ${plain(a.unit || '')}`]));
  blocks.forEach(b => C2.push([plain(b.id), b.members.join(' + '), `   → ${fmtN(b.value)}`]));
  if (est.central != null) C2.push(['estimate', plain(comb.rule_across_blocks || est.weight_rule || 'combine'), `   → ${fmtN(est.central)} ${plain(unit)}`]);
  if (C2.length) { setArr(CODE, C2); cLine = 0; cChar = 0; cNum = 1; typed = []; }

  // 舞台浮标：方法公式和结果轮播
  const CK = ms.filter(m => m.formula).map(m => [`${String(m.label || m.id).toUpperCase()} · ${String(m.method).toUpperCase()}`,
    `${m.formula} = ${mres(m, short)}`]);
  blocks.forEach(b => CK.push([`BLOCK ${b.id}`, `${b.members.join(' + ')} → ${short(b.value)}`]));
  if (est.central != null) CK.push(['ESTIMATE', `${short(est.central)} ${unit}`]);
  if (CK.length) setArr(CHECKS, CK);

  // 光环卡片上的字：真实数据点的编号、来源、数值、单位
  const pts = kept.slice(0, 80);
  if (pts.length) {
    setArr(HEAD, pts.map(p => `${String(p.id).toUpperCase()} ${String(p.domain || '').replace(/^www\./, '').toUpperCase().slice(0, 14)}`));
    setArr(KEYS, [...new Set(pts.map(p => String(p.unit || '').slice(0, 10)).filter(Boolean))].slice(0, 20));
    setArr(CODE_T, pts.map(p => String(p.value_as_written || '').slice(0, 12)).filter(Boolean));
    slots.forEach(s => s.c = null);
  }

  // 方向表：搜索 → 读页 → 留下点
  const top = dirs.slice(0, 6);
  setArr(ROUTES, top.map(x => `${x.id} ${CAT[x.category] || x.category}`));
  setArr(COLSR, ['search', 'read', 'keep']);
  setArr(rState, top.map(x => { const c = per(x); return c.k ? 3 : c.d ? 2 : 1; }));
  V.routePink = top.map(x => per(x).k === 0);
  renderRoutes();

  // 子 agent：每个方向的点，青色 = 留下，粉色 = 丢掉
  const agDirs = dirs.slice(0, 12);
  agEl.innerHTML = agDirs.map(x => `<div class="ag"><span class="id">${esc(x.id)}</span><span class="rl">${esc(CAT[x.category] || x.category)}</span>`
    + `<span class="cells">${'<i></i>'.repeat(6)}</span><span class="st"></span></div>`).join('');
  const rows = [...agEl.children];
  V.ag = agDirs.map((x, i) => ({ ...per(x), row: rows[i], p: 0 }));
  agentsTick = function (dt) {
    V.ag.forEach(a => {
      a.p = Math.min(6, a.p + dt * 2.5);
      const tot = a.k + a.d, nk = tot ? Math.round(6 * a.k / tot) : 0, fill = Math.floor(a.p);
      const cells = a.row.children[2].children;
      for (let c = 0; c < 6; c++) cells[c].style.background = c >= fill || !tot ? '#1d1f24' : c < nk ? '#98e0cf' : '#f0a6c6';
      const st = tot ? `${a.k} kept · ${a.d} out` : 'no points', se = a.row.children[3];
      if (se.textContent !== st) { se.textContent = st; se.className = 'st' + (a.k ? ' w' : ''); }
    });
  };

  // 估计 / 样本云：按 P10、P90 拟合的对数正态，实时抽样（点是从这个分布抽的，不是计算时的蒙特卡洛样本）
  const lp10 = Math.log(est.p10), lp90 = Math.log(est.p90), mu = (lp10 + lp90) / 2, sg = (lp90 - lp10) / (2 * 1.2816);
  V.dist = isFinite(mu) && sg > 0 ? { mu, sg } : null;
  V.samples = [];
  drawAdv = function (dt) {
    const x = cAdv.x, w = cAdv.w, h = cAdv.h;
    x.fillStyle = 'rgba(14,15,18,0.35)'; x.fillRect(0, 0, w, h);
    if (!V.dist) {
      x.fillStyle = '#6b6f78'; x.font = `600 8px ${FONT}`; x.textBaseline = 'middle';
      x.fillText(disc1 ? 'discrete target: outcome probabilities, no interval' : 'no interval for this run', 6, h / 2);
      return;
    }
    const lo = V.dist.mu - 2.6 * V.dist.sg, hi = V.dist.mu + 2.6 * V.dist.sg, X = l => (l - lo) / (hi - lo) * w;
    x.strokeStyle = 'rgba(235,238,244,.8)'; x.lineWidth = 1; x.beginPath();
    for (let i = 0; i <= 80; i++) {
      const l = lo + (hi - lo) * i / 80, z = (l - V.dist.mu) / V.dist.sg, y = h - 12 - Math.exp(-z * z / 2) * (h - 26);
      i ? x.lineTo(X(l), y) : x.moveTo(X(l), y);
    }
    x.stroke();
    for (let k = 0; k < 3; k++) V.samples.push({ l: V.dist.mu + gauss() * 1.5 * V.dist.sg, y: 0, v: rr(20, 60) });
    x.fillStyle = 'rgba(240,166,198,.85)';
    V.samples.forEach(sm => { sm.y += sm.v * dt; x.fillRect(X(sm.l), sm.y, 1.5, 1.5); });
    V.samples = V.samples.filter(sm => sm.y < h - 12);
    x.font = `600 7px ${FONT}`; x.textBaseline = 'alphabetic';
    [[lp10, 'P10'], [Math.log(est.central), 'EST'], [lp90, 'P90']].forEach(([l, t]) => {
      const xx = X(l);
      x.strokeStyle = t === 'EST' ? '#fff' : 'rgba(152,224,207,.8)'; x.beginPath(); x.moveTo(xx, 8); x.lineTo(xx, h - 12); x.stroke();
      x.fillStyle = '#9a9ea7'; x.fillText(`${t} ${short(Math.exp(l))}`, Math.min(w - 52, xx + 2), t === 'EST' ? 8 : h - 2);
    });
  };

  // 合并块：每块的值在对数刻度上，带区间和最终估计
  const items = blocks.length ? blocks.map(b => ({ id: b.id, v: b.value, lab: b.members.join('+') }))
    : okm.map(m => ({ id: m.label || m.id, v: m.estimate, lab: m.method }));
  drawDiff = function () {
    const x = cDiff.x, w = cDiff.w, h = cDiff.h;
    x.clearRect(0, 0, w, h);
    if (!items.length || est.central == null) return;
    const ls = items.map(i => Math.log(i.v)).concat(V.dist ? [lp10, lp90] : []);
    const lo = Math.min(...ls) - 0.15, hi = Math.max(...ls) + 0.15, X = l => 64 + (l - lo) / (hi - lo) * (w - 74);
    x.font = `600 7px ${FONT}`; x.textBaseline = 'middle';
    if (V.dist) { x.fillStyle = 'rgba(152,224,207,.12)'; x.fillRect(X(lp10), 0, X(lp90) - X(lp10), h); }
    const rh = Math.min(18, (h - 8) / items.length);
    items.forEach((it, i) => {
      const y = 6 + i * rh + rh / 2, xx = X(Math.log(it.v));
      x.fillStyle = '#9a9ea7'; x.fillText(`${it.id} ${it.lab}`.slice(0, 13), 0, y);
      x.fillStyle = '#2b2e34'; x.fillRect(64, y - 1, w - 74, 2);
      x.fillStyle = '#f0a6c6'; x.fillRect(xx - 2, y - 4, 4, 8);
      x.fillStyle = '#cfd2d8'; x.fillText(short(it.v), Math.min(w - 34, xx + 5), y);
    });
    const xc = X(Math.log(est.central));
    x.strokeStyle = '#fff'; x.beginPath(); x.moveTo(xc, 0); x.lineTo(xc, h); x.stroke();
  };

  // 代码检查：单位核对、输入审查、泄漏哨兵、丢页
  // 单位核对只算真走到这一步的：被别的检查拒掉的方法没有核对过单位，不算失败
  const unitOK = ms.filter(m => m.unit_check && m.unit_check.unit).length, unitBad = ms.filter(m => /unit check/i.test(m.error || '')).length;
  const nAudit = (d.audit_errors || []).length, hits = (d.leakage || {}).sentinel_hits || 0;
  V.checks = [['UNIT CHECK', `${unitOK} passed · ${unitBad} failed`, unitBad > 0],
    ['INPUT AUDIT', nAudit ? `${nAudit} methods rejected` : 'no rejections', nAudit > 0],
    ['LEAK SENTINEL', `${hits} hits`, hits > 0], ['PAGES DROPPED', `${dropped} of ${read + dropped}`, false]];
  drawVal = function () {
    const x = cVal.x, w = cVal.w, h = cVal.h;
    x.clearRect(0, 0, w, h);
    const rh = h / V.checks.length, scan = (T * 0.35 % 1) * w;
    x.textBaseline = 'middle';
    V.checks.forEach(([k, v, bad], i) => {
      const yc = rh * i + rh / 2;
      x.font = `800 7px ${FONT}`; x.fillStyle = '#9a9ea7'; x.fillText(k, 0, yc);
      x.strokeStyle = '#1f2227'; x.lineWidth = 1; x.beginPath(); x.moveTo(86, yc + 6); x.lineTo(w, yc + 6); x.stroke();
      x.font = `600 8px ${FONT}`; x.fillStyle = bad ? '#f0a6c6' : '#e6e8ec'; x.fillText(v, 92, yc);
    });
    x.strokeStyle = 'rgba(240,166,198,.45)'; x.beginPath(); x.moveTo(scan, 0); x.lineTo(scan, h); x.stroke();
  };

  // 方法 × 输入：哪个方法用了哪个数据点 / 假设
  const cols = [];
  ms.forEach(m => (m.inputs || []).forEach(i => {
    if (!cols.find(c => c.id === i.id)) cols.push({ id: i.id, kind: (i.evidence || {}).kind || (String(i.id).startsWith('a') ? 'assumption' : 'point') });
  }));
  const idxCols = cols.slice(0, 28);
  const idxRows = ms.slice(0, 11).map(m => ({ id: m.label || m.id, v: m.estimate, r: mres(m, short), ok: !m.error && (m.estimate != null || !!m.distribution),
    used: new Set((m.inputs || []).map(i => i.id)) }));
  drawIdx = function () {
    const x = cIdx.x, w = cIdx.w, h = cIdx.h;
    x.clearRect(0, 0, w, h);
    if (!idxRows.length || !idxCols.length) return;
    x.font = `600 6.5px ${FONT}`; x.textBaseline = 'middle';
    const lx = 26, rx = 40, cw = (w - lx - rx) / idxCols.length, ch = Math.min(14, h / idxRows.length);
    const scan = Math.floor((T * 4) % idxCols.length);
    idxRows.forEach((m, j) => {
      const y = j * ch;
      x.fillStyle = '#6b6f78'; x.fillText(String(m.id).toUpperCase(), 0, y + ch / 2);
      idxCols.forEach((c, i) => {
        const used = m.used.has(c.id);
        let col = used ? (c.kind === 'assumption' ? '#f0a6c6' : c.kind === 'constant' ? '#98e0cf' : '#e6e8ec') : '#1c1e23';
        if (i === scan) col = used ? '#ffffff' : '#2a2d33';
        x.fillStyle = col; x.fillRect(lx + i * cw, y + 1, Math.max(1, cw - 1), ch - 2);
      });
      x.fillStyle = m.ok ? '#9a9ea7' : '#f0a6c6'; x.fillText(m.r, w - rx + 4, y + ch / 2);
    });
  };

  V.ready = true;
}
vLoad();
