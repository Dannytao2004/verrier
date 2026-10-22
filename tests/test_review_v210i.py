"""v2.10i：v2.10h 审查发现的问题的回归测试。不联网、不读 key 文件：HTTP 换成 llm.urlopen_no_redirect 的假函数（Searcher 在调用时按这个
名字取，见 llm.urlopen_no_redirect 的说明）。

- 自带 key 的运行里，搜索回复没给 usage（Kimi Responses 的 usage 可以是 null；GLM 缺 usage）：token 按这次搜索预扣的 token 部分记账，
  不按 0（同 llm.py 的 JSON 调用，v2.10f）；命令行（DeepSeek）不变。
- Responses 回复 HTTP 200 但 status failed：日志 ok false、error response_failed，error.code / message 先 redact 再记、再往外报
  （Kimi K3 和 GPT 共用 openai_search_unpack）。
- Kimi、GLM 的搜索读超时：单次读超时取 adapter 的 search_timeout_s（1200 秒），超时后不重发，这次请求按预扣记账；连接失败照旧重试。
  DeepSeek（命令行、自带 key）、Claude、GPT 的超时和重发不变。
- GLM 的回复里没有查询词：账本写「(not reported by the provider)」；state.json 的 settings 记 GLM 的搜索端点和引擎。
- 网页的 GLM 说明标注国际站引擎名、链接来源没用真 key 测过；GLM 探针不再发已废弃的 /web_search。
"""
import json
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

KIMI_KEY = "sk-kimi-user-0123456789ABCDEFghij"
GLM_KEY = "0123456789abcdef0123456789abcdef.GLMuserSecret01"
GPT_KEY = "sk-proj-user-0123456789ABCDEFghij"
DS_KEY = "sk-deepseek-user-0123456789ABCDEF"
BRIEF = "Find official widget statistics for June 2026.\n\nAfter searching, reply with at most 4 URLs, most useful first."
EXTRA = config.THINKING_EXTRA_TOKENS
SEARCH_MAX = config.MAX_TOKENS["search"]
BYOK_IN = P.Budget.SEARCH_INPUT_TOKENS_BYOK


class _Resp:
    def __init__(self, body: dict, status: int = 200):
        self.status, self._raw = status, json.dumps(body).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self):
        return self._raw


class _Net:
    """假的 urlopen_no_redirect：按脚本依次回复（dict = HTTP 200 的 JSON body，异常 = 抛出），记下每次的 URL 和 timeout。"""

    def __init__(self, *script):
        self.script, self.seen = list(script), []

    def __call__(self, req, timeout):
        self.seen.append({"url": req.full_url, "timeout": timeout, "body": json.loads(req.data)})
        item = self.script.pop(0)
        if isinstance(item, BaseException):
            raise item
        return _Resp(item)


class _Case(unittest.TestCase):
    def setUp(self):
        self.sleeps = []
        p = mock.patch("time.sleep", self.sleeps.append)
        p.start()
        self.addCleanup(p.stop)

    def search(self, sp, *script, max_uses=3, cap=4, searcher=None):
        """一次 Searcher.search；返回 (结果, 假网络, 日志行)。"""
        net, logged = _Net(*script), []
        s = searcher or S.Searcher(log=logged.append, spec=sp)
        if searcher is not None:   # 传进来的 Searcher：日志照原样交给它自己的 log，同时记一份
            orig = s._log
            s._log = lambda rec: (logged.append(rec), orig(rec))
        with mock.patch.object(llm, "urlopen_no_redirect", net):
            out = s.search(BRIEF, role="search:d1", qid="t", max_uses=max_uses, cap=cap)
        return out, net, logged

    def assertNoKey(self, key, *objs):
        for o in objs:
            text = o if isinstance(o, str) else json.dumps(o, default=str, ensure_ascii=False)
            self.assertNotIn(key, text)


def kimi(region="global"):
    return PV.ModelSpec("kimi", "kimi-k3", KIMI_KEY, thinking="low", region=region)


def glm(model="glm-5.2", thinking="off", region="global"):
    return PV.ModelSpec("glm", model, GLM_KEY, thinking=thinking, region=region)


def k3_reply(status="completed", usage="default", error=None, text="https://a.example.org/w"):
    d = {"id": "resp_x", "object": "response", "status": status, "model": "kimi-k3",
         "output": [{"type": "message", "role": "assistant", "status": status,
                     "content": [{"type": "output_text", "text": text, "annotations": []}]}] if text else [],
         "incomplete_details": None, "error": error}
    if usage == "default":
        d["usage"] = {"input_tokens": 9_000, "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
                      "output_tokens": 600, "output_tokens_details": {"reasoning_tokens": 200}}
    elif usage != "absent":
        d["usage"] = usage
    return d


