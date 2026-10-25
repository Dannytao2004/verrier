"""v2.11d：引文没写期间的点，用页面自己声明的发布日期兜底（只一层）。
- verify_point：期初、期末都空才兜底（period_end = 页面日期，period_start 留空，period_source = page_date），不查期间年份；
  页面没有日期、写了但解析不了、只写了期初，照旧丢，原因串不变；base_rates 方向不再豁免。
- fetch.page_published：URL 路径日期 -> htmldate 结构化原始日期（不晚于上限）-> PDF CreationDate；快照页用原始 URL。
- build_series 不收页面日期点；各显示处写成「not stated (page dated YYYY-MM-DD)」，其余的点逐字不变。
G2 的假抽取员总会返回期间，看不到新标记，所以这里另外钉住裁判表里的那一行。全部离线：不联网、不调模型、不读 data/、results/。"""
import inspect
import json
import re
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import compute as C
from triangulate.agent import evidence as ev
from triangulate.agent import fetch as F
from triangulate.agent import net
from triangulate.agent import pipeline as P
from tests.test_live import FakeNet, NetCase
from tests.test_pdf import make_pdf

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

AS_OF = date(2026, 10, 21)
PUB = date(2026, 5, 25)
# epoch.ai 那页（token 题 v1 / v2 的 d2）的原句；正文里没有 2026
PAGE = ev.norm("Exponential View estimates the total tokens processed across all providers at 40 quadrillion tokens per quarter, "
               "i.e., around 5 billion tokens per second, four times Google's traffic.")
RAW = {"name": "tokens processed across all providers per second", "value_as_written": "5 billion", "scale_word": "",
       "unit": "tokens/second", "period_start": "", "period_end": "", "quote": "around 5 billion tokens per second"}
MISSING = "period_end missing or unparseable"
OLD_KEYS = {"name", "value", "value_as_written", "scale_word", "scale_basis", "unit", "period_start", "period_end",
            "published_at_if_visible", "quote"}
DATED = {"name": "x", "value": 5e9, "unit": "tokens/second", "period_start": "", "period_end": "2026-05-25",
         "period_source": "page_date", "source_url": "https://epoch.ai/gradient-updates/x", "via": "live_dated",
         "page_date": "2026-05-25", "quote": "around 5 billion tokens per second", "value_as_written": "5 billion",
         "scale_word": "", "published_at_if_visible": ""}
NORMAL = {**DATED, "period_start": "2025-06-01", "period_end": "2025-06-30"}
del NORMAL["period_source"]


def vp(raw=None, pub=PUB, page=PAGE, url="", **kw):
    return P.verify_point({**(raw or RAW), **kw}, page, AS_OF, None, pub, url=url)


