"""v2.11c（计划 D3，决定 17、18）：Searcher 的返回值多一个 candidates = {provider, by_query}，记下每次搜索每个查询词的全部结果 URL
（含没被选中的），只进 state.json 审计。
- Anthropic 格式（DeepSeek / Claude）：各轮的 content 拼起来，结果块先按 tool_use_id 对 server_tool_use 的 id，没有 id 或对不上的按
  先进先出配给还没配上的查询词，还配不上就记 query None；
- OpenAI / Kimi：每个 web_search_call 一组，queries 是列表；GLM：一组，query None；
- URL 用和选中的 URL 同一个 parse_urls 规范化；不带标题；
- 哨兵：没被选中的 URL 进了 state 的 results[*].search.candidates，但不出现在任何 prompt（含后面几次搜索的请求）里。
不联网、不读 key（假 urlopen、假模型、假取页）。"""
import json
import unittest
from datetime import date
from unittest import mock

from tests import fake_glm as FG
from tests import fake_kimi as FK
from tests import fake_openai as FO
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

try:
    import langgraph  # noqa: F401
    HAVE_LG = True
except ImportError:
    HAVE_LG = False


class _Resp:
    status = 200

    def __init__(self, body):
        self._body = body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self):
        return json.dumps(self._body).encode("utf-8")


def run(*bodies, sp=None, cap=4):
    """假 urlopen 按顺序回这些 200 的回复，返回 (search 的返回值, 发出的请求体)。sp 是 None 时走 DeepSeek 命令行路径（不读 key）。"""
    script, sent = list(bodies), []

    def fake(req, timeout):
        sent.append(req.data.decode("utf-8"))
        return _Resp(script.pop(0))

    if sp is None:
        s = object.__new__(S.Searcher)
        s.model, s._key, s._log = "deepseek-flash", "not-a-key", lambda rec: None
    else:
        s = S.Searcher(log=lambda rec: None, spec=sp)
    with mock.patch("triangulate.llm.urlopen_no_redirect", fake), mock.patch("time.sleep"):
        out = s.search("p", role="search:d1", qid="t", cap=cap)
    return out, sent


def use(q, i=None):
    b = {"type": "server_tool_use", "name": "web_search", "input": {"query": q}}
    if i is not None:
        b["id"] = i
    return b


def result(*urls, i=None, title="Some title"):
    b = {"type": "web_search_tool_result", "content": [{"type": "web_search_result", "title": title, "url": u} for u in urls]}
    if i is not None:
        b["tool_use_id"] = i
    return b


def error(i=None, code="max_uses_exceeded"):
    b = {"type": "web_search_tool_result", "content": [{"type": "web_search_tool_result_error", "error_code": code}]}
    if i is not None:
        b["tool_use_id"] = i
    return b


def anthropic(*content, stop="end_turn", n_req=2):
    return {"content": list(content), "stop_reason": stop,
            "usage": {"input_tokens": 100, "output_tokens": 10, "server_tool_use": {"web_search_requests": n_req}}}


A = [f"https://a.example.org/{k}" for k in range(10)]
B = [f"https://b.example.org/{k}" for k in range(10)]


