"""一次性生成 triangulate/web/static/verrier_halo.html：HALOFLUX lab.html（Ryder191/haloflux 5c1992a，2026-10-26，
PolyForm Noncommercial 1.0.0）的派生版本。每处替换都断言恰好命中一次。只读原文件 D:/_external/haloflux/lab.html。"""
import pathlib
import shutil

SRC = pathlib.Path("D:/_external/haloflux/lab.html")
LIC = pathlib.Path("D:/_external/haloflux/LICENSE")
STATIC = pathlib.Path(__file__).resolve().parents[1] / "triangulate" / "web" / "static"
s = SRC.read_text(encoding="utf-8")


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:90])
    s = s.replace(old, new)


def cut(start_marker, end_marker):
    """删掉 start_marker 到 end_marker（含）之间的整段。"""
    global s
    i = s.index(start_marker)
    j = s.index(end_marker, i) + len(end_marker)
    s = s[:i] + s[j:]


# ---------- 头注释和标题 ----------
rep("""  仅限非商业用途，严格禁止任何商业用途。转载或二创须保留本声明并注明出处。
-->""", """  仅限非商业用途，严格禁止任何商业用途。转载或二创须保留本声明并注明出处。
-->
<!--
  Required Notice: Copyright (c) 2026 Ryder191 (RYDER CODE / Ms MAIKEBAIs CAT) - https://github.com/Ryder191/haloflux
  Required Notice: Noncommercial use only. Any commercial use is strictly prohibited. No commercial licenses are offered.
  License terms: PolyForm Noncommercial License 1.0.0 - https://polyformproject.org/licenses/noncommercial/1.0.0
  (full text: /static/haloflux_LICENSE.txt)

  Verrier HALO: a noncommercial derivative of HALOFLUX by Ryder191 (RYDER CODE / Ms MAIKEBAIs CAT),
  lab.html at commit 5c1992a (2026-10-26). Changes: the header, panels, ring-card text and callouts show Verrier data
  instead of HALOFLUX's demo data: the question form, the live progress of a run (GET /api/runs/{id}), the approval gate
  and the saved result (GET /api/saved, /api/result), driven by Verrier's own script /static/verrier_halo_flow.js;
  an estimate overlay, a run selector and a credit line were added; the background music was removed.
  The ring, beams, web and motion design are HALOFLUX's.
-->""")
rep("<title>Paper Lab Console</title>", "<title>Verrier · HALO</title>")

# ---------- 样式：新加的浮层、选择框、署名、流水的动词颜色 ----------
rep("""@media (max-width:1000px){""", """/* ---------- Verrier additions ---------- */
.est{left:8px;top:6px;max-width:min(56vw,800px);z-index:3;padding:8px 48px 10px 10px;
  background:linear-gradient(90deg,rgba(8,9,11,.82),rgba(8,9,11,.55) 70%,rgba(8,9,11,0))}
.est .q{font-size:10px;color:var(--text);letter-spacing:.4px;line-height:1.35;max-height:2.8em;overflow:hidden;margin-bottom:6px}
.est .num{font-size:clamp(30px,4.4vw,60px);font-weight:800;color:var(--white);font-variant-numeric:tabular-nums;line-height:1;
  text-shadow:0 0 18px rgba(0,0,0,.9)}
.est .num small{font-size:.3em;color:var(--dim);margin-left:8px;font-weight:600;letter-spacing:.5px}
.est .iv{margin-top:6px;font-size:10px;color:var(--pink);font-variant-numeric:tabular-nums}
.est .meta{margin-top:3px;font-size:8px;color:var(--dim)}
.runsel{top:10px;right:104px;z-index:3;pointer-events:auto}
.runsel select{background:rgba(8,9,11,.85);color:var(--text);border:1px solid var(--line2);font:9px "JetBrains Mono",Consolas,monospace;
  padding:2px 4px;max-width:340px}
.vb.keep{color:var(--white)} .vb.drop{color:var(--pink)} .vb.calc{color:var(--teal)} .vb.seek{color:var(--text)}
.credit{grid-column:1/-1;font-size:8px;color:var(--dim);letter-spacing:.6px;padding:1px 2px 0}
.credit a{color:var(--text)}
@media (max-width:1000px){""")

