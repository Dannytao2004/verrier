"""v2.5 真实使用：直接抓 live 页（不查 Wayback）+ 确认了已公布的值就提前停。全部离线：假网络、假模型、假搜索。
- live 路径从不请求 web.archive.org、不调 cdx_lookup；超时短；robots、每个 host 的限速照旧；不同 host 同时抓。
- 回测路径（fetch_page）仍然只请求 Wayback，从不请求原网站。
- 提前停只在真实使用、确认出 published 时发生；没确认（different / conflict）时裁判、估计、终稿与关掉提前检查时相同。"""
import json
import re
import shutil
import tempfile
import threading
import time
import unittest
import urllib.parse
from datetime import date, timedelta
from pathlib import Path
from unittest import mock

from triangulate.agent import evidence as ev
from triangulate.agent import fetch as F
from triangulate.agent import net
from triangulate.agent import published as PB

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

AS_OF = date(2026, 10, 16)
HTML = (b"<html><head><meta property='article:published_time' content='2026-10-05'></head><body><p>"
        + b"UK car market report. " * 30 + b"September 2026: 350,518 new cars were registered.</p></body></html>")


class _Resp:
    def __init__(self, status, body, headers):
        self.status, self.body, self.headers = status, body, headers

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self, n=-1):
        return self.body


class FakeNet:
    """换掉 net._OPENER（限速、robots、重定向都还是真的）：记下每个请求的 URL、开始 / 结束时刻和超时。"""

    def __init__(self, routes, delay=0.0):
        self.routes, self.delay, self.log, self._lock = routes, delay, [], threading.Lock()

    def open(self, req, timeout=None):
        url, t0 = req.full_url, time.monotonic()
        host = urllib.parse.urlsplit(url).netloc
        if url.endswith("/robots.txt"):
            r = (200, b"User-agent: *\nDisallow: /private/\n" if host.startswith("c.") else b"User-agent: *\nAllow: /\n", {})
        else:
            time.sleep(self.delay)
            r = self.routes(url)
        with self._lock:
            self.log.append({"url": url, "host": host, "t0": t0, "t1": time.monotonic(), "timeout": timeout})
        return _Resp(*r)


class NetCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        for obj, name, val in ((F, "RAW_AGENT", self.tmp), (F, "CACHE", self.tmp / "_cache")):
            p = mock.patch.object(obj, name, val)
            p.start()
            self.addCleanup(p.stop)
        net._ROBOTS.clear()
        self.addCleanup(net._ROBOTS.clear)

    def use(self, fake, interval=0.5):
        for name, val in (("_OPENER", fake), ("LIMITER", net.HostLimiter(interval))):
            p = mock.patch.object(net, name, val)
            p.start()
            self.addCleanup(p.stop)


class TestLiveFetch(NetCase):
    def test_live_never_touches_wayback(self):
        fake = FakeNet(lambda u: (200, HTML, {"Content-Type": "text/html"}))
        self.use(fake, 0.01)
        with mock.patch.object(F, "cdx_lookup", side_effect=AssertionError("cdx_lookup in live use")):
            rec = F.fetch_live("https://web.archive.org/web/20261001000000/https://news.example.co.uk/sep#x", AS_OF, "t", today=AS_OF)
        self.assertEqual((rec["status"], rec["page_date"], rec["snapshot_ts"]), ("live_dated", "2026-10-05", None))
        self.assertEqual([x["url"] for x in fake.log], ["https://news.example.co.uk/robots.txt", "https://news.example.co.uk/sep"])
        self.assertEqual([x["timeout"] for x in fake.log], [net.LIVE_ROBOTS_TIMEOUT_S, net.LIVE_TIMEOUT_S])

    def test_live_checks_are_kept(self):
        undated = b"<html><body><p>" + b"No date here. " * 40 + b"</p></body></html>"
        pages = {"/undated": undated, "/later": HTML, "/gone": b""}
        fake = FakeNet(lambda u: (404 if u.endswith("/gone") else 200, pages[urllib.parse.urlsplit(u).path],
                                  {"Content-Type": "text/html"}))
        self.use(fake, 0.01)
        got = {k: F.fetch_live(f"https://a.example.org{k}", date(2026, 10, 1), "t", today=date(2026, 10, 1))["reason"] for k in pages}
        self.assertEqual(got, {"/undated": "live page has no readable date", "/later": "live page dated 2026-10-05 > as_of",
                               "/gone": "live http 404"})
        rec = F.fetch_live("https://c.example.org/private/x", AS_OF, "t", today=AS_OF)
        self.assertEqual(rec["reason"], "live fetch blocked by robots.txt")
        self.assertNotIn("https://c.example.org/private/x", [x["url"] for x in fake.log])
        self.assertEqual(F.fetch_live("https://a.example.org/r.zip", AS_OF, "t", today=AS_OF)["reason"], "binary file type not supported in MVP")   # v2.12h：xlsx 改成收

    def test_live_does_not_retry_or_back_off(self):
        import urllib.error
        n, sleeps = [], []

        def boom(req, timeout=None):
            n.append(req.full_url)
            if req.full_url.endswith("/robots.txt"):
                return _Resp(200, b"", {})
            raise urllib.error.URLError(ConnectionRefusedError(10061, "refused"))
        self.use(mock.Mock(open=boom), 0.01)
        with mock.patch.object(net.time, "sleep", lambda s: sleeps.append(s)):
            rec = F.fetch_live("https://slow.example.org/a", AS_OF, "t", today=AS_OF)
        self.assertEqual(rec["reason"], "live fetch error URLError")
        self.assertEqual(n, ["https://slow.example.org/robots.txt", "https://slow.example.org/a"])   # 一次，不重试
        self.assertFalse([s for s in sleeps if s >= 1])                                             # 没有 10 / 30 秒退避


