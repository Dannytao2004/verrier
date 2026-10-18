"""Verrier 页面 + 控制台（/verrier）：路由、静态文件、JS 语法、证据页（P1）。不联网、不调模型。"""
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

try:
    import fastapi  # noqa: F401
    HAVE_WEB = True
except ImportError:
    HAVE_WEB = False

STATIC = Path(__file__).resolve().parents[1] / "triangulate" / "web" / "static"


@unittest.skipUnless(HAVE_WEB, "fastapi not installed (use .venv)")
class TestVerrierPage(unittest.TestCase):
    def setUp(self):
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        self.c = TestClient(create_app(), base_url="http://127.0.0.1")

    def test_route_serves_console_page(self):
        r = self.c.get("/verrier")
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.headers["content-type"].startswith("text/html"))
        for s in ('id="cx"', 'id="cxBody"', "MISSION CONTROL", "/static/verrier_console.js", 'href="#console"', "mission: setMission",
                  'class="ask" id="askBtn" href="#console"', 'id="askView"'):
            self.assertIn(s, r.text)
        # 右下角原来的 HUD（ORBIT SOLVER）已换成提问按钮，场景脚本里也不再引用它的元素
        for gone in ('class="hud"', "hudPh", "hudSig", "ORBIT SOLVER"):
            self.assertNotIn(gone, r.text)
        self.assertEqual(self.c.get("/static/verrier_console.js").status_code, 200)

    def test_classic_app_unchanged(self):
        r = self.c.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn('<script src="/static/app.js"></script>', r.text)
        self.assertNotIn("verrier_console", r.text)

    def test_console_uses_only_existing_api_routes(self):
        js = (STATIC / "verrier_console.js").read_text(encoding="utf-8")
        routes = {r.path for r in self.c.app.routes}
        for path in ("/api/runs", "/api/runs/{run_id}", "/api/runs/{run_id}/approve", "/api/runs/{run_id}/cancel",
                     "/api/result", "/api/saved", "/api/file"):
            self.assertIn(path, routes)
        for used in ('"/api/runs"', "/api/runs/", "/approve", "/cancel", "/api/result?", '"/api/saved"', "/api/file?"):
            self.assertIn(used, js)

    def test_evidence_route_and_link(self):
        """P1：交付页的「证据、方法和假设」进控制台的 #console/evidence/<qid>/<tag>（不再开经典界面的结果页），返回按钮回到交付页。"""
        html = self.c.get("/verrier").text
        ev, con = '<script src="/static/verrier_evidence.js"></script>', '<script src="/static/verrier_console.js"></script>'
        self.assertIn(ev, html)
        self.assertLess(html.index(ev), html.index(con))   # 面板函数先加载
        self.assertEqual(self.c.get("/static/verrier_evidence.js").status_code, 200)
        js = (STATIC / "verrier_console.js").read_text(encoding="utf-8")
        for s in ('parts[1] === "evidence" && parts[2] ? viewEvidence(parts[2], parts[3] || "", tok)',
                  'href="#console/evidence/${encodeURIComponent(qid)}/${encodeURIComponent(tag || "")}"',
                  'href="#console/result/${encodeURIComponent(qid)}/${encodeURIComponent(tag)}"', "window.VERRIER_EVIDENCE(r, qid, tag)"):
            self.assertIn(s, js)
        self.assertNotIn("/#/result?", js)


