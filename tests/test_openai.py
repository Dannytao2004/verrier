"""v2.10c：GPT adapter（OpenAI：JSON 调用走 Chat Completions，搜索走 Responses API 的 web_search）。全部对着 127.0.0.1 上的
假服务（tests/fake_openai.py）跑：真实走 urllib + urlopen_no_redirect，请求头、请求体、HTTPError 的 body 都是真的；不联网、
不需要真 key、不读 key 文件。

每一项对照的官方文档写在各个测试的说明里（链接见 PROVIDERS.md 第 10 节）。
"""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import fake_openai as FO
from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

KEY = "sk-proj-user-0123456789ABCDEFghij"
SYSTEM = "You are a careful analyst. Reply with one JSON object."
MSGS = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "Estimate widgets in June 2026. Reply {\"a\": 1}."}]


def spec(model="gpt-6-luna", thinking="off", key=KEY, **kw):
    return PV.ModelSpec("gpt", model, key, thinking=thinking, **kw)


def ok(content='{"a": 1}', **kw):
    return ("json", 200, FO.chat_completion(content, **kw))


class _FakeServerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = FO.FakeOpenAI()

    @classmethod
    def tearDownClass(cls):
        cls.fake.close()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.sleeps = []
        patches = [mock.patch.object(PV.OpenAIAdapter, "regions", self.fake.regions()),
                   mock.patch("time.sleep", self.sleeps.append)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def chat(self, *script, sp=None, arm="judge:r1", max_tokens=12000, msgs=MSGS):
        """一次 LLM.json_call；返回 (结果或异常, 收到的请求, calls.jsonl 的行)。"""
        self.fake.reset(*script)
        calls = self.tmp / "calls.jsonl"
        calls.unlink(missing_ok=True)
        client = llm.LLM(calls_path=calls, spec=sp or spec())
        try:
            out = client.json_call(msgs, arm=arm, qid="t", attempt=1, max_tokens=max_tokens)
        except Exception as e:  # noqa: BLE001
            out = e
        lines = [json.loads(x) for x in calls.read_text(encoding="utf-8").splitlines()] if calls.exists() else []
        return out, list(self.fake.seen), lines

    def assertNoKeyIn(self, *texts):
        for t in texts:
            self.assertNotIn(KEY, t if isinstance(t, str) else json.dumps(t, default=str))


class TestChatRequest(_FakeServerCase):
    def test_chat_completions_request(self):
        """API 参考 Create chat completion：Authorization: Bearer；developer 消息（With o1 models and newer, use developer messages）；
        response_format json_object；reasoning_effort；max_completion_tokens（含 reasoning token，max_tokens 已 deprecated）；
        store: false。没有 DeepSeek 的 thinking 字段、没有 Anthropic 的请求头。"""
        out, seen, log = self.chat(ok(), sp=spec("gpt-6.1-sol", "high"))
        self.assertEqual(out, ({"a": 1}, '{"a": 1}', None))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/chat/completions"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        for h in ("x-api-key", "anthropic-version", "openai-organization", "openai-project"):
            self.assertNotIn(h, r["headers"])
        b = r["body"]
        self.assertEqual(list(b), ["model", "messages", "reasoning_effort", "response_format", "max_completion_tokens", "store"])
        self.assertEqual(b["model"], "gpt-6.1-sol")
        self.assertEqual(b["messages"], [{"role": "developer", "content": SYSTEM}, MSGS[1]])
        self.assertEqual((b["reasoning_effort"], b["response_format"], b["store"]), ("high", {"type": "json_object"}, False))
        self.assertEqual(b["max_completion_tokens"], 12000 + config.THINKING_EXTRA_TOKENS)
        for banned in ("temperature", "top_p", "max_tokens", "thinking", "stream", "tools", "logprobs"):
            self.assertNotIn(banned, b)
        self.assertEqual(log[0]["thinking"], "high")

    def test_reasoning_effort_per_model_and_role(self):
        """Reasoning 指南 / 模型页：Luna 支持 none（省略时默认 medium，所以关思考要显式发 none），6.1 Sol 和 Astra 不支持 none
        （HTTP 400）-> 网页不给 off，其余角色用 low。GPT-6 迁移指南：effort 不是 none 时去掉 temperature；是 none 时 Luna 可以带
        （照 DeepSeek 发 0）。思考 token 计入 max_completion_tokens：开思考的调用 +24,000。"""
        cases = [  # (模型, 网页档位, arm, 期望的 reasoning_effort, 有没有 temperature 0 / 有没有思考余量)
            ("gpt-6-luna", "off", "plan", "none", True),
            ("gpt-6-luna", "off", "extract:d1", "none", True),
            ("gpt-6-luna", "low", "judge:r1", "low", False),
            ("gpt-6-luna", "medium", "judge:r2:repair", "medium", False),
            ("gpt-6-luna", "high", "plan", "high", False),
            ("gpt-6-luna", "high", "audit", "none", True),
            ("gpt-6.1-sol", "low", "plan", "low", False),
            ("gpt-6.1-sol", "high", "value_check", "low", False),
            ("gpt-6-astra", "medium", "judge:r1", "medium", False),
            ("gpt-6-astra", "medium", "final", "low", False),
        ]
        for model, level, arm, effort, off in cases:
            with self.subTest(model=model, level=level, arm=arm):
                out, seen, log = self.chat(ok(), sp=spec(model, level), arm=arm, max_tokens=4000)
                b = seen[0]["body"]
                self.assertEqual(b["reasoning_effort"], effort)
                self.assertEqual(b.get("temperature"), 0 if off else None)
                self.assertEqual("temperature" in b, off)
                self.assertEqual(b["max_completion_tokens"], 4000 + (0 if off else config.THINKING_EXTRA_TOKENS))
                self.assertEqual(log[0].get("thinking"), None if off else effort)
        for model in ("gpt-6.1-sol", "gpt-6-astra"):
            with self.subTest(model=model):
                self.assertEqual(PV.thinking_levels(model), ("low", "medium", "high"))
                with self.assertRaises(PV.SpecError):
                    spec(model, "off")
                with self.assertRaises(ValueError):   # 防御：关不掉思考的模型不会发 none
                    PV.OPENAI.chat_request(model, KEY, MSGS, max_tokens=10, effort=None)
        self.assertEqual(PV.thinking_levels("gpt-6-luna"), ("off", "low", "medium", "high"))

    def test_headroom_is_capped_at_128k(self):
        _, seen, _ = self.chat(ok(), sp=spec("gpt-6-astra", "high"), max_tokens=120_000)
        self.assertEqual(seen[0]["body"]["max_completion_tokens"], 128_000)

    def test_retry_turns_keep_their_roles(self):
        """AgentLLM.ask 带错误重问时多一条 assistant 和一条 user：只有 system 改成 developer，其余原样。"""
        msgs = MSGS + [{"role": "assistant", "content": '{"a": '}, {"role": "user", "content": "Reply again with one valid JSON object."}]
        _, seen, _ = self.chat(ok(), msgs=msgs)
        self.assertEqual([m["role"] for m in seen[0]["body"]["messages"]], ["developer", "user", "assistant", "user"])
        self.assertEqual([m["content"] for m in seen[0]["body"]["messages"]], [m["content"] for m in msgs])


class TestChatReply(_FakeServerCase):
    def test_usage_is_metered_with_cache_reads_writes_and_reasoning(self):
        """API 参考 CompletionUsage：prompt_tokens_details.cached_tokens / cache_write_tokens、completion_tokens_details.reasoning_tokens。
        Prompt caching 页：普通 input = input - cached - cache_write；cached 按 cached input 价，写入按 30 分钟写入价（1.25 倍）。"""
        usage = {"prompt_tokens": 12_000, "completion_tokens": 900, "total_tokens": 12_900,
                 "prompt_tokens_details": {"cached_tokens": 4_000, "cache_write_tokens": 7_000},
                 "completion_tokens_details": {"reasoning_tokens": 600}}
        out, seen, log = self.chat(ok(usage=usage), sp=spec("gpt-6.1-sol", "low"))
        self.assertEqual(out[0], {"a": 1})
        rec = log[0]
        want = (1_000 * 2.00 + 4_000 * 0.10 + 7_000 * 2.50 + 900 * 10.00) / 1e6
        self.assertAlmostEqual(rec["usd"], round(want, 6))
        self.assertEqual((rec["finish_reason"], rec["prompt_tokens"], rec["cached_tokens"], rec["cache_write_tokens"],
                          rec["completion_tokens"], rec["reasoning_tokens"], rec["ok"]),
                         ("stop", 12_000, 4_000, 7_000, 900, 600, True))
        _, _, log = self.chat(ok(), sp=spec("gpt-6-luna", "off"))
        self.assertNotIn("reasoning_tokens", log[0])   # 关思考的调用不记（同 DeepSeek）
        self.assertAlmostEqual(log[0]["usd"], round((1000 * 0.10 + 300 * 0.50) / 1e6, 6))

    def test_refusal_length_and_content_filter(self):
        """Structured Outputs 指南 JSON mode 一节：先处理拒答（message.refusal）、撞到上限（finish_reason=length）、内容过滤
        （content_filter），不解析 JSON。拒答的文字不进日志。"""
        out, seen, log = self.chat(ok('{"a": ', finish_reason="length"))
        self.assertEqual(out, (None, '{"a": ', "reply was truncated (finish_reason=length)"))
        self.assertEqual((log[0]["error"], log[0]["finish_reason"], len(seen)), ("truncated", "length", 1))
        out, _, log = self.chat(ok('{"a"', finish_reason="content_filter"))
        self.assertEqual(out[2], "reply was stopped by the content filter (finish_reason=content_filter)")
        self.assertEqual(log[0]["error"], "content_filter")
        out, _, log = self.chat(ok(None, refusal="I can't help with that."))
        self.assertEqual(out, (None, "", "the model declined to answer (message.refusal)"))
        self.assertEqual((log[0]["error"], log[0]["refusal"]), ("refusal", True))
        self.assertNotIn("help with that", json.dumps(log))

    def test_json_is_not_repaired(self):
        """用户决定 4：不做 JSON 修补。"""
        out, _, log = self.chat(ok('```json\n{"a": 1}\n```'))
        self.assertEqual((out[0], out[2]), (None, "reply is not valid JSON"))
        self.assertEqual(log[0]["error"], "invalid_json")
        out, _, log = self.chat(ok("[1, 2]"))
        self.assertEqual(out[2], "reply is not a JSON object")

    def test_bad_bodies_are_retried(self):
        out, seen, log = self.chat(("json", 200, {"id": "x", "choices": []}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual((log[0]["error"], log[0]["will_retry"]), ("bad_response_body", True))
        out, seen, log = self.chat(("json", 200, {"choices": [{"message": None}]}), ok())
        self.assertEqual(out[0], {"a": 1})

    def test_ask_retries_once_after_a_refusal(self):
        self.fake.reset(ok(None, refusal="No."), ok())
        b = P.Budget.for_model("gpt-6-luna", usd=2.0)
        a = P.AgentLLM(self.tmp / "c.jsonl", b, spec=spec())
        self.assertEqual(a.ask("s JSON", "u", role="plan", qid="t", max_tokens=1000), ({"a": 1}, None))
        second = self.fake.seen[1]["body"]["messages"]
        self.assertEqual([m["role"] for m in second], ["developer", "user", "assistant", "user"])
        self.assertIn("declined to answer", second[-1]["content"])
        self.assertGreater(b.usd, 0)


class TestChatErrors(_FakeServerCase):
    def test_balance_and_spend_limits_stop_without_retrying(self):
        """Error codes 页：429 credit_balance_exhausted、organization / project_spend_limit_exceeded、
        organization_usage_limit_exceeded（error.type 可能是 insufficient_quota）——重试没用，抛 BalanceExhausted，不重试。"""
        cases = [("credit_balance_exhausted", "insufficient_quota", "no prepaid credits left"),
                 ("organization_spend_limit_exceeded", "insufficient_quota", "organization's spend limit"),
                 ("project_spend_limit_exceeded", "insufficient_quota", "project's spend limit"),
                 ("organization_usage_limit_exceeded", "insufficient_quota", "monthly usage limit"),
                 ("insufficient_quota", "insufficient_quota", "insufficient_quota"),
                 (None, "insufficient_quota", "insufficient_quota")]
        for code, etype, want in cases:
            with self.subTest(code=code):
                body = FO.error_body(etype, "You exceeded your current quota, please check your plan and billing details.", code)
                out, seen, log = self.chat(("json", 429, body, {"retry-after": "5"}))
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertIsInstance(out, llm.TransportError)
                self.assertEqual(len(seen), 1)
                self.assertIn(want, str(out))
                self.assertIn("OpenAI Platform", str(out))
                self.assertEqual(log[0]["error"], "http_429")
                self.assertEqual(self.sleeps, [])
                self.assertNoKeyIn(str(out), log)

    def test_rate_limits_and_overload_are_retried(self):
        """Rate limits 页：429 rate_limit_exceeded / slow_down 和 503 server_is_overloaded 是临时的，按 Retry-After（最少等这么久）
        重试；没有就退避。重试 3 次仍失败报传输错误，异常文字带 error.type / code / message。"""
        rl = FO.error_body("requests", "Rate limit reached for gpt-6-luna in organization org-abc on requests per min (RPM).",
                           "rate_limit_exceeded")
        out, seen, _ = self.chat(("json", 429, rl, {"retry-after": "17"}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertIn(17.0, self.sleeps)
        slow = FO.error_body("rate_limit_error", "Slow down", "slow_down")
        over = FO.error_body("service_unavailable_error", "The model is overloaded", "server_is_overloaded")
        out, seen, _ = self.chat(("json", 429, slow), ("json", 503, over, {"retry-after": "3"}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 3))
        out, seen, log = self.chat(*[("json", 503, over)] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 3)
        self.assertIn("http_503 (service_unavailable_error/server_is_overloaded: The model is overloaded)", str(out))
        self.assertEqual(log[-1]["server_error_code"], "server_is_overloaded")

    def test_other_errors_are_reported_as_they_are(self):
        """普通 400（参数不对等）不重试、不当成余额问题；error.type / code / message 前 200 字进日志和异常文字。
        401 / 403 = key 被拒（不读 body：401 的 message 会回显打了码的 key）。"""
        msg = "Unsupported value: 'reasoning_effort' does not support 'none' with this model."
        out, seen, log = self.chat(("json", 400, FO.error_body("invalid_request_error", msg, "unsupported_value",
                                                               "reasoning_effort")))
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 1)
        self.assertEqual((log[0]["error"], log[0]["server_error_type"], log[0]["server_error_code"], log[0]["server_error"]),
                         ("http_400", "invalid_request_error", "unsupported_value", msg))
        self.assertIn(msg, str(out))
        for status, body in ((401, FO.REAL_401_FAKE_KEY), (403, FO.error_body("invalid_request_error",
                                                                              "Country, region, or territory not supported"))):
            with self.subTest(status=status), mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
                out, seen, log = self.chat(("json", status, body))
                self.assertIsInstance(out, llm.KeyRejected)
                self.assertNotIn("server_error", log[0])   # message 一律不记
                self.assertNotIn("sk-proj", json.dumps(log))
                if status == 401:   # 401 的 message 回显打了码的 key：照旧不读 body
                    rb.assert_not_called()
                    self.assertEqual(str(out), "OpenAI rejected the API key (HTTP 401)")
                else:   # v2.10f：403 读 body，只取 error.type / code（不一定是 key 错了：例如地区不支持）
                    rb.assert_called_once()
                    self.assertEqual(str(out), "OpenAI rejected the API key or the request (HTTP 403: invalid_request_error)")
                    self.assertEqual(log[0]["server_error_type"], "invalid_request_error")
                    self.assertNotIn("Country", json.dumps(log))

    def test_masked_keys_in_server_messages_are_scrubbed(self):
        """兜底：读过的错误 body 里像 key 的片段（OpenAI 会回显 sk-proj-****0000）不进日志。"""
        body = FO.error_body("invalid_request_error", "Bad key sk-proj-**********************hij for this project")
        out, _, log = self.chat(("json", 400, body))
        self.assertEqual(log[0]["server_error"], "Bad key sk-*** for this project")
        self.assertIn("(invalid_request_error: Bad key sk-*** for this project)", str(out))
        self.assertNotIn("sk-proj", str(out) + json.dumps(log))

    def test_redirects_are_not_followed(self):
        out, seen, _ = self.chat(("redirect", 307, self.fake.url("/elsewhere")))
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual([r["path"] for r in seen], ["/v1/chat/completions"])


class TestOpenAICost(unittest.TestCase):
    """Pricing 页 Standard（2026-10-21）：Luna $0.10 / $0.50（cached $0.01，30 分钟写 $0.125，12 小时写 $0.25）、6.1 Sol $2 / $10
    （cached $0.10）、Astra $10 / $50（cached $1）；input 超过 272K token 的请求整次按 long context 价。"""

    def test_prices_match_the_pricing_page(self):
        want = {"gpt-6-luna": ((0.01, 0.10, 0.50), 0.125, 0.25, (0.02, 0.20, 0.75), 0.25, 0.50),
                "gpt-6.1-sol": ((0.10, 2.00, 10.00), 2.50, 5.00, (0.20, 4.00, 15.00), 5.00, 10.00),
                "gpt-6-astra": ((1.00, 10.00, 50.00), 12.50, 25.00, (2.00, 20.00, 75.00), 25.00, 50.00)}
        for m, (short, w30, w12, long, lw30, lw12) in want.items():
            with self.subTest(model=m):
                p = config.price(m)
                self.assertEqual((p["peak"], p["offpeak"], p["cache_write_30m"], p["cache_write_12h"]), (short, short, w30, w12))
                lc = p["long_context"]
                self.assertEqual((lc["threshold_tokens"], lc["peak"], lc["cache_write_30m"], lc["cache_write_12h"]),
                                 (272_000, long, lw30, lw12))
                self.assertEqual((p["provider"], p["source"], p["prompt_cache"]), ("gpt", config.OPENAI_PRICING, "implicit_write"))

    def test_usage_cost_chat_and_responses_fields(self):
        """Prompt caching 页的例子：input 12,000 = 普通 1,000 + cached 4,000 + 写入 7,000（30 分钟 3,000 + 12 小时 4,000）。"""
        resp = {"input_tokens": 12_000, "output_tokens": 2_000,
                "input_tokens_details": {"cached_tokens": 4_000, "cache_write_tokens": 7_000,
                                         "cache_write_tokens_details": {"ttl_30m_tokens": 3_000, "ttl_12h_tokens": 4_000}},
                "output_tokens_details": {"reasoning_tokens": 1_500}}
        self.assertAlmostEqual(PV.openai_usage_cost(resp, "gpt-6.1-sol"),
                               (1_000 * 2 + 4_000 * 0.10 + 3_000 * 2.5 + 4_000 * 5 + 2_000 * 10) / 1e6)
        chat = {"prompt_tokens": 12_000, "completion_tokens": 2_000,
                "prompt_tokens_details": {"cached_tokens": 4_000, "cache_write_tokens": 7_000}}   # Chat 只有 30 分钟一档
        self.assertAlmostEqual(PV.openai_usage_cost(chat, "gpt-6.1-sol"),
                               (1_000 * 2 + 4_000 * 0.10 + 7_000 * 2.5 + 2_000 * 10) / 1e6)
        self.assertAlmostEqual(PV.openai_usage_cost({"prompt_tokens": 1000, "completion_tokens": 10}, "gpt-6-luna"),
                               (1000 * 0.10 + 10 * 0.50) / 1e6)
        at = {"prompt_tokens": 272_000, "completion_tokens": 1_000}   # 正好 272K：Short context
        self.assertAlmostEqual(PV.openai_usage_cost(at, "gpt-6-astra"), (272_000 * 10 + 1_000 * 50) / 1e6)
        over = {"prompt_tokens": 272_001, "completion_tokens": 1_000, "prompt_tokens_details": {"cached_tokens": 1}}
        self.assertAlmostEqual(PV.openai_usage_cost(over, "gpt-6-astra"), (272_000 * 20 + 1 * 2 + 1_000 * 75) / 1e6)

    def test_directions_scale_with_gpt_prices(self):
        """默认 implicit 缓存会写缓存：「一个方向」的输入全部按 30 分钟写入价估（保守），加 $0.01 / 次搜索。"""
        pr = P.Budget.DIRECTION_PROFILE

        def cost(m):
            p = config.price(m)
            hit, miss, out = p["peak"]
            if m.startswith("gpt"):
                hit = miss = p["cache_write_30m"]
            return (pr["hit"] * hit + pr["miss"] * miss + pr["out"] * out) / 1e6 + pr["searches"] * 0.01
        flash = cost("deepseek-flash")
        got = {m: P.Budget.typical_direction_usd(m) for m in ("gpt-6-luna", "gpt-6.1-sol", "gpt-6-astra")}
        for m, v in got.items():
            with self.subTest(model=m):
                self.assertAlmostEqual(v, 0.06 * cost(m) / flash)
        dirs = {m: P.Budget.for_model(m, usd=2.0).directions for m in got}
        self.assertEqual(dirs, {m: max(1, min(16, 10, int(1.2 / got[m]))) for m in got})
        self.assertEqual(dirs, {"gpt-6-luna": 10, "gpt-6.1-sol": 5, "gpt-6-astra": 1})
        self.assertEqual(P.Budget().directions, 10)   # DeepSeek 默认路径不变
        self.assertEqual(P.Budget.typical_direction_usd("deepseek-flash"), 0.06)

    def test_reservations_include_the_cache_write_rate(self):
        """预扣：输入按 30 分钟写入价（最坏情况），超过 272K 按 long context 的写入价；搜索按 Searcher 实际发的 max_output_tokens。
        DeepSeek / Claude 的预扣和 peak_rates 相同（不变）。"""
        # v2.10f：输入按 1 个字符 1 个 token 估（DeepSeek 照旧 2 个）
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "gpt-6-luna"), (100_000 * 0.125 + 1000 * 0.5) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(300_000, 1000, "gpt-6-luna"), (300_000 * 0.25 + 1000 * 0.75) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(600_000, 1000, "gpt-6-luna"), (600_000 * 0.25 + 1000 * 0.75) / 1e6)
        for m in ("deepseek-flash", "claude-haiku-5-5", "claude-opus-5-5"):
            with self.subTest(model=m):
                self.assertEqual(P.Budget.reserve_rates(m, 1000), P.Budget.peak_rates(m, 1000))
        ctx = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("gpt-6-astra", "low"))
        self.assertEqual(ctx.budget.search_tokens, config.MAX_TOKENS["search"] + config.THINKING_EXTRA_TOKENS)
        self.assertAlmostEqual(ctx.budget.search_reserve(), (72_000 * 12.5 + ctx.budget.search_tokens * 50) / 1e6 + 8 * 0.01)
        ctx2 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("gpt-6-luna", "high"))
        self.assertEqual(ctx2.budget.search_tokens, config.MAX_TOKENS["search"])   # 搜索角色关思考（none）