class TestAnthropicPairing(unittest.TestCase):
    def test_deepseek_probe_shape_pairs_by_tool_use_id(self):
        """probes/out/deepseek_search_probe.json 的形状：两个 use、两个 result（各 10 条）、再两个 use、两个 max_uses_exceeded，
        id 形如 call_00_...。这里把前两个 result 的顺序对调：按 id 配仍然对；挂到最近一个查询词的做法会把两组都配给第二个查询词。"""
        body = anthropic({"type": "thinking", "thinking": "..."}, {"type": "text", "text": "Let me search."},
                         use("yell monthly visits", "call_00_x"), use("yell statistics 2025", "call_01_x"),
                         result(*B, i="call_01_x"), result(*A, i="call_00_x"),
                         use("nps news release", "call_02_x"), use("september 2024 site:nps.gov", "call_03_x"),
                         error("call_02_x"), error("call_03_x"),
                         {"type": "text", "text": f"Best: {A[0]} and {B[1]}"})
        out, _ = run(body)
        self.assertEqual(out["candidates"], {"provider": "deepseek", "by_query": [
            {"query": "yell statistics 2025", "urls": B}, {"query": "yell monthly visits", "urls": A},
            {"query": "nps news release", "urls": [], "error": "max_uses_exceeded"},
            {"query": "september 2024 site:nps.gov", "urls": [], "error": "max_uses_exceeded"}]})
        # 选中的 URL 照旧（模型挑的优先，cap 4）；没被选中的 16 个只在 candidates 里
        self.assertEqual(out["urls"], [A[0], B[1], B[0], B[2]])
        self.assertEqual(out["queries"], ["yell monthly visits", "yell statistics 2025", "nps news release",
                                          "september 2024 site:nps.gov"])

    def test_first_in_first_out_when_ids_are_missing(self):
        """tests/test_search_errors.py 的形状（块里没有 id，金样本 SEARCH_BODY 也没有）：按出现顺序配给还没配上的查询词。"""
        body = anthropic(use("q1"), use("q2"), result(A[0], A[1]), result(B[0]), use("q3"), use("q4"), error(), error(),
                         {"type": "text", "text": "none"})
        out, _ = run(body)
        self.assertEqual(out["candidates"]["by_query"], [
            {"query": "q1", "urls": [A[0], A[1]]}, {"query": "q2", "urls": [B[0]]},
            {"query": "q3", "urls": [], "error": "max_uses_exceeded"}, {"query": "q4", "urls": [], "error": "max_uses_exceeded"}])

    def test_ids_are_matched_before_first_in_first_out(self):
        """对不上 id 的组只拿还没被 id 配上的查询词：先出现的 zz 组不会抢走后面按 id 配给 a 的 q1。"""
        body = anthropic(use("q1", "a"), use("q2", "b"), result(A[0], i="zz"), result(B[0], i="a"))
        out, _ = run(body)
        self.assertEqual(out["candidates"]["by_query"], [{"query": "q2", "urls": [A[0]]}, {"query": "q1", "urls": [B[0]]}])

    def test_repeated_id_keeps_its_query(self):
        """同一个 id 的结果块出现两次（真实回复里没见过，pause_turn 续接会不会重复未核实）：第二块的 id 仍对得上 q1，记 q1，
        不按先进先出拿走 q2；q2 留给后面没有 id 的块。"""
        body = anthropic(use("q1", "a"), use("q2", "b"), result(A[0], i="a"), result(A[1], i="a"), result(B[0]))
        out, _ = run(body)
        self.assertEqual(out["candidates"]["by_query"], [{"query": "q1", "urls": [A[0]]}, {"query": "q1", "urls": [A[1]]},
                                                          {"query": "q2", "urls": [B[0]]}])

    def test_unpaired_results_get_query_none(self):
        out, _ = run(anthropic(use("q1"), result(A[0]), result(B[0]), result()))
        self.assertEqual(out["candidates"]["by_query"], [{"query": "q1", "urls": [A[0]]}, {"query": None, "urls": [B[0]]},
                                                          {"query": None, "urls": []}])
        out, _ = run(anthropic(result(A[0], i="x")))   # 没有 server_tool_use
        self.assertEqual(out["candidates"]["by_query"], [{"query": None, "urls": [A[0]]}])

    def test_claude_pause_turn_pairs_across_rounds(self):
        """Claude 续接 pause_turn：use 在第一轮、result 在第二轮，拼起来按 id 配；Claude 的错误对象（content 不是 list）记 error_code。"""
        first = {**anthropic({"type": "text", "text": "I'll search."}, use("widgets June 2025", "srvtoolu_1"),
                             use("widgets 2024", "srvtoolu_2"), stop="pause_turn"), "type": "message", "role": "assistant"}
        second = anthropic(result(A[0], A[1], i="srvtoolu_1", title="Widgets | Stats Office"),
                           {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_2",
                            "content": {"type": "web_search_tool_result_error", "error_code": "too_many_requests"}},
                           {"type": "text", "text": f"Final: {A[1]}"})
        out, sent = run(first, second, sp=PV.ModelSpec("claude", "claude-opus-5-5", "sk-ant-api03-user-0123456789ABCDEF",
                                                      thinking="low"))
        self.assertEqual(len(sent), 2)
        self.assertEqual(out["candidates"], {"provider": "claude", "by_query": [
            {"query": "widgets June 2025", "urls": [A[0], A[1]]}, {"query": "widgets 2024", "urls": [], "error": "too_many_requests"}]})
        self.assertNotIn("Stats Office", json.dumps(out))

    def test_urls_are_normalised_like_the_selected_urls_and_titles_stay_out(self):
        raw = ["https://a.example.org/x.", "https://a.example.org/x#frag", "https://b.example.org/y)", "http://s.co",
               "https://c.example.org/z?q=1"]
        out, _ = run(anthropic(use("q"), result(*raw, title="Secret Title")))
        want = S.parse_urls("\n".join(raw), cap=50)
        self.assertEqual(want, ["https://a.example.org/x", "https://b.example.org/y", "https://c.example.org/z?q=1"])
        self.assertEqual(out["candidates"]["by_query"], [{"query": "q", "urls": want}])
        self.assertEqual(out["urls"], want)
        self.assertNotIn("Secret Title", json.dumps(out))

    def test_failed_request_has_no_candidates(self):
        """一轮都没拿到（这里是 401）：返回值和 v2.11b 相同，没有 candidates。"""
        import io
        import urllib.error

        def fake(req, timeout):
            raise urllib.error.HTTPError(req.full_url, 401, "x", {}, io.BytesIO(b""))

        s = object.__new__(S.Searcher)
        s.model, s._key, s._log = "deepseek-flash", "not-a-key", lambda rec: None
        with mock.patch("triangulate.llm.urlopen_no_redirect", fake), mock.patch("time.sleep"):
            out = s.search("p", role="search:d1", qid="t")
        self.assertEqual(out["error"], "http_401")
        self.assertNotIn("candidates", out)


