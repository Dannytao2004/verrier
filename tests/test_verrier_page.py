"""Verrier 页面 + 控制台（/verrier）：路由、静态文件、JS 语法、证据页（P1）、依赖图（P2）。不联网、不调模型。"""
import json
import re
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
                     "/api/result", "/api/saved", "/api/file", "/api/graph"):
            self.assertIn(path, routes)
        for used in ('"/api/runs"', "/api/runs/", "/approve", "/cancel", "/api/result?", '"/api/saved"', "/api/file?", "/api/graph?"):
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

    def test_graph_route_and_link(self):
        """P2：交付页的「依赖图」进控制台的 #console/graph/<qid>/<tag>（不再新开 graph.html），图纸由 verrier_graph.js 画。"""
        html = self.c.get("/verrier").text
        gr, con = '<script src="/static/verrier_graph.js"></script>', '<script src="/static/verrier_console.js"></script>'
        self.assertIn(gr, html)
        self.assertLess(html.index(gr), html.index(con))
        self.assertEqual(self.c.get("/static/verrier_graph.js").status_code, 200)
        js = (STATIC / "verrier_console.js").read_text(encoding="utf-8")
        for s in ('parts[1] === "graph" && parts[2] ? viewGraph(parts[2], parts[3] || "", tok)',
                  'href="#console/graph/${encodeURIComponent(qid)}/${encodeURIComponent(tag || "")}">${T("Dependency graph", "依赖图")}',
                  "api(`/api/graph?qid=${encodeURIComponent(qid)}&tag=${encodeURIComponent(tag)}`)",
                  "window.VERRIER_GRAPH.draw(g)", "window.VERRIER_GRAPH.detail(g, id)"):
            self.assertIn(s, js)
        self.assertNotIn('fileHref(qid, tag, "graph.html")', js)


