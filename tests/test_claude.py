"""v2.10b：Claude adapter（原生 Messages API）和 Claude 搜索。全部对着 127.0.0.1 上的假服务（tests/fake_claude.py）跑：
真实走 urllib + urlopen_no_redirect，请求头、请求体、流式读取、HTTPError 的 body 都是真的；不联网、不需要真 key、不读 key 文件。

每一项对照的官方文档写在各个测试的说明里（链接见 PROVIDERS.md 的 Claude 一节）。
"""
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

from tests import fake_claude as FC
from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

KEY = "sk-ant-api03-user-0123456789ABCDEF"
SYSTEM = "You are a careful analyst. Reply with one JSON object."
MSGS = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "Estimate widgets in June 2026. Reply {\"a\": 1}."}]
USAGE = {"input_tokens": 1000, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0, "output_tokens": 300}


def spec(model="claude-opus-5-5", thinking="low", key=KEY, **kw):
    return PV.ModelSpec("claude", model, key, thinking=thinking, **kw)


def ok_stream(text='{"a": 1}', usage=None, **kw):
    return ("sse", FC.sse_message([("thinking", ""), ("text", text)], usage=usage or {"output_tokens": 300},
                                  start_usage={"input_tokens": 1000, "cache_read_input_tokens": 0,
                                               "cache_creation_input_tokens": 0, "output_tokens": 1}, **kw))