class TestVerifyPoint(unittest.TestCase):
    def test_blank_period_takes_the_page_date(self):
        p, why = vp()
        self.assertEqual(why, "")
        self.assertEqual((p["period_start"], p["period_end"], p["period_source"]), ("", "2026-05-25", "page_date"))
        self.assertEqual(p["value"], 5e9)
        p2, _ = vp(period_start="  ", period_end=" \t")   # 只有空白也算没写
        self.assertEqual(p2, p)
        p3, _ = vp(period_start=None, period_end=None)
        self.assertEqual(p3, p)

    def test_no_page_date_drops_with_the_same_reason(self):
        self.assertEqual(vp(pub=None), (None, MISSING))

    def test_written_but_unparseable_periods_are_not_replaced(self):
        for pe in ("2025-Q3", "FY2025", "unknown", "N/A"):
            self.assertEqual(vp(period_end=pe), (None, MISSING), pe)

    def test_only_period_start_drops(self):
        self.assertEqual(vp(period_start="2026-01-01"), (None, MISSING))

    def test_year_check_skipped_only_for_page_dated_points(self):
        self.assertIsNotNone(vp()[0])   # 正文里没有 2026，页面日期点照样收
        p, why = vp(period_end="2026-05-25")   # 引文期间照旧查年份
        self.assertIsNone(p)
        self.assertIn("period year 2026 does not appear", why)
        self.assertIsNotNone(vp(period_end="2026-05-25", url="https://x.org/2026/report")[0])

    def test_other_date_gates_still_apply(self):
        self.assertEqual(vp(pub=date(2026, 10, 25)), (None, "page date 2026-10-25 after as_of"))   # v2.12f：原因串改了，照旧丢
        self.assertEqual(vp(published_at_if_visible="2026-11-02"), (None, "published 2026-11-02 after as_of"))
        p, why = P.verify_point(RAW, PAGE, AS_OF, date(2026, 10, 30), PUB)
        self.assertEqual((p, why), (None, "page date 2026-10-30 after as_of"))

    def test_points_with_a_period_are_unchanged(self):
        page = ev.norm("In June 2025 shops sold 1,210 widgets. Annual total for 2025 was 14,000 widgets.")
        for raw in ({"name": "w", "value_as_written": "1,210", "unit": "widgets", "period_start": "2025-06-01",
                     "period_end": "2025-06-30", "quote": "In June 2025 shops sold 1,210 widgets."},
                    {"name": "w", "value_as_written": "14,000", "unit": "widgets", "period_start": "",
                     "period_end": "2025", "quote": "Annual total for 2025 was 14,000 widgets."}):
            a = P.verify_point(raw, page, AS_OF, None, None)
            b = P.verify_point(raw, page, AS_OF, None, PUB)
            self.assertEqual(a, b)
            self.assertEqual(set(a[0]), OLD_KEYS)   # 不多出 period_source 键

    def test_base_rates_exemption_is_gone(self):
        self.assertNotIn("allow_no_period", inspect.signature(P.verify_point).parameters)
        self.assertNotIn("allow_no_period", inspect.signature(ev.date_check).parameters)
        self.assertEqual(ev.date_check({"period_end": ""}, AS_OF, None), MISSING)

        class LLM:
            def ask(self, *a, **k):
                return {"points": [dict(RAW)]}, None
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.as_of, ctx.budget, ctx.progress, ctx.llm = "t", AS_OF, P.Budget(), None, LLM()
        ctx.leak_patterns, ctx.leak_values = [], None
        for pub, kept in ((None, 0), ("2026-05-25", 1)):
            out = {"pages": [], "points": [], "dropped_points": []}
            page = {"url": "https://epoch.ai/x", "status": "live_dated", "page_date": "2026-05-25", "page_published": pub}
            P._process_page(ctx, {"what": "w"}, {"id": "b1", "category": "base_rates"}, 1, page, PAGE, out)
            self.assertEqual(len(out["points"]), kept)
            self.assertEqual([x["reason"] for x in out["dropped_points"]], [] if kept else [MISSING])
        self.assertEqual(out["points"][0]["period_source"], "page_date")


HTML_DATES = (b"<html><head><meta property='article:published_time' content='%s'>%s</head><body><p>"
              + b"Token usage report. " * 30 + b"</p></body></html>")


def html(published: str, modified: str = "") -> bytes:
    mod = b"<meta property='article:modified_time' content='%s'>" % modified.encode() if modified else b""
    return HTML_DATES % (published.encode(), mod)


UNDATED = b"<html><body><p>" + b"No date here. " * 40 + b"</p></body></html>"
H = {"Content-Type": "text/html"}


