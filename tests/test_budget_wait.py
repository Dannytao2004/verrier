"""v2.10f：自带 key 的运行里，预扣放不下只是因为在途的预扣时等在途的调用结束（Budget.wait_for_room），只有「已花 + 这一次」放不下
才中止；Claude 搜索的 pause_turn 续接每次另预扣一份（Budget.renew_current，放不下就不续、不中止）；预扣的输入估计
（搜索输入按 p99、别家按 1 个字符 1 个 token）。命令行（没有 spec）的预算行为不变。不联网（续接的测试对着 127.0.0.1 上的假 Claude）。"""
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

from tests import fake_claude as FC
from triangulate import config
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

KEY = "sk-ant-api03-user-0123456789ABCDEF"


def byok_budget(usd=1.0, **kw):
    b = P.Budget(usd=usd, **kw)
    b.wait_for_room = True
    return b


def in_thread(fn):
    """在另一个线程里跑 fn，返回 (线程, 结果 dict)。结果：ok / error（异常对象）、t（用时）。"""
    out = {}

    def run():
        t0 = time.time()
        try:
            out["ok"] = fn()
        except Exception as e:  # noqa: BLE001
            out["error"] = e
        out["t"] = time.time() - t0
    th = threading.Thread(target=run, daemon=True)
    th.start()
    return th, out


def holder(b, amount, release: threading.Event, spend=0.0, entered: threading.Event | None = None):
    """占着一份预扣，等 release 再退回；退回之前按 spend 记一笔实际花费（同 AgentLLM._log -> Budget.add）。"""
    def fn():
        with b.hold(amount):
            if entered is not None:
                entered.set()
            release.wait(5)
            if spend:
                b.add({"usd": spend})
        return True
    return fn


class TestCommandLineBudgetUnchanged(unittest.TestCase):
    def test_no_wait_without_spec(self):
        """没有 spec（命令行、回测）：放不下就立刻中止，原因的文字和以前相同；snapshot 的字段不变；预扣的估计不变。"""
        b = P.Budget(usd=1.0)
        self.assertFalse(b.wait_for_room)
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.6, go, entered=entered))
        entered.wait(5)
        t0 = time.time()
        with self.assertRaises(P.BudgetExceeded) as cm:
            with b.hold(0.6):
                pass
        self.assertLess(time.time() - t0, 0.2)
        self.assertEqual(str(cm.exception), "usd cap 1.0 would be exceeded (spent 0.0000 + in flight 0.6000 + 0.6000)")
        go.set()
        th.join(5)
        self.assertEqual(set(P.Budget().snapshot()), {"usd_total_assumed", "usd_tokens", "usd_search_fee_assumed", "usd_cap",
                                                      "pages_used", "pages_cap", "round1_pages", "max_directions",
                                                      "urls_per_direction", "n_calls_logged", "aborted"})
        # DeepSeek 照旧每个 token 2 个字符、搜索输入 30,000 token
        self.assertAlmostEqual(P.Budget.llm_reserve(40_000, 16_000), (20_000 * 0.30 + 16_000 * 1.20) / 1e6)
        self.assertAlmostEqual(P.Budget().search_reserve(), (30_000 * 0.30 + 8192 * 1.20) / 1e6 + 8 * 0.01)
        self.assertEqual(P.Budget().directions, 10)


