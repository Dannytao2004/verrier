"""v2.7e：显示单位（UNITS_PLAN.md「显示单位」）。终稿的 [[unit]]（钉死的 unit_canonical，没有就用 target.unit）和 FINAL prompt 的要求、
没钉住单位时终稿末尾的说明；ledger 的 Result 行、graph.html 页头、网页结果 JSON 的 estimate.unit；运行 API 的 target；两个页面 JS 的语法。
披萨夹具同 tests/test_coverage.py（字面值，不读 results/）：m1 + 餐馆 + 冷冻的 sum 方法，钉成 t/day，合并 74.72 [35.67, 156.53]。
不联网、不调模型。"""
import json
import shutil
import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest import mock

from triangulate.agent import outputs as O
from triangulate.agent.prompts import FINAL_USER

try:
    import fastapi  # noqa: F401
    import langgraph  # noqa: F401
    HAVE_WEB = True
except ImportError:
    HAVE_WEB = False

STATIC = Path(__file__).resolve().parent.parent / "triangulate" / "web" / "static"
# 终稿模型照 FINAL_USER 的例子写单位
ANSWER = "About [[estimate]] [[unit]] ([[interval_level]] interval [[p10]] to [[p90]] [[unit]])."


class FinalLLM:
    model = "fake"

    def __init__(self, answer=ANSWER):
        self.answer, self.users = answer, {}

    def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
        self.users[role] = user
        return ({"answer": self.answer}, None) if self.answer else (None, "fake failure")


def node(llm, name):
    """graph 的一个节点函数（同 probes/out/stages/_s7_rerender.py）：不跑整张图，直接给 state。"""
    from tests.test_plan_unit import _ctx
    from triangulate.agent import graph as G
    return G.build(_ctx(llm)).builder.nodes[name].runnable.func