class TestBacktestFetchPath(NetCase):
    """回测（as_of 早于今天）：fetch_page 只请求 web.archive.org（CDX + id_ 快照），从不请求原网站。"""

    def _run(self, rows):
        snap = "https://web.archive.org/web/20260901000000id_/https://news.example.co.uk/sep"

        def routes(u):
            if u.startswith(F.CDX):
                return 200, json.dumps(rows).encode(), {"Content-Type": "application/json"}
            if u == snap:
                return 200, HTML.replace(b"2026-10-05", b"2026-08-31"), {"Content-Type": "text/html"}
            raise AssertionError(u)
        fake = FakeNet(routes)
        self.use(fake, 0.01)
        with mock.patch.dict(net.HOST_INTERVAL, {"web.archive.org": 0.01}):
            rec = F.fetch_page("https://news.example.co.uk/sep", date(2026, 9, 6), "t", today=AS_OF)
        return rec, fake.log

    def test_snapshot_from_the_archive_only(self):
        head = ["timestamp", "original", "statuscode", "mimetype"]
        rec, log = self._run([head, ["20260901000000", "https://news.example.co.uk/sep", "200", "text/html"]])
        self.assertEqual((rec["status"], rec["snapshot_ts"]), ("snapshot", "20260901000000"))
        self.assertEqual({x["host"] for x in log}, {"web.archive.org"})
        self.assertEqual(len([x for x in log if x["url"].startswith(F.CDX)]), 1)

    def test_no_snapshot_no_live_page(self):
        rec, log = self._run([])
        self.assertEqual(rec["status"], "dropped")
        self.assertIn("live pages not used in backtests", rec["reason"])
        self.assertEqual({x["host"] for x in log}, {"web.archive.org"})

    def test_live_fetch_after_the_as_of_day_uses_the_archive(self):
        """v2.5.2（审查复现）：真实使用的运行跨过午夜或隔天才批准，取页这天 as_of 已早于今天：fetch_live 不抓 live 页，
        走 fetch_page 的快照路径。live 页日期 2026-10-05、正文没有更晚的日期，v2.5.1 会把它收成 live_dated。"""
        head = ["timestamp", "original", "statuscode", "mimetype"]
        rows = {"/none": [head], "/snap": [head, ["20261015000000", "https://news.example.co.uk/snap", "200", "text/html"]],
                "/today": [head]}

        def routes(u):
            if u.startswith(F.CDX):
                orig = urllib.parse.parse_qs(urllib.parse.urlsplit(u).query)["url"][0]
                return 200, json.dumps(rows[urllib.parse.urlsplit(orig).path]).encode(), {"Content-Type": "application/json"}
            return 200, HTML, {"Content-Type": "text/html"}   # 快照和 live 页都是这一页
        fake = FakeNet(routes)
        self.use(fake, 0.01)
        with mock.patch.dict(net.HOST_INTERVAL, {"web.archive.org": 0.01}):
            none = F.fetch_live("https://news.example.co.uk/none", AS_OF, "t", today=date(2026, 10, 17))
            snap = F.fetch_live("https://news.example.co.uk/snap", AS_OF, "t", today=date(2026, 10, 17))
            dflt = F.fetch_live("https://news.example.co.uk/today", date.today() - timedelta(days=1), "t")   # 默认的「今天」
        self.assertEqual(none["status"], "dropped")
        self.assertIn("live pages not used in backtests (as_of before fetch day)", none["reason"])
        self.assertEqual((snap["status"], snap["snapshot_ts"]), ("snapshot", "20261015000000"))
        self.assertEqual(dflt["status"], "dropped")
        self.assertTrue(all(r["live_skipped"] for r in (none, snap, dflt)))
        self.assertEqual({x["host"] for x in fake.log}, {"web.archive.org"})                # 从不请求原网站
        self.assertEqual(len([x for x in fake.log if x["url"].startswith(F.CDX)]), 3)


