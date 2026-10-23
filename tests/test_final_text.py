"""v2.6d 终稿数字出口（D4、F1、F2、N32、N33、N34）和 score_all 去掉「去年同月」臂（N44）。
scrub_digits 保留离 as_of ±10 年、不贴字母数字的四位年份、Q1–Q4 / H1–H2、方法用到的点 id；方法用到的观测点有 p{n}_value 占位符；
区间依据用 outputs.BASIS_TEXT（终稿、ledger、graph.html 页头、网页共用）；state.final 存模型原文 model_text。
不联网、不调模型（假搜索、假取页、假模型）。"""
import json
import shutil
import tempfile
import time
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate.agent import outputs as O
from triangulate.agent import pipeline as P

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

ANSWER = ("About [[estimate]] widgets in Q3 2026 ([[interval_level]] interval [[p10]] to [[p90]], basis: [[interval_basis]]). "
          "The observed 2025 monthly total in point p4 ([[p4_value]]) drives m1; p1 is not an input; roughly 1,234 more.")
# 点 p1..p6：往年 6 月和 2025、2026 年 5 月。v2.12：裁判用 series_auto（series_naive 只作对照基线），yoy1 = 6 月 1,210 x
# 2026 年 5 月 / 2025 年 5 月（1,000 / 1,000）；方法的输入是用到的 3 个月 p4、p5、p6，p1..p3 不是
YEARS = ((2022, 6, 30, "June", 950), (2023, 6, 30, "June", 1000), (2024, 6, 30, "June", 1100), (2025, 6, 30, "June", 1210),
         (2025, 5, 31, "May", 1000), (2026, 5, 31, "May", 1000))