class TestMissingUsageIsBilledAtTheReserve(_Case):
    def test_glm_reply_without_usage(self):
        """GLM 的回复没有 usage：token 按预扣的 token 部分（72,000 输入 + 发出的 max_tokens 输出，按这个模型的预扣单价）记；
        搜索照旧每个 HTTP 200 记一次。两站、关不掉思考的 5.3（max_tokens 带思考余量）都按这次实际发出的值算。"""
        for sp, out_tokens, rate in ((glm(), SEARCH_MAX, (1.4, 4.4)), (glm("glm-5.3", "low", "cn"), SEARCH_MAX + EXTRA, None)):
            with self.subTest(price_id=sp.price_id):
                out, net, log = self.search(sp, {"id": "x", "choices": [{"index": 0, "finish_reason": "stop",
                                                                         "message": {"role": "assistant", "content": "https://a.example.org/w"}}]})
                want = P.Budget.search_tokens_reserve(sp.price_id, BYOK_IN, out_tokens)
                if rate:
                    self.assertAlmostEqual(want, (BYOK_IN * rate[0] + out_tokens * rate[1]) / 1e6)
                self.assertEqual(net.seen[0]["body"]["max_tokens"], out_tokens)
                self.assertAlmostEqual(out["usd"], want)
                self.assertEqual((out["urls"], out["web_search_requests"]), (["https://a.example.org/w"], 1))
                rec = log[0]
                self.assertEqual((rec["ok"], rec["usage_missing"], rec["usd_basis"], rec["usd"]),
                                 (True, True, "reserve (usage missing)", round(want, 6)))

    def test_budget_gets_the_reserve_not_zero(self):
        """日志行进预算（Context 里 Searcher 的 log 是 AgentLLM._log -> Budget.add，这里直接接 Budget.add）：缺 usage 的 K3 搜索让
        「已花」多出约 $0.70，而不是 0。"""
        b = P.Budget.for_model("kimi-k3", usd=5.0)
        P.configure_byok(b, "kimi-k3", "low")
        s = S.Searcher(log=lambda rec: b.add(rec), spec=kimi())
        out, _, _ = self.search(kimi(), k3_reply(usage=None), searcher=s)
        tok = P.Budget.search_tokens_reserve("kimi-k3", BYOK_IN, SEARCH_MAX + EXTRA)
        self.assertAlmostEqual(b.usd_tokens, round(tok, 6))
        self.assertGreater(b.usd_tokens, 0.69)
        self.assertAlmostEqual(out["usd"], tok)
        # 预扣本身没变：search_reserve = token 部分 + (2 x max_uses + 2) 次搜索费
        self.assertEqual(b.search_reserve(), P.Budget.search_tokens_reserve("kimi-k3", BYOK_IN, b.search_tokens)
                         + (2 * b.search_max_uses + 2) * PV.search_fee_usd("kimi-k3"))

    def test_deepseek_command_line_is_unchanged(self):
        """命令行（没有 spec）的 DeepSeek 搜索回复没有 usage 时照旧记 0（金样本之外的边角也不变）；自带 key 的 DeepSeek 运行按预扣。"""
        reply = {"content": [{"type": "text", "text": "https://a.example.org/w"}], "stop_reason": "end_turn"}
        with mock.patch("triangulate.agent.search.read_key", lambda: DS_KEY):
            cli = S.Searcher(log=lambda r: None, model="deepseek-flash")
        out, net, log = self.search(None, reply, searcher=cli)
        self.assertEqual((out["usd"], net.seen[0]["timeout"]), (0, 600))
        self.assertFalse({"usage_missing", "usd_basis"} & set(log[0]))
        sp = PV.ModelSpec("deepseek", "deepseek-flash", DS_KEY)
        out, _, log = self.search(sp, reply)
        self.assertAlmostEqual(out["usd"], P.Budget.search_tokens_reserve("deepseek-flash", BYOK_IN, SEARCH_MAX))
        self.assertEqual(log[0]["usd_basis"], "reserve (usage missing)")