def _ctx(live, early=None, as_of="2026-10-16", check=None):
    from triangulate.agent import pipeline as P
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many new cars?", as_of, date.fromisoformat(as_of)
    ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
    ctx.check_published = live if check is None else check
    ctx.live_fetch, ctx.early = live, early
    return ctx


class _Searcher:
    def __init__(self, urls):
        self.urls = urls

    def search(self, prompt, *, role, qid, max_uses=3, cap=5):
        return {"queries": ["q"], "urls": self.urls, "web_search_requests": 1}


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestLiveConcurrency(NetCase):
    def test_hosts_in_parallel_same_host_paced_robots_respected(self):
        from triangulate.agent import pipeline as P
        fake = FakeNet(lambda u: (200, HTML, {"Content-Type": "text/html"}), delay=0.3)
        self.use(fake, 0.5)
        ctx = _ctx(True, as_of=date.today().isoformat())   # 取页用真的「今天」（v2.5.2 每次取页判断 as_of >= 今天）
        urls = ["https://a.example.org/1", "https://a.example.org/2", "https://b.example.org/1", "https://c.example.org/private/x"]
        ctx.searcher = _Searcher(urls)
        ctx.llm = mock.Mock(ask=lambda *a, **k: ({"points": []}, None))
        with mock.patch.object(P, "fetch_page", side_effect=AssertionError("snapshot path in live use")), \
                mock.patch.object(F, "cdx_lookup", side_effect=AssertionError("cdx_lookup in live use")):
            out = P.run_direction(ctx, {"what": "w"}, {"id": "d1", "category": "own_history"}, 1)
        self.assertEqual([pg["url"] for pg in out["pages"]], urls)                       # 按 URL 顺序记录
        self.assertEqual([pg["status"] for pg in out["pages"]], ["live_dated"] * 3 + ["dropped"])
        self.assertEqual(out["pages"][3]["reason"], "live fetch blocked by robots.txt")
        log = fake.log
        self.assertNotIn("https://c.example.org/private/x", [x["url"] for x in log])
        self.assertFalse([x for x in log if x["host"] == "web.archive.org"])
        a = sorted(x["t0"] for x in log if x["host"] == "a.example.org")                 # robots + 2 页
        self.assertEqual(len(a), 3)
        self.assertTrue(all(t2 - t1 >= 0.45 for t1, t2 in zip(a, a[1:])), a)            # 同一 host：开始至少隔一个间隔
        a_end = max(x["t1"] for x in log if x["host"] == "a.example.org")
        b_page = next(x["t0"] for x in log if x["url"] == "https://b.example.org/1")
        self.assertLess(b_page, a_end)                                                    # 不同 host 同时抓
        self.assertTrue(all(pg.get("fetch_s") is not None for pg in out["pages"][:3]))
        self.assertEqual(ctx.budget.pages_used, 3)                                        # 丢掉的页退回名额

    def test_backtest_direction_uses_the_snapshot_path(self):
        from triangulate.agent import pipeline as P
        ctx = _ctx(False, as_of="2026-09-06")
        ctx.searcher = _Searcher(["https://a.example.org/1"])
        ctx.llm = mock.Mock(ask=lambda *a, **k: ({"points": []}, None))
        seen = []

        def fake_page(url, as_of, qid):
            seen.append(url)
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260901000000", "page_date": "2026-09-01", "text": "x"}
        with mock.patch.object(P, "fetch_page", fake_page), \
                mock.patch.object(P, "fetch_live", side_effect=AssertionError("live page in a backtest")):
            out = P.run_direction(ctx, {"what": "w"}, {"id": "d1", "category": "own_history"}, 1)
        self.assertEqual(seen, ["https://a.example.org/1"])
        self.assertEqual(out["pages"][0]["status"], "snapshot")