def _graph_run(tmp: Path):
    """假模型跑一遍连续值的图再 save_run 到 tmp；返回 (state, 终稿的 system / user prompt)。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import run as R
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    seen = {}

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            if role == "plan":
                return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30",
                                   "publisher": "X"}, "market_keywords": [],
                        "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
            if role.startswith("extract"):
                return {"points": [{"name": f"widgets {mon} {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                    "period_start": f"{y}-{mo:02d}-01", "period_end": f"{y}-{mo:02d}-{d}",
                                    "quote": f"{mon} {y}: {v:,} widgets"} for y, mo, d, mon, v in YEARS]}, None
            if role.startswith("judge"):
                return {"decisions": [], "extra_directions": [],
                        "methods": [{"id": "m1", "method": "series_auto",
                                     "params": {"target_history": ["p2", "p3", "p4", "p5", "p6"]}}]}, None
            if role == "audit":
                return {"methods": []}, None
            if role == "final":
                seen["system"], seen["user"] = system, user
                return {"answer": ANSWER}, None
            raise AssertionError(role)

    class FakeSearcher:
        def search(self, prompt, *, role, qid, max_uses=3, cap=5):
            return {"queries": ["q"], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}

    def fake_fetch(url, as_of, qid, **kw):
        return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                "text": " ".join(f"{mon} {y}: {v:,} widgets." for y, _, _, mon, v in YEARS)}

    ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
    with mock.patch.object(P, "fetch_page", fake_fetch), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "ft1"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        h = {"q": {"id": "t", "question": ctx.question, "as_of": ctx.as_of_s}, "g": g, "cfg": cfg, "ctx": ctx,
             "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": None, "ablate": False, "t0": time.time()}
        st = R.save_run(h, [])
    return st, seen


class TestScrubDigits(unittest.TestCase):
    def test_years_quarters_and_point_ids_kept(self):
        from triangulate.agent.graph import scrub_digits
        self.assertEqual(scrub_digits("observed 2025 monthly total", 2026), ("observed 2025 monthly total", 0))
        self.assertEqual(scrub_digits("Q3 2026", 2026), ("Q3 2026", 0))
        self.assertEqual(scrub_digits("H1 2026 and H2 2025", 2026), ("H1 2026 and H2 2025", 0))
        self.assertEqual(scrub_digits("point p12 and p13", 2026, {"p12"}), ("point p12 and p[n]", 1))
        self.assertEqual(scrub_digits("point p12", 2026), ("point p[n]", 1))          # p12 不是方法用到的点：照旧替换

    def test_other_digits_still_replaced(self):
        from triangulate.agent.graph import scrub_digits
        self.assertEqual(scrub_digits("FY2025, 2025s, 2025-26", 2026)[0], "FY[n], [n]s, 2025-[n]")   # 贴着字母；连字符后的两位数
        self.assertEqual(scrub_digits("in 2014 and 2040", 2026)[0], "in [n] and [n]")                # 离 as_of 超过 10 年
        self.assertEqual(scrub_digits("Q5, q3, FAQ3, H3", 2026)[0], "Q[n], q[n], FAQ[n], H[n]")
        self.assertEqual(scrub_digits("about 1,234 or 2,025 or 2025.5", 2026)[0], "about [n] or [n] or [n]")


class TestBasisText(unittest.TestCase):
    def test_mapping(self):
        self.assertEqual(set(O.BASIS_TEXT), {"historical_errors", "method_spread", "monte_carlo", "no_basis", "no_method",
                                             "published", "series_calibration", "backtest_t", "blocks", "blocks_disagree"})
        for k, v in O.BASIS_TEXT.items():
            self.assertEqual(O.basis_text(k), v)
            self.assertFalse(any(c.isdigit() for c in v), v)                       # 说明里不写数字
            self.assertFalse(v.endswith(".") or "(" in v or v[0].isupper(), v)     # 嵌在句中用
        self.assertEqual(O.basis_text("outcome_probabilities"), "outcome probabilities")   # 表里没有的值照旧
        self.assertEqual(O.basis_text(None), "")

    def test_ledger_result_line(self):
        st = {"qid": "t", "question": "q", "as_of": "2026-06-20", "plan": {"target": {}},
              "compute": {"result": {"central": 100.0, "p10": 80.0, "p90": 125.0, "basis": "no_basis", "weight_rule": "equal",
                                     "weights": {}}, "methods": []}}
        self.assertIn(f"basis no_basis ({O.BASIS_TEXT['no_basis']}), weight rule equal", O.ledger(st, None))

    def test_ledger_without_basis(self):
        # compute 之前就中止（compute 为空）：basis 是 None，说明是空串，Result 行和 v2.6c 一样，不出现空括号
        st = {"qid": "t", "question": "q", "as_of": "2026-06-20", "plan": {"target": {}}, "compute": {}, "aborted": "budget"}
        led = O.ledger(st, None)
        self.assertIn("Result: central **n/a**, 80% interval [n/a, n/a], basis None, weight rule None", led)
        self.assertNotIn("()", led)


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestFinalText(unittest.TestCase):
    def test_continuous_final(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            st, seen = _graph_run(tmp)
            page = (tmp / "graph.html").read_text(encoding="utf-8")
            ledger = (tmp / "ledger.md").read_text(encoding="utf-8")
            saved = json.loads((tmp / "state.json").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        f, r = st["final"], st["compute"]["result"]
        self.assertEqual(r["basis"], "series_calibration")   # v2.12：只有一个 series_auto，区间用它的校准行
        basis = O.BASIS_TEXT["series_calibration"]
        self.assertEqual(f["placeholders"]["interval_level"], "80% model-based")
        self.assertEqual(f["placeholders"]["interval_basis"], basis)
        # 方法用到的点有占位符（值 + 单位）：series_auto 用到的 3 个月 p4–p6（按月份排）；p1..p3 没被方法用到，没有
        self.assertEqual(f["placeholders"]["p4_value"], "1,210 widgets")
        self.assertEqual(f["placeholders"]["p5_value"], "1,000 widgets")
        for k in ("p1_value", "p2_value", "p3_value"):
            self.assertNotIn(k, f["placeholders"])
        self.assertIn("[[p5_value]], [[p4_value]], [[p6_value]]", seen["user"])
        self.assertIn("- observed point p4 (input of m1): widgets June 2025, value 1,210 widgets, period 2025-06-01..2025-06-30",
                      seen["user"])
        self.assertIn(f"combined estimate 1,210, 80% model-based interval 1,008 to 1,485 (basis: {basis})", seen["user"])
        # v2.12（决定 8）：summary 里有方法细节和块结构；终稿末尾有代码写的「Method details」，数字走占位符
        self.assertIn("  details: m1 series_auto, yoy path: yoy1: last year's same month x the year-on-year growth", seen["user"])
        self.assertIn("- Combination: 1 block(s), equal weight per block", seen["user"])
        self.assertIn("\n\nMethod details (computed by code):\n- m1 series_auto, yoy path:", f["text"])
        self.assertIn("Data window 2025-05 (p5), 2025-06 (p4), 2026-05 (p6) (3 months used, not consecutive; last month 2026-05",
                      f["text"])
        self.assertIn("row yoy|pairs1|h1", f["text"])
        self.assertIn("Seasonal naive baseline (not combined): 1,210 (2025-06, point p4, from m1); the estimate is +0.0% "
                      "against it.", f["text"])
        self.assertIn("Data window [[m1_window]] ([[m1_n_months]] months used", f["template"])
        self.assertEqual(f["placeholders"]["m1_row"], "yoy|pairs1|h1")
        self.assertEqual(f["placeholders"]["block1_value"], "1,210")
        self.assertIn("quarter and half-year labels (Q1 to Q4, H1, H2)", seen["system"])
        # system 说的例外范围 = 代码保留的范围：年份离 as_of 不超过 10 年；点 id 只限 summary 里「- observed point」行列出的
        self.assertIn("four-digit years within ten years of the information cutoff", seen["system"])
        self.assertIn("method ids, and the ids of the assumptions and observed points listed in the '- assumption' and "
                      "'- observed point' lines below", seen["system"])
        self.assertEqual(f["text"].split("\n\n")[0],
                         f"About 1,210 widgets in Q3 2026 (80% model-based interval 1,008 to 1,485, basis: {basis}). The observed "
                         "2025 monthly total in point p4 (1,210 widgets) drives m1; p[n] is not an input; roughly [n] more.")
        self.assertEqual(f["digits_removed"], 2)
        self.assertNotIn("unknown placeholder", f["text"])
        self.assertEqual(f["model_text"], ANSWER)       # 清洗之前的原文只进 state
        self.assertEqual(saved["final"]["model_text"], ANSWER)
        self.assertIn(f"(series_calibration: {basis.replace(chr(39), '&#x27;')})", page)   # graph.html 页头
        self.assertIn(f"basis series_calibration ({basis})", ledger)
        self.assertIn("Method details (computed by code):\n\n- m1 series_auto, yoy path:", ledger)

    def test_graph_header_without_basis(self):
        # compute 为空的运行（例如 plan 失败）：graph.html 页头只写 basis 键「(None)」，和 v2.6c 一样，不出现「(None: )」
        from types import SimpleNamespace as NS

        from triangulate.agent import run as R
        st = {"qid": "t", "question": "q", "as_of": "2026-06-20", "plan": {"target": {}}, "compute": {}, "aborted": "budget"}
        tmp = Path(tempfile.mkdtemp())
        h = {"q": {"id": "t", "question": "q", "as_of": "2026-06-20"}, "g": NS(get_state=lambda cfg: NS(values=st)), "cfg": {},
             "ctx": NS(budget=P.Budget(), llm=NS(model="fake")), "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": None,
             "ablate": False, "t0": time.time()}
        try:
            with mock.patch("builtins.print"):
                R.save_run(h, [])
            page = (tmp / "graph.html").read_text(encoding="utf-8")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertIn("80% [n/a, n/a] (None)</div>", page)
        self.assertNotIn("(None:", page)

    def test_discrete_final_has_point_placeholders(self):
        from tests.test_discrete import discrete_graph_run
        st, seen = discrete_graph_run()
        f = st["final"]
        self.assertEqual(f["placeholders"]["p1_value"], "56.4%")
        self.assertIn("[[p1_value]]", seen["final_user"])
        self.assertIn("- observed point p1 (input of m1", seen["final_user"])
        self.assertEqual(f["model_text"], "Markets put about 56% on [[o2_label]] ([[o2_prob]]); m1 uses p1.")
        self.assertIn("m1 uses p1", f["text"])


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestResultViewBasisText(unittest.TestCase):
    def test_estimate_has_basis_text(self):
        from triangulate.web import results as W
        for basis in ("monte_carlo", "published"):       # 网页结果页 JSON 的 estimate 追加 basis_text（同一张 BASIS_TEXT）
            est = W.result_view({"compute": {"result": {"basis": basis}}}, "t")["estimate"]
            self.assertEqual(est["basis"], basis)
            self.assertEqual(est["basis_text"], O.BASIS_TEXT[basis])


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestScoreAllArms(unittest.TestCase):
    def test_no_last_year_arm_and_old_summaries_still_read(self):
        from triangulate.agent import run as R
        from triangulate.web import results as W
        tmp = Path(tempfile.mkdtemp())
        st = {"compute": {"result": {"central": 110.0, "p10": 90.0, "p90": 130.0, "basis": "monte_carlo"}},
              "budget": {"usd_total_assumed": 0.1, "usd_tokens": 0.05}, "wall_s": 1.0}
        q = {"id": "fc_yell_2026_08", "as_of": "2026-08-15", "answer_value": 100.0, "last_year": 105.0}
        fc = [{"id": "fc_yell_2026_08", "naive": {"estimate": 120.0}, "structured": {"estimate": 95.0}}]
        try:
            (tmp / "fc_yell_2026_08" / "x").mkdir(parents=True)
            (tmp / "fc_yell_2026_08" / "x" / "state.json").write_text(json.dumps(st), encoding="utf-8")
            with mock.patch.object(R, "RES", tmp):
                rows = R.score_all([q], "x", fc)
            written = json.loads((tmp / "summary_x.json").read_text(encoding="utf-8"))
            # 旧的 summary（带 last_year_same_period）照样能读：网页回测表只取 naive / structured_no_retrieval
            old = [dict(rows[0], arms={**rows[0]["arms"], "last_year_same_period": {"estimate": 105.0, "pct_err": 0.05}})]
            new_row = W.backtest_row("fc_yell_2026_08", "x", written, res=tmp)
            old_row = W.backtest_row("fc_yell_2026_08", "x", old, res=tmp)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(set(rows[0]["arms"]), {"agent", "naive", "structured_no_retrieval"})
        self.assertEqual(set(rows[0]["within_20pct"]), {"agent", "naive", "structured_no_retrieval"})
        self.assertEqual(written[0]["arms"], rows[0]["arms"])
        self.assertAlmostEqual(rows[0]["arms"]["agent"]["pct_err"], 0.1)
        self.assertEqual(new_row, old_row)
        self.assertEqual(new_row["naive"]["estimate"], 120.0)
        self.assertAlmostEqual(new_row["naive"]["pct_err"], 0.2)


if __name__ == "__main__":
    unittest.main()