# ---------- 页头：品牌和 5 个统计 ----------
rep("""    <div class="brand"><h1>RYDER CODE / Ms MAIKEBAIs CAT</h1><p>RESEARCH PAPERS → REPRODUCIBLE EXPERIMENTS</p></div>
    <div class="kpi"><div class="k">PAPERS</div><div class="v" id="k0">64</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">AGENTS</div><div class="v pink" id="k1">12</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">METHODS</div><div class="v" id="k2">11</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">REF. SCENES</div><div class="v" id="k3">28</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">FURTHER REVIEW</div><div class="v" id="k4">4</div><div class="seg"><i></i></div></div>""",
    """    <div class="brand"><h1>VERRIER</h1><p>PUBLIC DATA → AUDITABLE ESTIMATES</p></div>
    <div class="kpi"><div class="k">DIRECTIONS</div><div class="v" id="k0">—</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">PAGES READ</div><div class="v" id="k1">—</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">POINTS KEPT</div><div class="v pink" id="k2">—</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">METHODS</div><div class="v" id="k3">—</div><div class="seg"><i></i></div></div>
    <div class="kpi"><div class="k">BLOCKS</div><div class="v" id="k4">—</div><div class="seg"><i></i></div></div>""")

# ---------- 舞台：去掉背景音乐，加估计值浮层和运行选择框 ----------
cut('    <div class="ov music" id="bgm">', '<audio id="bgmAudio" data-src="audio/sw421k.mp3" loop preload="auto" playsinline></audio>\n')
rep("""    <div class="ov chk" id="chk">""", """    <div class="ov est" id="est"><div class="q" id="estQ">loading…</div><div class="num" id="estNum">—</div>
      <div class="iv" id="estIv"></div><div class="meta" id="estMeta"></div></div>
    <div class="ov runsel"><select id="runSel" title="saved Verrier runs"></select></div>
    <div class="ov chk" id="chk">""")
rep("""<div class="ov chk" id="chk"><b id="chkK">STABILITY CHECK</b><span id="chkV">CFL = |u| Δt / Δx</span></div>""",
    """<div class="ov chk" id="chk"><b id="chkK">VERRIER</b><span id="chkV">loading…</span></div>""")
rep("""<div class="ov status"><div class="big" id="stBig">7 / 11 METHODS · 4 PENDING</div><div class="sm">independent runs · shared event bus</div></div>""",
    """<div class="ov status"><div class="big" id="stBig">loading…</div><div class="sm" id="stSm"></div></div>""")

# ---------- 底部面板：标题、说明，加署名行 ----------
rep("""<h3>ADVECTION / PARTICLE SOLVER</h3><canvas id="cAdv"></canvas>
      <div class="btns" id="advBtns"><span class="on">ADVECT</span><span>PROJECT</span><span>RENDER</span></div>""",
    """<h3>ESTIMATE / SAMPLE CLOUD</h3><canvas id="cAdv"></canvas>
      <div class="btns" id="advBtns"><span class="on">P10</span><span>ESTIMATE</span><span>P90</span></div>""")
rep("""<h3>SHARED SCENE / DIFFERENCE FIELD</h3><canvas id="cDiff"></canvas><div class="cap">same input · local difference · inspect source</div>""",
    """<h3>BLOCKS / ROUTE AGREEMENT</h3><canvas id="cDiff"></canvas><div class="cap">one row per block · white line = estimate · band = 80% interval</div>""")
rep("""<h3>SOURCE / EXTRACTION ROUTES</h3><div class="routes" id="routes"></div><div class="cap">pages → equations → runnable source</div>""",
    """<h3>DIRECTIONS / EVIDENCE ROUTES</h3><div class="routes" id="routes"></div><div class="cap">search → read → keep (code-checked points)</div>""")
rep("""<h3>VALIDATION / SAMPLE BUFFER</h3><canvas id="cVal"></canvas><div class="cap">illustrative / source check required</div>""",
    """<h3>CODE CHECKS</h3><canvas id="cVal"></canvas><div class="cap">unit check · input audit · leak sentinel · pages</div>""")
rep("""<h3>12 AGENTS / DISPATCH</h3><div class="agents" id="agents"></div><div class="cap">independent jobs / shared event bus</div>""",
    """<h3>DIRECTIONS / SUB-AGENTS</h3><div class="agents" id="agents"></div><div class="cap">teal = kept points · pink = discarded</div>""")
rep("""<h3>METHOD / REFERENCE INDEX</h3><canvas id="cIdx"></canvas><div class="cap">28 scenes / 7 matched / 4 further review</div></div>
  </section>""",
    """<h3>METHOD × INPUT INDEX</h3><canvas id="cIdx"></canvas><div class="cap">white = data point · pink = assumption · teal = constant</div></div>
    <div class="credit">Visual design and animation: <a href="https://github.com/Ryder191/haloflux" target="_blank" rel="noopener">HALOFLUX
      by Ryder191 (RYDER CODE / Ms MAIKEBAIs CAT)</a> · PolyForm Noncommercial 1.0.0 (<a href="/static/haloflux_LICENSE.txt"
      target="_blank">license</a>) · noncommercial use only · every number shown comes from the selected Verrier run</div>
  </section>""")