@unittest.skipUnless(shutil.which("node"), "node not installed")
class TestConsoleJsSyntax(unittest.TestCase):
    def test_node_check(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_console.js")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)

    def test_node_check_evidence(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_evidence.js")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)


# node 里加载 verrier_evidence.js，把 /api/result 的 JSON 画成 HTML（和浏览器里同一个函数）
NODE_RENDER = ("globalThis.window = globalThis; require(process.argv[1]); const [r, qid, tag] = "
               "JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8')); process.stdout.write(window.VERRIER_EVIDENCE(r, qid, tag));")


def esc(s):
    """和 JS 里的 esc 相同的转义。"""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")


def render(result, qid, tag):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "r.json"
        p.write_text(json.dumps([result, qid, tag]), encoding="utf-8")
        out = subprocess.run(["node", "-e", NODE_RENDER, str(STATIC / "verrier_evidence.js"), str(p)],
                             capture_output=True, text=True, encoding="utf-8")
    assert out.returncode == 0, out.stderr
    return out.stdout


@unittest.skipUnless(HAVE_WEB and shutil.which("node"), "fastapi or node not installed")
class TestEvidenceView(unittest.TestCase):
    def test_saved_run_renders_every_section(self):
        """保存的运行（仓库里只读的 fc_jp_births_2026_07/test1），在进程内走 /api/result，再用证据页的函数画出来：每一节的内容都在。"""
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        r = TestClient(create_app(), base_url="http://127.0.0.1").get("/api/result", params={"qid": "fc_jp_births_2026_07", "tag": "test1"})
        self.assertEqual(r.status_code, 200)
        v = r.json()
        self.assertTrue(v["methods"] and all(m["unit_check"] is None for m in v["methods"]))   # 已存的运行没有钉单位
        h = render(v, "fc_jp_births_2026_07", "test1")
        for code in ("E-01", "E-02", "E-03", "E-04", "E-05", "E-06", "E-07", "E-08"):
            self.assertIn(f"<span>{code} · ", h)
        self.assertIn('<section class="card cx-ev"><div class="bh">', h)
        self.assertIn('62,965 <span style="font-size:.4em;font-stretch:100%;letter-spacing:0">births</span>', h)
        self.assertIn("80% model-based [30,888, 128,351] births", h)
        self.assertIn(esc(v["estimate"]["basis_text"]), h)
        self.assertIn("OFFICIAL <b>62,479</b>", h)
        self.assertIn(f'<pre class="cx-answer">{esc(v["final_text"])}</pre>', h)
        self.assertIn(esc(v["target"]["what"]), h)
        for m in v["methods"]:
            self.assertIn(f'<code class="cx-f">{esc(m["formula"])}</code>', h)
            for i in m["inputs"]:
                self.assertIn(f"<td><b>{esc(i['name'])}</b> = {esc(i['id'])}</td><td>{esc(i['role'])}</td>", h)
        for p in v["repairs"]:
            for e in p["errors"]:
                self.assertIn(f"<li>{esc(e)}</li>", h)
        for a in v["assumptions"]:
            for k in ("rationale", "falsified_by"):
                self.assertIn(f"<td>{esc(a[k])}</td>", h)
        for p in v["evidence"]["kept"] + v["evidence"]["discarded"]:
            self.assertIn(f'<td class="cx-qt">{esc(p["quote"])}</td>', h)
            self.assertIn(f'href="{esc(p["source_url"])}"', h)
        for x in v["leakage"]["residual_risks"]:
            self.assertIn(f"<li>{esc(x)}</li>", h)
        for d in v["directions"]:
            self.assertIn(esc(d["hypothesis"]), h)

    def test_pizza_units_and_coverage(self):
        """披萨题的字面值夹具（tests/test_coverage，不读 results/）：钉成 t/day，m1 g/day、餐馆 + 冷冻的 sum 方法 kg/year 进合并，
        m3 只覆盖冷冻、不进合并；证据页显示单位检查、覆盖范围和 m3 只作参考的估计。"""
        from tests import test_coverage as TC
        from triangulate.web import results as R
        comp = TC.run([TC.M1, TC.SUPPLY, dict(TC.M3, coverage=TC.PART)])
        st = {"qid": "q", "question": "pizza", "as_of": "2026-10-17", "plan": {"target": TC.TARGET}, "compute": comp,
              "points": list(TC.PTS.values()), "assumptions": TC.A.validate(TC.RAW_A, TC.TARGET)}
        v = R.clean(R.result_view(st, "q"))
        uc = {m["id"]: m["unit_check"] for m in v["methods"]}
        self.assertEqual((uc["m1"]["unit"], uc["m1"]["target_unit"]), ("g/day", "t/day"))
        self.assertAlmostEqual(uc["m1"]["factor"] * 1e6, 1, places=12)
        self.assertEqual((uc["m2"]["unit"], uc["m3"]["unit"]), ("kg/year", "kg/year"))
        self.assertAlmostEqual(uc["m2"]["factor"] * 365250, 1, places=12)
        h = render(v, "q", "")
        for s in ("74.72 <span", "80% model-based [35.67, 157] t/day", "<b>64.79</b>", "<b>86.18</b>",
                  "Unit check</span><span class=\"zh\">单位检查</span></span> g/day → t/day × 0.000001</span>",
                  "kg/year → t/day × 0.000002738", "sum over channel: restaurant + frozen_retail",
                  "only frozen_retail of channel (siblings: restaurant, other)", "(reference only)", "22.29 · P10..P90 10.21..48.6",
                  f'<span class="cx-bad">{esc(TC.PART_ERR)}</span>', "Pinned unit"):
            self.assertIn(s, h)
        self.assertEqual(h.count('<div class="cx-dir ok">'), 2)
        self.assertEqual(h.count('<div class="cx-dir bad">'), 1)

    def test_every_string_is_escaped(self):
        """引文、名字、单位、URL 都来自网页或模型：每个字符串（和以数据为键的字典的键）前面加一段 HTML，画出来不能出现原样的标签。"""
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        evil = '<img src=x onerror="alert(1)">'

        def poison(x, key=None):
            if isinstance(x, str):
                return evil + x
            if isinstance(x, list):
                return [poison(v) for v in x]
            if isinstance(x, dict):
                keyed = key in ("dropped_by_code", "distribution", "target_series", "signal_series")
                return {(evil + k if keyed else k): poison(v, k) for k, v in x.items()}
            return x
        c = TestClient(create_app(), base_url="http://127.0.0.1")
        for qid, tag in (("fc_jp_births_2026_07", "test1"), ("ask_0e2d5021", "discrete2")):
            v = c.get("/api/result", params={"qid": qid, "tag": tag}).json()
            h = render(poison(v), evil + qid, evil + tag)
            self.assertNotIn("<img", h)
            self.assertGreater(h.count(esc(evil)), 50)


if __name__ == "__main__":
    unittest.main()