class TestFailedResponses(_Case):
    def test_k3_failed_status_is_reported_redacted(self):
        """Responses 页：status failed 时 error = {code, message}（completed_at、usage 可以是 null）。以前当成 ok=True、不报 error；
        现在日志 ok false、error response_failed，code / message 先 redact（这次运行的 key）再记、再往外报；usage null 照样按预扣记账。"""
        reply = k3_reply(status="failed", usage=None, text=None,
                         error={"code": "server_error", "message": f"upstream failed for key {KIMI_KEY}"})
        out, net, log = self.search(kimi(), reply)
        self.assertEqual(len(net.seen), 1)   # 不重试
        self.assertEqual(out["error"], "response_failed (code server_error: upstream failed for key ***)")
        self.assertEqual(out["urls"], [])
        rec = log[0]
        self.assertEqual((rec["ok"], rec["error"], rec["server_error_code"], rec["server_error"], rec["stop"]),
                         (False, "response_failed", "server_error", "upstream failed for key ***", "failed"))
        self.assertAlmostEqual(rec["usd"], round(P.Budget.search_tokens_reserve("kimi-k3", BYOK_IN, SEARCH_MAX + EXTRA), 6))
        self.assertNoKey(KIMI_KEY, out, log)

    def test_gpt_shares_the_unpack(self):
        """GPT 的搜索也是 Responses（同一个 openai_search_unpack）：status failed 同样报出来；completed / incomplete 不带 error（不变）。"""
        bad = {"status": "failed", "output": [], "usage": {"input_tokens": 10, "output_tokens": 0},
               "error": {"code": "rate_limit_exceeded", "message": "slow down"}}
        self.assertEqual(PV.OPENAI.search_unpack(bad)["error"], {"code": "rate_limit_exceeded", "message": "slow down"})
        self.assertEqual(PV.OPENAI.search_unpack({**bad, "error": None})["error"], {"code": "", "message": ""})
        for status in ("completed", "incomplete"):
            self.assertNotIn("error", PV.OPENAI.search_unpack({**bad, "status": status}))
        sp = PV.ModelSpec("gpt", "gpt-6-luna", GPT_KEY)
        out, _, log = self.search(sp, bad)
        self.assertEqual((out["error"], log[0]["ok"]), ("response_failed (code rate_limit_exceeded: slow down)", False))