class TestWaitForRoom(unittest.TestCase):
    def test_waits_for_in_flight_then_goes(self):
        """在途 0.6 + 这次 0.6 > 1.0，但已花 0 + 0.6 放得下：等在途的退回再预扣，不中止。"""
        b = byok_budget()
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.6, go, entered=entered))
        entered.wait(5)
        cms = []   # 留着 context manager 的引用：拿到预扣就返回，不退回
        th2, res = in_thread(lambda: cms.append(b.hold(0.6)) or bool(cms[-1].__enter__()))
        time.sleep(0.3)
        self.assertNotIn("ok", res)                  # 还在等
        go.set()
        th.join(5)
        th2.join(5)
        self.assertTrue(res.get("ok"), res)
        self.assertEqual(b.aborted, "")
        self.assertEqual(b.n_waits, 1)
        self.assertGreater(b.wait_s, 0.2)
        self.assertAlmostEqual(b.reserved, 0.6)
        cms[0].__exit__(None, None, None)
        self.assertAlmostEqual(b.reserved, 0.0)
        snap = b.snapshot()
        self.assertEqual((snap["waited_for_room"], snap["aborted"]), (1, ""))

    def test_aborts_when_spent_plus_this_does_not_fit(self):
        """已花 0.5 + 这次 0.6 > 1.0：等也没用，立刻中止（原因的文字同命令行）。"""
        b = byok_budget()
        b.add({"usd": 0.5})
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.1, go, entered=entered))
        entered.wait(5)
        t0 = time.time()
        with self.assertRaises(P.BudgetExceeded):
            with b.hold(0.6):
                pass
        self.assertLess(time.time() - t0, 0.2)
        self.assertIn("usd cap 1.0 would be exceeded (spent 0.5000 + in flight 0.1000 + 0.6000)", b.aborted)
        go.set()
        th.join(5)

    def test_no_in_flight_no_wait(self):
        b = byok_budget()
        with self.assertRaises(P.BudgetExceeded):
            with b.hold(1.5):
                pass
        self.assertEqual(b.n_waits, 0)

    def test_wait_then_abort_when_the_in_flight_call_spends_the_room(self):
        """等的时候在途的调用实际花了 0.6：退回之后已花 0.6 + 0.6 > 1.0，中止。"""
        b = byok_budget()
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.7, go, spend=0.6, entered=entered))
        entered.wait(5)
        th2, res = in_thread(lambda: b.hold(0.6).__enter__())
        time.sleep(0.2)
        go.set()
        th.join(5)
        th2.join(5)
        self.assertIsInstance(res.get("error"), P.BudgetExceeded, res)
        self.assertIn("spent 0.6000 + in flight 0.0000 + 0.6000", b.aborted)

    def test_cancel_and_balance_stop_wake_the_waiters(self):
        """等着的预扣在中止（网页取消 / 余额不足的 Budget.halt）后马上放弃，不等在途的调用结束。"""
        b = byok_budget()
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.9, go, entered=entered))
        entered.wait(5)
        th2, res = in_thread(lambda: b.hold(0.5).__enter__())
        time.sleep(0.2)
        b.halt("cancelled from the web UI")
        th2.join(2)
        self.assertIsInstance(res.get("error"), P.BudgetExceeded, res)
        self.assertLess(res["t"], 1.5)
        self.assertEqual(b.aborted, "cancelled from the web UI")
        go.set()
        th.join(5)

    def test_many_concurrent_holds_never_exceed_the_cap_and_all_finish(self):
        """20 个调用、每个预扣 0.3、上限 1.0：任何时刻在途最多 3 份（不超过上限），全部跑完，不中止、不死锁。"""
        b = byok_budget()
        peak, lock = [0.0], threading.Lock()

        def call():
            with b.sem, b.hold(0.3):
                with lock:
                    peak[0] = max(peak[0], b.reserved)
                time.sleep(0.02)
                b.add({"usd": 0.01})
            return True
        threads = [in_thread(call) for _ in range(20)]
        for th, _ in threads:
            th.join(10)
        self.assertTrue(all(r.get("ok") for _, r in threads), [r for _, r in threads if not r.get("ok")])
        self.assertLessEqual(peak[0], 0.9 + 1e-9)
        self.assertEqual(b.aborted, "")
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(b._n_holds, 0)
        self.assertGreater(b.n_waits, 0)


class TestRenew(unittest.TestCase):
    def test_renew_swaps_the_spent_reservation(self):
        """同一次调用里的下一个请求：换掉已用掉的那份（不等自己）；放不下返回 False，不中止整次运行。"""
        b = byok_budget()
        self.assertTrue(b.renew_current())   # 不在预扣里：不管
        with b.hold(0.4) as h:
            b.add({"usd": 0.3})                # 第一个请求的实际花费
            t0 = time.time()
            self.assertTrue(b.renew_current())  # 0.3 + 0.4 <= 1.0（旧的那份先退回，不会等自己）
            self.assertLess(time.time() - t0, 0.2)
            self.assertAlmostEqual(b.reserved, 0.4)
            self.assertEqual((b._n_holds, h.amount, h.live), (1, 0.4, True))
            b.add({"usd": 0.5})                # 第二个请求花了 0.5：已花 0.8
            self.assertFalse(b.renew_current())   # 0.8 + 0.4 > 1.0：不续
            self.assertAlmostEqual(b.reserved, 0.0)
            self.assertEqual((b._n_holds, h.live), (0, False))
        self.assertEqual(b.aborted, "")         # 没有中止
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(b._n_holds, 0)

    def test_renew_waits_for_other_threads(self):
        b = byok_budget()
        go, entered = threading.Event(), threading.Event()
        th, _ = in_thread(holder(b, 0.5, go, entered=entered))
        entered.wait(5)
        got = {}

        def mine():
            with b.hold(0.4):
                got["first"] = True
                threading.Timer(0.3, go.set).start()
                b.add({"usd": 0.2})
                return b.renew_current()       # 0.2 + 0.5（别人在途）+ 0.4 > 1.0：等别人退回后 0.2 + 0.4 放得下
        th2, res = in_thread(mine)
        th2.join(5)
        th.join(5)
        self.assertTrue(res.get("ok"), res)
        self.assertGreater(res["t"], 0.25)