class TestPagePublished(unittest.TestCase):
    def test_url_date_first(self):
        self.assertEqual(F.page_published("https://x.org/news/2025/03/04/a", html("2026-05-25"), H, AS_OF), date(2025, 3, 4))
        self.assertEqual(F.page_published("https://x.org/2024-01/report-2025-06-30.html", UNDATED, H, AS_OF), date(2025, 6, 30))

    def test_structured_original_date_capped(self):
        self.assertEqual(F.page_published("https://x.org/a", html("2026-05-25"), H, AS_OF), PUB)
        self.assertEqual(F.page_published("https://x.org/a", html("2026-05-25"), H, PUB), PUB)   # 上限当天也认
        self.assertIsNone(F.page_published("https://x.org/a", html("2026-07-31"), H, date(2026, 4, 15)))   # 越过上限不认
        # htmldate 的已知行为（BUGS S41）：日期越过上限、但同月 1 日没越过时，退成当月 1 日
        self.assertEqual(F.page_published("https://x.org/a", html("2026-09-03"), H, date(2026, 9, 1)), date(2026, 9, 1))
        # 原始日期优先于修改日期（themeisle：2024-01-04 发布，2026 年改过）
        self.assertEqual(F.page_published("https://x.org/a", html("2024-01-04", "2026-08-13"), H, AS_OF), date(2024, 1, 4))
        self.assertIsNone(F.page_published("https://x.org/a", UNDATED, H, AS_OF))

    def test_pdf_creation_date(self):
        pdf = make_pdf([["Visitors in September 2026: 35,518"]],
                       info={"CreationDate": "D:20260915083000+09'00'", "ModDate": "D:20260916090000+09'00'"})
        pdf_h = {"Content-Type": "application/pdf"}
        self.assertEqual(F.page_published("https://x.org/r.pdf", pdf, pdf_h, AS_OF), date(2026, 9, 15))   # 不用 ModDate
        self.assertEqual(F.page_published("https://x.org/2026/08/r.pdf", pdf, pdf_h, AS_OF), date(2026, 8, 1))
        self.assertIsNone(F.page_published("https://x.org/r.pdf", make_pdf([["x 1"]]), pdf_h, AS_OF))

    def test_wayback_timestamp_is_not_a_url_date(self):
        self.assertIsNone(F.page_published("https://web.archive.org/web/20230524123456id_/https://ycharts.com/indicators/x",
                                           UNDATED, H, date(2023, 5, 24)))


class TestFetchStoresPagePublished(NetCase):
    def _snapshot(self, original, final, body, as_of=date(2026, 9, 6)):
        rows = [["timestamp", "original", "statuscode", "mimetype"], ["20260901000000", original, "200", "text/html"]]

        def routes(u):
            if u.startswith(F.CDX):
                return 200, json.dumps(rows).encode(), {"Content-Type": "application/json"}
            if u == f"https://web.archive.org/web/20260901000000id_/{original}":
                return 200, body, H
            raise AssertionError(u)
        self.use(FakeNet(routes), 0.01)
        real = net.get

        def get(url, timeout=None):   # 快照的最终 URL 换成 final（跳转到 Wayback 上的另一个地址）
            st, b, h, fin = real(url, timeout=timeout)
            return st, b, h, (final if "id_/" in url else fin)
        with mock.patch.dict(net.HOST_INTERVAL, {"web.archive.org": 0.01}), mock.patch.object(net, "get", get):
            return F.fetch_page(original, as_of, "t", today=date(2026, 10, 16))

    def test_snapshot_uses_the_original_url_and_snapshot_date(self):
        orig = "https://news.example.org/2025/03/04/story"
        rec = self._snapshot(orig, "https://web.archive.org/web/20260901000000id_/https://news.example.org/2026/08/31/other",
                             UNDATED)
        self.assertEqual((rec["status"], rec["page_date"], rec["page_published"]), ("snapshot", "2026-09-01", "2025-03-04"))
        rec = self._snapshot("https://news.example.org/story", "https://web.archive.org/web/20260901000000id_/https://news.example.org/story",
                             html("2026-10-15"), as_of=date(2026, 10, 20))   # 晚于快照日（2026-09-01）、早于 as_of：上限是快照日，不认
        self.assertEqual((rec["status"], rec["page_published"]), ("snapshot", None))
        rec = self._snapshot("https://news.example.org/story2", "https://web.archive.org/web/20260901000000id_/https://news.example.org/story2",
                             html("2026-08-20"))
        self.assertEqual(rec["page_published"], "2026-08-20")

    def test_live_page_capped_at_as_of(self):
        body = html("2024-01-04", "2026-10-05")
        self.use(FakeNet(lambda u: (200, body, H)), 0.01)
        rec = F.fetch_live("https://a.example.org/blog", date(2026, 10, 16), "t", today=date(2026, 10, 16))
        self.assertEqual((rec["status"], rec["page_date"], rec["page_published"]), ("live_dated", "2026-10-05", "2024-01-04"))