def pizza_state(llm) -> dict:
    """披萨夹具走 graph 的 compute 节点和 final 节点（裁判那一轮的方法和假设是字面值）。"""
    from tests.test_coverage import M1, PTS, RAW_A, SUPPLY, TARGET
    st = {"qid": "ask_pizza", "question": "How much pizza do people in Chicago eat per day?", "as_of": "2026-10-17",
          "plan": {"target": dict(TARGET)},
          "points": [dict(p, judged_round=1, direction_id="d1", source_url="https://a.org/x") for p in PTS.values()],
          "judge_rounds": [{"round": 1, "methods": [M1, SUPPLY], "assumptions": RAW_A}],
          "published": {"status": "not_checked"}}
    st.update(node(llm, "compute")(st))
    st.update(node(llm, "final")(st))
    return st


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestPizzaUnitShown(unittest.TestCase):
    def test_final_text_and_prompt(self):
        llm = FinalLLM()
        st = pizza_state(llm)
        r, f = st["compute"]["result"], st["final"]
        self.assertAlmostEqual(r["central"], 74.72, delta=0.01)
        self.assertEqual(f["placeholders"]["unit"], "t/day")
        self.assertEqual(f["text"].split("\n\n")[0], "About 74.72 t/day (80% model-based interval 35.67 to 157 t/day).")
        self.assertNotIn("Unit not pinned", f["text"])
        user = llm.users["final"]
        self.assertIn("[[p90]], [[unit]], [[interval_level]]", user)          # 占位符清单里有 [[unit]]
        self.assertIn("Write [[unit]] (the target unit) right after the estimate and right after the interval", user)
        self.assertIn('"unit_canonical": "t/day"', user)

    def test_default_text_when_the_final_model_fails(self):
        st = pizza_state(FinalLLM(answer=None))
        self.assertTrue(st["final"]["text"].startswith(
            "Estimate: 74.72 t/day (80% model-based interval 35.67 to 157 t/day, basis: too few backtest years"), st["final"]["text"])

    def test_ledger_graph_header_and_result_api(self):
        from fastapi.testclient import TestClient

        from triangulate.agent import pipeline as P
        from triangulate.agent import run as R
        from triangulate.web.app import create_app
        st = pizza_state(FinalLLM())
        tmp = Path(tempfile.mkdtemp())
        out_dir = tmp / "ask_pizza" / "web_1"
        out_dir.mkdir(parents=True)
        h = {"q": {"id": "ask_pizza", "question": st["question"], "as_of": st["as_of"]},
             "g": NS(get_state=lambda cfg: NS(values=st)), "cfg": {}, "ctx": NS(budget=P.Budget(), llm=NS(model="fake")),
             "out_dir": out_dir, "stamp": "x", "tag": "web_1", "leak_values": None, "ablate": False, "t0": time.time()}
        try:
            with mock.patch("builtins.print"):
                R.save_run(h, [])
            page = (out_dir / "graph.html").read_text(encoding="utf-8")
            c = TestClient(create_app(res=tmp), base_url="http://127.0.0.1")
            res = c.get("/api/result", params={"qid": "ask_pizza", "tag": "web_1"}).json()
            led = c.get("/api/file", params={"qid": "ask_pizza", "tag": "web_1", "name": "ledger.md"}).text
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertIn("estimate <b>75</b> t/day &middot; 80% [36, 157] t/day (monte_carlo: ", page)
        self.assertEqual(res["estimate"]["unit"], "t/day")
        self.assertAlmostEqual(res["estimate"]["central"], 74.72, delta=0.01)
        self.assertIn("About 74.72 t/day", res["final_text"])
        self.assertIn("Result: central **74.72** t/day, 80% interval [35.67, 157] t/day, basis monte_carlo (", led)


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestGraphRuns(unittest.TestCase):
    def test_unpinned_run_falls_back_to_target_unit_and_says_so(self):
        """tests/test_web.FakeLLM 的规划没有 unit_canonical（U1 记 plan note）：[[unit]] 用 target.unit，终稿末尾写明没钉住。"""
        from tests.test_plan_unit import graph_run, unit_notes
        from tests.test_web import FakeLLM
        from triangulate.agent.graph import UNIT_NOT_PINNED
        st = graph_run(FakeLLM())
        f = st["final"]
        self.assertTrue(unit_notes(st)[0].startswith("unit not pinned: "))
        self.assertEqual(f["placeholders"]["unit"], "widgets")
        self.assertTrue(f["text"].startswith("About 1,210 widgets.\n\nKey assumptions: none"), f["text"])
        self.assertTrue(f["text"].endswith("\n\n" + UNIT_NOT_PINNED))
        self.assertTrue(f["template"].endswith("\n\n" + UNIT_NOT_PINNED))

    def test_pinned_run_through_the_api(self):
        """网页运行（真的图 + 假模型，同 tests/test_web.TestApiRuns），规划钉 widget：运行 API 的 target 带 unit_canonical
        （经典界面运行页、控制台的「代码计算」从这里取单位），结果 API 的 estimate.unit 是 widget，终稿在估计值和区间后面写单位。"""
        from fastapi.testclient import TestClient

        import tests.test_web as TW
        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        from triangulate.web.app import create_app
        from triangulate.web.runs import Registry

        class LLM(TW.FakeLLM):
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                out, err = super().ask(system, user, role=role, qid=qid, max_tokens=max_tokens, tries=tries)
                if role == "plan":
                    out["target"]["unit_canonical"] = "widget"
                return ({"answer": ANSWER}, None) if role == "final" else (out, err)

        tmp = Path(tempfile.mkdtemp())
        reg = Registry(prepare=TW.make_prepare(tmp), max_active=1)
        c = TestClient(create_app(reg, res=tmp), base_url="http://127.0.0.1")
        try:
            with mock.patch.object(TW, "FakeLLM", LLM), mock.patch.object(P, "fetch_page", TW.fake_fetch), \
                    mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
                rid = c.post("/api/runs", json={"question": "How many widgets in June 2026?", "as_of": "2026-06-20"}).json()["id"]
                TW.wait_for(c, rid, ("awaiting_approval",))
                c.post(f"/api/runs/{rid}/approve", json={})
                run = TW.wait_for(c, rid, ("done", "failed"))
                res = c.get("/api/result", params=run["result"]).json()
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(run["status"], "done", run.get("error"))
        self.assertEqual(run["target"]["unit_canonical"], "widget")
        self.assertAlmostEqual(run["compute"]["central"], 1210.0)
        self.assertEqual(res["estimate"]["unit"], "widget")
        self.assertTrue(res["final_text"].startswith("About 1,210 widget (80% model-based interval 1,071 to 1,367 widget)."),
                        res["final_text"])
        self.assertNotIn("Unit not pinned", res["final_text"])


class TestSavedRunsAndPages(unittest.TestCase):
    def test_saved_run_without_unit_canonical(self):
        """已存的运行没有 unit_canonical、终稿里没有 [[unit]]：estimate.unit 用 target.unit，终稿原样；没有单位时什么都不加。"""
        from tests.test_web import _state
        from triangulate.web.results import result_view
        v = result_view(_state(), "ask_x", "web_1")
        self.assertEqual(v["estimate"]["unit"], "widgets")
        self.assertEqual(v["final_text"], "About 1,000 widgets.")
        self.assertEqual(result_view({"compute": {}}, "t")["estimate"]["unit"], "")
        self.assertIn("Result: central **1,000** widgets, 80% interval [800, 1,250] widgets, basis monte_carlo (",
                      O.ledger(_state(), None))
        self.assertEqual(O.unit_text({"unit": " widgets ", "unit_canonical": ""}), "widgets")
        self.assertEqual(O.unit_text({"unit": "widgets", "unit_canonical": "widget"}), "widget")
        self.assertEqual(O.unit_text(None), "")

    def test_final_prompt_example_uses_only_known_placeholders(self):
        from triangulate.agent.graph import PLACEHOLDER
        self.assertEqual(set(PLACEHOLDER.findall(FINAL_USER)), {"unit", "estimate", "interval_level", "p10", "p90"})

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_js_syntax(self):
        for name in ("app.js", "verrier_console.js"):
            out = subprocess.run(["node", "--check", str(STATIC / name)], capture_output=True, text=True)
            self.assertEqual(out.returncode, 0, out.stderr)


if __name__ == "__main__":
    unittest.main()
