"""v2.11f 现成数据前置步骤（existing.py）。全部离线：假模型、假搜索、假网页（复用 test_live 的 UK 新车注册题）。
- 只在真实使用、有人确认、连续值目标、目标期末 <= as_of 时跑；回测、--auto-approve、消融、离散、未来期间不发任何调用；
- 回测和 --auto-approve 的路径和 HEAD（537bf73）逐字节相同（test_live.live_graph 的调用和 state 的 sha256，改前算好写死）；
- 候选在同一个人工确认里；选用 -> 不跑路线、终稿由代码写；排除 -> 原流程里同值、期间重叠的点丢掉并写进终稿；没找到 -> 和今天相同。"""
import hashlib
import json
import re
import shutil
import tempfile
import threading
import time
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate.agent import existing as EX
from triangulate.agent import published as PB
from tests import test_live as TL

try:
    import fastapi  # noqa: F401
    import langgraph  # noqa: F401
    HAVE_WEB = True
except ImportError:
    HAVE_WEB = False

CONSENSUS = "Analyst consensus for UK new car registrations, September 2026"
PRE = {"https://smmt.example.co.uk/official": [(TL.TOTAL, 350518, "2026-09-01", "2026-09-30"),
                                               ("UK new car registrations, September 2025", 312891, "2025-09-01", "2025-09-30")],
       "https://analyst.example.org/est": [(CONSENSUS, 345000, "2026-09-01", "2026-09-30")]}
PRE_ROLES = ("existing:search", "extract:existing", "existing:published", "existing:check")
# HEAD 537bf73（改前）上 test_live.live_graph 三条路径的 sha256：排序后的 (role, user) 加 state 的这些键（probes/out/v211f/head_sha.py）
# v2.12 重新登记：假裁判改用 series_auto、新闻页多两个 8 月的点、合并规则和终稿的方法细节都变了（existing 步骤本身没改）。
# 537bf73 上的值是 live_auto fcf8a78c…、backtest 3b62e930…、live_early_stop cf1767ee…
# v2.12d（审查修正）又登记一次：series_auto 的结果多了 seasonal_baseline、window_month_ids、yoy 的 base_value，对照多了点 id，
# 终稿和终稿 prompt 的方法细节多写了同比对的值、逐月的点和校准表 id；数字、existing 步骤都没变（逐键比较：probes/out/v212d_existing_sha_diff.txt，只在本机）。
# v2.12c 工作区上的值是 live_auto 95447ed8…、backtest d706917c…；live_early_stop 没有方法，不变
HEAD_KEYS = ("plan", "directions", "approval", "points", "judge_rounds", "compute", "published", "final")
# v2.12e（抽取 prompt 的 unit 一条加了「韩文单位译成英文」一句；c / d 两个编号上面已用过）再登记：进程内把这一句去掉，三条都等于上一版的值
# live_auto 9f789faa…、backtest 829af9c9…、live_early_stop a4dc822d…，所以只有这一句变了
# v2.13a（单位带期间：抽取 prompt 多 unit_calc 和单位规则、裁判表格多一列、单位核对规则改写；终稿先写答案的单位）再登记。
# 逐键比较三条路径的状态（probes/out/_st_head.json 对 _st_new.json，只在本机）：数字全同，只有终稿多了「Unit of the estimate」
# 一行和 unit_full 占位符；其余差别都在发出去的 prompt 里。上一版 live_auto 91223122…、backtest 5ffb4c9d…、live_early_stop d6af7b62…
# v2.15f：compute 的 magnitude 记录多了 repair_sent（上一版 live_auto 6260287c…、backtest b01d9a74…）。
# v2.15e：抽取 prompt 的上限 15 -> 30（三条路径都发抽取，prompt 变了）；v2.15d：compute 多了 magnitude 记录（这组假题没钉单位，
# 闸门 not_checked、不发调用）。上一版 live_auto 15270f36…（v2.15d）/ 980cf6d6…、backtest c2030d2f… / d20e30ad…、live_early_stop f3cde67f…
# v2.16a：抽取上限退回 15（11-19 回归 6 次：方法用到的 23 个点没有一个排在页内第 16 位以后，点却多了约一半）。进程内把这一句
# 换回 30，三条都等于上一版的值（live_auto 9c664624…、backtest 2bf126dc…、live_early_stop 956a9004…），所以只有这一句变了
HEAD_SHA = {"live_auto": "c8bb9a63135b51425aaa54cb2ac65aab7121beacf427ded080110aac9ada2d4c",
            "backtest": "d26038f727e1d64d5de30bc1d6956ee44d06be9bd11bbe750677a4402a5a7931",
            "live_early_stop": "f3cde67fad0e808c441992428b2fd2105b068273bd0b8d8ee2a5328d90307002"}