def search_reply(extra=(), text="Best: https://stats.example.org/w and https://c.example.org/y", status="completed",
                 incomplete=None, usage=None):
    out = [{"type": "reasoning", "id": "rs_1", "summary": []}, FO.search_call(), *extra]
    if text is not None:
        out.append(FO.message(text, citations=[("https://c.example.org/y", "Widgets | C Office")]))
    return FO.response(out, status=status, incomplete=incomplete, usage=usage)


class TestOpenAISearch(_FakeServerCase):
    def search(self, *script, sp=None):
        self.fake.reset(*script)
        logged = []
        s = S.Searcher(log=logged.append, spec=sp or spec())
        try:
            out = s.search("Find official widget statistics.", role="search:d1", qid="t", max_uses=3, cap=4)
        except Exception as e:  # noqa: BLE001
            out = e
        return out, list(self.fake.seen), logged

    def test_request_uses_the_responses_web_search_tool(self):
        """Web search 指南：Responses API + {"type": "web_search"}；tool_choice "required"（auto 时搜索可选）；sources 要
        include web_search_call.action.sources；max_tool_calls 封顶所有内置工具调用。Responses 参考：store 默认 true（保存至少
        30 天）-> 显式 false；max_output_tokens 含 reasoning token。Luna 搜索角色关思考（none），Astra 用 low + 思考余量。"""
        out, seen, log = self.search(("json", 200, search_reply()))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/responses"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        b = r["body"]
        self.assertEqual(b, {"model": "gpt-6-luna", "input": "Find official widget statistics.", "tools": [{"type": "web_search"}],
                             "tool_choice": "required", "max_tool_calls": 3, "include": ["web_search_call.action.sources"],
                             "reasoning": {"effort": "none"}, "max_output_tokens": config.MAX_TOKENS["search"], "store": False})
        for banned in ("temperature", "messages", "stream", "background", "previous_response_id"):
            self.assertNotIn(banned, b)
        _, seen, _ = self.search(("json", 200, search_reply()), sp=spec("gpt-6-astra", "high"))
        b = seen[0]["body"]
        self.assertEqual((b["reasoning"], b["max_output_tokens"]),
                         ({"effort": "low"}, config.MAX_TOKENS["search"] + config.THINKING_EXTRA_TOKENS))

    def test_urls_queries_titles_and_fee(self):
        """输出项（Responses 参考）：web_search_call.action（search 带 queries / sources；open_page 带 url）、message 的 output_text
        和 url_citation（url、title）。只有 search 动作计次（$0.01 / 次）；标题解析出来但不外传（分析角色只拿得到 URL）。"""
        extra = (FO.search_call(queries=("widget output 2025", "widgets statistics office"), sources=("https://d.example.org/z",)),
                 FO.search_call(kind="open_page", url="https://e.example.org/p"),
                 FO.search_call(kind="find_in_page", url="https://e.example.org/p"))
        usage = {"input_tokens": 20_000, "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 1_000},
                 "output_tokens": 900, "output_tokens_details": {"reasoning_tokens": 0}}
        out, seen, log = self.search(("json", 200, search_reply(extra=extra, usage=usage)))
        self.assertEqual(out["urls"], ["https://stats.example.org/w", "https://c.example.org/y", "https://b.example.org/x",
                                       "https://d.example.org/z"])
        self.assertEqual(out["queries"], ["widgets June 2025", "widget output 2025", "widgets statistics office"])
        self.assertEqual((out["web_search_requests"], out["usd_search_fee_assumed"]), (2, 0.02))
        self.assertAlmostEqual(out["usd"], (19_000 * 0.10 + 1_000 * 0.125 + 900 * 0.50) / 1e6)
        self.assertNotIn("C Office", json.dumps(out))
        parsed = PV.OPENAI.search_unpack(search_reply(extra=extra))
        self.assertEqual(parsed["result_urls"], ["https://c.example.org/y", "https://stats.example.org/w", "https://b.example.org/x",
                                                 "https://d.example.org/z", "https://e.example.org/p"])
        self.assertEqual(parsed["result_titles"], ["Widgets | C Office", "", "", "", ""])
        rec = log[0]
        self.assertEqual((rec["kind"], rec["ok"], rec["stop"], rec["web_search_requests"], rec["usd_search_fee_assumed"],
                          rec["cache_write_tokens"], rec["reasoning_tokens"]), ("search", True, "completed", 2, 0.02, 1_000, 0))

    def test_failed_calls_incomplete_replies_and_no_text(self):
        """web_search_call.status 可以是 failed（记一个搜索错误，仍按一次计费：保守）；status incomplete（撞到
        max_output_tokens）时照样用已有的文字和 sources；没有 message 时用 sources 补。"""
        out, _, log = self.search(("json", 200, search_reply(extra=(FO.search_call(status="failed", sources=()),))))
        self.assertEqual((log[0]["n_search_errors"], log[0]["web_search_requests"]), (1, 2))
        out, _, log = self.search(("json", 200, search_reply(text="https://f.example.org/q", status="incomplete",
                                                             incomplete="max_output_tokens")))
        self.assertEqual(log[0]["stop"], "incomplete:max_output_tokens")
        self.assertEqual(out["urls"][:1], ["https://f.example.org/q"])
        out, _, log = self.search(("json", 200, search_reply(text=None)))
        self.assertEqual(out["urls"], ["https://stats.example.org/w", "https://b.example.org/x"])
        self.assertEqual(log[0]["n_text_urls"], 0)

    def test_errors_and_balance(self):
        """余额 / 额度（429 credit_balance_exhausted 等）抛 BalanceExhausted（run_direction 据此停下整次运行），不重试；
        503 / 普通 429 重试；400 照原样记在 error 里，不抛。"""
        out, seen, _ = self.search(("json", 429, FO.error_body("insufficient_quota", "You exceeded your current quota.",
                                                               "credit_balance_exhausted")))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertIn("OpenAI HTTP 429 credit_balance_exhausted", str(out))
        self.assertEqual(len(seen), 1)
        over = FO.error_body("service_unavailable_error", "overloaded", "server_is_overloaded")
        out, seen, _ = self.search(("json", 503, over, {"retry-after": "2"}), ("json", 200, search_reply()))
        self.assertEqual((len(seen), len(out["urls"])), (2, 3))
        bad = FO.error_body("invalid_request_error", "Hosted tool 'web_search' is not supported with this model.", None, "tools")
        out, seen, _ = self.search(("json", 400, bad))
        self.assertEqual((out["urls"], len(seen)), ([], 1))
        self.assertEqual(out["error"], "http_400 (invalid_request_error: Hosted tool 'web_search' is not supported with this model.)")