class TestBuildSeries(unittest.TestCase):
    def test_page_dated_points_are_not_used(self):
        pts = {f"p{i}": {"value": v, "unit": "w", "period_start": f"{y}-06-01", "period_end": f"{y}-06-30"}
               for i, (y, v) in enumerate(((2023, 1000.0), (2024, 1100.0), (2025, 1210.0)), 1)}
        before = C.build_series(["p1", "p2", "p3"], pts)
        pts["p4"] = {"value": 1300.0, "unit": "w", "period_start": "", "period_end": "2026-05-25", "period_source": "page_date"}
        note = "p4: period not stated in the source (page dated 2026-05-25), not used in a series"
        for ref in (None, (date(2025, 6, 1), date(2025, 6, 30))):   # signal（参照取最晚的点）和 target_history 都不进
            s, notes, used = C.build_series(["p1", "p2", "p3", "p4"], pts, ref)
            self.assertEqual((s, used), (before[0], before[2]))
            self.assertEqual(notes, [note])


class TestDisplay(unittest.TestCase):
    def test_period_text(self):
        self.assertEqual(ev.period_text(DATED), "not stated (page dated 2026-05-25)")
        self.assertEqual(ev.period_text(NORMAL), "2025-06-01..2025-06-30")
        self.assertEqual(ev.period_text({"period_end": "2025-06-30"}), "?..2025-06-30")
        self.assertEqual(ev.period_text({"period_start": "", "period_end": "2025-06-30"}, blank=""), "..2025-06-30")
        self.assertEqual(ev.period_text({}), "?..?")

    def test_prompt_sites(self):
        from triangulate.agent import graph as G
        from triangulate.agent import jev as J
        from triangulate.agent import published as PB
        from triangulate.agent import unit_review as UR
        d, n = {**DATED, "id": "p4", "direction_id": "d2"}, {**NORMAL, "id": "p1", "direction_id": "d2"}
        rows = G._table([n, d]).splitlines()
        self.assertEqual(rows[1], "p1 | d2 | x | 5,000,000,000 | tokens/second | 2025-06-01..2025-06-30 |  | epoch.ai | "
                                  "live_dated 2026-05-25 | around 5 billion tokens per second")
        self.assertEqual(rows[2], "p4 | d2 | x | 5,000,000,000 | tokens/second | not stated (page dated 2026-05-25) |  | "
                                  "epoch.ai | live_dated 2026-05-25 | around 5 billion tokens per second")
        self.assertEqual(G._evidence("p4", {"p4": d}, {}), 'data point p4: "x" = 5,000,000,000 tokens/second, period '
                                                           'not stated (page dated 2026-05-25), source epoch.ai')
        _, lines = G.point_placeholders([d], [{"id": "m1", "used_ids": ["p4"]}])
        self.assertEqual(lines, ["- observed point p4 (input of m1): x, value 5,000,000,000 tokens/second, "
                                 "period not stated (page dated 2026-05-25)"])
        self.assertIn(", period not stated (page dated 2026-05-25), source epoch.ai (live_dated page dated 2026-05-25)",
                      PB.candidate_line(d))
        self.assertEqual(PB._summary(d)["period_source"], "page_date")
        self.assertIn("(period not stated (page dated 2026-05-25)), from epoch.ai",
                      PB._evidence_lines({"point": PB._summary(d), "id": "p4"})[0])
        self.assertIn("(period 2025-06-01..2025-06-30), from epoch.ai", PB._evidence_lines({"point": PB._summary(n), "id": "p1"})[0])
        brief = J.evidence_brief({"what": "w", "unit": "tokens/second"}, [d, n], "2026-10-21")
        self.assertIn("- x = 5,000,000,000 tokens/second, period not stated (page dated 2026-05-25), source epoch.ai, 2026-05-25",
                      brief)
        self.assertIn("- x = 5,000,000,000 tokens/second, period 2025-06-01..2025-06-30, source epoch.ai, 2026-05-25", brief)
        ln = UR.input_lines({}, {"inputs_detail": [{"name": "r", "kind": "point", "id": "p4", "value": 5e9}]}, {"p4": d}, {})
        self.assertEqual(json.loads(ln[0])["period"], "not stated (page dated 2026-05-25)")

    def test_ledger_and_web(self):
        from triangulate.agent import outputs as O
        from triangulate.agent import run as R
        from triangulate.web import results as W
        st = {"published": {"status": "not_published", "note": "", "candidates": [{**DATED, "domain": "epoch.ai", "id": "p4"},
                                                                                   {**NORMAL, "domain": "epoch.ai", "id": "p1"}]}}
        md = "\n".join(O.published_md(st))
        self.assertIn("| p4 | x | 5,000,000,000 | tokens/second | not stated (page dated 2026-05-25) | epoch.ai |", md)
        self.assertIn("| p1 | x | 5,000,000,000 | tokens/second | 2025-06-01..2025-06-30 | epoch.ai |", md)
        pts = [{**DATED, "id": "p4", "direction_id": "d1", "ablation_excluded": "own history"},
               {**NORMAL, "id": "p1", "direction_id": "d1", "ablation_excluded": "own history"}]
        ab = R.ablation_summary({"plan": {"target": {"what": "w"}}, "points": pts})
        self.assertEqual([sorted(x) for x in ab["excluded_points"]],
                         [sorted(["id", "name", "value", "unit", "period_end", "direction_id", "period_source", "reason"]),
                          sorted(["id", "name", "value", "unit", "period_end", "direction_id", "reason"])])
        md = "\n".join(O.ablation_md({"ablation": ab}))
        self.assertIn("  - p4 x = 5,000,000,000 (not stated (page dated 2026-05-25)): own history", md)
        self.assertIn("  - p1 x = 5,000,000,000 (2025-06-30): own history", md)
        self.assertEqual(W._point_view(DATED)["period_text"], "not stated (page dated 2026-05-25)")
        self.assertEqual(W._point_view(NORMAL)["period_text"], "2025-06-01..2025-06-30")
        self.assertEqual(W._point_view({**NORMAL, "period_start": ""})["period_text"], "?..2025-06-30")