class TestSearchTimeouts(_Case):
    def test_kimi_and_glm_do_not_resend_after_a_read_timeout(self):
        """Kimi（非流式 Responses：服务端 900 秒没回给 504）和 GLM（非流式 Chat Completions，同 JSON 调用的 1200 秒）：单次读等 1200 秒；
        读超时（请求已发出）以后不重发，这次请求按预扣记账：token 部分 + (2 x max_uses + 2) 次搜索费。"""
        for sp, out_tokens in ((kimi(), SEARCH_MAX + EXTRA), (glm(), SEARCH_MAX), (glm("glm-5.3", "low", "cn"), SEARCH_MAX + EXTRA)):
            with self.subTest(price_id=sp.price_id):
                self.sleeps.clear()
                out, net, log = self.search(sp, TimeoutError("timed out"), max_uses=3)
                self.assertEqual([x["timeout"] for x in net.seen], [1200])
                tok = P.Budget.search_tokens_reserve(sp.price_id, BYOK_IN, out_tokens)
                fees = 8 * PV.search_fee_usd(sp.price_id)
                self.assertEqual(len(log), 1)
                rec = log[0]
                self.assertEqual((rec["ok"], rec["error"], rec["resent"], rec["timeout_s"], rec["usd_basis"]),
                                 (False, "TimeoutError", False, 1200, "reserve (read timeout, not resent)"))
                self.assertEqual((rec["usd"], rec["usd_search_fee_assumed"]), (round(tok, 6), round(fees, 4)))
                self.assertEqual((out["urls"], out["error"]), ([], "TimeoutError"))
                self.assertAlmostEqual(out["usd"], round(tok, 6))
                self.assertAlmostEqual(out["usd_search_fee_assumed"], round(fees, 4))
                self.assertEqual(self.sleeps, [])

    def test_connection_failures_are_still_retried(self):
        """连接阶段的失败（urllib 包成 URLError，请求没发出去）照旧最多试 3 次，不记账。"""
        out, net, log = self.search(kimi(), *[urllib.error.URLError(TimeoutError("timed out"))] * 3)
        self.assertEqual((len(net.seen), self.sleeps, out["usd"]), (3, [3, 6, 9], 0.0))
        self.assertEqual((log[0]["error"], log[0]["http_try"]), ("URLError", 3))
        self.assertNotIn("usd", log[0])
        glm_ok = {"choices": [{"index": 0, "finish_reason": "stop", "message": {"role": "assistant", "content": "https://a.example.org/w"}}],
                  "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
        out, net, _ = self.search(glm(), urllib.error.URLError(OSError("reset")), glm_ok)
        self.assertEqual((len(net.seen), out["urls"]), (2, ["https://a.example.org/w"]))

    def test_other_providers_keep_600_seconds_and_resend(self):
        """DeepSeek（命令行和自带 key）、Claude、GPT 不变：单次读 600 秒，读超时照旧重发（最多 3 次），不记账。"""
        with mock.patch("triangulate.agent.search.read_key", lambda: DS_KEY):
            cli = S.Searcher(log=lambda r: None, model="deepseek-flash")
        specs = (None, PV.ModelSpec("deepseek", "deepseek-flash", DS_KEY), PV.ModelSpec("claude", "claude-haiku-5-5", DS_KEY),
                 PV.ModelSpec("gpt", "gpt-6-luna", GPT_KEY))
        for sp in specs:
            with self.subTest(provider=None if sp is None else sp.provider):
                self.sleeps.clear()
                out, net, log = self.search(sp, *[TimeoutError("timed out")] * 3, searcher=cli if sp is None else None)
                self.assertEqual([x["timeout"] for x in net.seen], [600, 600, 600])
                self.assertEqual((self.sleeps, out["usd"], log[0]["error"]), ([3, 6, 9], 0.0, "TimeoutError"))
                self.assertFalse({"usd", "resent", "usd_basis"} & set(log[0]))


class TestQueriesAndSettings(_Case):
    def test_glm_ledger_says_not_reported(self):
        """GLM 的回复里没有查询词：Searcher 返回 queries_reported False，账本写「(not reported by the provider)」；
        别家（K3 服务端没搜时）照旧「(none)」。"""
        from triangulate.agent import outputs
        out, _, _ = self.search(glm(), {"choices": [{"index": 0, "finish_reason": "stop",
                                                     "message": {"role": "assistant", "content": "https://a.example.org/w"}}],
                                        "usage": {"prompt_tokens": 10, "completion_tokens": 5}})
        self.assertIs(out["queries_reported"], False)
        k3, _, _ = self.search(kimi(), k3_reply())
        self.assertNotIn("queries_reported", k3)

        def line(search):
            st = {"qid": "t", "question": "q", "as_of": "2026-09-08", "plan": {"target": {}}, "points": [], "judge_rounds": [],
                  "directions": [{"id": "d1", "category": "own_history"}], "compute": {"methods": [], "result": {}},
                  "final": {"text": "x"}, "results": [{"direction_id": "d1", "round": 1, "search": search, "pages": []}]}
            return next(x for x in outputs.ledger(st).splitlines() if x.startswith("Queries issued by the searcher"))
        self.assertEqual(line(out), "Queries issued by the searcher: (not reported by the provider)")
        self.assertEqual(line(k3), "Queries issued by the searcher: (none)")
        self.assertEqual(line({"queries": ["a b"], "urls": [], "queries_reported": False}), "Queries issued by the searcher: a b")

    def test_glm_runs_record_the_search_tool(self):
        """state.json 的 settings.search_tool：GLM 记搜索端点、工具、引擎（国际站 search_pro_jina 没实测：search_engine_tested False）；
        DeepSeek / Claude / GPT / Kimi 的 settings 不变（没有 search_tool），也不含 key。"""
        from triangulate.agent import run as R
        s = R.run_settings(glm())
        self.assertEqual(s["search_tool"], {"endpoint": "https://api.z.ai/api/paas/v4/chat/completions", "tool": "web_search",
                                            "search_engine": "search_pro_jina", "search_engine_tested": False})
        self.assertEqual(R.run_settings(glm("glm-5.3", "low", "cn"))["search_tool"],
                         {"endpoint": "https://open.bigmodel.cn/api/paas/v4/chat/completions", "tool": "web_search",
                          "search_engine": "search_std", "search_engine_tested": False})
        self.assertNoKey(GLM_KEY, s)
        self.assertNoKey(GLM_KEY.split(".")[1], s)
        for sp in (PV.ModelSpec("deepseek", "deepseek-flash", DS_KEY), kimi(), PV.ModelSpec("gpt", "gpt-6-luna", GPT_KEY),
                   PV.ModelSpec("claude", "claude-haiku-5-5", DS_KEY)):
            self.assertNotIn("search_tool", R.run_settings(sp))
        self.assertNotIn("search_tool", R.run_settings())


class TestNotesAndProbe(unittest.TestCase):
    def test_glm_web_note_says_untested(self):
        from triangulate.web import catalog
        v = catalog.providers_view(2.0)
        notes = next(p for p in v["providers"] if p["id"] == "glm")["notes"]
        en = " ".join(n["en"] for n in notes)
        zh = " ".join(n["zh"] for n in notes)
        self.assertIn("Not tested with a real key", en)
        self.assertIn("search-prime", en)
        self.assertIn("HTTP 400", en)
        self.assertIn("没用真 key 测过", zh)
        self.assertIn("search-prime", zh)

    def test_glm_probe_no_longer_calls_the_retired_search_endpoint(self):
        src = (Path(__file__).resolve().parent.parent / "probes" / "glm_key_probe.py").read_text(encoding="utf-8")
        self.assertNotIn('"/web_search"', src)
        self.assertNotIn("search-prime", src)


if __name__ == "__main__":
    unittest.main()