class _FakeServerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = FC.FakeClaude()

    @classmethod
    def tearDownClass(cls):
        cls.fake.close()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.sleeps = []
        patches = [mock.patch.object(PV.ClaudeAdapter, "regions", self.fake.regions()),
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
    def test_native_messages_request(self):
        """Messages API：顶层 system、messages 只有 user / assistant、max_tokens 必填；Authentication 页：Authorization: Bearer +
        anthropic-version: 2023-06-01；不发 temperature / top_p / top_k（5.5 代模型非默认值 400）；不发 output_config.format；流式。"""
        out, seen, log = self.chat(ok_stream(), sp=spec(thinking="high"))
        self.assertEqual(out, ({"a": 1}, '{"a": 1}', None))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/messages"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["anthropic-version"], "2023-06-01")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        self.assertNotIn("x-api-key", r["headers"])
        b = r["body"]
        self.assertEqual(list(b), ["model", "max_tokens", "system", "messages", "thinking", "output_config", "stream"])
        self.assertEqual(b["model"], "claude-opus-5-5")
        self.assertEqual(b["system"], SYSTEM)
        self.assertEqual(b["messages"], [MSGS[1]])
        self.assertEqual((b["thinking"], b["output_config"], b["stream"]), ({"type": "adaptive"}, {"effort": "high"}, True))
        self.assertEqual(b["max_tokens"], 12000 + config.THINKING_EXTRA_TOKENS)
        for banned in ("temperature", "top_p", "top_k", "response_format", "reasoning_effort"):
            self.assertNotIn(banned, b)
        self.assertNotIn("format", b["output_config"])

    def test_thinking_per_model_and_role(self):
        """Effort / Errors 页：Opus 5.5、Fable 5.1 思考关不掉（disabled 400）-> 网页不给 off，其余角色用最低一档 low；
        Sonnet 5.5 关思考是 between_tools，Haiku 5.5 是 disabled，两种都只在 effort ≤ high 时接受 -> 写模型默认档。"""
        cases = [  # (模型, 网页档位, arm, 期望的 thinking, 期望的 effort, 有没有思考余量)
            ("claude-opus-5-5", "low", "plan", {"type": "adaptive"}, "low", True),
            ("claude-opus-5-5", "high", "judge:r2:repair", {"type": "adaptive"}, "high", True),
            ("claude-opus-5-5", "high", "extract:d1", {"type": "adaptive"}, "low", True),
            ("claude-fable-5-1", "medium", "judge:r1", {"type": "adaptive"}, "medium", True),
            ("claude-fable-5-1", "medium", "final", {"type": "adaptive"}, "low", True),
            ("claude-sonnet-5-5", "off", "judge:r1", {"type": "between_tools"}, "high", False),
            ("claude-sonnet-5-5", "medium", "plan", {"type": "adaptive"}, "medium", True),
            ("claude-sonnet-5-5", "medium", "audit", {"type": "between_tools"}, "high", False),
            ("claude-haiku-5-5", "off", "plan", {"type": "disabled"}, "medium", False),
            ("claude-haiku-5-5", "high", "judge:r1", {"type": "adaptive"}, "high", True),
            ("claude-haiku-5-5", "high", "value_check", {"type": "disabled"}, "medium", False),
        ]
        for model, level, arm, thinking, effort, headroom in cases:
            with self.subTest(model=model, level=level, arm=arm):
                out, seen, log = self.chat(ok_stream(), sp=spec(model, level), arm=arm, max_tokens=4000)
                b = seen[0]["body"]
                self.assertEqual((b["thinking"], b["output_config"]), (thinking, {"effort": effort}))
                self.assertEqual(b["max_tokens"], 4000 + (config.THINKING_EXTRA_TOKENS if headroom else 0))
                self.assertEqual(log[0].get("thinking"), effort if headroom else None)
        for model in ("claude-opus-5-5", "claude-fable-5-1"):
            with self.subTest(model=model):
                self.assertEqual(PV.thinking_levels(model), ("low", "medium", "high"))
                with self.assertRaises(PV.SpecError):
                    spec(model, "off")
        for model in ("claude-haiku-5-5", "claude-sonnet-5-5"):
            self.assertEqual(PV.thinking_levels(model), ("off", "low", "medium", "high"))

    def test_headroom_is_capped_at_128k(self):
        _, seen, _ = self.chat(ok_stream(), sp=spec(thinking="high"), max_tokens=120_000)
        self.assertEqual(seen[0]["body"]["max_tokens"], 128_000)

    def test_retry_after_an_empty_reply_drops_the_empty_assistant_turn(self):
        """AgentLLM.ask 带错误重问时把上次的回复放进 assistant 消息；回复为空（比如拒答）时这条不发（TextBlockParam 至少 1 个字），
        两条 user 消息由 API 合并成一轮（Messages API：Consecutive user or assistant turns ... combined into a single turn）。"""
        msgs = MSGS + [{"role": "assistant", "content": ""}, {"role": "user", "content": "Reply again with one valid JSON object."}]
        _, seen, _ = self.chat(ok_stream(), msgs=msgs)
        self.assertEqual([m["role"] for m in seen[0]["body"]["messages"]], ["user", "user"])
        msgs[2]["content"] = '{"a": '
        _, seen, _ = self.chat(ok_stream(), msgs=msgs)
        self.assertEqual([m["role"] for m in seen[0]["body"]["messages"]], ["user", "assistant", "user"])
        self.assertEqual(seen[0]["body"]["messages"][-1]["role"], "user")   # 不是 prefill（5.5 代模型 prefill 400）

    def test_system_message_in_the_middle_is_refused(self):
        with self.assertRaises(ValueError):
            PV.CLAUDE.chat_request("claude-opus-5-5", KEY, MSGS + [{"role": "system", "content": "x"}], max_tokens=10,
                                   effort="low")


class TestChatReply(_FakeServerCase):
    def test_only_text_blocks_are_parsed_and_usage_is_metered(self):
        """Streaming 页：message_start 带输入用量，message_delta 的 usage 是累计值；思考块（display omitted 时是空字符串）不解析。"""
        usage = {"input_tokens": 1000, "cache_read_input_tokens": 2000, "cache_creation_input_tokens": 400, "output_tokens": 900,
                 "output_tokens_details": {"thinking_tokens": 600}}
        ev = FC.sse_message([("thinking", "A summary {not json"), ("text", '{"a": '), ("text", "1}")], usage=usage,
                            start_usage={"input_tokens": 1000, "output_tokens": 1})   # 有文字的思考块（display summarized）也不解析
        with mock.patch.object(config, "is_peak", lambda t: True):
            out, seen, log = self.chat(("sse", ev), sp=spec("claude-sonnet-5-5", "high"))
        self.assertEqual(out[0], {"a": 1})
        rec = log[0]
        p = config.PRICES["claude-sonnet-5-5"]
        want = (1000 * 2.00 + 2000 * 0.10 + 400 * 2.50 + 900 * 10.00) / 1e6
        self.assertAlmostEqual(rec["usd"], round(want, 6))
        self.assertEqual(p["cache_write_5m"], 2.50)
        self.assertEqual((rec["finish_reason"], rec["prompt_tokens"], rec["input_tokens"], rec["cache_read_input_tokens"],
                          rec["cache_creation_input_tokens"], rec["completion_tokens"], rec["reasoning_tokens"]),
                         ("end_turn", 3400, 1000, 2000, 400, 900, 600))
        self.assertTrue(rec["ok"])

    def test_stop_reasons(self):
        """Messages API stop_reason：max_tokens / model_context_window_exceeded = 没写完（先报截断，不解析 JSON）；refusal = 拒答
        （HTTP 200，stop_details.category）；pause_turn = 暂停。end_turn / stop_sequence 照常解析。"""
        cases = [("max_tokens", "truncated", "reply was truncated (stop_reason=max_tokens)"),
                 ("model_context_window_exceeded", "truncated", "reply was truncated (stop_reason=model_context_window_exceeded)"),
                 ("pause_turn", "paused", "reply was paused before it finished (stop_reason=pause_turn)")]
        for stop, code, msg in cases:
            with self.subTest(stop=stop):
                out, seen, log = self.chat(("sse", FC.sse_message([("text", '{"a": ')], stop_reason=stop)))
                self.assertEqual(out, (None, '{"a": ', msg))
                self.assertEqual((log[0]["error"], log[0]["finish_reason"], len(seen)), (code, stop, 1))
        ev = FC.sse_message([], stop_reason="refusal", stop_details={"type": "refusal", "category": "cyber",
                                                                       "explanation": "declined"})
        out, seen, log = self.chat(("sse", ev))
        self.assertEqual(out, (None, "", "the model declined to answer (stop_reason=refusal, category=cyber)"))
        self.assertEqual((log[0]["error"], log[0]["stop_category"]), ("refusal", "cyber"))
        out, _, _ = self.chat(("sse", FC.sse_message([("text", '{"b": 2}')], stop_reason="stop_sequence")))
        self.assertEqual(out[0], {"b": 2})

    def test_json_is_not_repaired(self):
        """用户决定 4：不做 JSON 修补。代码块包着的 JSON 照样按不合法报。"""
        out, _, log = self.chat(ok_stream('```json\n{"a": 1}\n```'))
        self.assertEqual((out[0], out[2]), (None, "reply is not valid JSON"))
        self.assertEqual(log[0]["error"], "invalid_json")

    def test_ask_retries_once_after_a_refusal(self):
        ev = FC.sse_message([], stop_reason="refusal", stop_details={"type": "refusal", "category": None})
        self.fake.reset(("sse", ev), ok_stream())
        b = P.Budget.for_model("claude-opus-5-5", usd=2.0)
        a = P.AgentLLM(self.tmp / "c.jsonl", b, spec=spec())
        self.assertEqual(a.ask("s", "u", role="plan", qid="t", max_tokens=1000), ({"a": 1}, None))
        second = self.fake.seen[1]["body"]["messages"]
        self.assertEqual([m["role"] for m in second], ["user", "user"])   # 空的 assistant 回复不发
        self.assertIn("declined to answer", second[-1]["content"])
        self.assertGreater(b.usd, 0)

    def test_overloaded_and_server_errors_are_retried(self):
        """Errors 页：529 overloaded_error、500 api_error 退避重试；流里的 error 事件（overloaded_error）对应非流式的 529。"""
        out, seen, log = self.chat(("json", 529, FC.error_body("overloaded_error", "Overloaded")), ok_stream())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual([x["http"] for x in log], [200])
        mid = [FC.sse_message([("text", "x")])[0], ("error", {"type": "error", "error": {"type": "overloaded_error",
                                                                                         "message": "Overloaded"}})]
        out, seen, log = self.chat(("sse", mid), ok_stream())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual((log[0]["error"], log[0]["stream_error"], log[0]["will_retry"]), ("bad_response_body", "overloaded_error", True))
        cut = FC.sse_message([("text", '{"a": 1}')])[:-2]   # 连接在 message_stop 之前断了
        out, seen, log = self.chat(("sse", cut), ok_stream())
        self.assertEqual((out[0], log[0]["stream_error"]), ({"a": 1}, "incomplete_stream"))
        out, seen, log = self.chat(*[("json", 529, FC.error_body("overloaded_error", "Overloaded"))] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual(len(seen), 3)
        self.assertIn("http_529 (overloaded_error: Overloaded)", str(out))

    def test_rate_limit_waits_for_retry_after(self):
        """Rate limits 页：429 带 retry-after 时等那么多秒（这里最多 60 秒）再重试。"""
        out, seen, _ = self.chat(("json", 429, FC.error_body("rate_limit_error", "Too many"), {"retry-after": "17"}), ok_stream())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertIn(17.0, self.sleeps)
        self.assertEqual(llm.retry_wait(2, "500"), 60)
        self.assertEqual(llm.retry_wait(2, "soon"), 2)
        self.assertEqual(llm.retry_wait(4, None), 4)

    def test_balance_and_spend_limits_stop_without_retrying(self):
        """Errors / Rate limits / API credits 页的四种「钱不够」：402 billing_error；400 credit balance too low；400 自设的
        spend limit；429 enforced_spend_limit_reached（没有 retry-after，重试没用）。都不重试，抛 BalanceExhausted。"""
        cases = [
            (402, FC.error_body("billing_error", "There is an issue with your billing."), "HTTP 402 billing_error"),
            (400, FC.error_body("invalid_request_error", "Your credit balance is too low to access the Anthropic API. "
                                                         "Please go to Plans & Billing to upgrade or purchase credits."),
             "HTTP 400 credit balance too low"),
            (400, FC.error_body("invalid_request_error", "You have reached your specified API usage limits. You will "
                                                         "regain access on 2026-11-01 at 00:00 UTC."), "HTTP 400 spend limit"),
            (400, FC.error_body("invalid_request_error", "You have reached your specified workspace API usage limits."),
             "HTTP 400 spend limit"),
            (429, FC.error_body("rate_limit_error", "You have reached your API usage limits: ...",
                                details={"error_code": "enforced_spend_limit_reached"}), "enforced_spend_limit_reached"),
        ]
        for status, body, want in cases:
            with self.subTest(want=want):
                out, seen, log = self.chat(("json", status, body))
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertIsInstance(out, llm.TransportError)
                self.assertEqual(len(seen), 1)
                self.assertIn(want, str(out))
                self.assertIn("Claude Console", str(out))
                self.assertEqual(log[0]["error"], f"http_{status}")
                self.assertNoKeyIn(str(out), log)

    def test_other_errors_are_reported_as_they_are(self):
        """普通 400（参数不对、身份绑定的 key 没带 workspace id 等）不重试、不当成余额问题；服务端的 error.type 和 message 前 200 字
        记进日志和异常文字。401 / 403 = key 被拒（不读 body）。"""
        msg = ("anthropic-workspace-id is required when authenticating with an identity-linked API key; "
               "send the id of the workspace this request acts in.")
        out, seen, log = self.chat(("json", 400, FC.error_body("invalid_request_error", msg)))
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 1)
        self.assertEqual((log[0]["error"], log[0]["server_error_type"], log[0]["server_error"]),
                         ("http_400", "invalid_request_error", msg[:200]))
        self.assertIn("anthropic-workspace-id is required", str(out))
        out, seen, log = self.chat(("json", 429, FC.error_body("rate_limit_error", "rate limited")),
                                   ("json", 429, FC.error_body("rate_limit_error", "rate limited")),
                                   ("json", 429, FC.error_body("rate_limit_error", "rate limited")))
        self.assertNotIsInstance(out, llm.BalanceExhausted)   # 普通限流：重试 3 次后报传输错误
        self.assertEqual(len(seen), 3)
        for status, body in ((401, FC.REAL_401_FAKE_KEY), (403, FC.error_body("permission_error", "no"))):
            with self.subTest(status=status):
                out, seen, log = self.chat(("json", status, body))
                self.assertIsInstance(out, llm.KeyRejected)
                self.assertEqual(str(out), f"Claude rejected the API key (HTTP {status})")
                self.assertNotIn("server_error", log[0])

    def test_redirects_are_not_followed(self):
        out, seen, _ = self.chat(("redirect", 307, self.fake.url("/elsewhere")))
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual([r["path"] for r in seen], ["/v1/messages"])


class TestClaudeCost(unittest.TestCase):
    """Pricing 页（2026-10-21）：Opus 5.5 $4 / $20、Sonnet 5.5 $2 / $10、Haiku 5.5 $0.10 / $0.50（prompt > 100K：$0.50 / $2.50）、
    Fable 5.1 $10 / $50；cache 写入 5 分钟 1.25 倍、1 小时 2 倍；cache 读 Opus / Sonnet 5.5 0.05 倍、Fable 5.1 0.025 倍、Haiku 0.1 倍。"""

    def test_prices_match_the_pricing_page(self):
        want = {"claude-opus-5-5": (4, 5, 8, 0.20, 20), "claude-sonnet-5-5": (2, 2.5, 4, 0.10, 10),
                "claude-haiku-5-5": (0.10, 0.125, 0.20, 0.01, 0.50), "claude-fable-5-1": (10, 12.5, 20, 0.25, 50)}
        for m, (base, w5, w1, hit, out) in want.items():
            with self.subTest(model=m):
                p = config.price(m)
                self.assertEqual((p["peak"], p["offpeak"]), ((hit, base, out), (hit, base, out)))
                self.assertEqual((p["cache_write_5m"], p["cache_write_1h"]), (w5, w1))
                self.assertEqual((p["provider"], p["source"]), ("claude", config.CLAUDE_PRICING))

    def test_cache_tiers_long_context_and_geo(self):
        u = {"input_tokens": 10_000, "cache_read_input_tokens": 20_000, "cache_creation_input_tokens": 3_000,
             "cache_creation": {"ephemeral_5m_input_tokens": 1_000, "ephemeral_1h_input_tokens": 2_000}, "output_tokens": 5_000}
        self.assertAlmostEqual(PV.claude_usage_cost(u, "claude-opus-5-5"),
                               (10_000 * 4 + 20_000 * 0.20 + 1_000 * 5 + 2_000 * 8 + 5_000 * 20) / 1e6)
        no_split = {k: v for k, v in u.items() if k != "cache_creation"}   # 没有分档：按 5 分钟（默认 TTL）
        self.assertAlmostEqual(PV.claude_usage_cost(no_split, "claude-opus-5-5"),
                               (10_000 * 4 + 20_000 * 0.20 + 3_000 * 5 + 5_000 * 20) / 1e6)
        small = {"input_tokens": 60_000, "cache_read_input_tokens": 40_000, "output_tokens": 1_000}   # 正好 100,000：不超
        self.assertAlmostEqual(PV.claude_usage_cost(small, "claude-haiku-5-5"), (60_000 * 0.10 + 40_000 * 0.01 + 1_000 * 0.5) / 1e6)
        big = {**small, "input_tokens": 60_001}   # 超过 100,000（cache 读也算）：整次按高价
        self.assertAlmostEqual(PV.claude_usage_cost(big, "claude-haiku-5-5"), (60_001 * 0.50 + 40_000 * 0.05 + 1_000 * 2.5) / 1e6)
        us = {**u, "inference_geo": "us"}
        self.assertAlmostEqual(PV.claude_usage_cost(us, "claude-opus-5-5"), 1.1 * PV.claude_usage_cost(u, "claude-opus-5-5"))
        self.assertAlmostEqual(PV.claude_usage_cost({**u, "inference_geo": "global"}, "claude-opus-5-5"),
                               PV.claude_usage_cost(u, "claude-opus-5-5"))

    def test_directions_scale_with_claude_prices(self):
        """没有缓存（不写 cache_control），DeepSeek 一个方向里命中缓存的那部分在 Claude 上按 base input 算。"""
        pr = P.Budget.DIRECTION_PROFILE

        def cost(m, hit_is_miss):
            hit, miss, out = config.price(m)["peak"]
            hit = miss if hit_is_miss else hit
            return (pr["hit"] * hit + pr["miss"] * miss + pr["out"] * out) / 1e6 + pr["searches"] * 0.01
        flash = cost("deepseek-flash", False)
        got = {}
        for m in ("claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1"):
            with self.subTest(model=m):
                got[m] = P.Budget.typical_direction_usd(m)
                self.assertAlmostEqual(got[m], 0.06 * cost(m, True) / flash)
        self.assertLess(got["claude-haiku-5-5"], got["claude-sonnet-5-5"])
        self.assertLess(got["claude-sonnet-5-5"], got["claude-opus-5-5"])
        self.assertLess(got["claude-opus-5-5"], got["claude-fable-5-1"])
        dirs = {m: P.Budget.for_model(m, usd=2.0).directions for m in got}
        self.assertEqual(dirs, {m: max(1, min(16, 10, int(1.2 / got[m]))) for m in got})
        self.assertEqual(P.Budget().directions, 10)   # DeepSeek 默认路径不变
        self.assertEqual(P.Budget.typical_direction_usd("deepseek-flash"), 0.06)

    def test_reservations(self):
        """预扣：Haiku 5.5 的 prompt 估计超过 100,000 token 时按高价；搜索也开思考的模型（Opus 5.5）按带余量的 max_tokens 预扣。"""
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "claude-haiku-5-5"), (50_000 * 0.10 + 1000 * 0.5) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(400_000, 1000, "claude-haiku-5-5"), (200_000 * 0.50 + 1000 * 2.5) / 1e6)
        ctx = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("claude-opus-5-5", "low"))
        self.assertEqual(ctx.budget.search_tokens, config.MAX_TOKENS["search"] + config.THINKING_EXTRA_TOKENS)
        self.assertAlmostEqual(ctx.budget.search_reserve(),
                               (30_000 * 4 + ctx.budget.search_tokens * 20) / 1e6 + 8 * 0.01)
        ctx2 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("claude-haiku-5-5", "high"))
        self.assertEqual(ctx2.budget.search_tokens, config.MAX_TOKENS["search"])   # 搜索角色关思考