# v2.12：series_naive 只作对照基线、不进合并，假裁判改用 series_auto；假网页多两个 5 月的点（2026 年 5 月 / 2025 年 5 月 = 1），
# yoy1 = 去年 6 月 1,210 x 1 = 1,210，和以前 series_naive 的估计相同
MONTHS = ((2023, 6, 30, "June", 1000), (2024, 6, 30, "June", 1100), (2025, 6, 30, "June", 1210),
          (2025, 5, 31, "May", 1000), (2026, 5, 31, "May", 1000))
MONTHS_TEXT = " ".join(f"{mon} {y}: {v:,} widgets." for y, _, _, mon, v in MONTHS)


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestPinnedJudgePrompt(unittest.TestCase):
    """假模型跑一遍图：页面日期点进裁判表的那一行逐字钉住；没有页面日期的页上同一个点被丢（own_history 和 base_rates 都一样）；
    序列方法跳过它并写 note；正常的点那一行和以前的写法相同。"""

    def test_graph_with_a_page_dated_point(self):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import outputs as O
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
        log = []

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                log.append((role, user))
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30",
                                       "publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                           {"category": "base_rates", "hypothesis": "h2", "data_to_find": "f2"}]}, None
                if role.startswith("extract"):
                    pts = [{"name": f"widgets {mon} {y}", "value_as_written": f"{v:,}", "unit": "widgets", "period_start": f"{y}-{mo:02d}-01",
                            "period_end": f"{y}-{mo:02d}-{d}", "quote": f"{mon} {y}: {v:,} widgets"} for y, mo, d, mon, v in MONTHS]
                    pts.append({"name": "widgets sold per day across all shops", "value_as_written": "5 billion", "unit": "widgets/day",
                                "period_start": "", "period_end": "", "quote": "around 5 billion widgets per day"})
                    return {"points": pts}, None
                if role.startswith("judge"):
                    ids = re.findall(r"^(p\d+) \| d1 \|", user, re.M)
                    return {"decisions": [], "extra_directions": [],
                            "methods": [{"id": "m1", "method": "series_auto", "params": {"target_history": ids}}]}, None
                if role == "audit":
                    return {"methods": []}, None
                if role == "final":
                    return {"answer": "About [[estimate]]."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                return {"queries": ["q"], "urls": ["https://a.org/dated", "https://a.org/undated"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid, **kw):
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                    "page_published": "2026-05-25" if url.endswith("/dated") else None,
                    "text": MONTHS_TEXT + " Shops sell around 5 billion widgets per day."}
        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        with mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "t1"}}
            g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = g.get_state(cfg).values
        dated = [p for p in st["points"] if p.get("period_source")]
        self.assertEqual([(p["direction_id"], p["source_url"], p["period_end"]) for p in dated],
                         [("d1", "https://a.org/dated", "2026-05-25"), ("d2", "https://a.org/dated", "2026-05-25")])
        self.assertTrue(all("period_source" not in p for p in st["points"] if p["name"].startswith(("widgets June", "widgets May"))))
        drops = [(r["direction_id"], x["source_url"], x["reason"]) for r in st["results"] for x in r["dropped_points"]]
        self.assertEqual(drops, [("d1", "https://a.org/undated", MISSING), ("d2", "https://a.org/undated", MISSING)])
        judge = next(u for r, u in log if r == "judge:r1")
        pid = dated[0]["id"]
        self.assertIn(f"\n{pid} | d1 | widgets sold per day across all shops | 5,000,000,000 | widgets/day | "
                      "not stated (page dated 2026-05-25) |  | a.org | snapshot 2026-06-01 | around 5 billion widgets per day\n", judge)
        self.assertIn("\np1 | d1 | widgets June 2023 | 1,000 | widgets | 2023-06-01..2023-06-30 |  | a.org | snapshot 2026-06-01 | "
                      "June 2023: 1,000 widgets\n", judge)
        m1 = next(m for m in st["compute"]["methods"] if m["id"] == "m1")
        self.assertEqual(m1["estimate"], 1210.0)
        self.assertIn(f"{pid}: period not stated in the source (page dated 2026-05-25), not used in a series", m1["notes"])
        self.assertIn(f"  - {pid} widgets sold per day across all shops = **5,000,000,000** widgets/day "
                      "(not stated (page dated 2026-05-25)) [keep: ", O.ledger(st))


if __name__ == "__main__":
    unittest.main()


class TestPublishedSkipsPageDated(unittest.TestCase):
    """S43：时点目标下，期间是页面日期补的点不进「已公布」候选；同一个点写明期间照旧是候选。"""

    def test_point_in_time_target(self):
        from triangulate.agent import published as PB
        t = {"what": "number of AI accelerators installed worldwide", "unit": "accelerators",
             "period_start": "2026-10-21", "period_end": "2026-10-21"}
        base = {"id": "p1", "value": 3.5e7, "name": "AI accelerators installed worldwide", "unit": "accelerators",
                "quote": "about 35 million AI accelerators are installed worldwide", "keep": True, "judged_round": 1,
                "page_date": "2026-10-21"}
        stated = dict(base, period_start="2026-10-19", period_end="2026-10-19")
        page_dated = dict(base, period_start="", period_end="2026-10-19", period_source="page_date")
        self.assertEqual(len(PB.candidates([stated], t, date(2026, 10, 21))[0]), 1)
        self.assertEqual(PB.candidates([page_dated], t, date(2026, 10, 21))[0], [])