class TestKeyCheck(_FakeServerCase):
    def check(self, *script, sp=None):
        self.fake.reset(*script)
        out = llm.check_key(sp or spec())
        self.assertNoKeyIn(out)
        return out, list(self.fake.seen)

    def test_models_list(self):
        """List models：GET /v1/models，Authorization: Bearer，回复 {"object": "list", "data": [{"id", ...}]}（没有分页）。"""
        page = {"object": "list", "data": [{"id": "gpt-6-luna", "object": "model", "created": 1, "owned_by": "openai",
                                            "shutdown_date": None},
                                           {"id": "gpt-6-astra", "object": "model", "created": 1, "owned_by": "openai"}]}
        out, seen = self.check(("json", 200, page))
        self.assertEqual((seen[0]["method"], seen[0]["path"]), ("GET", "/v1/models"))
        self.assertEqual(seen[0]["headers"]["authorization"], f"Bearer {KEY}")
        self.assertIsNone(seen[0]["body"])
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"], out["status"]), (True, True, 2, 200))
        out, _ = self.check(("json", 200, page), sp=spec("gpt-6.1-sol", "low"))
        self.assertEqual((out["ok"], out["model_listed"]), (True, False))   # 列表完整：没有就是没有
        self.assertIn("not in the models list", out["message"])

    def test_rejected_keys_use_the_real_401_bodies(self):
        """2026-10-21 实测（probes/openai_key_probe.py，没花钱）：不带 key / 假 key 调 GET /v1/models 都是 HTTP 401；假 key 的
        message 回显了打码的 key，返回值里没有它。"""
        for body in (FO.REAL_401_NO_KEY, FO.REAL_401_FAKE_KEY):
            with self.subTest(message=body["error"]["message"][:30]):
                out, _ = self.check(("json", 401, body))
                self.assertEqual(out, {"provider": "gpt", "model": "gpt-6-luna", "ok": False, "status": 401,
                                       "error": "key_rejected", "message": "OpenAI rejected the API key (HTTP 401)"})

    def test_other_outcomes(self):
        out, _ = self.check(("json", 429, FO.error_body("insufficient_quota", "quota", "credit_balance_exhausted")))
        self.assertEqual(out["error"], "balance")
        self.assertIn("credit_balance_exhausted", out["message"])
        out, _ = self.check(("json", 403, FO.error_body("invalid_request_error", "Country, region, or territory not supported")))
        self.assertEqual(out["error"], "forbidden")   # v2.10f：403 单独记，说明里有 error.type（不一定是 key 错了）
        self.assertEqual(out["message"], "OpenAI rejected the API key or the request (HTTP 403: invalid_request_error)")
        self.assertNotIn("Country", out["message"])   # message 不取
        out, _ = self.check(("raw", 200, b"<html>"))
        self.assertEqual(out["error"], "bad_response_body")
        out, _ = self.check(("redirect", 302, self.fake.url("/x")))
        self.assertEqual(out["error"], "redirect")