SEARCH_RESULT = {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_1", "content": [
    {"type": "web_search_result", "url": "https://stats.example.org/w", "title": "Widgets 2025 | Stats Office",
     "encrypted_content": "Eqgf...", "page_age": "April 30, 2025"},
    {"type": "web_search_result", "url": "https://b.example.org/x", "title": "B", "encrypted_content": "Eqx..."}]}


def search_reply(stop="end_turn", text="Best: https://stats.example.org/w and https://c.example.org/y.", n_req=1, extra=()):
    content = [{"type": "text", "text": "I'll search."},
               {"type": "server_tool_use", "id": "srvtoolu_1", "name": "web_search", "input": {"query": "widgets June 2025"}},
               SEARCH_RESULT, *extra]
    if text is not None:
        content.append({"type": "text", "text": text, "citations": [{"type": "web_search_result_location",
                                                                     "url": "https://stats.example.org/w", "title": "W",
                                                                     "encrypted_index": "Eo8", "cited_text": "..."}]})
    return {"id": "msg_s", "type": "message", "role": "assistant", "model": "claude-opus-5-5", "content": content,
            "stop_reason": stop, "usage": {"input_tokens": 6039, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
                                           "output_tokens": 931, "server_tool_use": {"web_search_requests": n_req}}}


class TestClaudeSearch(_FakeServerCase):
    def search(self, *script, sp=None):
        self.fake.reset(*script)
        logged = []
        s = S.Searcher(log=logged.append, spec=sp or spec())
        try:
            out = s.search("Find official widget statistics.", role="search:d1", qid="t", max_uses=3, cap=4)
        except Exception as e:  # noqa: BLE001
            out = e
        return out, list(self.fake.seen), logged

    def test_request_uses_the_native_web_search_tool(self):
        """Web search tool 页：tools 里声明 {"type": "web_search_20250305", "name": "web_search", "max_uses": N}，不需要 beta 头；
        非流式。思考按模型：Opus 5.5 关不掉 -> adaptive + low（并给思考余量）；Haiku 5.5 搜索角色关思考。"""
        out, seen, log = self.search(("json", 200, search_reply()))
        b, h = seen[0]["body"], seen[0]["headers"]
        self.assertEqual(h["authorization"], f"Bearer {KEY}")
        self.assertNotIn("anthropic-beta", h)
        self.assertEqual(b["tools"], [{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}])
        self.assertEqual(b["messages"], [{"role": "user", "content": "Find official widget statistics."}])
        self.assertEqual((b["thinking"], b["output_config"]), ({"type": "adaptive"}, {"effort": "low"}))
        self.assertEqual(b["max_tokens"], config.MAX_TOKENS["search"] + config.THINKING_EXTRA_TOKENS)
        self.assertNotIn("stream", b)
        self.assertNotIn("temperature", b)
        _, seen, _ = self.search(("json", 200, search_reply()), sp=spec("claude-haiku-5-5", "high"))
        b = seen[0]["body"]
        self.assertEqual((b["thinking"], b["max_tokens"]), ({"type": "disabled"}, config.MAX_TOKENS["search"]))

    def test_urls_queries_titles_and_fee(self):
        """结果只往外给 URL 和查询词（标题解析出来但不外传：分析角色只拿得到 URL）；搜索费按 usage.server_tool_use.web_search_requests
        每次 $0.01（$10 / 1,000）。"""
        out, seen, log = self.search(("json", 200, search_reply(n_req=2)))
        self.assertEqual(out["urls"], ["https://stats.example.org/w", "https://c.example.org/y", "https://b.example.org/x"])
        self.assertEqual(out["queries"], ["widgets June 2025"])
        self.assertEqual((out["web_search_requests"], out["usd_search_fee_assumed"]), (2, 0.02))
        self.assertAlmostEqual(out["usd"], (6039 * 4 + 931 * 20) / 1e6)
        self.assertNotIn("Stats Office", json.dumps(out))
        parsed = PV.CLAUDE.search_unpack(search_reply())
        self.assertEqual(parsed["result_titles"], ["Widgets 2025 | Stats Office", "B"])
        rec = log[0]
        self.assertEqual((rec["kind"], rec["ok"], rec["stop"], rec["web_search_requests"], rec["usd_search_fee_assumed"]),
                         ("search", True, "end_turn", 2, 0.02))
        self.assertEqual(rec["cache_creation_input_tokens"], 0)

    def test_search_error_object_is_counted(self):
        """出错时 HTTP 仍是 200，web_search_tool_result 的 content 是一个错误对象（不是列表）；出错的搜索不计费。"""
        err = {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_2",
               "content": {"type": "web_search_tool_result_error", "error_code": "max_uses_exceeded"}}
        out, _, log = self.search(("json", 200, search_reply(extra=(err,))))
        self.assertEqual(log[0]["n_search_errors"], 1)
        self.assertEqual(len(out["urls"]), 3)

    def test_pause_turn_is_continued_with_the_content_as_is(self):
        """Server tools 页：pause_turn 时把这次的 assistant content 原样接在 messages 后面、工具不变，再发一次；可以再暂停，
        要限制续的次数（这里最多 2 次）。每次请求一行日志，结果合并。"""
        first = search_reply(stop="pause_turn", text=None)
        second = {**search_reply(n_req=1), "content": [{"type": "text", "text": "Final: https://d.example.org/z"}]}
        out, seen, log = self.search(("json", 200, first), ("json", 200, second))
        self.assertEqual(len(seen), 2)
        b0, b1 = seen[0]["body"], seen[1]["body"]
        self.assertEqual(b1["tools"], b0["tools"])
        self.assertEqual(b1["messages"], b0["messages"] + [{"role": "assistant", "content": first["content"]}])
        self.assertEqual({k: v for k, v in b1.items() if k != "messages"}, {k: v for k, v in b0.items() if k != "messages"})
        self.assertEqual(out["urls"][:1], ["https://d.example.org/z"])
        self.assertEqual((out["web_search_requests"], out["continuations"]), (2, 1))
        self.assertEqual([r.get("continuation") for r in log], [None, 1])
        self.assertEqual([r["stop"] for r in log], ["pause_turn", "end_turn"])
        out, seen, log = self.search(*[("json", 200, first)] * 4)
        self.assertEqual(len(seen), 3)   # 1 次 + 最多续 2 次
        self.assertEqual(out["continuations"], 2)
        out, seen, log = self.search(("json", 200, first), ("json", 400, FC.error_body("invalid_request_error", "bad")))
        self.assertEqual(out["urls"], ["https://stats.example.org/w", "https://b.example.org/x"])   # 续失败：用已经拿到的结果
        self.assertEqual(out["error"], "continuation 1: http_400 (invalid_request_error: bad)")

    def test_web_search_disabled_and_balance(self):
        """Web search tool 页：组织管理员关了 web search 时请求 400 invalid_request_error（不是结果里的错误码）-> 照原样报，不抛；
        余额不足（402）抛 BalanceExhausted（run_direction 据此停下整次运行）。"""
        out, seen, log = self.search(("json", 400, FC.error_body("invalid_request_error", "web search is not enabled")))
        self.assertEqual((out["urls"], out["error"]), ([], "http_400 (invalid_request_error: web search is not enabled)"))
        self.assertEqual(len(seen), 1)
        out, seen, log = self.search(("json", 402, FC.error_body("billing_error", "billing")))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 1)
        out, seen, _ = self.search(("json", 529, FC.error_body("overloaded_error", "Overloaded")), ("json", 200, search_reply()))
        self.assertEqual((len(seen), len(out["urls"])), (2, 3))


