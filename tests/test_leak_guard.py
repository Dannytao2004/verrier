"""v2.6c 回测泄漏护栏（D3、C2、N31）：回测时查询词命中登记值的方向作废（不取页、不重搜，search.voided 记命中的写法，
账本和泄漏审计列出）；以 k / M 结尾的缩写写法后面不能接字母。不联网、不调模型、不读 key（假搜索、假取页、假模型）。"""
import json
import re
import shutil
import tempfile
import time
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate import forecast
from triangulate.agent import evidence as ev
from triangulate.agent import pipeline as P

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

NHS = next(q for q in forecast.QUESTIONS if q["id"] == "fc_nhs_ae_2026_09")
# results/agent/fc_nhs_ae_2026_09/showcase1 里 d6 和 d1 保存的查询词：d6 第 3 条带着今年 9 月的真值 2.44 million
NHS_D6 = ["NHS strikes September 2026 A&E attendances impact", "NHS England winter plan 2026 A&E attendances forecast",
          "NHS England A&E attendances September 2025 2.44 million busiest September record",
          "NHS industrial action announced 2026 junior doctors ballot strike dates",
          "UK flu season 2026-27 forecast early peak respiratory viruses September"]
NHS_D1 = ["NHS England A&E attendances September 2025 monthly statistics", "monthly A&E attendances England 2026 statistics",
          "NHS England A&E attendances July 2026 2.49 million total attendances",
          "September 2023 A&E attendances England 2.2 million record"]
HIT_244 = r"(?<![\d.,])2\.44\ million(?!\d|[.,]\d)"
URLS = [f"https://example.org/{i}" for i in range(4)]


def _ctx(pats, searcher):
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "q", "2026-09-08", date(2026, 9, 8)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), pats, False
    ctx.early, ctx.live_fetch, ctx.progress = None, False, None
    ctx.searcher, ctx.llm = searcher, None
    return ctx


class Searcher:
    def __init__(self, queries):
        self.queries, self.calls, self.returned = queries, 0, []

    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        self.calls += 1
        self.returned.append({"queries": list(self.queries), "urls": list(URLS), "web_search_requests": 3})
        return self.returned[-1]


class TestPatterns(unittest.TestCase):
    def test_abbreviations_need_a_non_letter_after(self):
        pats = ev.leak_patterns(NHS["leak_values"])   # 6-8 月合计 7,268,445 登记了「7.27 M」「7.27M」
        self.assertFalse(ev.leak_scan("the trail is 7.27 miles long", pats))
        for t in ("7.27M attendances", "about 7.27 M.", "(7.27m)", "7.27 M", "a total of 7.27 million"):
            self.assertTrue(ev.leak_scan(t, pats), t)
        pats = ev.leak_patterns(856467)               # 「856k」「856.5k」「856 k」
        for t in ("856 km away", "856.5 kg of it", "856kWh"):
            self.assertFalse(ev.leak_scan(t, pats), t)
        for t in ("856k visits", "856.5k.", "856 K", "856,467 visits", "856.5 thousand", "856.5 thousands"):
            self.assertTrue(ev.leak_scan(t, pats), t)

    def test_only_k_and_m_forms_change(self):
        """写法列表不变；thousand / million 和纯数字写法的正则和 v2.6b 逐字相同；k / M 写法只是后面多了 (?![A-Za-z])。"""
        for v in NHS["leak_values"] + [856467, 24275, 4.25]:
            forms = ev.leak_forms(v)
            pats = ev.leak_patterns(v)
            self.assertEqual(len(pats), len(forms))
            for f, p in zip(forms, pats):
                old = rf"(?<![\d.,]){re.escape(f)}(?!\d|[.,]\d)"
                self.assertEqual(p.pattern, old + "(?![A-Za-z])" if f.endswith(("k", "M")) else old, f)
                self.assertEqual(p.flags & re.I, re.I)
        self.assertIn("7.27 M", ev.leak_forms(7268445))
        self.assertIn(r"(?<![\d.,])7\.27\ million(?!\d|[.,]\d)", [p.pattern for p in ev.leak_patterns(NHS["leak_values"])])


