"""v2.5.5（N2）：先拿并发名额（Budget.sem）再预扣（Budget.hold）。以前是先预扣、再排队等名额，排队的调用也占着预扣：
Budget() 第一轮 10 个方向同时搜索时，在途预扣到 10 x search_reserve（约 $0.915，上限 $1.00）。现在任何时刻最多 llm_concurrency（8）份。
粘滞中止不变：超限时 hold 立即抛 BudgetExceeded，名额随 with 一起退回；之后的调用都不发。
不调模型、不联网（假 searcher / 假 json_call）。"""
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import date

from triangulate.agent import pipeline as P

N_DIRECTIONS = 10


class PeakBudget(P.Budget):
    """Budget 加一个记录：每次预扣成功后记下当时的在途预扣总额（peak）。预扣和中止的逻辑都用父类的。"""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.peak = 0.0

    @contextmanager
    def hold(self, amount):
        with super().hold(amount):
            with self._lock:
                self.peak = max(self.peak, self.reserved)
            yield


class Gate:
    """假调用的闸门：等到 n 个调用同时在里面，再停 0.2 秒（给还在排队的调用时间：旧顺序下它们这时已经预扣了），然后放行。"""

    def __init__(self, n):
        self.n, self.lock, self.full = n, threading.Lock(), threading.Event()
        self.inside = self.max_inside = self.calls = 0

    def pass_through(self):
        with self.lock:
            self.inside += 1
            self.calls += 1
            self.max_inside = max(self.max_inside, self.inside)
            if self.inside >= self.n:
                self.full.set()
        self.full.wait(5)
        time.sleep(0.2)
        with self.lock:
            self.inside -= 1


def _ctx(budget, searcher):
    ctx = object.__new__(P.Context)
    ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
    ctx.budget, ctx.searcher, ctx.leak_patterns = budget, searcher, []
    return ctx


def _free_slots(b):
    """名额是否全部退回：能不阻塞地拿到 llm_concurrency 个、第 9 个拿不到。拿到的再还回去。"""
    got = 0
    while got < 50 and b.sem.acquire(blocking=False):
        got += 1
    for _ in range(got):
        b.sem.release()
    return got


class TestSearchReservedInsideSlot(unittest.TestCase):
    def test_ten_directions_never_exceed_eight_search_reservations(self):
        b = PeakBudget()
        self.assertEqual(b.directions, N_DIRECTIONS)    # Budget() 第一轮就是 10 个方向
        gate = Gate(8)

        class GateSearcher:
            def search(self, prompt, *, role, qid, max_uses=3, cap=5):
                gate.pass_through()
                return {"queries": ["q"], "urls": [], "web_search_requests": 1}
        ctx = _ctx(b, GateSearcher())
        with ThreadPoolExecutor(N_DIRECTIONS) as ex:
            outs = list(ex.map(lambda i: P.run_direction(ctx, {"what": "w"}, {"id": f"d{i}", "category": "own_history"}, 1),
                               range(1, N_DIRECTIONS + 1)))
        sr = b.search_reserve()
        self.assertEqual([o.get("aborted") or o.get("error") for o in outs], [None] * N_DIRECTIONS)
        self.assertEqual(gate.calls, N_DIRECTIONS)
        self.assertEqual(gate.max_inside, 8)               # 并发名额照旧是 8
        self.assertLessEqual(b.peak, 8 * sr + 1e-9)        # 旧顺序：10 x sr（排队的 2 个也预扣了）
        self.assertGreaterEqual(b.peak, 8 * sr - 1e-9)     # 确实有 8 份同时在途（测试不是空的）
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(b.aborted, "")
        self.assertEqual(_free_slots(b), 8)


class TestAskReservedInsideSlot(unittest.TestCase):
    def test_ten_concurrent_asks_never_exceed_eight_reservations(self):
        b = PeakBudget()
        gate = Gate(8)

        class Fake(P.AgentLLM):
            def __init__(self):
                self.budget = b

            def json_call(self, msgs, **kw):
                gate.pass_through()
                return {"a": 1}, "", None
        llm = Fake()
        with ThreadPoolExecutor(N_DIRECTIONS) as ex:
            outs = list(ex.map(lambda i: llm.ask("s", "u", role=f"extract:d{i}", qid="t"), range(N_DIRECTIONS)))
        need = P.Budget.llm_reserve(2, P.MAX_TOKENS["final"])
        self.assertEqual(outs, [({"a": 1}, None)] * N_DIRECTIONS)
        self.assertEqual(gate.max_inside, 8)
        self.assertLessEqual(b.peak, 8 * need + 1e-9)
        self.assertGreaterEqual(b.peak, 8 * need - 1e-9)
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(_free_slots(b), 8)


class TestStickyAbortUnchanged(unittest.TestCase):
    def test_search_over_cap_aborts_and_returns_slot(self):
        b = P.Budget(usd=0.05)

        class NoSearch:
            def search(self, *a, **k):
                raise AssertionError("search must not run when the reservation does not fit")
        out = P.run_direction(_ctx(b, NoSearch()), {"what": "w"}, {"id": "d1", "category": "own_history"}, 1)
        self.assertIn("usd cap 0.05 would be exceeded", out["aborted"])
        self.assertEqual(out["search"], {})
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(_free_slots(b), 8)

    def test_abort_is_sticky_for_later_calls(self):
        b = P.Budget(usd=0.05)
        sent = []

        class Fake(P.AgentLLM):
            def __init__(self):
                self.budget = b

            def json_call(self, msgs, **kw):
                sent.append(msgs)
                return {"a": 1}, "", None
        llm = Fake()
        with self.assertRaises(P.BudgetExceeded):                       # 0.05 放不下一次 search_reserve
            with b.sem, b.hold(b.search_reserve()):
                pass
        first = b.aborted
        self.assertIn("would be exceeded", first)
        with self.assertRaises(P.BudgetExceeded):                       # 之后很小的调用也不发（粘滞）
            llm.ask("s", "u", role="final", qid="t", max_tokens=1)
        self.assertEqual(sent, [])
        self.assertEqual(b.aborted, first)                              # 中止原因是第一次的，不覆盖
        self.assertAlmostEqual(b.reserved, 0.0)
        self.assertEqual(_free_slots(b), 8)


if __name__ == "__main__":
    unittest.main()