class TestKeyCheck(_FakeServerCase):
    def check(self, *script, sp=None):
        self.fake.reset(*script)
        out = llm.check_key(sp or spec())
        self.assertNoKeyIn(out)
        return out, list(self.fake.seen)

    def test_models_list(self):
        """List Models：GET /v1/models（limit 最多 1000），带 key 和 anthropic-version。所选模型在列表里 -> model_listed True。"""
        page = {"data": [{"id": "claude-opus-5-5", "type": "model"}, {"id": "claude-haiku-5-5", "type": "model"}],
                "has_more": False, "first_id": "claude-opus-5-5", "last_id": "claude-haiku-5-5"}
        out, seen = self.check(("json", 200, page))
        self.assertEqual((seen[0]["method"], seen[0]["path"]), ("GET", "/v1/models?limit=1000"))
        self.assertEqual(seen[0]["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(seen[0]["headers"]["anthropic-version"], "2023-06-01")
        self.assertIsNone(seen[0]["body"])
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"], out["status"]), (True, True, 2, 200))
        out, _ = self.check(("json", 200, page), sp=spec("claude-sonnet-5-5", "off"))
        self.assertEqual((out["ok"], out["model_listed"]), (True, False))
        self.assertIn("not in the models list", out["message"])
        out, _ = self.check(("json", 200, {**page, "has_more": True}), sp=spec("claude-sonnet-5-5", "off"))
        self.assertEqual((out["ok"], out["model_listed"]), (True, None))

    def test_rejected_keys_use_the_real_401_bodies(self):
        """2026-10-21 实测（没花钱）：不带 key / 假 key 调 GET /v1/models 都是 HTTP 401 authentication_error。"""
        for body in (FC.REAL_401_NO_KEY, FC.REAL_401_FAKE_KEY):
            with self.subTest(message=body["error"]["message"]):
                out, _ = self.check(("json", 401, body, {"x-should-retry": "false"}))
                self.assertEqual((out["ok"], out["error"], out["status"]), (False, "key_rejected", 401))
                self.assertEqual(out["message"], "Claude rejected the API key (HTTP 401)")

    def test_other_outcomes(self):
        out, _ = self.check(("json", 402, FC.error_body("billing_error", "b")))
        self.assertEqual(out["error"], "balance")
        out, _ = self.check(("json", 500, FC.error_body("api_error", "x")))
        self.assertEqual(out["error"], "http_500")
        out, _ = self.check(("raw", 200, b"<html>"))
        self.assertEqual(out["error"], "bad_response_body")
        out, _ = self.check(("redirect", 302, self.fake.url("/x")))
        self.assertEqual(out["error"], "redirect")
        with mock.patch.object(PV.ClaudeAdapter, "regions", {"global": {"models": "http://127.0.0.1:9/v1/models"}}):
            out = llm.check_key(spec())
        self.assertEqual(out["error"], "network")

    def test_deepseek_key_check(self):
        """DeepSeek List Models：GET /models，Bearer；示例回复的 data[].id 有 deepseek-flash、deepseek-v4-pro。"""
        self.fake.reset(("json", 200, {"object": "list", "data": [{"id": "deepseek-flash", "object": "model",
                                                                    "owned_by": "deepseek"}]}))
        with mock.patch.object(PV.DeepSeekAdapter, "regions", {"global": {"models": self.fake.url("/models")}}):
            out = llm.check_key(PV.ModelSpec("deepseek", "deepseek-flash", KEY))
        self.assertEqual((out["ok"], out["model_listed"]), (True, True))
        self.assertEqual(self.fake.seen[0]["headers"]["authorization"], f"Bearer {KEY}")


class TestModelSpecClaude(unittest.TestCase):
    def test_official_endpoints(self):
        """只有一个官方端点（没有分区）；不用 OpenAI 兼容层 /v1/chat/completions。"""
        self.assertEqual(PV.CLAUDE.regions, {"global": {"chat": "https://api.anthropic.com/v1/messages",
                                                        "search": "https://api.anthropic.com/v1/messages",
                                                        "models": "https://api.anthropic.com/v1/models"}})
        self.assertEqual(PV.CLAUDE.key_check_request("global", KEY)[0], "https://api.anthropic.com/v1/models?limit=1000")

    def test_choices_and_public_view(self):
        self.assertEqual(PV.PROVIDERS["claude"]["models"],
                         ("claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1"))
        self.assertEqual(PV.PROVIDERS["claude"]["default_model"], "claude-opus-5-5")
        sp = spec("claude-fable-5-1", "high", usd_cap=5)
        self.assertEqual(sp.public(), {"provider": "claude", "model": "claude-fable-5-1", "region": "global", "thinking": "high",
                                       "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high", "*": "low"},
                                       "usd_cap": 5.0, "byok": True})
        self.assertNotIn(KEY, repr(sp))
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("claude", "deepseek-flash", KEY)
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("deepseek", "claude-opus-5-5", KEY)
        with self.assertRaises(PV.SpecError):
            spec(region="cn")

    def test_sse_parser(self):
        raw = FC.encode_sse(FC.sse_message([("thinking", ""), ("text", "héllo 世界")], usage={"output_tokens": 7}))
        msg = PV.parse_sse_message(raw.replace(b"\n", b"\r\n"))
        self.assertEqual([b["type"] for b in msg["content"]], ["thinking", "text"])
        self.assertEqual(msg["content"][1]["text"], "héllo 世界")
        self.assertEqual(msg["content"][0]["signature"], "EqQBsig")
        self.assertEqual((msg["stop_reason"], msg["usage"]["output_tokens"]), ("end_turn", 7))
        tool = [("message_start", {"type": "message_start", "message": {"content": [], "usage": {"input_tokens": 5}}}),
                ("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {
                    "type": "server_tool_use", "id": "srvtoolu_1", "name": "web_search", "input": {}}}),
                ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                         "delta": {"type": "input_json_delta", "partial_json": "{\"query\": \"wid"}}),
                ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                         "delta": {"type": "input_json_delta", "partial_json": "gets\"}"}}),
                ("content_block_stop", {"type": "content_block_stop", "index": 0}),
                ("future_event", {"type": "future_event"}),
                ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn"},
                                   "usage": {"output_tokens": 3, "input_tokens": None}}),
                ("message_stop", {"type": "message_stop"})]
        msg = PV.parse_sse_message(FC.encode_sse(tool))
        self.assertEqual(msg["content"][0]["input"], {"query": "widgets"})
        self.assertEqual(msg["usage"], {"input_tokens": 5, "output_tokens": 3})
        for bad, kind in ((tool[1:], "malformed_stream"), (tool[:-1], "incomplete_stream"), (b"", "incomplete_stream")):
            with self.subTest(kind=kind):
                with self.assertRaises(PV.StreamError) as cm:
                    PV.parse_sse_message(bad if isinstance(bad, bytes) else FC.encode_sse(bad))
                self.assertEqual(cm.exception.error_type, kind)
                self.assertIsInstance(cm.exception, ValueError)   # json_call 当作 bad_response_body 重试