class TestOtherProviders(unittest.TestCase):
    def test_openai_one_group_per_web_search_call(self):
        """每个 web_search_call 一组：search 带 queries 列表和 sources（这里 20 个，组内不截断）；open_page 是打开的 url；find_in_page
        没有 URL；status failed 记 error。message 里引用的 URL（c.example.org/y）不属于哪一次调用，不进 by_query（它照旧在选中的 URL 里）。"""
        reply = FO.response([{"type": "reasoning", "id": "rs_1", "summary": []},
                             FO.search_call(queries=("widget output 2025", "widgets statistics office"), sources=A + B),
                             FO.search_call(kind="open_page", url=B[0]), FO.search_call(kind="find_in_page", url=B[0]),
                             FO.search_call(status="failed", sources=()),
                             FO.message(f"Best: {A[0]} and https://c.example.org/y",
                                        citations=[("https://c.example.org/y", "Widgets | C Office")])])
        out, _ = run(reply, sp=PV.ModelSpec("gpt", "gpt-6-luna", "sk-proj-user-0123456789ABCDEFghij"))
        self.assertEqual(out["candidates"], {"provider": "gpt", "by_query": [
            {"queries": ["widget output 2025", "widgets statistics office"], "urls": A + B},
            {"queries": [], "urls": [B[0]]}, {"queries": [], "urls": []},
            {"queries": ["widgets June 2025"], "urls": [], "error": "failed"}]})
        self.assertIn("https://c.example.org/y", out["urls"])
        self.assertNotIn("C Office", json.dumps(out))

    def test_kimi_uses_the_same_groups(self):
        sp = PV.ModelSpec("kimi", "kimi-k3", "sk-kimi-user-0123456789ABCDEFghij", thinking="low")
        out, _ = run(FK.search_response(text=A[0], query="widgets June 2026", sources=(A[0], A[1], A[2])), sp=sp)
        self.assertEqual(out["candidates"], {"provider": "kimi", "by_query": [{"queries": ["widgets June 2026"],
                                                                               "urls": [A[0], A[1], A[2]]}]})
        self.assertNotIn("Title of", json.dumps(out))
        out, _ = run(FK.search_response(text=A[0], searched=False), sp=sp)   # 服务端没搜：没有 web_search_call
        self.assertEqual(out["candidates"]["by_query"], [])

    def test_glm_has_one_group_without_a_query(self):
        sp = PV.ModelSpec("glm", "glm-5.2", "0123456789abcdef0123456789abcdef.GLMuserSecret01")
        out, _ = run(FG.completion(content=f"Best: {A[0]}", web=[A[0], A[1], B[0]]), sp=sp)
        self.assertEqual(out["candidates"], {"provider": "glm", "by_query": [{"query": None, "urls": [A[0], A[1], B[0]]}]})
        self.assertNotIn("Title of", json.dumps(out))


SENTINEL = "https://sentinel.example.org/never-selected-candidate"
PICKED = [f"https://pick.example.org/{k}" for k in range(4)]   # Budget.urls_per_direction = 4：模型挑的正好 4 个