class Harness:
    """真的 LangGraph 图 + 假模型 / 假搜索 / 假 live 页。matches：existing:check 回的 estimate 候选；verdict：PUBLISHED_*
    三处（existing:published、published:early、published）的回答方式（test_live._verdict）。"""

    def __init__(self, human=True, live=True, matches=("x3",), verdict="target", target=None, pre=None, name_extra=""):
        self.human, self.live, self.matches, self.verdict, self.target = human, live, matches, verdict, target
        pre = {u: [(n + name_extra if n == CONSENSUS else n, *r) for n, *r in rows] for u, rows in (pre or PRE).items()}
        self.pages = {**{k: v for k, v in TL.PAGES.items()}, **{u: TL._pts(rows) for u, rows in pre.items()}}
        self.pre_urls = list(pre)
        self.texts = {u: " ".join(p["quote"] for p in pts) + " 2023 2024 2025 2026" for u, pts in self.pages.items()}
        self.calls, self.searches, self.lock = [], [], threading.Lock()

    def ctx(self):
        ctx = TL._ctx(self.live, PB.EarlyWatch() if self.live else None, as_of="2026-10-16" if self.live else "2026-10-10")
        ctx.human = self.human
        h = self

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                with h.lock:
                    h.calls.append((role, user))
                if role == "plan":
                    return {"target": h.target or TL.UK, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"},
                                           {"category": "related_series", "hypothesis": "h2", "data_to_find": "f2"}]}, None
                if role.startswith("extract"):
                    return {"points": next(pts for u, pts in h.pages.items() if h.texts[u][:60] in user)}, None
                if role.startswith("judge"):
                    return {"decisions": [], "extra_directions": [], "methods": TL.judge_methods(user)}, None
                if role == "audit":
                    return {"methods": []}, None
                if role in ("published", PB.EARLY_ROLE, "existing:published"):
                    rows = re.findall(r"^- ([epx]\d+): (.*)$", user, re.M)
                    return {"candidates": [{"id": i, "reason": "r", "verdict": TL._verdict(h.verdict, line)} for i, line in rows]}, None
                if role == "existing:check":
                    return {"matches": [{"id": i, "label": "estimate", "reason": "analyst consensus for the period"}
                                        for i in h.matches]}, None
                if role == "final":
                    return {"answer": "About [[estimate]]."}, None
                raise AssertionError(role)

        class Searcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                with h.lock:
                    h.searches.append((role, prompt, max_uses, cap))
                urls = (h.pre_urls if role == "existing:search" else ["https://other.example.org/x"] if role == "search:d2"
                        else ["https://news.example.co.uk/sep"])
                return {"queries": ["q"], "urls": urls, "web_search_requests": 1}

        ctx.llm, ctx.searcher = FakeLLM(), Searcher()
        return ctx

    def live_page(self, url, as_of, qid):
        return {"url": url, "status": "live_dated", "snapshot_ts": None, "page_date": "2026-10-05", "text": self.texts[url]}

    def snap_page(self, url, as_of, qid):
        return {"url": url, "status": "snapshot", "snapshot_ts": "20261005000000", "page_date": "2026-10-05", "text": self.texts[url]}

    def patches(self):
        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        return [mock.patch.object(P, "fetch_live", self.live_page), mock.patch.object(P, "fetch_page", self.snap_page),
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"})]

    def run(self, decision=None):
        """跑到人工确认，再按 decision 恢复（默认批准路线）。返回 (state, 确认的 payload, ctx, g, cfg)。"""
        from langgraph.types import Command

        from triangulate.agent import graph as G
        ps = self.patches()
        for p in ps:
            p.start()
        try:
            ctx = self.ctx()
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "x"}}
            out = g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            payload = out["__interrupt__"][0].value
            g.invoke(Command(resume=decision or {"approved": True, "by": "human"}), cfg)
            return dict(g.get_state(cfg).values), payload, ctx, g, cfg
        finally:
            for p in ps:
                p.stop()

    def roles(self):
        return [r for r, _ in self.calls] + [r for r, *_ in self.searches]