# ---------- 脚本：数据读到之前只显示占位，不出现原作的演示数据 ----------
rep("const TAU = Math.PI * 2, rnd = Math.random;",
    "const TAU = Math.PI * 2, rnd = Math.random;\n"
    "// Verrier：流程数据（verrier_halo_flow.js 写入）。写入之前面板只显示占位\n"
    "const V = { ready: false, feed: [], feedI: 0, push: () => {} };")
rep("const HEAD = ['SOLVER/02',", "const HEAD = ['VERRIER'], HEAD_DEMO = ['SOLVER/02',")
rep("const KEYS = ['dt',", "const KEYS = ['…'], KEYS_DEMO = ['dt',")
rep("const CODE_T = ['load()',", "const CODE_T = ['…'], CODE_T_DEMO = ['load()',")
rep("const CHECKS = [['STABILITY CHECK',", "const CHECKS = [['VERRIER', 'loading run…']], CHECKS_DEMO = [['STABILITY CHECK',")
rep("""function kpiTick() {
  segs.forEach(s => s.style.width = rr(25, 100) + '%');""", """function kpiTick() {
  if (V.ready) return;   // Verrier：读到运行以后是真实的数（vBind 写入），不再随机跳
  segs.forEach(s => s.style.width = rr(25, 100) + '%');
  if (true) return;""")
rep("""function feedPush() {
  const v = pick(VERBS), d = document.createElement('div');""", """function feedPush() {
  if (!V.feed.length) return;   // Verrier：只放这次运行的真实记录（V.push 在 verrier_halo_flow.js 里）
  V.push(...V.feed[V.feedI++ % V.feed.length]);
  if (true) return;
  const v = pick(VERBS), d = document.createElement('div');""")
rep("""const CODE = [['papers', 'load_collection', '()'],""", """const CODE = [['', 'load_run', '()']], CODE_DEMO = [['papers', 'load_collection', '()'],""")
rep("""const ROUTES = ['navier-st', 'settings', 'lbm-d2q9', 'stam-fluid', 'page refs', 'missing'];""",
    """const ROUTES = [], ROUTES_DEMO = ['navier-st', 'settings', 'lbm-d2q9', 'stam-fluid', 'page refs', 'missing'];""")
rep("""  let h = '<span class="h">PAPER</span><span class="h">EXTRACT</span><span class="h">CODE</span><span class="h">CHECK</span>';""",
    """  let h = '<span class="h">DIRECTION</span><span class="h">SEARCH</span><span class="h">READ</span><span class="h">KEEP</span>';""")
rep("""      const cls = j < st ? 'done' : j === st ? (i === 5 ? 'pk' : 'on') : '';""",
    """      const cls = j < st ? 'done' : j === st ? (V.routePink && V.routePink[i] ? 'pk' : 'on') : '';""")
rep("""setInterval(() => { const i = (rnd() * ROUTES.length) | 0; rState[i] = (rState[i] + 1) % 4; renderRoutes(); }, 500);""",
    """setInterval(() => { if (V.ready || !ROUTES.length) return; const i = (rnd() * ROUTES.length) | 0; rState[i] = (rState[i] + 1) % 4; renderRoutes(); }, 500);""")
rep("""const AG = Array.from({ length: 12 },""", """const AG = Array.from({ length: 0 },""")
rep("""  drawAdv(dt); drawDiff(); drawVal(); drawIdx(); agentsTick(dt);""",
    """  if (V.ready) { drawAdv(dt); drawDiff(); drawVal(); drawIdx(); agentsTick(dt); }   // Verrier：读到运行之前面板留空""")

# ---------- 去掉背景音乐 ----------
cut("/* =========================================================\n   BGM — background music", "  if (st.on) play();\n})();\n")

# ---------- 流程：Verrier 自己的脚本（提问、进度、人工确认、结果），单独一个文件，不并进派生页 ----------
rep("</script>\n</body>", '</script>\n<script src="/static/verrier_halo_flow.js"></script>\n</body>')

out = STATIC / "verrier_halo.html"
out.write_text(s, encoding="utf-8")
shutil.copyfile(LIC, STATIC / "haloflux_LICENSE.txt")
print("wrote", out, len(s), "chars; license copied")