SEARCH_RESULT = {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_1", "content": [
    {"type": "web_search_result", "url": "https://stats.example.org/w", "title": "W"}]}


def search_reply(stop="end_turn", text="Best: https://stats.example.org/w"):
    content = [{"type": "server_tool_use", "id": "srvtoolu_1", "name": "web_search", "input": {"query": "widgets"}}, SEARCH_RESULT]
    if text is not None:
        content.append({"type": "text", "text": text})
    return {"id": "msg_s", "type": "message", "role": "assistant", "model": "claude-opus-5-5", "content": content,
            "stop_reason": stop, "usage": {"input_tokens": 6000, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
                                           "output_tokens": 900, "server_tool_use": {"web_search_requests": 1}}}


class TestSearchContinuationReserves(unittest.TestCase):
    """Claude 搜索的 pause_turn 续接：Context 把 Searcher.renew 设成 Budget.renew_current；续接之前另预扣一份。"""

    @classmethod
    def setUpClass(cls):
        cls.fake = FC.FakeClaude()

    @classmethod
    def tearDownClass(cls):
        cls.fake.close()

    def setUp(self):
        p = mock.patch.object(PV.ClaudeAdapter, "regions", self.fake.regions())
        p.start()
        self.addCleanup(p.stop)

    def ctx(self, cap):
        sp = PV.ModelSpec("claude", "claude-opus-5-5", KEY, thinking="low", usd_cap=cap)
        return P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=sp)

    def run_search(self, ctx, *script):
        self.fake.reset(*script)
        b = ctx.budget
        with b.sem, b.hold(b.search_reserve()):
            out = ctx.searcher.search("Find widgets.", role="search:d1", qid="t", max_uses=3, cap=4)
        return out, list(self.fake.seen)

    def test_continuation_reserves_again(self):
        ctx = self.ctx(10.0)
        self.assertEqual(ctx.searcher.renew, ctx.budget.renew_current)
        calls = []
        real = ctx.budget.renew_current
        ctx.searcher.renew = lambda: calls.append(1) or real()
        out, seen = self.run_search(ctx, ("json", 200, search_reply("pause_turn", None)), ("json", 200, search_reply()))
        self.assertEqual((len(seen), len(calls), out["continuations"]), (2, 1, 1))
        self.assertNotIn("error", out)
        self.assertEqual(ctx.budget.aborted, "")
        self.assertAlmostEqual(ctx.budget.reserved, 0.0)

    def test_no_room_for_the_continuation(self):
        """上限只剩不到一份搜索预扣：不发续接的请求，用第一次的结果，不中止整次运行。"""
        ctx = self.ctx(3.0)
        b = ctx.budget
        first_cost = (6000 * 4 + 900 * 20) / 1e6 + 0.01
        b.add({"usd": 3.0 - b.search_reserve() - first_cost + 1e-3})   # 第一个请求记账后，已花 + 一份 > 上限
        out, seen = self.run_search(ctx, ("json", 200, search_reply("pause_turn", None)), ("json", 200, search_reply()))
        self.assertEqual(len(seen), 1)
        self.assertEqual(out["urls"], ["https://stats.example.org/w"])
        self.assertEqual(out["error"], "continuation 1: not sent: the spending cap has no room for another worst-case "
                                       "search request")
        self.assertEqual(b.aborted, "")
        self.assertAlmostEqual(b.reserved, 0.0)

    def test_reserve_inputs(self):
        """模型自己搜的 provider（Claude、GPT、DeepSeek）搜索输入按 72,000 token；生成查询词的（Kimi、GLM）照旧 30,000。"""
        ctx = self.ctx(10.0)
        self.assertEqual(ctx.budget.search_input_tokens, 72_000)
        for provider, model, want in (("kimi", "kimi-k2.6", 30_000), ("glm", "glm-5.2", 30_000), ("gpt", "gpt-6-luna", 72_000),
                                      ("deepseek", "deepseek-flash", 72_000)):
            sp = PV.ModelSpec(provider, model, KEY)
            c = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=sp)
            self.assertEqual((c.budget.search_input_tokens, c.budget.wait_for_room), (want, True), model)
        self.assertEqual(PV.reserve_chars_per_token("deepseek-v4-pro"), 2)
        for m in ("claude-sonnet-5-5", "gpt-6.1-sol", "kimi-k3@cn", "glm-5.3"):
            self.assertEqual(PV.reserve_chars_per_token(m), 1, m)
        self.assertEqual(config.MAX_TOKENS["search"], 8192)


if __name__ == "__main__":
    unittest.main()