class TestModelSpecGPT(unittest.TestCase):
    def test_official_endpoints(self):
        """只用 api.openai.com（global）。不提供 data residency 端点（us. / eu.：加价 10%、要项目有资格）。"""
        self.assertEqual(PV.OPENAI.regions, {"global": {"chat": "https://api.openai.com/v1/chat/completions",
                                                        "search": "https://api.openai.com/v1/responses",
                                                        "models": "https://api.openai.com/v1/models"}})
        self.assertEqual(PV.OPENAI.key_check_request("global", KEY), ("https://api.openai.com/v1/models",
                                                                     {"Authorization": f"Bearer {KEY}"}))

    def test_choices_and_public_view(self):
        self.assertEqual(PV.PROVIDERS["gpt"]["models"], ("gpt-6-luna", "gpt-6.1-sol", "gpt-6-astra"))
        self.assertEqual(PV.PROVIDERS["gpt"]["default_model"], "gpt-6-luna")
        self.assertEqual({m: PV.MODELS[m]["max_output"] for m in PV.PROVIDERS["gpt"]["models"]},
                         dict.fromkeys(PV.PROVIDERS["gpt"]["models"], 128_000))
        sp = spec("gpt-6-astra", "high", usd_cap=5)
        self.assertEqual(sp.public(), {"provider": "gpt", "model": "gpt-6-astra", "region": "global", "thinking": "high",
                                       "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high", "*": "low"},
                                       "usd_cap": 5.0, "byok": True})
        self.assertEqual(spec().public()["thinking_by_role"], {})
        self.assertNotIn(KEY, repr(sp))
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("gpt", "claude-opus-5-5", KEY)
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("openai", "gpt-6-luna", KEY)
        with self.assertRaises(PV.SpecError):
            spec(region="us")