@unittest.skipUnless(HAVE_LG, "langgraph not installed (use .venv)")
class TestSentinelNeverReachesAPrompt(unittest.TestCase):
    def test_unselected_candidate_is_archived_but_never_prompted(self):
        """连续题跑完整张图（两轮搜索、抽取、裁判、修正轮、输入核对、终稿；假模型同 probes/compare_continuous_prompts.py），搜索走真的
        Searcher（假 urlopen 回 DeepSeek 形状的回复）。哨兵 URL 只在搜索结果里、不在模型挑的 URL 里：它要进 state 的 candidates，
        但不能出现在任何分析角色的 prompt、任何一次搜索请求、任何取页里。哨兵排在结果的第一个：按顺序拿候选再截到 4 个的回归也抓得到。"""
        from langgraph.types import Command

        from triangulate.agent import graph as G
        body = anthropic(use("widgets June 2025 official", "call_00"), result(SENTINEL, *PICKED, i="call_00"),
                         {"type": "text", "text": " ".join(PICKED)}, n_req=1)
        prompts, sent, fetched = [], [], []
        extra = [{"id": "b1", "category": "base_rates", "hypothesis": "h3", "data_to_find": "f3", "search_hints": ["q"]}]

        class FakeLLM:
            model = "fake"

            def ask(self, system, user, *, role, qid, max_tokens=4000, tries=2):
                prompts.append((role, system, user))
                if role == "plan":
                    return {"target": {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01",
                                       "period_end": "2026-06-30", "publisher": "X"}, "market_keywords": [],
                            "directions": [{"category": "own_history", "hypothesis": "h", "data_to_find": "f"}]}, None
                if role.startswith("extract"):
                    return {"points": [{"name": f"widgets June {y}", "value_as_written": f"{v:,}", "unit": "widgets",
                                        "period_start": f"{y}-06-01", "period_end": f"{y}-06-30", "quote": f"June {y}: {v:,} widgets"}
                                       for y, v in ((2023, 1000), (2024, 1100), (2025, 1210))]}, None
                if role.startswith("judge"):
                    bad = [{"id": "m1", "method": "linear_fit", "params": {"target_history": ["p1"]}}]
                    # v2.12：series_naive 只作对照基线、不进合并；修正轮里「能跑的方法」改成两个保留点的平均（formula_mc）
                    good = [{"id": "m1", "method": "formula_mc", "params": {"formula": "mean(a, b)", "inputs": {
                        "a": {"id": "p1", "role": "June 2023 widgets"}, "b": {"id": "p3", "role": "June 2025 widgets"}}}}]
                    return {"decisions": [], "extra_directions": extra if role == "judge:r1" else [],
                            "methods": bad if role in ("judge:r1", "judge:r2") else good}, None
                if role == "audit":
                    return {"methods": []}, None
                if role == "final":
                    return {"answer": "About [[estimate]]."}, None
                raise AssertionError(role)

        def fake_urlopen(req, timeout):
            sent.append(req.data.decode("utf-8"))
            return _Resp(body)

        def fake_fetch(url, as_of, qid, **kw):
            fetched.append(url)
            return {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                    "text": "June 2023: 1,000 widgets. June 2024: 1,100 widgets. June 2025: 1,210 widgets."}

        ctx = object.__new__(P.Context)
        ctx.qid, ctx.question, ctx.as_of_s, ctx.as_of = "t", "How many widgets in June 2026?", "2026-06-20", date(2026, 6, 20)
        ctx.budget, ctx.leak_patterns, ctx.ablate_own_history = P.Budget(), [], False
        searcher = object.__new__(S.Searcher)
        searcher.model, searcher._key, searcher._log = "deepseek-flash", "not-a-key", lambda rec: None
        ctx.llm, ctx.searcher = FakeLLM(), searcher
        with mock.patch("triangulate.llm.urlopen_no_redirect", fake_urlopen), mock.patch.object(P, "fetch_page", fake_fetch), \
                mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}):
            g = G.build(ctx)
            cfg = {"configurable": {"thread_id": "t1"}}
            g.invoke({"qid": "t", "question": ctx.question, "as_of": ctx.as_of_s}, cfg)
            g.invoke(Command(resume={"approved": True}), cfg)
            st = g.get_state(cfg).values
        searched = [r for r in st["results"] if r.get("search")]
        self.assertEqual(len(searched), 2)   # d1（第 1 轮）和 b1（第 2 轮）各搜一次
        for r in searched:
            self.assertEqual(r["search"]["urls"], PICKED)
            self.assertEqual(r["search"]["candidates"]["by_query"],
                             [{"query": "widgets June 2025 official", "urls": [SENTINEL] + PICKED}])
        self.assertEqual(len(sent), 2)
        self.assertIn("judge:r2:repair", [p[0] for p in prompts])   # 修正轮也跑到了
        self.assertIn("final", [p[0] for p in prompts])
        for role, system, user in prompts:
            with self.subTest(role=role):
                self.assertNotIn("sentinel.example.org", system + user)
        for b in sent:
            self.assertNotIn("sentinel.example.org", b)
        self.assertNotIn(SENTINEL, fetched)
        self.assertTrue(fetched)


if __name__ == "__main__":
    unittest.main()