def _head_sha(**kw):
    st, calls, *_ = TL.live_graph(**kw)
    calls = sorted((r, re.sub(r"\be\d+\b", "e#", u) if r == PB.EARLY_ROLE else u) for r, u in calls)
    blob = json.dumps({"calls": calls, "state": {k: st.get(k) for k in HEAD_KEYS}}, sort_keys=True, default=str)
    return hashlib.sha256(blob.encode()).hexdigest(), st


@unittest.skipUnless(TL.HAVE_LG, "langgraph not installed (use .venv)")
class TestNotRun(unittest.TestCase):
    def test_backtest_auto_approve_and_early_stop_paths_identical_to_head(self):
        for name, kw in (("live_auto", dict(verdict="different")), ("backtest", dict(live=False, early=False)),
                         ("live_early_stop", dict(block_d2="search"))):
            sha, st = _head_sha(**kw)
            self.assertEqual(sha, HEAD_SHA[name], name)
            self.assertEqual(st["existing"]["status"], "not_checked", name)

    def test_no_human_backtest_or_ablation_makes_no_existing_calls(self):
        for kw, abl in ((dict(human=False), False), (dict(live=False), False), ({}, True)):
            h = Harness(**kw)
            orig = h.ctx

            def ctx(orig=orig):
                c = orig()
                c.ablate_own_history = abl
                return c
            h.ctx = ctx
            st, payload, *_ = h.run()
            self.assertEqual(st["existing"], {"status": "not_checked", "note": EX.NOT_CHECKED}, kw)
            self.assertFalse([r for r in h.roles() if "existing" in r], kw)
            self.assertEqual(set(payload), {"target", "directions"})

    def test_pre_step_reserve_that_does_not_fit_is_skipped_and_the_run_goes_on(self):
        from triangulate.agent.pipeline import Budget, configure_byok
        h = Harness(matches=(), verdict="different")   # 审查 10-22：claude-haiku-5-5 思考 off、上限 $0.14（网页接受，run_floor 0.130）
        orig = h.ctx

        def ctx():
            c = orig()
            c.budget = configure_byok(Budget.for_model("claude-haiku-5-5", usd=0.14), "claude-haiku-5-5", "off")
            return c
        h.ctx = ctx
        st, payload, c, *_ = h.run()
        self.assertEqual(st["existing"]["status"], "skipped")             # 前置搜索预扣 0.151 放不下：不发调用
        self.assertIn("would be exceeded", st["existing"]["note"])
        self.assertEqual(c.budget.aborted, "")                           # 但不中止整次运行：原流程照今天跑
        self.assertFalse([r for r in h.roles() if "existing" in r])
        self.assertEqual(set(payload), {"target", "directions"})
        self.assertEqual(round(st["compute"]["result"]["central"]), 312891)
        c2 = Harness().ctx()
        c2.budget.halt("cancelled from the web UI")                      # 取消、余额不足：照旧中止
        self.assertEqual(EX.run(c2, {"plan": {"target": TL.UK}})["status"], "skipped")
        self.assertEqual(c2.budget.aborted, "cancelled from the web UI")

    def test_discrete_and_future_targets_are_not_applicable(self):
        h = Harness(target={**TL.UK, "period_start": "2026-10-01", "period_end": "2026-10-31"})
        st, payload, *_ = h.run()
        self.assertEqual(st["existing"]["status"], "not_applicable")
        self.assertIn("after as_of", st["existing"]["note"])
        self.assertFalse([r for r in h.roles() if "existing" in r])
        self.assertEqual(set(payload), {"target", "directions"})
        hh = Harness()
        rec = EX.run(hh.ctx(), {"plan": {"target": {**TL.UK, "outcome_type": "discrete"}}})
        self.assertEqual(rec, {"status": "not_applicable", "note": "discrete target"})
        self.assertFalse(hh.calls or hh.searches)