class TestRunDirection(unittest.TestCase):
    def _run(self, pats, queries, did="d6"):
        fetched, s = [], Searcher(queries)

        def fake_fetch(url, as_of, qid, **kw):
            fetched.append(url)
            return {"url": url, "status": "dropped", "reason": "fake"}
        ctx = _ctx(pats, s)
        with mock.patch.object(P, "fetch_page", fake_fetch):
            out = P.run_direction(ctx, {"what": "w"}, {"id": did, "category": "shocks"}, 1)
        return out, fetched, s, ctx

    def test_nhs_query_voids_the_direction(self):
        out, fetched, s, ctx = self._run(ev.leak_patterns(NHS["leak_values"]), NHS_D6)
        self.assertEqual(out["search"]["voided"], [HIT_244])
        self.assertEqual(fetched, [])                                   # 不取页
        self.assertEqual(s.calls, 1)                                    # 不重搜
        self.assertEqual((out["pages"], out["points"], out["dropped_points"]), ([], [], []))
        self.assertEqual(ctx.budget.pages_used, 0)
        self.assertNotIn("error", out)
        self.assertNotIn("aborted", out)
        self.assertNotIn("stopped", out)
        self.assertEqual({k: v for k, v in out["search"].items() if k != "voided"}, s.returned[0])   # 其余字段原样
        self.assertNotIn("voided", s.returned[0])                       # 不改 searcher 返回的对象

    def test_clean_queries_fetch_as_before(self):
        out, fetched, s, _ = self._run(ev.leak_patterns(NHS["leak_values"]), NHS_D1, "d1")   # 2.49 / 2.2 million 不是登记值
        self.assertNotIn("voided", out["search"])
        self.assertEqual(out["search"], s.returned[0])
        self.assertEqual(fetched, URLS)
        self.assertEqual(len(out["pages"]), 4)

    def test_live_runs_have_no_patterns(self):
        out, fetched, _, _ = self._run([], NHS_D6)
        self.assertNotIn("voided", out["search"])
        self.assertEqual(fetched, URLS)


# v2.12：series_naive 只作对照基线、不进合并，假裁判改用 series_auto；假网页多两个 5 月的点（2026 年 5 月 / 2025 年 5 月 = 1），
# yoy1 = 去年 6 月 1,210 x 1 = 1,210，和以前 series_naive 的估计相同
MONTHS = ((2023, 6, 30, "June", 1000), (2024, 6, 30, "June", 1100), (2025, 6, 30, "June", 1210),
          (2025, 5, 31, "May", 1000), (2026, 5, 31, "May", 1000))
