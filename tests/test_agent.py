"""Agent MVP 的代码部分：URL 解析、快照选择、quote 核对、数字解析、哨兵、日期过滤、方法库、加权与区间、图的连线。
需要 .venv（langgraph）；没有装时整组跳过。"""
import math
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import evidence as ev
from triangulate.agent import methods as M
from triangulate.agent.fetch import clean_url, select_snapshot
from triangulate.agent.search import parse_urls

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False


class TestSearcherParsing(unittest.TestCase):
    def test_only_urls_survive(self):
        text = ("Here are the sources (official!): https://example.gov/data/2025.htm, and "
                "[news](https://news.example.com/a?b=1#frag). The value is 123,456 visits.\n"
                "https://example.gov/data/2025.htm again; http://x.org/p).")
        self.assertEqual(parse_urls(text), ["https://example.gov/data/2025.htm", "https://news.example.com/a?b=1",
                                            "http://x.org/p"])

    def test_cap(self):
        text = " ".join(f"https://a{i}.example.com/x" for i in range(9))
        self.assertEqual(len(parse_urls(text, cap=5)), 5)

    def test_wayback_url_is_unwrapped(self):
        self.assertEqual(clean_url("https://web.archive.org/web/20250101000000/https://a.org/b#c"), "https://a.org/b")


class TestSnapshotSelection(unittest.TestCase):
    ROWS = [["timestamp", "original", "statuscode", "mimetype"],
            ["20250910040101", "https://a.org/x", "200", "text/html"],
            ["20260815235900", "https://a.org/x", "200", "text/html"],
            ["20260816000001", "https://a.org/x", "200", "text/html"],
            ["20260801000000", "https://a.org/x", "404", "text/html"]]

    def test_latest_on_or_before_as_of(self):
        self.assertEqual(select_snapshot(self.ROWS, date(2026, 8, 15))["timestamp"], "20260815235900")

    def test_none_before(self):
        self.assertIsNone(select_snapshot(self.ROWS, date(2025, 9, 1)))
        self.assertIsNone(select_snapshot([["timestamp"]], date(2026, 1, 1)))


class TestQuoteAndNumbers(unittest.TestCase):
    PAGE = ev.norm("The park hosted 881,936 recreation visits in August 2025, up 2% from\n August 2024 "
                   "(868,259 recreation visits). Revenue was $4.8 million. Table values in thousands.")

    def test_quote_verbatim_whitespace_normalised(self):
        self.assertTrue(ev.quote_in_text("hosted 881,936 recreation visits in August 2025", self.PAGE))
        self.assertTrue(ev.quote_in_text("up 2% from August 2024", self.PAGE))
        self.assertFalse(ev.quote_in_text("hosted 881,937 recreation visits", self.PAGE))
        self.assertTrue(ev.quote_in_text("hosted 881,936 ... (868,259 recreation", self.PAGE))
        self.assertFalse(ev.quote_in_text("(868,259 ... hosted 881,936", self.PAGE))  # 顺序不对

    def test_parse_value(self):
        self.assertEqual(ev.parse_value("881,936", ""), (881936.0, False))
        self.assertEqual(ev.parse_value("$4.8 million", ""), (4.8e6, False))
        self.assertEqual(ev.parse_value("4.8", "million"), (4.8e6, False))
        self.assertEqual(ev.parse_value("2.5M", ""), (2.5e6, False))
        self.assertEqual(ev.parse_value("12%", ""), (12.0, True))
        self.assertEqual(ev.parse_value("(1,234)", ""), (-1234.0, False))
        for bad in [("about 3 to 4", ""), ("n/a", ""), ("4.8 million", "billion"), ("7", "dozens")]:
            with self.assertRaises(ValueError):
                ev.parse_value(*bad)

    def test_scale_needs_textual_support(self):
        self.assertEqual(ev.scale_supported("million", ev.norm("Revenue was $4.8 million."), self.PAGE), "quote")
        self.assertEqual(ev.scale_supported("thousand", "value 12", self.PAGE), "page_header")
        self.assertEqual(ev.scale_supported("billion", "value 12", self.PAGE), "")
        self.assertEqual(ev.scale_supported("", "value 12", self.PAGE), "none_needed")