@unittest.skipUnless(TL.HAVE_LG, "langgraph not installed (use .venv)")
class TestFound(unittest.TestCase):
    def test_candidates_join_the_same_approval(self):
        h = Harness()
        st, payload, ctx, *_ = h.run({"approved": False, "by": "human"})   # 不批准：图直接结束
        self.assertEqual(set(payload), {"target", "directions", "existing"})
        xs = payload["existing"]
        self.assertEqual([(x["id"], x["type"], x["value"]) for x in xs], [("x1", "official", 350518.0), ("x3", "estimate", 345000.0)])
        ex = st["existing"]
        self.assertEqual(ex["status"], "found")
        self.assertEqual([p["id"] for p in ex["points"]], ["x1", "x2", "x3"])
        self.assertNotIn("points", st)                                   # 前置步骤的点不进原流程
        self.assertNotIn("accepted", ex)
        self.assertNotIn("excluded", ex)                                 # 不批准不算排除
        self.assertEqual(h.searches[0][0::2], ("existing:search", 6))
        self.assertEqual(h.searches[0][3], 8)
        self.assertIn("Prefer English and Chinese sources", h.searches[0][1])
        roles = [r for r, _ in h.calls]
        self.assertEqual(roles.count("extract:existing"), 2)
        self.assertEqual((roles.count("existing:published"), roles.count("existing:check")), (1, 1))
        self.assertNotIn(PB.EARLY_ROLE, roles)                           # 前置步骤的点不交给 EarlyWatch
        check = dict(h.calls)["existing:check"]
        self.assertIn("- x2:", check)
        self.assertIn("- x3:", check)
        self.assertNotIn("- x1:", check)                                 # 已确认的官方值不再送
        self.assertEqual(ctx.budget.pages_used, 0)                       # 页数名额全部退回

    def test_accept_skips_the_routes(self):
        from triangulate.agent import outputs
        from triangulate.agent import run as R
        from triangulate.web import results as WR
        h = Harness()
        st, _, ctx, g, cfg = h.run({"approved": False, "use_existing": "x1", "by": "human"})
        roles = h.roles()
        for r in roles:
            self.assertFalse(r.startswith(("search:d", "extract:d", "judge", "audit", "published", "final")), r)
        self.assertEqual(st["existing"]["accepted"]["id"], "x1")
        r = st["compute"]["result"]
        self.assertEqual((r["central"], r["p10"], r["p90"], r["basis"]), (350518.0, None, None, "existing"))
        self.assertEqual(st["compute"]["methods"], [])
        text = st["final"]["text"]
        self.assertTrue(text.startswith("Existing figure: 350,518 new cars registered (official figure)."), text)
        self.assertIn("it is not an estimate by this agent, and no estimate was made", text)
        self.assertIn(f'"{TL.TOTAL}: 350,518 new cars"', text)
        self.assertIn("smmt.example.co.uk", text)
        self.assertEqual(st["final"]["written_by"], "code (existing figure)")
        view = WR.result_view(st, "t")
        self.assertEqual((view["existing"]["id"], view["existing"]["type"], view["estimate"]["central"]), ("x1", "official", 350518.0))
        self.assertIn("basis existing (existing), weight rule none: existing figure accepted", outputs.ledger(st, None))
        tmp = Path(tempfile.mkdtemp())
        try:   # save_run（state.json、ledger.md、graph.html）对选用现成数据的运行不出错
            hh = {"q": {"id": "t", "question": ctx.question, "as_of": ctx.as_of_s}, "g": g, "cfg": cfg, "ctx": ctx,
                  "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": None, "ablate": False, "t0": time.time()}
            R.save_run(hh, [])
            self.assertIn("existing figure <b>350,518 new cars registered</b> (official, smmt.example.co.uk)",
                          (tmp / "graph.html").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_exclude_drops_same_value_and_period_from_the_routes(self):
        h = Harness()
        st, _, ctx, *_ = h.run()                                          # 批准路线 = 排除 x1、x3
        self.assertEqual(st["existing"]["excluded"], ["x1", "x3"])
        drops = [d for r in st["results"] for d in r["dropped_points"] if d["reason"].startswith(EX.EXCLUDED)]
        self.assertEqual([(d["name"], d["reason"]) for d in drops], [(TL.TOTAL, f"{EX.EXCLUDED} x1")])
        self.assertFalse([p for p in st["points"] if p["value"] == 350518.0])
        for role, user in h.calls:   # 抽取员照旧读到整页；之后的 EarlyWatch、裁判、published 节点、终稿都看不到这个值
            if not role.startswith(PRE_ROLES + ("extract",)):
                self.assertNotIn("350,518", user, role)
        self.assertIn(PB.EARLY_ROLE, [r for r, _ in h.calls])
        self.assertIn("published", [r for r, _ in h.calls])
        self.assertNotEqual(st["published"].get("status"), "published")
        text = st["final"]["text"]
        self.assertTrue(text.startswith("About 312,891."), text)
        self.assertIn("Existing figures you excluded (not used as evidence): x1 350,518 new cars registered (official figure, "
                      "smmt.example.co.uk); x3 345,000 new cars registered (third-party estimate, analyst.example.org).", text)
        self.assertIn(f'Code dropped 1 data point(s) found by the routes with the same value (exact match, relative tolerance '
                      f'1e-09) and an overlapping '
                      f'period: "{TL.TOTAL}" = 350,518 (https://news.example.co.uk/sep).', text)
        self.assertTrue(st["final"]["template"].endswith(EX.excluded_note(st)))

    def test_nothing_found_runs_as_today(self):
        a = Harness(matches=(), verdict="different")
        st_a, pay_a, *_ = a.run()
        b = Harness(human=False, verdict="different")
        st_b, pay_b, *_ = b.run()
        self.assertEqual(st_a["existing"]["status"], "none")
        self.assertEqual(st_a["existing"]["candidates"], [])
        self.assertEqual(json.dumps(pay_a, sort_keys=True), json.dumps(pay_b, sort_keys=True))   # payload 和今天相同
        later = lambda h: sorted((r, re.sub(r"\be\d+\b", "e#", u)) for r, u in h.calls if not r.startswith(PRE_ROLES))
        self.assertEqual(later(a), later(b))                             # 确认之后的请求逐字相同
        self.assertEqual(sorted(s for s in a.searches if s[0] != "existing:search"), sorted(b.searches))
        for k in ("points", "judge_rounds", "compute", "published", "final", "approval"):
            self.assertEqual(json.dumps(st_a[k], sort_keys=True, default=str), json.dumps(st_b[k], sort_keys=True, default=str), k)
        self.assertNotIn("excluded", st_a["existing"])


class TestRules(unittest.TestCase):
    def test_excluded_by_tolerance_and_period(self):
        x = {"id": "x1", "value": 350518.0, "period_start": "2026-09-01", "period_end": "2026-09-30"}

        def p(v, ps="2026-09-01", pe="2026-09-30"):
            return {"value": v, "period_start": ps, "period_end": pe}
        self.assertEqual(EX.excluded_by(p(350518.0), [x]), "x1")
        self.assertEqual(EX.excluded_by(p(350518.0 * (1 + 1e-12)), [x]), "x1")      # 只吸收浮点误差
        self.assertEqual(EX.excluded_by(p(350519.0), [x]), "")                       # 差 1 就不是同一个数
        self.assertEqual(EX.excluded_by(p(350518.0), [{**x, "value": 349000.0}]), "")   # 排除一致预期 349,000：官方值 350,518 照旧（审查 10-22）
        self.assertEqual(EX.excluded_by(p(350518.0, "2026-09-10", "2026-09-20"), [x]), "x1")   # 期间重叠
        self.assertEqual(EX.excluded_by(p(350518.0, "2026-08-01", "2026-08-31"), [x]), "")     # 不重叠
        self.assertEqual(EX.excluded_by(p(350518.0, "", "2026-10-05"), [x]), "")     # 页面日期兜底的点：期间是页面日期，不重叠
        self.assertEqual(EX.excluded_by(p(350518.0, "", ""), [x]), "")

    def test_readings_are_value_checked_before_they_count(self):
        pt = {"id": "x1", "name": CONSENSUS, "value": 345000.0, "value_as_written": "three hundred forty-five thousand",
              "scale_word": "", "unit": "new cars registered", "period_start": "2026-09-01", "period_end": "2026-09-30",
              "quote": "consensus: three hundred forty-five thousand new cars", "reading": {"number": 345000},
              "value_check": "pending", "source_url": "https://a.example.org/x", "via": "live_dated", "page_date": "2026-10-05"}
        for ok in (True, False):
            seen = []

            class LLM:
                def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                    seen.append(role)
                    if role == "existing:check":
                        return {"matches": [{"id": "x1", "label": "estimate", "reason": "r"}]}, None
                    if role.startswith("value_check"):
                        return {"match": ok}, None
                    if role.startswith("value_reread"):
                        return {"number": 345000}, None
                    raise AssertionError(role)
            ctx = type("C", (), {"llm": LLM(), "qid": "t", "as_of": date(2026, 10, 16), "as_of_s": "2026-10-16"})()
            out = EX.check(ctx, TL.UK, [dict(pt)])
            self.assertIn("value_check:x1", seen)
            self.assertEqual([c["id"] for c in out["candidates"]], ["x1"] if ok else [], ok)

    def test_page_dated_points_and_ranges_are_not_candidates(self):
        seen = []

        class LLM:
            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                seen.append((role, user))
                return {"matches": []}, None
        base = {"name": CONSENSUS, "value": 345000.0, "unit": "new cars registered", "source_url": "https://a.example.org/x",
                "via": "live_dated", "page_date": "2026-10-05", "quote": "q"}
        pts = [{**base, "id": "x1", "period_start": "", "period_end": "2026-10-05", "period_source": "page_date"},
               {**base, "id": "x2", "period_start": "2026-09-01", "period_end": "2026-09-30", "value_low": 1.0, "value_high": 2.0}]
        ctx = type("C", (), {"llm": LLM(), "qid": "t", "as_of": date(2026, 10, 16), "as_of_s": "2026-10-16"})()
        self.assertEqual(EX.check(ctx, TL.UK, pts)["candidates"], [])
        self.assertEqual(seen, [])                                       # 一个都不送


class TestCli(unittest.TestCase):
    def test_ask_human_offers_the_candidates(self):
        from triangulate.agent import run as R
        pay = {"target": {}, "directions": [], "existing": [{"id": "x1"}, {"id": "x3"}]}
        for ans, want in (("x3", {"approved": False, "use_existing": "x3", "by": "human"}),
                          ("y", {"approved": True, "by": "human"}), ("", {"approved": False, "by": "human"})):
            with mock.patch("builtins.input", return_value=ans) as inp, mock.patch("builtins.print"):
                self.assertEqual(R._ask_human(pay), want)
            self.assertIn("[y/N/x1/x3]", inp.call_args[0][0])
        with mock.patch("builtins.input", return_value="x1") as inp, mock.patch("builtins.print"):   # 没有候选：和以前相同
            self.assertEqual(R._ask_human({"target": {}, "directions": []}), {"approved": False, "by": "human"})
        self.assertEqual(inp.call_args[0][0], "Approve these directions? [y/N] ")

    def test_run_question_sets_human_only_without_auto_approve(self):
        from triangulate.agent import run as R
        seen = {}

        def prepare(q, tag, abl):
            ctx = type("C", (), {})()
            g = mock.Mock()
            g.invoke.return_value = {}
            seen[q["id"]] = ctx
            return {"g": g, "cfg": {}, "ctx": ctx}
        with mock.patch.object(R, "prepare_run", prepare), mock.patch.object(R, "save_run", lambda h, a: h):
            R.run_question({"id": "a", "question": "?", "as_of": "2026-10-16"}, auto_approve=True)
            R.run_question({"id": "b", "question": "?", "as_of": "2026-10-16"}, auto_approve=False)
        self.assertEqual((seen["a"].human, seen["b"].human), (False, True))


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestWeb(unittest.TestCase):
    def setUp(self):
        from fastapi.testclient import TestClient

        from triangulate.agent import graph as G
        from triangulate.web.app import create_app
        from triangulate.web.runs import Registry
        from tests import test_web as TW
        self.TW = TW
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.h = h = Harness(name_extra=f" {TW.FAKE_KEY}")   # key 混进候选的文字：状态视图里也要换成 ***
        for p in h.patches():
            p.start()
            self.addCleanup(p.stop)

        def prepare(q, tag="", spec=None):
            ctx = h.ctx()
            out_dir = self.tmp / q["id"] / tag
            out_dir.mkdir(parents=True, exist_ok=True)
            return {"q": q, "g": G.build(ctx), "cfg": {"configurable": {"thread_id": tag}}, "ctx": ctx, "out_dir": out_dir,
                    "stamp": "s", "tag": tag, "leak_values": None, "ablate": False, "t0": time.time()}
        self.reg = Registry(prepare=prepare, max_active=1)
        self.c = TestClient(create_app(self.reg, res=self.tmp), base_url="http://127.0.0.1")

    def test_use_existing_from_the_approval_panel(self):
        TW = self.TW
        rid = self.c.post("/api/runs", json={**TW.BYOK, "question": "UK new cars, September 2026?", "as_of": "2026-10-16"}).json()["id"]
        st = TW.wait_for(self.c, rid, ("awaiting_approval", "failed"))
        self.assertEqual(st["status"], "awaiting_approval", st.get("error"))
        self.assertEqual([x["id"] for x in st["existing"]], ["x1", "x3"])
        self.assertNotIn(TW.FAKE_KEY, json.dumps(st))
        self.assertIn("***", st["existing"][1]["name"])
        r = self.c.post(f"/api/runs/{rid}/approve", json={"use_existing": "x9"})
        self.assertEqual(r.status_code, 400)
        self.assertIn("unknown existing figure id", r.json()["detail"])
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={"use_existing": 1}).status_code, 400)
        self.assertEqual(self.c.post(f"/api/runs/{rid}/approve", json={"use_existing": "x1"}).status_code, 200)
        st = TW.wait_for(self.c, rid, ("done", "failed"))
        self.assertEqual(st["status"], "done", st.get("error"))
        self.assertEqual(st["approvals"], [{"approved": False, "use_existing": "x1", "by": "web"}])
        stages = {s["key"]: s for s in st["stages"]}
        self.assertEqual((stages["approve"]["status"], stages["approve"]["detail"]), ("done", "选用现成数据 x1"))
        self.assertEqual(stages["final"]["status"], "done")
        self.assertEqual(st["directions"], [])                           # 一个方向都没跑
        res = self.c.get("/api/result", params=st["result"]).json()
        self.assertEqual((res["existing"]["id"], res["existing"]["type"], res["estimate"]["central"]), ("x1", "official", 350518))
        self.assertNotIn(TW.FAKE_KEY, json.dumps(self.c.get(f"/api/runs/{rid}").json()))

    def test_approving_the_routes_excludes_the_candidates(self):
        TW = self.TW
        rid = self.c.post("/api/runs", json={**TW.BYOK, "question": "UK new cars, September 2026?", "as_of": "2026-10-16"}).json()["id"]
        TW.wait_for(self.c, rid, ("awaiting_approval",))
        self.c.post(f"/api/runs/{rid}/approve", json={})
        st = TW.wait_for(self.c, rid, ("done", "failed"))
        self.assertEqual(st["approvals"], [{"approved": True, "by": "web"}])
        self.assertNotIn("existing", [d["id"] for d in st["directions"]])   # 前置步骤的取页不进方向进度
        res = self.c.get("/api/result", params=st["result"]).json()
        self.assertNotIn("existing", res)
        self.assertIn("Existing figures you excluded", res["final_text"])


if __name__ == "__main__":
    unittest.main()
