"""v2.5.3：max_tokens 只有一个来源（config.MAX_TOKENS），state.json 记一份 settings。
假模型跑一遍连续值的图（设置同 probes/compare_continuous_prompts.py，另外打开「答案已公布」确认），记下每个角色实际传的
max_tokens，和表逐项比对；离散值的图、提前停确认、searcher 的请求体和预扣、arm (1)(2)(3) 也一样比对。不调模型、不联网、不读 key。"""
import inspect
import json
import shutil
import tempfile
import time
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from triangulate import arms, config, forecast
from triangulate import search_direct as SD
from triangulate.agent import pipeline as P
from triangulate.agent import published as PB
from triangulate.agent import search as S

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False

# 比对时每个键换成一个不同的值：调用处查错了键（比如修正轮查了 judge、提前停查了 published），比对就会失败
DISTINCT = {k: v + i + 1 for i, (k, v) in enumerate(config.MAX_TOKENS.items())}
Q = next(q for q in forecast.QUESTIONS if q["id"] == "fc_jnto_2026_09")


def role_key(role: str) -> str:
    """calls.jsonl 里的角色名 -> 表里的键（extract:d1 -> extract，judge:r2:repair -> repair，published:early -> early）。"""
    if role.endswith(":repair"):
        return "repair"
    if role == PB.EARLY_ROLE:
        return "early"
    return role.split(":")[0]