class TestLeakSentinel(unittest.TestCase):
    def test_formats(self):
        pats = ev.leak_patterns(856467)
        for t in ["visits: 856,467 in", "856467", "856 467 visits", "856.5 thousand", "about 856.5k", "0.856 million",
                  "nearly 856,000 visitors", "856 467"]:
            self.assertTrue(ev.leak_scan(t, pats), t)
        for t in ["1,856,467", "856,4670", "8564671", "881,936", "856.47 thousand"]:
            self.assertFalse(ev.leak_scan(t, pats), t)


class TestDateFilter(unittest.TestCase):
    A = date(2026, 8, 15)

    def test_parse_date(self):
        self.assertEqual(ev.parse_date("2025-08", end=True), date(2025, 8, 31))
        self.assertEqual(ev.parse_date("2025", end=True), date(2025, 12, 31))
        self.assertEqual(ev.parse_date("August 2025"), date(2025, 8, 1))
        self.assertEqual(ev.parse_date("Sep 4, 2025"), date(2025, 9, 4))
        self.assertIsNone(ev.parse_date("last summer"))

    def test_check(self):
        ok = {"period_start": "2026-07-01", "period_end": "2026-07-31", "published_at_if_visible": "2026-08-12"}
        self.assertEqual(ev.date_check(ok, self.A, date(2026, 8, 14)), "")
        self.assertIn("period_end", ev.date_check({**ok, "period_end": "2026-08-31"}, self.A, None))
        self.assertIn("published", ev.date_check({**ok, "published_at_if_visible": "2026-09-15"}, self.A, None))
        self.assertIn("page date", ev.date_check(ok, self.A, date(2026, 8, 16)))
        self.assertIn("missing", ev.date_check({"period_end": ""}, self.A, None))
        self.assertEqual(ev.date_check({"period_end": ""}, self.A, None, allow_no_period=True), "")


class TestMethods(unittest.TestCase):
    T = {2022: 100.0, 2023: 110.0, 2024: 121.0, 2025: 133.1}
    S = {2022: 10.0, 2023: 11.0, 2024: 12.1, 2025: 13.31, 2026: 14.641}

    def test_series_naive(self):
        self.assertEqual(M.series_naive(self.T, 2026, 1), 133.1)
        self.assertAlmostEqual(M.series_naive(self.T, 2026, 2), (121 + 133.1) / 2)
        with self.assertRaises(M.MethodError):
            M.series_naive({2025: 1.0}, 2026, 2)

    def test_yoy(self):
        self.assertAlmostEqual(M.yoy_scaling(self.T, self.S, 2026), 146.41)
        with self.assertRaises(M.MethodError):
            M.yoy_scaling(self.T, {2025: 1.0}, 2026)

    def test_linear_and_ratio(self):
        self.assertAlmostEqual(M.linear_fit(self.T, self.S, 2026), 146.41, places=6)  # 精确线性关系 y = 10x
        self.assertAlmostEqual(M.ratio(self.T, self.S, 2026), 146.41, places=6)
        with self.assertRaises(M.MethodError):
            M.linear_fit({2024: 1.0, 2025: 2.0}, self.S, 2026)

    def test_formula_mc(self):
        s = M.formula_mc("a * b", {"a": (1000.0, 0.0), "b": (0.08, 0.0)})
        self.assertAlmostEqual(s["median"], 80.0)
        s = M.formula_mc("a * b", {"a": (1000.0, 0.2), "b": (0.08, 0.2)})
        self.assertLess(s["p10"], 80.0)
        self.assertGreater(s["p90"], 80.0)
        with self.assertRaises(M.MethodError):
            M.formula_mc("a * 3", {"a": (1.0, 0.1)})

    def test_backtest_no_lookahead(self):
        bt = M.backtest("series_naive", self.T, {}, 2026, 1)
        self.assertEqual([b["year"] for b in bt], [2023, 2024, 2025])
        self.assertAlmostEqual(bt[0]["log_err"], math.log(100 / 110))
        bt = M.backtest("yoy_scaling", self.T, self.S, 2026)
        self.assertTrue(all(abs(b["log_err"]) < 1e-12 for b in bt))
        bt = M.backtest("linear_fit", self.T, self.S, 2026)
        self.assertEqual([b["year"] for b in bt], [2022, 2023, 2024, 2025])