@unittest.skipUnless(shutil.which("node"), "node not installed")
class TestConsoleJsSyntax(unittest.TestCase):
    def test_node_check(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_console.js")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)

    def test_node_check_evidence(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_evidence.js")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)

    def test_node_check_graph(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_graph.js")], capture_output=True, text=True)
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
                  f'<span class="cx-bad">{esc(TC.PART_ERR)}</span>', "Target lock", '<span class="cx-unit">t/day</span>'):
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


@unittest.skipUnless(HAVE_WEB, "fastapi not installed (use .venv)")
class TestGraphApi(unittest.TestCase):
    """P2：GET /api/graph 返回保存运行的 outputs.dep_graph（和 graph.html 同一个函数），找不到时和 /api/result 一样 404。"""

    def setUp(self):
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        self.c = TestClient(create_app(), base_url="http://127.0.0.1")

    def test_saved_run_and_404(self):
        from triangulate.agent.outputs import dep_graph
        from triangulate.web import results as R
        r = self.c.get("/api/graph", params={"qid": "fc_jp_births_2026_07", "tag": "test1"})
        self.assertEqual(r.status_code, 200)
        g = r.json()
        self.assertEqual(g, json.loads(json.dumps(R.clean(dep_graph(R.load_state("fc_jp_births_2026_07", "test1"))))))
        self.assertEqual({n["kind"] for n in g["nodes"]}, {"source", "point", "assumption", "method", "target"})
        self.assertEqual((len(g["nodes"]), len(g["edges"])), (23, 25))
        for p in ({"qid": "nope", "tag": ""}, {"qid": "fc_jp_births_2026_07", "tag": "nope"}, {"qid": "..", "tag": ""},
                  {"qid": "fc_jp_births_2026_07", "tag": "../x"}):
            a, b = self.c.get("/api/graph", params=p), self.c.get("/api/result", params=p)
            self.assertEqual((a.status_code, a.json()), (404, b.json()))

    def test_source_ids_are_unique(self):
        """published2 有一个网址被两个方向取过：P2 之前这个网址的来源节点拿到 S:5，和下一个新网址撞号（51 个保存的运行里 40 个有这种撞号）。
        现在每个网址一个 id，来源 -> 数据点的边都从这个点的 source_url 对应的节点出发。"""
        g = self.c.get("/api/graph", params={"qid": "ask_a63174a0", "tag": "published2"}).json()
        ids = [n["id"] for n in g["nodes"]]
        self.assertEqual(len(ids), len(set(ids)))
        url = {n["id"]: n["detail"]["url"] for n in g["nodes"] if n["kind"] == "source"}
        self.assertEqual(sorted(url), ["S:1", "S:2", "S:3", "S:4"])
        pts = {n["id"]: n["detail"] for n in g["nodes"] if n["kind"] == "point"}
        src_edges = [e for e in g["edges"] if e["from"].startswith("S:")]
        self.assertEqual(len(src_edges), 73)
        for e in src_edges:
            self.assertEqual(url[e["from"]], pts[e["to"]]["source_url"])


# node 里加载 verrier_graph.js：画出整张图，并给每个节点画侧栏详情（和浏览器里同一个函数）
NODE_GRAPH = ("globalThis.window = globalThis; require(process.argv[1]); const g = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8')); "
              "process.stdout.write(JSON.stringify({html: window.VERRIER_GRAPH.draw(g), "
              "detail: Object.fromEntries(g.nodes.map(n => [n.id, window.VERRIER_GRAPH.detail(g, n.id)]))}));")
# 10-18 起节点画成星球（verrier_graph.js 的 planet）：从外圈 pl-limb 的圆心和半径还原列的 x（星球轴线离列左边 AX = 44）、行的上沿和行高
NODE_RE = (r'<g class="g-n g-(\w+)((?: dash| red)*)" data-id="([^"]*)">(?:(?!<g class="g-n).)*?'
           r'<circle class="pl-limb" cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"/>')


def draw(graph):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "g.json"
        p.write_text(json.dumps(graph), encoding="utf-8")
        out = subprocess.run(["node", "-e", NODE_GRAPH, str(STATIC / "verrier_graph.js"), str(p)], capture_output=True, text=True,
                             encoding="utf-8")
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout)


@unittest.skipUnless(HAVE_WEB and shutil.which("node"), "fastapi or node not installed")
class TestGraphView(unittest.TestCase):
    @staticmethod
    def nodes(html):
        out = {}
        for m in re.findall(NODE_RE, html, re.S):
            cx, cy, r = float(m[3]), float(m[4]), float(m[5])
            h = max(2 * r, 28)
            out[m[2]] = {"kind": m[0], "cls": m[1].split(), "x": round(cx - 44), "y": cy - h / 2, "h": h, "r": r}
        return out

    def test_published_run_drawing(self):
        """已提交的 ask_a63174a0/published1（结果是已公布的 p52）：四列，每个节点和每条边都画出来；没连到目标的方法和裁判丢弃的点是虚线，
        p52、它连到目标的边和目标是红色；每列按右边邻居的平均 y 排过（右边没有邻居的在最后）、不重叠；侧栏是表格，不是 JSON。"""
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        g = TestClient(create_app(), base_url="http://127.0.0.1").get("/api/graph", params={"qid": "ask_a63174a0", "tag": "published1"}).json()
        out = draw(g)
        h, ns = out["html"], self.nodes(out["html"])
        self.assertEqual(set(ns), {n["id"] for n in g["nodes"]})
        self.assertEqual({k: {n["x"] for n in ns.values() if n["kind"] == k} for k in ("source", "point", "method", "target")},
                         {"source": {12}, "point": {334}, "method": {656}, "target": {978}})
        self.assertEqual(h.count('<path class="g-e'), len(g["edges"]))
        failed = {n["id"] for n in g["nodes"] if n["kind"] == "method" and n["detail"]["estimate"] is None}
        discarded = {n["id"] for n in g["nodes"] if n["kind"] == "point" and not n["detail"]["keep"]}
        self.assertEqual(failed, {"M:m3"})
        self.assertEqual(len(discarded), 159)
        self.assertEqual({i for i, n in ns.items() if "dash" in n["cls"]}, failed | discarded)
        self.assertEqual({i for i, n in ns.items() if "red" in n["cls"]}, {"P:p52", "target"})
        self.assertEqual(h.count('<path class="g-e red"'), 1)
        mid = {i: n["y"] + n["h"] / 2 for i, n in ns.items()}
        right = {}
        for e in g["edges"]:
            right.setdefault(e["from"], []).append(mid[e["to"]])
        deg = {}
        for e in g["edges"]:
            deg[e["from"]] = deg.get(e["from"], 0) + 1
            deg[e["to"]] = deg.get(e["to"], 0) + 1
        for i, n in ns.items():   # 星球半径按连线数：7 + 5·√连线数，最大 40
            self.assertAlmostEqual(n["r"], min(40, 7 + 5 * deg.get(i, 0) ** .5), delta=.06, msg=i)
        for x in (12, 334, 656):
            col = sorted((n["y"], i) for i, n in ns.items() if n["x"] == x)
            keys = [sum(right[i]) / len(right[i]) if i in right else float("inf") for _, i in col]
            self.assertEqual(keys, sorted(keys), x)
            self.assertTrue(all(b[0] >= a[0] + ns[a[1]]["h"] - .2 for a, b in zip(col, col[1:])), x)   # 同一列不重叠（坐标取一位小数）
        d = out["detail"]
        self.assertIn("Published value", d["P:p52"])
        self.assertIn("<th>quote</th><td>350,536 new cars were registered in September, up from 312,891 during the same month last year</td>",
                      d["P:p52"])
        self.assertIn('<a href="https://www.fleetnews.co.uk/news/fleet-registrations-pass-one-million-as-september-market-grows-121"', d["P:p52"])
        self.assertIn("Not in the combined estimate", d["M:m3"])
        self.assertIn("Discarded by the judge", d["P:p1"])
        self.assertIn("<th>basis</th><td>published</td>", d["target"])
        for x in d.values():
            self.assertNotIn('{"', x)

    def test_pizza_fixture(self):
        """披萨题的字面值夹具（tests/test_coverage，不读 results/）：m3 只覆盖冷冻、不进合并 -> 虚线、不连到目标；目标 74.72，m1 64.79。"""
        from tests import test_coverage as TC
        from triangulate.agent.outputs import dep_graph
        from triangulate.web import results as R
        comp = TC.run([TC.M1, TC.SUPPLY, dict(TC.M3, coverage=TC.PART)])
        st = {"plan": {"target": TC.TARGET}, "compute": comp, "points": [dict(p, direction_id="d1") for p in TC.PTS.values()],
              "assumptions": TC.A.validate(TC.RAW_A, TC.TARGET)}
        g = json.loads(json.dumps(R.clean(dep_graph(st))))
        out = draw(g)
        ns = self.nodes(out["html"])
        self.assertEqual({i for i, n in ns.items() if "dash" in n["cls"]}, {"M:m3"})
        self.assertNotIn({"from": "M:m3", "to": "target"}, g["edges"])
        self.assertRegex(out["html"], r'(?s)<g class="g-n g-target" data-id="target">(?:(?!<g class="g-n).)*?<text x="\d+" y="[\d.]+">74\.72</text>')
        self.assertRegex(out["html"], r'(?s)data-id="M:m1">(?:(?!<g class="g-n).)*?<text x="\d+" y="[\d.]+">64\.79</text>')
        self.assertIn("Not in the combined estimate", out["detail"]["M:m3"])
        self.assertIn("<th>factor</th><td>0.000002738</td>", out["detail"]["M:m2"])

    def test_every_string_is_escaped(self):
        """标签、id、详情都来自网页或模型：每个字符串和字典键前面加一段 HTML，画出来（图和每个节点的侧栏）不能有原样的标签。"""
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        evil = '<img src=x onerror="alert(1)">'

        def poison(x):
            if isinstance(x, str):
                return evil + x
            if isinstance(x, list):
                return [poison(v) for v in x]
            if isinstance(x, dict):
                return {evil + k: poison(v) for k, v in x.items()}
            return x
        g = TestClient(create_app(), base_url="http://127.0.0.1").get("/api/graph", params={"qid": "fc_jp_births_2026_07", "tag": "test1"}).json()
        bad = {"nodes": [{"id": evil + n["id"], "kind": n["kind"], "label": evil + n["label"], "detail": poison(n["detail"])} for n in g["nodes"]],
               "edges": [{"from": evil + e["from"], "to": evil + e["to"]} for e in g["edges"]]}
        out = draw(bad)
        for h in [out["html"], *out["detail"].values()]:
            self.assertNotIn("<img", h)
        self.assertEqual(out["html"].count('<path class="g-e'), len(g["edges"]))
        self.assertGreater(sum(h.count(esc(evil)) for h in out["detail"].values()), 500)


if __name__ == "__main__":
    unittest.main()