class TestRunWithGPTSpec(_FakeServerCase):
    """prepare_run(spec=GPT) -> 图 -> save_run，全部对着假服务：规划一步收到 429 credit_balance_exhausted 就干净停下；state.json
    记 provider，不记 key；结果目录里没有 key；写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop(self):
        from triangulate.agent import run as R
        sp = spec("gpt-6.1-sol", "medium", usd_cap=1.5)
        q = {"id": "ask_gpt1", "question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20"}
        body = FO.error_body("insufficient_quota", "You exceeded your current quota.", "credit_balance_exhausted")
        self.fake.reset(*[("json", 429, body)] * 3)
        with mock.patch.object(R, "RES", self.tmp):
            h = R.prepare_run(q, "web_t", spec=sp)
            out = h["g"].invoke(R.initial_input(q), h["cfg"])
            self.assertFalse(out.get("__interrupt__"))
            st = R.save_run(h, [])
        self.assertEqual(len(self.fake.seen), 1)
        b = self.fake.seen[0]["body"]
        self.assertEqual((b["model"], b["reasoning_effort"]), ("gpt-6.1-sol", "medium"))
        self.assertTrue(st["aborted"].startswith("insufficient balance: OpenAI HTTP 429 credit_balance_exhausted"), st["aborted"])
        self.assertEqual((st["provider"], st["model"]), ("gpt", "gpt-6.1-sol"))
        self.assertEqual(st["settings"]["run_spec"]["thinking_by_role"],
                         {"plan": "medium", "judge": "medium", "repair": "medium", "*": "low"})
        files = list((self.tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            self.assertNotIn(KEY, f.read_text(encoding="utf-8"), f.name)
        self.assertFalse(sp.has_key)


if __name__ == "__main__":
    unittest.main()