class TestCombine(unittest.TestCase):
    def test_inverse_error_weights_and_hist_interval(self):
        a = {"id": "m1", "estimate": 100.0, "backtest": [{"log_err": 0.1}, {"log_err": -0.1}]}
        b = {"id": "m2", "estimate": 110.0, "backtest": [{"log_err": 0.01}, {"log_err": -0.01}]}
        c = M.combine([a, b])
        self.assertAlmostEqual(c["weights"]["m1"] / c["weights"]["m2"], (0.01 + M.EPS) / (0.1 + M.EPS))
        self.assertEqual(c["weight_rule"], "inverse_backtest_error")
        self.assertTrue(100 < c["central"] < 110)
        self.assertIn(c["basis"], ("historical_errors", "method_spread"))
        self.assertAlmostEqual(math.log(c["p90"] / c["central"]), M.Z90 * c["sigma_ln"])

    def test_no_backtest_equal_weights_spread(self):
        c = M.combine([{"id": "m1", "estimate": 100.0}, {"id": "m2", "estimate": 400.0}])
        self.assertEqual(c["weight_rule"], "equal")
        self.assertAlmostEqual(c["central"], 200.0)
        self.assertEqual(c["basis"], "method_spread")
        self.assertAlmostEqual(c["sigma_ln"], math.log(2))

    def test_single_method_fallback_and_mc(self):
        self.assertEqual(M.combine([{"id": "m1", "estimate": 5.0}])["basis"], "no_basis")
        c = M.combine([{"id": "m1", "estimate": 5.0, "mc": {"p10": 4.0, "p90": 6.25}}])
        self.assertEqual(c["basis"], "monte_carlo")
        self.assertIsNone(M.combine([])["central"])

    def test_untested_method_gets_median_weight(self):
        a = {"id": "m1", "estimate": 100.0, "backtest": [{"log_err": 0.05}]}
        b = {"id": "m2", "estimate": 100.0, "backtest": [{"log_err": 0.15}]}
        c = M.combine([a, b, {"id": "m3", "estimate": 100.0}])
        w1, w2, w3 = (c["weights"][k] for k in ("m1", "m2", "m3"))
        self.assertAlmostEqual(w3, (w1 + w2) / 2)


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestGraphOffline(unittest.TestCase):
    """假模型、假搜索、假网页：只检查图的连线、interrupt、Send 扇出、编号、计算和模板。"""

    def test_end_to_end_with_fakes(self):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P

        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget = P.Budget()
        ctx.leak_patterns = ev.leak_patterns(4242)

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"id": "d1", "category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                           {"id": "d2", "category": "physical_flow", "hypothesis": "h2", "data_to_find": "f2"}]}, None
                if role.startswith("extract"):
                    if "LEAKPAGE" in user:
                        raise AssertionError("leak-flagged page reached the extractor")
                    pts = [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "scale_word": "", "unit": "widgets",
                            "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                           for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]
                    pts.append({"name": "bad", "value_as_written": "9", "quote": "not in page", "period_end": "2025-01-01"})
                    return {"points": pts}, None
                if role.startswith("judge"):
                    return {"decisions": [], "extra_directions": [],
                            "methods": [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}},
                                        {"id": "m2", "method": "linear_fit", "params": {"target_history": ["p1"]}}]}, None
                if role == "final":
                    return {"answer": "About [[estimate]] widgets (range [[p10]] to [[p90]]); I think 1,234 too."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                return {"queries": ["q"], "urls": ["https://a.org/1", "https://leak.org/2"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid):
            text = "LEAKPAGE value 4,242" if "leak" in url else "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01", "text": text}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "t1"}}
            out = g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            self.assertIn("__interrupt__", out)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = g.get_state(cfg).values
        self.assertEqual(len([r for r in st["results"] if r["direction_id"] != "markets"]), 2)
        self.assertEqual(len(st["points"]), 6)  # 2 个方向 x 3 个核对通过的点
        self.assertEqual([p["id"] for p in st["points"]][:3], ["p1", "p2", "p3"])
        leak_pages = [pg for r in st["results"] for pg in r["pages"] if pg.get("leak_hits")]
        self.assertEqual(len(leak_pages), 2)
        dropped = [x["reason"] for r in st["results"] for x in r["dropped_points"]]
        self.assertIn("quote not found verbatim in page", dropped)
        m = {x["id"]: x for x in st["compute"]["methods"]}
        self.assertEqual(m["m1"]["estimate"], 1210.0)
        self.assertIn("error", m["m2"])
        self.assertIn("1,210", st["final"]["text"])
        self.assertNotIn("1,234", st["final"]["text"])
        self.assertEqual(st["final"]["digits_removed"], 1)


if __name__ == "__main__":
    unittest.main()