class TestRunWithClaudeSpec(_FakeServerCase):
    """prepare_run(spec=Claude) -> 图 -> save_run，全部对着假服务：规划一步收到 402 就干净停下；state.json 记 provider，不记 key；
    结果目录里没有 key；写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop(self):
        from triangulate.agent import run as R
        sp = spec("claude-sonnet-5-5", "medium", usd_cap=1.5)
        q = {"id": "ask_claude1", "question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20"}
        self.fake.reset(*[("json", 402, FC.error_body("billing_error", "billing"))] * 3)
        with mock.patch.object(R, "RES", self.tmp):
            h = R.prepare_run(q, "web_t", spec=sp)
            out = h["g"].invoke(R.initial_input(q), h["cfg"])
            self.assertFalse(out.get("__interrupt__"))
            st = R.save_run(h, [])
        self.assertEqual(len(self.fake.seen), 1)
        b = self.fake.seen[0]["body"]
        self.assertEqual((b["model"], b["thinking"], b["output_config"]), ("claude-sonnet-5-5", {"type": "adaptive"},
                                                                          {"effort": "medium"}))
        self.assertTrue(st["aborted"].startswith("insufficient balance: Claude HTTP 402 billing_error"))
        self.assertEqual((st["provider"], st["model"]), ("claude", "claude-sonnet-5-5"))
        self.assertEqual(st["settings"]["run_spec"]["thinking_by_role"], {"plan": "medium", "judge": "medium", "repair": "medium"})
        files = list((self.tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            self.assertNotIn(KEY, f.read_text(encoding="utf-8"), f.name)
        self.assertFalse(sp.has_key)


if __name__ == "__main__":
    unittest.main()