UK = {"what": "New passenger car registrations in the United Kingdom, as reported by SMMT",
      "unit": "number of new cars registered", "period_start": "2026-09-01", "period_end": "2026-09-30",
      "publisher": "Society of Motor Manufacturers and Traders (SMMT)"}
TOTAL = "UK new car registrations, September 2026 (preliminary SMMT figure)"


def _pts(rows):
    return [{"name": n, "value_as_written": f"{v:,}", "unit": "new cars registered", "period_start": ps,
             "period_end": pe, "quote": f"{n}: {v:,} new cars"} for n, v, ps, pe in rows]


HIST = [(f"UK new car registrations, September {y}", v, f"{y}-09-01", f"{y}-09-30")
        for y, v in ((2023, 270000), (2024, 290000), (2025, 312891))]
SEP = [(TOTAL, 350518, "2026-09-01", "2026-09-30"),
       ("UK private new car registrations, September 2026", 149158, "2026-09-01", "2026-09-30")]
# v2.12：series_naive 只作对照基线，假裁判改用 series_auto（judge_methods）；新闻页多两个 8 月的点（同比增长正好 1），
# yoy1 = 2025 年 9 月 312,891，和以前 series_naive 的估计相同。8 月的点排在 SEP 后面，p4 仍是 9 月总量
AUG = [(f"UK new car registrations, August {y}", 100000, f"{y}-08-01", f"{y}-08-31") for y in (2025, 2026)]
PAGES = {"https://news.example.co.uk/sep": _pts(HIST + SEP + AUG),
         "https://other.example.org/x": _pts([("UK used car sales, September 2026", 600000, "2026-09-01", "2026-09-30")])}


def judge_methods(user: str) -> list:
    """假裁判的方法：series_auto，target_history = 裁判表格里目标自身往年 9 月和 8 月的点（按名字找 id）。"""
    ids = re.findall(r"^(p\d+) \| [^|]+ \| UK new car registrations, (?:September 202[345]|August 202[56]) \|", user, re.M)
    return [{"id": "m1", "method": "series_auto", "params": {"target_history": ids}}]