class TestTable(unittest.TestCase):
    def test_values_are_the_ones_before_v253(self):
        """收拢时值都不变：和收拢前各处写的字面量相同（以后改哪个值，同时改这里）。v2.6a 只改了 search：2048 -> 8192。"""
        self.assertEqual(config.MAX_TOKENS, {"plan": 6000, "extract": 4000, "judge": 12000, "repair": 12000, "audit": 4000,
                                             "published": 3000, "early": 3000, "final": 4000, "search": 8192,
                                             "naive": 500, "structured": 6000, "search_direct": 4096})

    def test_defaults_point_at_the_table(self):
        self.assertEqual(SD.MAX_TOKENS, config.MAX_TOKENS["search_direct"])
        self.assertEqual(inspect.signature(SD.run_search_direct).parameters["max_tokens"].default,
                         config.MAX_TOKENS["search_direct"])
        self.assertEqual(inspect.signature(P.AgentLLM.ask).parameters["max_tokens"].default, config.MAX_TOKENS["final"])


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestGraphRoles(unittest.TestCase):
    def test_every_role_passes_its_table_value_and_state_records_settings(self):
        from langgraph.types import Command

        from triangulate.agent import graph as G
        from triangulate.agent import run as R
        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
        ctx.check_published = True   # 「答案已公布」确认也走一次（候选由下面的 mock 给）
        calls = []
        extra = [{"id": "b1", "category": "base_rates", "hypothesis": "h3", "data_to_find": "f3", "search_hints": ["q"]}]

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens, tries=2):   # 不给默认值：漏传就报 TypeError
                calls.append((role, max_tokens))
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
                if role.startswith("extract"):
                    return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                        "period_start": f"{y}-06-01", "period_end": f"{y}-06-30",
                                        "quote": f"June {y}: {v:,} widgets"}
                                       for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
                if role.startswith("judge"):
                    bad = [{"id": "m1", "method": "linear_fit", "params": {"target_history": ["p1"]}}]
                    good = [{"id": "m1", "method": "series_naive", "params": {"target_history": ["p1", "p2", "p3"], "k": 1}}]
                    return {"decisions": [{"id": "p2", "keep": False, "reason": "x"}] if role == "judge:r2" else [],
                            "extra_directions": extra if role == "judge:r1" else [],
                            "methods": bad if role in ("judge:r1", "judge:r2") else good}, None
                if role == "audit":
                    return {"methods": []}, None
                if role == "published":
                    return None, "fake: not checked"
                if role == "final":
                    return {"answer": "About [[estimate]]."}, None
                raise AssertionError(role)

        class FakeSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                return {"queries": ["q"], "urls": [f"https://a.org/{role}"], "web_search_requests": 1}

        def fake_fetch(url, as_of, qid, **kw):
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                    "text": "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."}

        ctx.llm, ctx.searcher = FakeLLM(), FakeSearcher()
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.dict(config.MAX_TOKENS, DISTINCT), mock.patch.object(P, "fetch_page", fake_fetch), \
                    mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}), \
                    mock.patch.object(PB, "candidates", lambda pts, target, as_of: (pts[:1], "fake candidates")), \
                    mock.patch.object(PB, "prompt", lambda target, as_of, cands: ("system", "user")):
                g = G.build(ctx)
                cfg = {"configurable": {"thread_id": "s1"}}
                g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
                g.invoke(Command(resume={"approved": True}), cfg)
                h = {"q": {"id": "t", "question": ctx.question, "as_of": ctx.as_of_s}, "g": g, "cfg": cfg, "ctx": ctx,
                     "out_dir": tmp, "stamp": "x", "tag": "", "leak_values": None, "ablate": False, "t0": time.time()}
                R.save_run(h, [])
                expected_settings = R.run_settings()
            saved = json.loads((tmp / "state.json").read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual({role_key(r) for r, _ in calls}, {"plan", "extract", "judge", "repair", "audit", "published", "final"})
        self.assertEqual([(r, m) for r, m in calls if m != DISTINCT[role_key(r)]], [])
        self.assertEqual(saved["settings"], expected_settings)
        self.assertEqual(saved["settings"]["max_tokens"], DISTINCT)        # 记的是运行时的表
        self.assertEqual(saved["settings"]["budget_defaults"],
                         {"usd": 1.0, "pages": 48, "round1_pages": 40, "llm_concurrency": 8, "extra_directions": 3,
                          "urls_per_direction": 4, "search_max_uses": 3, "max_directions_hard": 16})
        self.assertEqual(saved["settings"]["interval"], {"MIN_WIDTH": 2.0, "MIN_WIDTH_CHANGE": 1.25, "FALLBACK_SIGMA": 0.25,
                                                         "DEFAULT_REL_U": 0.2, "EPS": 0.01})
        for k in ("budget", "leakage", "model", "tag", "compute", "final", "published"):   # 原有的键都还在
            self.assertIn(k, saved)
        self.assertEqual(saved["published"]["status"], "error")

    def test_discrete_graph_passes_table_values_too(self):
        """离散值的图（tests.test_discrete 的假模型）：离散终稿和其他角色一样显式查表。"""
        from tests.test_discrete import discrete_graph_run
        from triangulate.agent import graph as G
        calls, build = [], G.build

        def build_recording(ctx):   # 把假模型包一层：ask 不给 max_tokens 默认值，漏传就报 TypeError
            inner = ctx.llm

            class Rec:
                model = inner.model

                def ask(self, system, user, *, role, qid, max_tokens, tries=2):
                    calls.append((role, max_tokens))
                    return inner.ask(system, user, role=role, qid=qid, max_tokens=max_tokens, tries=tries)
            ctx.llm = Rec()
            return build(ctx)
        with mock.patch.dict(config.MAX_TOKENS, DISTINCT), mock.patch.object(G, "build", build_recording):
            st, _ = discrete_graph_run()
        self.assertEqual(st["compute"]["result"]["mode"], "discrete")
        self.assertIn("final", [r for r, _ in calls])
        self.assertEqual([(r, m) for r, m in calls if m != DISTINCT[role_key(r)]], [])


class TestOtherCallers(unittest.TestCase):
    def test_early_check(self):
        calls = []

        def ask(system, user, *, role, qid, max_tokens):
            calls.append((role, max_tokens))
            return None, "fake: not checked"
        pt = {"name": "widgets June 2026", "value": 1300.0, "value_as_written": "1,300", "unit": "widgets",
              "period_start": "2026-06-01", "period_end": "2026-06-30", "direction_id": "d1", "order": (0, 0),
              "source_url": "https://a.org/x", "via": "live_dated", "page_date": "2026-07-05", "quote": "June 2026: 1,300"}
        target = {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30"}
        with mock.patch.dict(config.MAX_TOKENS, DISTINCT), \
                mock.patch.object(PB, "candidates", lambda pts, t, a, judged_only=True: (pts, "fake candidates")), \
                mock.patch.object(PB, "prompt", lambda t, a, c: ("system", "user")):
            PB.EarlyWatch().offer(mock.Mock(ask=ask), "t", target, "2026-07-10", date(2026, 7, 10), [pt])
        self.assertEqual(calls, [(PB.EARLY_ROLE, DISTINCT["early"])])

    def test_searcher_body_and_reserve(self):
        sent = []

        class Resp:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def read(self):
                return json.dumps({"content": [], "usage": {}, "stop_reason": "end_turn"}).encode("utf-8")

        def urlopen(req, timeout):
            sent.append(json.loads(req.data))
            return Resp()
        s = object.__new__(S.Searcher)   # 不走 __init__：不读 key
        s.model, s._key, s._log = "fake", "not-a-key", lambda rec: None
        with mock.patch.dict(config.MAX_TOKENS, DISTINCT), mock.patch("urllib.request.urlopen", urlopen):
            s.search("p", role="search:d1", qid="t")
        self.assertEqual([b["max_tokens"] for b in sent], [DISTINCT["search"]])
        b = P.Budget()   # 搜索预扣按表里的 search 上限算：上限改成 0，预扣正好少了「上限 x 峰时输出价」
        out = config.PRICES.get(config.MODEL, config.PRICES["deepseek-flash"])["peak"][2]
        with mock.patch.dict(config.MAX_TOKENS, {"search": 0}):
            zero = b.search_reserve()
        self.assertAlmostEqual(b.search_reserve() - zero, config.MAX_TOKENS["search"] * out / 1e6)

    def test_arms(self):
        calls = []

        class FakeLLM:
            def json_call(self, messages, *, arm, qid, attempt, max_tokens):
                calls.append((arm, max_tokens))
                return {"estimate": 3100000, "unit": ""}, '{"estimate": 3100000, "unit": ""}', None
        with mock.patch.dict(config.MAX_TOKENS, DISTINCT):
            arms.run_naive(FakeLLM(), Q)
            arms.run_structured(FakeLLM(), Q)   # 回复不合格：重试一次，两次都查表
        self.assertEqual(calls, [("naive", DISTINCT["naive"]), ("structured", DISTINCT["structured"]),
                                 ("structured", DISTINCT["structured"])])


if __name__ == "__main__":
    unittest.main()