MONTHS_TEXT = " ".join(f"{mon} {y}: {v:,} widgets." for y, _, _, mon, v in MONTHS)


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestAuditLedgerAndGraph(unittest.TestCase):
    def test_audit_and_ledger_list_voided_directions(self):
        from triangulate.agent import outputs, run
        st = {"qid": "t", "question": "q", "as_of": "2026-09-08", "plan": {"target": {}}, "points": [], "judge_rounds": [],
              "directions": [{"id": "d1", "category": "own_history"}, {"id": "d6", "category": "shocks"}],
              "compute": {"methods": [], "result": {}}, "final": {"text": "x"},
              "results": [{"direction_id": "d1", "round": 1, "search": {"queries": NHS_D1, "urls": URLS}, "pages": []},
                          {"direction_id": "d6", "round": 1, "search": {"queries": NHS_D6, "urls": URLS, "voided": [HIT_244]},
                           "pages": []}]}
        a = run.leakage_audit(st, "2026-09-08", NHS["leak_values"])
        self.assertEqual(a["directions_voided"], [{"direction_id": "d6", "round": 1, "hits": [HIT_244]}])
        self.assertEqual(a["searcher_queries_containing_registered_values"], [NHS_D6[2]])
        L = outputs.ledger(st).splitlines()
        i = L.index("### d6 [shocks] ")
        self.assertTrue(L[i + 4].startswith("Queries issued by the searcher: NHS strikes"), L[i + 4])
        self.assertEqual(L[i + 6], f"**DIRECTION VOIDED: a searcher query contains a registered value {[HIT_244]}; "
                                   "no pages fetched**")
        self.assertEqual(sum("DIRECTION VOIDED" in x for x in L), 1)
        st["results"][1]["search"].pop("voided")
        self.assertEqual(run.leakage_audit(st, "2026-09-08", NHS["leak_values"])["directions_voided"], [])
        self.assertNotIn("DIRECTION VOIDED", outputs.ledger(st))

    def test_graph_and_save_run_with_a_voided_direction(self):
        """整图（假模型）+ save_run：d2 的查询词带登记值 4,242，d2 不取页；其余照常；没有任何 prompt 含这个值。"""
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import run as R
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), ev.leak_patterns([4242]), False
        prompts, searched, fetched = [], [], []

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                prompts.append(system + user)
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                           {"category": "physical_flow", "hypothesis": "h2", "data_to_find": "f2"}]}, None
                if role.startswith("extract"):
                    return {"points": [{"name": f"widgets {mon} {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                        "period_start": f"{y}-{mo:02d}-01", "period_end": f"{y}-{mo:02d}-{d}",
                                        "quote": f"{mon} {y}: {v:,} widgets"}
                                       for y, mo, d, mon, v in MONTHS]}, None
                if role.startswith("judge"):
                    return {"decisions": [], "extra_directions": [],
                            "methods": [{"id": "m1", "method": "series_auto",
                                         "params": {"target_history": ["p1", "p2", "p3", "p4", "p5"]}}]}, None
                if role == "audit":
                    return {"methods": []}, None
                if role == "final":
                    return {"answer": "About [[estimate]] widgets."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                searched.append(role)
                q = "widgets June 2026 total 4,242" if role == "search:d2" else "widgets June statistics"
                return {"queries": [q], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid, **kw):
            fetched.append(url)
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                    "text": MONTHS_TEXT}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(P, "fetch_page", fake_fetch), \
                    mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
                g = G.build(ctx)
                cfg = {"configurable": {"thread_id": "lg1"}}
                g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
                g.invoke(Command(resume={"approved": True}), cfg)
                h = {"q": {"id": "t", "question": ctx.question, "as_of": ctx.as_of_s}, "g": g, "cfg": cfg, "ctx": ctx,
                     "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": [4242], "ablate": False, "t0": time.time()}
                R.save_run(h, [])
            saved = json.loads((tmp / "state.json").read_text(encoding="utf-8"))
            ledger = (tmp / "ledger.md").read_text(encoding="utf-8")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        res = {r["direction_id"]: r for r in saved["results"]}
        hit = r"(?<![\d.,])4,242(?!\d|[.,]\d)"
        self.assertEqual(res["d2"]["search"]["voided"], [hit])
        self.assertEqual(res["d2"]["pages"], [])
        self.assertNotIn("voided", res["d1"]["search"])
        self.assertEqual(fetched, ["https://a.org/search:d1"])
        self.assertEqual(sorted(searched), ["search:d1", "search:d2"])        # d2 没有重搜
        self.assertEqual({p["direction_id"] for p in saved["points"]}, {"d1"})
        self.assertAlmostEqual(saved["compute"]["result"]["central"], 1210.0, places=6)
        self.assertEqual(saved["leakage"]["directions_voided"], [{"direction_id": "d2", "round": 1, "hits": [hit]}])
        self.assertEqual(saved["leakage"]["searcher_queries_containing_registered_values"], ["widgets June 2026 total 4,242"])
        self.assertIn(f"**DIRECTION VOIDED: a searcher query contains a registered value {[hit]}; no pages fetched**", ledger)
        self.assertFalse([x for x in prompts if "4,242" in x or "4242" in x])   # 查询词和登记值不进任何 prompt


if __name__ == "__main__":
    unittest.main()