def live_graph(live=True, early=True, verdict="target", block_d2=None, extra=(), target=None):
    """假模型跑整张图。live：ctx.live_fetch / check_published；early：ctx.early = EarlyWatch()。
    verdict：假确认模型的回答方式（published 和 published:early 都按它答，见 _verdict）。
    block_d2："search" / "fetch"：d2 的搜索 / 取页等到提前检查有了结论（停下或关掉，最多 5 秒）才返回。返回 (state, [(role, user)], ctx, g, cfg)。"""
    from langgraph.types import Command

    from triangulate.agent import graph as G
    from triangulate.agent import pipeline as P
    ctx = _ctx(live, PB.EarlyWatch() if early else None, as_of="2026-10-16" if live else "2026-10-10")
    calls, lock, d2_fetching = [], threading.Lock(), threading.Event()
    pages = {k: v + (_pts(extra) if "news" in k else []) for k, v in PAGES.items()}
    texts = {u: " ".join(p["quote"] for p in pts) + " 2023 2024 2025 2026" for u, pts in pages.items()}

    class FakeLLM:
        model = "fake"

        def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
            with lock:
                calls.append((role, user))
            if role == "plan":
                return {"target": target or UK, "market_keywords": [],
                        "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                       {"category": "related_series", "hypothesis": "h2", "data_to_find": "f2"}]}, None
            if role.startswith("extract"):
                return {"points": next(pts for u, pts in pages.items() if texts[u][:60] in user)}, None
            if role.startswith("judge"):
                return {"decisions": [], "extra_directions": [], "methods": judge_methods(user)}, None
            if role == "audit":
                return {"methods": []}, None
            if role == PB.EARLY_ROLE and block_d2 == "fetch":   # 等 d2 进了取页等待（过了取页前的检查）再确认
                d2_fetching.wait(5)
                time.sleep(0.2)
            if role in ("published", PB.EARLY_ROLE):
                rows = re.findall(r"^- ([ep]\d+): (.*)$", user, re.M)
                return {"candidates": [{"id": i, "reason": "r", "verdict": _verdict(verdict, line)} for i, line in rows]}, None
            if role == "final":
                return {"answer": "About [[estimate]]."}, None
            raise AssertionError(role)

    class Searcher:
        def search(self, prompt, *, role, qid, max_uses=3, cap=5):
            if role == "search:d2":
                if block_d2 == "search":
                    wait_early()
                return {"queries": ["q"], "urls": ["https://other.example.org/x"], "web_search_requests": 1}
            return {"queries": ["q"], "urls": ["https://news.example.co.uk/sep"], "web_search_requests": 1}

    def wait_early():
        t_end = time.monotonic() + 5
        while not (ctx.early.stop.is_set() or ctx.early.off) and time.monotonic() < t_end:
            time.sleep(0.01)

    def fake_live(url, as_of, qid):
        if block_d2 == "fetch" and "other" in url:
            d2_fetching.set()
            wait_early()
        return {"url": url, "status": "live_dated", "snapshot_ts": None, "page_date": "2026-10-05", "text": texts[url]}

    def fake_snap(url, as_of, qid):
        return {"url": url, "status": "snapshot", "snapshot_ts": "20261005000000", "page_date": "2026-10-05", "text": texts[url]}

    ctx.llm, ctx.searcher = FakeLLM(), Searcher()
    no = AssertionError("wrong fetch path")
    with mock.patch.object(P, "fetch_live", fake_live if live else mock.Mock(side_effect=no)), \
            mock.patch.object(P, "fetch_page", fake_snap if not live else mock.Mock(side_effect=no)), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
        g = G.build(ctx)
        cfg = {"configurable": {"thread_id": "live"}}
        g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
        g.invoke(Command(resume={"approved": True}), cfg)
        st = dict(g.get_state(cfg).values)
    return st, calls, ctx, g, cfg


def _verdict(mode: str, line: str) -> str:
    """假确认模型："target" = 只认总数（preliminary）；"conflict" = 认每个 9 月新车注册（总数和分项，值不同）；
    "different" = 全不认。"""
    if mode == "target":
        return "target" if "preliminary" in line else "different"
    if mode == "conflict":
        return "target" if "new car registrations, September 2026" in line else "different"
    return "different"


def _roles(calls):
    return [r for r, _ in calls]


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestEarlyStop(unittest.TestCase):
    def test_confirmed_value_stops_the_run(self):
        from triangulate.agent import outputs
        from triangulate.agent import run as R
        st, calls, ctx, g, cfg = live_graph(block_d2="search")
        roles = _roles(calls)
        self.assertEqual(roles.count(PB.EARLY_ROLE), 1)
        for r in ("judge:r1", "audit", "published", "final", "extract:d2"):
            self.assertNotIn(r, roles)                                   # 裁判、估计、终稿模型、d2 的抽取都跳过
        user = dict(calls)[PB.EARLY_ROLE]
        self.assertIn(f'- e4: "{TOTAL}" = 350,518', user)                # 只送候选：历史和分项不在
        self.assertNotIn("- e1:", user)
        d2 = next(r for r in st["results"] if r["direction_id"] == "d2")
        self.assertIn("stopped early", d2["stopped"])
        self.assertEqual(d2["pages"], [])
        pub = st["published"]
        self.assertEqual((pub["status"], pub["id"], pub["value"], pub["early_stop"]), ("published", "p4", 350518.0, True))
        self.assertEqual(pub["point"]["early_id"], "e4")
        r = st["compute"]["result"]
        self.assertEqual((r["central"], r["p10"], r["basis"]), (350518.0, None, "published"))
        self.assertIsNone(st["compute"]["estimate_result"])
        self.assertEqual(st["compute"]["methods"], [])
        self.assertEqual(st["judge_rounds"], [{"round": 1, "skipped": "published value confirmed early; judge not called"}])
        text = st["final"]["text"]
        self.assertTrue(text.startswith("Published value: 350,518 new cars registered."))
        self.assertIn(PB.EARLY_NO_ESTIMATE, text)
        self.assertIn("data point p4", text)
        pe = st["published_early"]
        self.assertEqual((pe["status"], pe["n_checks"], pe["checks"][0]["confirmed_ids"]), ("published", 1, ["p4"]))
        led = outputs.ledger(st, None)
        self.assertIn("No estimate was made", led)
        self.assertIn("Sub-agent stopped: stopped early", led)
        self.assertIn("Early checks while the sub-agents were running: 1 (published)", led)
        tmp = Path(tempfile.mkdtemp())
        try:   # save_run（state.json、ledger.md、graph.html）对提前停的运行不出错
            h = {"q": {"id": "t", "question": ctx.question, "as_of": ctx.as_of_s}, "g": g, "cfg": cfg, "ctx": ctx,
                 "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": None, "ablate": False, "t0": time.time()}
            R.save_run(h, [])
            self.assertIn("no estimate was made", (tmp / "graph.html").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_page_fetched_after_the_stop_is_not_extracted(self):
        st, calls, ctx, *_ = live_graph(block_d2="fetch")   # d2 已经在等取页时，提前停发生了
        self.assertNotIn("extract:d2", _roles(calls))
        d2 = next(r for r in st["results"] if r["direction_id"] == "d2")
        self.assertIn("stopped early", d2["stopped"])
        self.assertEqual(d2["pages"], [])
        self.assertEqual(ctx.budget.pages_used, 1)                       # d2 的名额退回

    def test_not_confirmed_runs_as_without_the_early_check(self):
        a, ca, *_ = live_graph(verdict="different")
        b, cb, *_ = live_graph(verdict="different", early=False)
        self.assertGreaterEqual(_roles(ca).count(PB.EARLY_ROLE), 1)
        self.assertNotIn(PB.EARLY_ROLE, _roles(cb))
        self.assertEqual(a["published_early"]["status"], "not_confirmed")
        self.assertNotIn("published_early", b)
        later = ("judge:r1", "audit", "published", "final")   # 裁判之后单线程：prompt 逐字相同
        self.assertEqual([c for c in ca if c[0] in later], [c for c in cb if c[0] in later])
        self.assertEqual(sorted(c for c in ca if c[0].startswith(("search", "extract"))),
                         sorted(c for c in cb if c[0].startswith(("search", "extract"))))
        for k in ("points", "judge_rounds", "compute", "published", "final"):
            self.assertEqual(json.dumps(a[k], sort_keys=True, default=str), json.dumps(b[k], sort_keys=True, default=str), k)
        self.assertNotEqual(a["compute"]["result"]["basis"], "published")

    def test_conflict_turns_the_early_check_off(self):
        st, calls, *_ = live_graph(verdict="conflict", block_d2="search", extra=[("UK new car registrations, September 2026 (revised)", 300000,
                                                               "2026-09-01", "2026-09-30")])
        roles = _roles(calls)
        self.assertEqual(roles.count(PB.EARLY_ROLE), 1)
        self.assertIn("judge:r1", roles)
        self.assertEqual(st["published_early"]["status"], "off")
        self.assertEqual(st["published"]["status"], "conflict")         # v2.4 的检查照常（裁判之后）
        self.assertFalse(st["published"].get("early_stop"))
        self.assertTrue(st["final"]["text"].startswith("About 312,891."))

    def test_backtest_never_stops_early(self):
        st, calls, *_ = live_graph(live=False, early=False)
        roles = _roles(calls)
        self.assertNotIn(PB.EARLY_ROLE, roles)
        self.assertNotIn("published", roles)
        self.assertIn("judge:r1", roles)
        self.assertEqual(st["published"]["status"], "not_checked")
        self.assertNotIn("published_early", st)
        self.assertTrue(all(pg["status"] == "snapshot" for r in st["results"] for pg in r["pages"]))

    def test_discrete_target_is_not_stopped_early(self):
        w = PB.EarlyWatch()
        llm = mock.Mock(ask=mock.Mock(side_effect=AssertionError("no early check for discrete targets")))
        pts = [{**p, "direction_id": "d1", "order": (0, j), "source_url": "u", "via": "live_dated", "page_date": "2026-10-05",
                "value": 350518.0, "published_at_if_visible": ""} for j, p in enumerate(_pts(SEP))]
        w.offer(llm, "t", {**UK, "outcome_type": "discrete"}, "2026-10-16", AS_OF, pts)
        self.assertEqual((w.checks, w.stop.is_set()), ([], False))

    def test_only_new_points_are_sent_and_nothing_after_stop(self):
        w, sent = PB.EarlyWatch(), []

        def ask(system, user, *, role, qid, max_tokens):
            sent.append(re.findall(r"^- (e\d+): ", user, re.M))
            return {"candidates": [{"id": i, "verdict": "different", "reason": "r"} for i in sent[-1]]}, None
        llm = mock.Mock(ask=ask)

        def page(n):
            return [{**p, "direction_id": "d1", "order": (n, j), "source_url": f"u{n}", "via": "live_dated",
                     "page_date": "2026-10-05", "value": float(p["value_as_written"].replace(",", "")),
                     "published_at_if_visible": ""} for j, p in enumerate(_pts(SEP))]
        w.offer(llm, "t", UK, "2026-10-16", AS_OF, page(0))
        w.offer(llm, "t", UK, "2026-10-16", AS_OF, page(1))
        self.assertEqual(sent, [["e1", "e2"], ["e3", "e4"]])
        w.stop.set()
        w.offer(llm, "t", UK, "2026-10-16", AS_OF, page(2))
        self.assertEqual(len(sent), 2)

    def test_failed_check_candidates_are_resent(self):
        """v2.5.2（审查复现）：第一次提前检查出错（transport），第二页的检查确认了。v2.5.1 只送第二页的点、确认就停，
        出错页上的 340,000 没人看；现在出错那次的候选和下一页的一起送，相差 2.9% 判 conflict、关掉提前检查。"""
        from triangulate.agent import outputs

        def run(second):
            w, sent = PB.EarlyWatch(), []

            def ask(system, user, *, role, qid, max_tokens):
                sent.append(re.findall(r"^- (e\d+): ", user, re.M))
                if len(sent) == 1:
                    return None, "transport: timeout"
                return {"candidates": [{"id": i, "verdict": "target", "reason": "r"} for i in sent[-1]]}, None
            for n, (d, v) in enumerate((("d1", 340000), ("d2", second))):
                pts = [{**p, "direction_id": d, "order": (n, 0), "source_url": f"u{n}", "via": "live_dated",
                        "page_date": "2026-10-05", "value": float(v), "published_at_if_visible": ""}
                       for p in _pts([(TOTAL, v, "2026-09-01", "2026-09-30")])]
                w.offer(mock.Mock(ask=ask), "t", UK, "2026-10-16", AS_OF, pts)
            return w, sent
        w, sent = run(350536)
        self.assertEqual(sent, [["e1"], ["e1", "e2"]])
        self.assertFalse(w.stop.is_set())
        self.assertIn("disagree", w.off)
        rec = w.record({"e1": "p1", "e2": "p2"})
        self.assertEqual((rec["status"], rec["n_error"], rec["by_status"]), ("off", 1, {"error": 1, "conflict": 1}))
        self.assertEqual(rec["checks"][1]["resent_ids"], ["p1"])
        w, sent = run(340100)   # 两个值一致（相差 0.03%）：照样停，记录写明重送过
        self.assertEqual((sent, w.stop.is_set()), ([["e1"], ["e1", "e2"]], True))
        self.assertIn("re-sent 1 candidate(s) from failed early check(s)", w.rec["note"])
        led = "\n".join(outputs.published_md({"published": {"status": "published", "note": w.rec["note"]},
                                              "published_early": w.record({})}))
        self.assertIn("Early checks while the sub-agents were running: 2 (published; by status: error 1, published 1; "
                      "candidates of a failed check are re-sent with the next check)", led)

    def test_prepare_run_flags(self):
        from triangulate.agent import run as R

        class FakeCtx:   # 真的 Context 会读 DeepSeek key：测试里换掉
            def __init__(self, *a, **kw):
                pass
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(R, "RES", tmp), mock.patch.object(R, "Context", FakeCtx), \
                    mock.patch.object(R, "build", lambda ctx: None):
                live = R.prepare_run({"id": "a", "question": "?", "as_of": date.today().isoformat()})["ctx"]
                back = R.prepare_run({"id": "b", "question": "?", "as_of": "2026-09-06"})["ctx"]
                scored = R.prepare_run({"id": "c", "question": "?", "as_of": date.today().isoformat(), "answer_value": 1})["ctx"]
                abl = R.prepare_run({"id": "d", "question": "?", "as_of": date.today().isoformat()}, ablate_own_history=True)["ctx"]
            self.assertTrue(live.live_fetch)
            self.assertIsInstance(live.early, PB.EarlyWatch)
            for c in (back, scored):
                self.assertEqual((c.live_fetch, c.early), (False, None))
            self.assertEqual((abl.live_fetch, abl.early), (True, None))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
