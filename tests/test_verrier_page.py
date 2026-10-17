"""Verrier 页面 + 控制台（/verrier）：路由、静态文件、JS 语法。不联网、不调模型。"""
import shutil
import subprocess
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
        for s in ('id="cx"', 'id="cxBody"', "MISSION CONTROL", "/static/verrier_console.js", 'href="#console"', "mission: setMission"):
            self.assertIn(s, r.text)
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


@unittest.skipUnless(shutil.which("node"), "node not installed")
class TestConsoleJsSyntax(unittest.TestCase):
    def test_node_check(self):
        out = subprocess.run(["node", "--check", str(STATIC / "verrier_console.js")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)


if __name__ == "__main__":
    unittest.main()
