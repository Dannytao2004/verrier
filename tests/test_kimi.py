"""v2.10d：Kimi adapter（Moonshot AI 开放平台：国际站 api.moonshot.ai / 国内站 api.moonshot.cn）。全部对着 127.0.0.1 上的
假服务（tests/fake_kimi.py）跑：真实走 urllib + urlopen_no_redirect，请求头、请求体、HTTPError 的 body 都是真的；不联网、
不需要真 key、不读 key 文件。

JSON 调用：OpenAI 兼容的流式 Chat Completions；搜索：一次 JSON 调用生成查询词 + 每个查询词 POST /v1/tools/search。
每一项对照的官方文档写在各个测试的说明里（链接见 PROVIDERS.md 第 11 节）。
"""
import http.client
import json
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from tests import fake_kimi as FK
from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import prompts as PR
from triangulate.agent import search as S

KEY = "sk-kimi-user-0123456789ABCDEFghij"
SYSTEM = "You are a careful analyst. Reply with one JSON object."
MSGS = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "Estimate widgets in June 2026. Reply {\"a\": 1}."}]
BRIEF = "Find official widget statistics for June 2026.\n\nAfter searching, reply with at most 4 URLs, most useful first."
FX = config.CNY_PER_USD
EXTRA = config.THINKING_EXTRA_TOKENS


def spec(model="kimi-k2.6", thinking="off", key=KEY, **kw):
    return PV.ModelSpec("kimi", model, key, thinking=thinking, **kw)


def ok(content='{"a": 1}', **kw):
    return ("raw", 200, FK.sse(content, **kw))


def queries_reply(*qs, **kw):
    return ok(json.dumps({"queries": list(qs)}), **kw)


def results(*urls):
    return ("json", 200, FK.search_results(*urls))


class _FakeServerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = FK.FakeKimi()

    @classmethod
    def tearDownClass(cls):
        cls.fake.close()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.sleeps = []
        patches = [mock.patch.object(PV.KimiAdapter, "regions", self.fake.regions()),
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

    def search(self, *script, sp=None, max_uses=3, cap=4):
        """一次 Searcher.search；返回 (结果或异常, 收到的请求, 日志行)。"""
        self.fake.reset(*script)
        logged = []
        s = S.Searcher(log=logged.append, spec=sp or spec())
        try:
            out = s.search(BRIEF, role="search:d1", qid="t", max_uses=max_uses, cap=cap)
        except Exception as e:  # noqa: BLE001
            out = e
        return out, list(self.fake.seen), logged

    def assertNoKeyIn(self, *texts):
        for t in texts:
            self.assertNotIn(KEY, t if isinstance(t, str) else json.dumps(t, default=str))


class TestChatRequest(_FakeServerCase):
    def test_chat_completions_request(self):
        """Chat API：POST /v1/chat/completions，Authorization: Bearer；response_format json_object；max_completion_tokens
        （max_tokens 已 Deprecated）；stream: true + stream_options.include_usage（错误码页：非流式 900 秒没回就 504，要用流式）。
        Model Parameter Reference：temperature / top_p / n / presence_penalty / frequency_penalty 是固定值，传了报错，不发。
        K2.6 关思考：thinking {"type": "disabled"}（默认是 enabled，要关必须写）；不支持 reasoning_effort。"""
        out, seen, log = self.chat(ok())
        self.assertEqual(out, ({"a": 1}, '{"a": 1}', None))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/chat/completions"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        for h in ("x-api-key", "anthropic-version"):
            self.assertNotIn(h, r["headers"])
        b = r["body"]
        self.assertEqual(list(b), ["model", "messages", "thinking", "response_format", "max_completion_tokens", "stream",
                                   "stream_options"])
        self.assertEqual((b["model"], b["messages"]), ("kimi-k2.6", MSGS))   # Kimi 收 system 角色，原样
        self.assertEqual((b["thinking"], b["response_format"], b["max_completion_tokens"], b["stream"], b["stream_options"]),
                         ({"type": "disabled"}, {"type": "json_object"}, 12000, True, {"include_usage": True}))
        for banned in ("temperature", "top_p", "n", "presence_penalty", "frequency_penalty", "max_tokens", "reasoning_effort",
                       "tools", "tool_choice", "prompt_cache_options", "store"):
            self.assertNotIn(banned, b)
        self.assertNotIn("thinking", log[0])
        self.assertEqual((log[0]["model"], log[0]["ok"]), ("kimi-k2.6", True))

    def test_thinking_per_model_and_role(self):
        """K3（Reasoning Effort 页）：永远在想，顶层 reasoning_effort 只有 low / high / max（省略时 max），不发 thinking；网页档位
        low -> low、medium -> high、high -> max（调研的映射），plan / judge / repair 以外用 low。K2.6：thinking enabled / disabled，
        没有深度。思考 token 和正文共用 max_completion_tokens（Thinking 指南）：开思考的调用 +24,000。"""
        dis, en = {"thinking": {"type": "disabled"}}, {"thinking": {"type": "enabled"}}
        cases = [  # (模型, 网页档位, arm, 期望的思考字段, 有没有思考余量)
            ("kimi-k2.6", "off", "plan", dis, False),
            ("kimi-k2.6", "low", "judge:r1", en, True),
            ("kimi-k2.6", "medium", "judge:r2:repair", en, True),
            ("kimi-k2.6", "high", "plan", en, True),
            ("kimi-k2.6", "high", "extract:d1", dis, False),
            ("kimi-k3", "low", "plan", {"reasoning_effort": "low"}, True),
            ("kimi-k3", "medium", "judge:r1", {"reasoning_effort": "high"}, True),
            ("kimi-k3", "high", "judge:r2:repair", {"reasoning_effort": "max"}, True),
            ("kimi-k3", "high", "audit", {"reasoning_effort": "low"}, True),
            ("kimi-k3", "medium", "final", {"reasoning_effort": "low"}, True),
        ]
        for model, level, arm, want, extra in cases:
            with self.subTest(model=model, level=level, arm=arm):
                out, seen, log = self.chat(ok(), sp=spec(model, level), arm=arm, max_tokens=4000)
                b = seen[0]["body"]
                key = next(iter(want))
                self.assertEqual(b[key], want[key])
                self.assertNotIn("reasoning_effort" if key == "thinking" else "thinking", b)
                self.assertEqual(b["max_completion_tokens"], 4000 + (EXTRA if extra else 0))
                self.assertEqual(log[0].get("thinking"), (b.get("reasoning_effort") or "enabled") if extra else None)
        self.assertEqual(PV.thinking_levels("kimi-k3"), ("low", "medium", "high"))
        self.assertEqual(PV.thinking_levels("kimi-k2.6"), ("off", "low", "medium", "high"))
        self.assertFalse(PV.MODELS["kimi-k2.6"]["thinking_depth"])   # 网页把 low / medium / high 合并成「开」
        with self.assertRaises(PV.SpecError):
            spec("kimi-k3", "off")
        with self.assertRaises(ValueError):   # 防御：K3 不会不带 reasoning_effort
            PV.KIMI.chat_request("kimi-k3", KEY, MSGS, max_tokens=10, effort=None)
        self.assertEqual(spec("kimi-k3", "high").thinking_by_role(), {"plan": "max", "judge": "max", "repair": "max", "*": "low"})
        self.assertEqual(spec("kimi-k2.6", "medium").thinking_by_role(), {"plan": "enabled", "judge": "enabled", "repair": "enabled"})

    def test_headroom_is_capped_at_the_models_max_output(self):
        _, seen, _ = self.chat(ok(), sp=spec("kimi-k2.6", "high"), arm="plan", max_tokens=250_000)
        self.assertEqual(seen[0]["body"]["max_completion_tokens"], 262_144)
        _, seen, _ = self.chat(ok(), sp=spec("kimi-k3", "low"), max_tokens=1_040_000)
        self.assertEqual(seen[0]["body"]["max_completion_tokens"], 1_048_576)

    def test_region_and_retry_turns(self):
        """国内站的请求发到国内站的地址（假服务上是 /cn/...）。Chat API：content must not be empty -> AgentLLM.ask 重问时
        内容为空的 assistant 消息不发；有内容的照原样。"""
        _, seen, _ = self.chat(ok(), sp=spec(region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/v1/chat/completions")
        empty = MSGS + [{"role": "assistant", "content": ""}, {"role": "user", "content": "Reply again with one valid JSON object."}]
        _, seen, _ = self.chat(ok(), msgs=empty)
        self.assertEqual([m["role"] for m in seen[0]["body"]["messages"]], ["system", "user", "user"])
        full = MSGS + [{"role": "assistant", "content": '{"a": '}, {"role": "user", "content": "again"}]
        _, seen, _ = self.chat(ok(), msgs=full)
        self.assertEqual(seen[0]["body"]["messages"], full)


class TestChatReply(_FakeServerCase):
    def test_stream_is_reassembled_without_the_reasoning(self):
        """Chat API 流式格式：每个事件一行 data: <chunk>，content 在 delta 里累加，[DONE] 结束；Thinking 指南：reasoning_content
        总在 content 之前，只解析 content。思考内容不进返回值、不进日志。CRLF 和 : 注释行（keep-alive）都认。"""
        content = '{"answer": "widgets", "n": 3, "notes": "x"}'
        out, _, log = self.chat(ok(content, pieces=5, crlf=True, reasoning="SECRET-REASONING about widgets"))
        self.assertEqual(out, ({"answer": "widgets", "n": 3, "notes": "x"}, content, None))
        self.assertNotIn("SECRET-REASONING", json.dumps(log))
        parsed = PV.parse_chat_sse(FK.sse(content, reasoning="SECRET-REASONING"))
        self.assertEqual(parsed["choices"][0]["message"], {"role": "assistant", "content": content})
        self.assertNotIn("SECRET-REASONING", json.dumps(parsed))

    def test_usage_is_metered_with_cache_reads_and_writes(self):
        """Chat API usage：prompt_tokens 是全部输入，prompt_tokens_details 的 cached_tokens / cache_write_tokens 和未缓存的部分互斥。
        K3 价格（国际站）：miss $3、5 分钟写入 $3、命中 $0.30、输出 $15；K2.6：命中 $0.16、miss $0.95、输出 $4（K2 没有单列写入价，
        写入按 miss）。国内站：CNY 价按 2026-10-21 中间价 6.7192 折成 USD。"""
        u = FK.usage(prompt=12_000, completion=900, cached=4_000, write=7_000)
        cases = [(spec("kimi-k3", "low"), (1_000 * 3.00 + 4_000 * 0.30 + 7_000 * 3.00 + 900 * 15.00) / 1e6),
                 (spec("kimi-k2.6"), (8_000 * 0.95 + 4_000 * 0.16 + 900 * 4.00) / 1e6),
                 (spec("kimi-k2.6", region="cn"), (8_000 * 6.50 + 4_000 * 1.10 + 900 * 27.00) / 1e6 / FX),
                 (spec("kimi-k3", "low", region="cn"), (1_000 * 20 + 4_000 * 2 + 7_000 * 20 + 900 * 100) / 1e6 / FX)]
        for sp, want in cases:
            with self.subTest(model=sp.model, region=sp.region):
                _, _, log = self.chat(ok(use=u), sp=sp)
                rec = log[0]
                self.assertAlmostEqual(rec["usd"], round(want, 6))
                self.assertEqual((rec["finish_reason"], rec["prompt_tokens"], rec["cached_tokens"], rec["cache_write_tokens"],
                                  rec["completion_tokens"]), ("stop", 12_000, 4_000, 7_000, 900))
                self.assertNotIn("reasoning_tokens", rec)   # Chat API 的 usage 没有这个字段：没有就不记
                self.assertEqual(rec["model"], sp.model)    # 日志里是模型名；计价 id 只用来查价格
        # 没有 prompt_tokens_details 时用顶层 cached_tokens；有 completion_tokens_details.reasoning_tokens 时记下
        self.assertAlmostEqual(PV.kimi_usage_cost({"prompt_tokens": 1000, "cached_tokens": 400, "completion_tokens": 10}, "kimi-k2.6"),
                               (600 * 0.95 + 400 * 0.16 + 10 * 4) / 1e6)
        u2 = {**FK.usage(), "completion_tokens_details": {"reasoning_tokens": 120}}
        _, _, log = self.chat(ok(use=u2))
        self.assertEqual(log[0]["reasoning_tokens"], 120)

    def test_truncation_and_unexpected_finish_reasons(self):
        """finish_reason（Chat API 枚举：stop / length / tool_calls）：length = 思考 + 正文撞到 max_completion_tokens，报截断不解析；
        不带工具时出现 tool_calls、或流里没给 finish_reason：照原样报，不解析。"""
        out, seen, log = self.chat(ok('{"a": ', finish_reason="length"))
        self.assertEqual(out, (None, '{"a": ', "reply was truncated (finish_reason=length)"))
        self.assertEqual((log[0]["error"], log[0]["finish_reason"], len(seen)), ("truncated", "length", 1))
        for fr in (None, "tool_calls"):
            with self.subTest(finish_reason=fr):
                out, _, log = self.chat(ok(finish_reason=fr))
                self.assertEqual(out[2], f"reply ended with finish_reason={fr}")
                self.assertEqual(log[0]["error"], "unexpected_finish")

    def test_broken_streams_are_retried(self):
        """没收到 data: [DONE]（流被打断）或流里来了 error 对象：按形状不对（bad_response_body）重试，stream_error 记类型。"""
        out, seen, log = self.chat(ok(done=False), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual((log[0]["error"], log[0]["stream_error"], log[0]["will_retry"]), ("bad_response_body", "incomplete_stream", True))
        err = b'data: {"error": {"type": "engine_overloaded_error", "message": "overloaded"}}\n\n'
        out, seen, log = self.chat(("raw", 200, err), ok())
        self.assertEqual((out[0], log[0]["stream_error"]), ({"a": 1}, "engine_overloaded_error"))
        out, seen, log = self.chat(*[ok(done=False)] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual(len(seen), 3)

    def test_missing_usage_is_flagged_not_retried(self):
        """stream_options 文档：流被打断时可能收不到最后的 usage chunk。收到 [DONE] 却没有 usage：照常用回复（重试会重复计费），
        日志标 usage_missing。v2.10f：usd 按这次调用的预扣（最坏情况）记，不记 0（审查发现：预算会漏掉这次），usd_basis 写明。"""
        out, seen, log = self.chat(ok(include_usage=False))
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 1))
        sent = seen[0]["body"]
        want = P.Budget.llm_reserve(sum(len(m["content"]) for m in MSGS), sent["max_completion_tokens"], "kimi-k2.6")
        self.assertGreater(want, 0)
        self.assertEqual((log[0]["usage_missing"], log[0]["usd"], log[0]["usd_basis"]), (True, round(want, 6), "reserve (usage missing)"))
        self.assertNotIn("usd_basis", self.chat(ok())[2][0])   # 有 usage 的回复照旧按 usage 计价

    def test_json_is_not_repaired(self):
        """用户决定 4：不做 JSON 修补（不剥代码块）。"""
        out, _, log = self.chat(ok('```json\n{"a": 1}\n```'))
        self.assertEqual((out[0], out[2]), (None, "reply is not valid JSON"))
        self.assertEqual(log[0]["error"], "invalid_json")
        out, _, _ = self.chat(ok("[1, 2]"))
        self.assertEqual(out[2], "reply is not a JSON object")


class TestChatErrors(_FakeServerCase):
    def test_balance_stops_without_retrying(self):
        """Common Error Codes 页：429 exceeded_current_quota_error = 余额不足或账户停用 / token 额度不足（充值后再试），
        重试没用 -> BalanceExhausted，不重试。"""
        for msg in ("Account balance is insufficient or the account has been disabled", "Token quota is insufficient"):
            with self.subTest(message=msg):
                out, seen, log = self.chat(("json", 429, FK.error_body("exceeded_current_quota_error", msg), {"retry-after": "5"}))
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertIsInstance(out, llm.TransportError)
                self.assertEqual(len(seen), 1)
                self.assertIn("insufficient balance: Kimi HTTP 429 exceeded_current_quota_error", str(out))
                self.assertIn("platform.kimi.ai or platform.kimi.com", str(out))
                self.assertNotIn(msg, str(out))   # 不含服务端原文
                self.assertEqual(log[0]["error"], "http_429")
                self.assertEqual(self.sleeps, [])
                self.assertNoKeyIn(str(out), log)

    def test_overload_and_rate_limits_are_retried(self):
        """429 engine_overloaded_error（按 Retry-After 等、退避重试）和 rate_limit_reached_error（组织并发 / RPM / TPM 超限）、
        503 server_unavailable 是临时的：重试；3 次仍失败报传输错误，异常文字带 error.type 和 message。"""
        over = FK.error_body("engine_overloaded_error", "The engine is currently overloaded, please try again later")
        out, seen, _ = self.chat(("json", 429, over, {"retry-after": "7"}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertIn(7.0, self.sleeps)
        rl = FK.error_body("rate_limit_reached_error", "Organization-level RPM limit reached")
        out, seen, _ = self.chat(("json", 429, rl), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        down = FK.error_body("server_unavailable", "The service is temporarily unavailable")
        out, seen, log = self.chat(*[("json", 503, down)] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 3)
        self.assertIn("http_503 (server_unavailable: The service is temporarily unavailable)", str(out))

    def test_other_errors_are_reported_as_they_are(self):
        """400（参数不对、输入 + max_completion_tokens 超过上下文、内容审核 content_filter）、404（K3 没解锁 / 没权限）不重试、
        不当成余额问题；error.type 和 message 前 200 字进日志和异常文字。401 / 403 = key 被拒，不读 body。"""
        cases = [(400, "invalid_request_error", "prompt tokens + max_tokens exceeds the model specification"),
                 (400, "content_filter", "The request was rejected because it was considered high risk"),
                 (404, "resource_not_found_error", "Model not found, or this account does not have permission to access the model")]
        for status, etype, msg in cases:
            with self.subTest(etype=etype):
                out, seen, log = self.chat(("json", status, FK.error_body(etype, msg)))
                self.assertIsInstance(out, llm.TransportError)
                self.assertNotIsInstance(out, llm.BalanceExhausted)
                self.assertEqual(len(seen), 1)
                self.assertEqual((log[0]["error"], log[0]["server_error_type"], log[0]["server_error"]), (f"http_{status}", etype, msg))
                self.assertIn(f"({etype}: {msg})", str(out))
        for status, body in ((401, FK.REAL_401_FAKE_KEY), (403, FK.error_body("permission_denied_error",
                                                                               "Your IP is not allowed to access this organization"))):
            with self.subTest(status=status), mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
                out, _, log = self.chat(("json", status, body))
                rb.assert_not_called()
                self.assertIsInstance(out, llm.KeyRejected)
                self.assertEqual(str(out), "Kimi rejected the API key (HTTP 401)" if status == 401
                                 else "Kimi rejected the API key or the request (HTTP 403)")   # v2.10f：403 的说法
                self.assertNotIn("server_error", log[0])

    def test_redirects_are_not_followed(self):
        out, seen, _ = self.chat(("redirect", 301, self.fake.url("/elsewhere")))
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual([r["path"] for r in seen], ["/v1/chat/completions"])


class TestKimiCost(unittest.TestCase):
    """Pricing 页（国际站 USD、国内站 CNY，2026-10-21）和 WebSearch Pricing 页（Basic：$0.002 / ¥0.01 一次）。"""

    def test_prices_match_the_pricing_pages(self):
        want = {"kimi-k3": ("USD", (0.30, 3.00, 15.00), 3.00, 6.00, 0.002),
                "kimi-k2.6": ("USD", (0.16, 0.95, 4.00), None, None, 0.002),
                "kimi-k3@cn": ("CNY", (2.00, 20.00, 100.00), 20.00, 40.00, 0.01),
                "kimi-k2.6@cn": ("CNY", (1.10, 6.50, 27.00), None, None, 0.01)}
        for pid, (cur, listed, w5, w1, fee) in want.items():
            with self.subTest(price_id=pid):
                p = config.price(pid)
                r = 1.0 if cur == "USD" else 1 / FX
                self.assertEqual((p["provider"], p["currency"], p["prompt_cache"], p["checked"]), ("kimi", cur, "implicit", "2026-10-21"))
                self.assertEqual((p["listed"]["hit"], p["listed"]["miss"], p["listed"]["out"], p["listed"]["search_fee"]), (*listed, fee))
                for got, base in zip(p["peak"], listed):
                    self.assertAlmostEqual(got, base * r)
                self.assertEqual(p["peak"], p["offpeak"])
                self.assertAlmostEqual(p["search_fee_usd"], fee * r)
                self.assertEqual(p.get("cache_write_5m") is None, w5 is None)
                if w5 is not None:
                    self.assertAlmostEqual(p["cache_write_5m"], w5 * r)
                    self.assertAlmostEqual(p["cache_write_1h"], w1 * r)
                self.assertTrue(p["source"].startswith("https://platform.kimi." + ("ai" if cur == "USD" else "com")))
                self.assertEqual("fx" in p, cur == "CNY")
        self.assertEqual(config.price("kimi-k3@cn")["fx"], {"cny_per_usd": 6.7192, "source": config.CNY_PER_USD_SOURCE,
                                                            "date": "2026-10-21"})

    def test_directions_scale_with_kimi_prices(self):
        """「一个方向」的估价：Kimi 自动缓存，但这个 agent 的命中率没测过，输入全按 miss（K3 的 5 分钟写入价同 miss）算，
        加 4 次 × 每次搜索费。$2 上限：K2.6 10 个方向、K3 5 个。"""
        pr = P.Budget.DIRECTION_PROFILE

        def cost(m):
            p = config.price(m)
            hit, miss, out = p["peak"]
            if m.startswith("kimi"):
                hit = miss = max(miss, p.get("cache_write_5m", miss))
            fee = p.get("search_fee_usd", 0.01)
            return (pr["hit"] * hit + pr["miss"] * miss + pr["out"] * out) / 1e6 + pr["searches"] * fee
        flash = cost("deepseek-flash")
        ids = ("kimi-k2.6", "kimi-k3", "kimi-k2.6@cn", "kimi-k3@cn")
        for m in ids:
            with self.subTest(price_id=m):
                self.assertAlmostEqual(P.Budget.typical_direction_usd(m), 0.06 * cost(m) / flash)
        self.assertEqual({m: P.Budget.for_model(m, usd=2.0).directions for m in ids},
                         {"kimi-k2.6": 10, "kimi-k3": 5, "kimi-k2.6@cn": 10, "kimi-k3@cn": 5})
        self.assertEqual(P.Budget().directions, 10)   # DeepSeek 默认路径不变

    def test_reservations_and_the_context_budget(self):
        """预扣：输入按 miss 和 5 分钟写入价中较高的；国内站按折算后的价格。Context 按 spec.price_id 计价；搜索的预扣按「生成查询词」
        那次调用发出的 max_completion_tokens（K3 永远在想：+24,000）加 (2 × max_uses + 2) 次搜索费。"""
        # v2.10f：别家的 tokenizer 没测过，输入按 1 个字符 1 个 token 预扣（DeepSeek 照旧 2 个字符）
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "kimi-k3"), (100_000 * 3 + 1000 * 15) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "kimi-k3@cn"), (100_000 * 20 + 1000 * 100) / 1e6 / FX)
        ctx = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("kimi-k3", "high", region="cn"))
        self.assertEqual((ctx.budget.model, ctx.budget.usd_cap), ("kimi-k3@cn", 2.0))
        self.assertEqual(ctx.budget.search_tokens, S.SEARCH_QUERIES_MAX_TOKENS + EXTRA)
        self.assertAlmostEqual(ctx.budget.search_reserve(),
                               (30_000 * 20 + ctx.budget.search_tokens * 100) / 1e6 / FX + 8 * 0.01 / FX)
        ctx2 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("kimi-k2.6", "high"))
        self.assertEqual(ctx2.budget.search_tokens, S.SEARCH_QUERIES_MAX_TOKENS)   # 搜索不是 plan / judge / repair：K2.6 关思考
        self.assertAlmostEqual(ctx2.budget.search_reserve(), (30_000 * 0.95 + 2000 * 4) / 1e6 + 8 * 0.002)

    def test_search_fee_by_region_and_other_providers_unchanged(self):
        self.assertAlmostEqual(PV.search_fee_usd("kimi-k2.6"), 0.002)
        self.assertAlmostEqual(PV.search_fee_usd("kimi-k3@cn"), 0.01 / FX)
        for m, fee in (("deepseek-flash", 0.01), ("claude-opus-5-5", 0.01), ("gpt-6-luna", 0.01)):
            self.assertEqual(PV.search_fee_usd(m), fee)
        self.assertEqual(spec("kimi-k3", "low").price_id, "kimi-k3")
        self.assertEqual(spec("kimi-k3", "low", region="cn").price_id, "kimi-k3@cn")
        self.assertEqual(PV.ModelSpec("deepseek", "deepseek-flash", KEY).price_id, "deepseek-flash")


class TestKimiSearch(_FakeServerCase):
    QS = ("widgets June 2026 national statistics office", "widget production 2025 annual report", "widget exports customs data")

    def test_queries_then_tools_search(self):
        """模型侧的 $web_search 已在 2026-10-20 下线（WebSearch Pricing 页）。改为：一次 JSON 调用（SEARCH_QUERIES_* 包着同一段
        搜索 prompt）生成查询词，再逐个 POST /v1/tools/search（Web Search Basic 页：text_query 必填、limit 1–20、timeout_seconds 1–60、
        include_content 默认 false）。搜索不是 plan / judge / repair：K2.6 关思考。"""
        a1, a2, b1, c1 = (f"https://{h}.example.org/w" for h in ("a1", "a2", "b1", "c1"))
        out, seen, log = self.search(queries_reply(*self.QS), results(a1, a2), results(b1, a1), results(c1))
        q = seen[0]
        self.assertEqual((q["method"], q["path"]), ("POST", "/v1/chat/completions"))
        self.assertEqual(q["body"]["messages"], [{"role": "system", "content": PR.SEARCH_QUERIES_SYSTEM},
                                                 {"role": "user", "content": PR.SEARCH_QUERIES_USER.format(n=3, brief=BRIEF)}])
        self.assertIn(BRIEF, q["body"]["messages"][1]["content"])
        self.assertEqual((q["body"]["thinking"], q["body"]["max_completion_tokens"], q["body"]["response_format"]),
                         ({"type": "disabled"}, S.SEARCH_QUERIES_MAX_TOKENS, {"type": "json_object"}))
        self.assertEqual(len(seen), 4)
        for r, text in zip(seen[1:], self.QS):
            self.assertEqual((r["method"], r["path"]), ("POST", "/v1/tools/search"))
            self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
            self.assertEqual(r["body"], {"text_query": text, "limit": 4, "timeout_seconds": 30})
        # 按名次交替合并：每个查询词的第 1 名，再第 2 名……；重复的去掉，最多 cap 个
        self.assertEqual(out["urls"], [a1, b1, c1, a2])
        self.assertEqual(out["queries"], list(self.QS))
        self.assertEqual((out["web_search_requests"], out["n_result_urls"], out["n_text_urls"]), (3, 5, 0))
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.006)
        self.assertAlmostEqual(out["usd"], (1000 * 0.95 + 300 * 4) / 1e6)
        self.assertNotIn("Title of", json.dumps(out))   # 标题解析出来但不往外传
        self.assertNotIn("error", out)
        self.assertEqual(log[0]["arm"], "search:d1:queries")
        self.assertNotIn("kind", log[0])
        self.assertAlmostEqual(log[0]["usd"], out["usd"])
        for i, rec in enumerate(log[1:], 1):
            self.assertEqual((rec["arm"], rec["kind"], rec["query_n"], rec["ok"], rec["web_search_requests"], rec["usd"],
                              rec["usd_search_fee_assumed"]), ("search:d1", "search", i, True, 1, 0.0, 0.002))
        self.assertEqual([r["n_result_urls"] for r in log[1:]], [2, 2, 1])
        self.assertNoKeyIn(out, log)

    def test_k3_and_the_china_endpoint(self):
        """K3 的查询词调用用 low（永远在想，+24,000 余量）；国内站发到国内站的两个地址，搜索费按 ¥0.01 折算。"""
        out, seen, log = self.search(queries_reply("widgets 2026"), results("https://a.example.org/w"),
                                     sp=spec("kimi-k3", "high", region="cn"))
        self.assertEqual([r["path"] for r in seen], ["/cn/v1/chat/completions", "/cn/v1/tools/search"])
        b = seen[0]["body"]
        self.assertEqual((b["reasoning_effort"], b["max_completion_tokens"]), ("low", S.SEARCH_QUERIES_MAX_TOKENS + EXTRA))
        self.assertNotIn("thinking", b)
        self.assertEqual(log[0]["thinking"], "low")
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.01 / FX)
        self.assertAlmostEqual(log[1]["usd_search_fee_assumed"], round(0.01 / FX, 6))

    def test_empty_and_failed_queries(self):
        """Web Search Basic 计费：只有 HTTP 200 且 search_results 非空才收费（空结果、失败都不收）。一个查询词失败不影响其余的，
        失败原因合在 error 里（400 的 error.type / message 照原样）。"""
        x = "https://x.example.org/w"
        bad = FK.error_body("invalid_request", "limit must be between 1 and 20")
        out, seen, log = self.search(queries_reply(*self.QS), ("json", 200, {"search_results": []}), ("json", 400, bad), results(x))
        self.assertEqual((out["urls"], out["web_search_requests"], len(seen)), ([x], 1, 4))
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.002)
        self.assertEqual(out["error"], "query 2: http_400 (invalid_request: limit must be between 1 and 20)")
        self.assertEqual((log[1]["web_search_requests"], log[1]["usd_search_fee_assumed"], log[1]["n_result_urls"]), (0, 0.0, 0))
        self.assertEqual((log[2]["ok"], log[2]["error"], log[2]["server_error_type"]), (False, "http_400", "invalid_request"))
        self.assertNotIn("usd", log[2])

    def test_rate_limits_wait_for_the_reset_time(self):
        """429 rate_limited 带 X-RateLimit-Limit / Remaining，按秒限速时还有 X-RateLimit-Reset（Unix 秒）：没有 Retry-After 时
        等到 reset（不少于默认的 3 秒，最多 60 秒）再重试；rate_limit_unavailable 没有这些头：照常退避。"""
        hdr = {"X-RateLimit-Limit": "1", "X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(int(time.time()) + 9)}
        out, seen, _ = self.search(queries_reply("q1"), ("json", 429, FK.error_body("rate_limited", "project qps limit exceeded"), hdr),
                                   results("https://a.example.org/w"), max_uses=1)
        self.assertEqual((len(seen), out["urls"]), (3, ["https://a.example.org/w"]))
        self.assertEqual(len(self.sleeps), 1)
        self.assertTrue(7 <= self.sleeps[0] <= 9.5, self.sleeps)
        self.sleeps.clear()
        out, seen, _ = self.search(queries_reply("q1"), ("json", 429, FK.error_body("rate_limit_unavailable", "rate limit store unavailable")),
                                   results("https://a.example.org/w"), max_uses=1)
        self.assertEqual((len(seen), self.sleeps), (3, [3]))
        h = http.client.HTTPMessage()   # 和 HTTPError.headers 同类（不分大小写）
        h["Retry-After"], h["X-RateLimit-Reset"] = "4", "1"
        self.assertEqual(llm.retry_after(PV.KIMI, h), "4")   # Retry-After 优先
        self.assertIsNone(llm.retry_after(PV.DEEPSEEK, h))   # DeepSeek 不看（同 v2.9b）
        self.assertIsNone(llm.retry_after(PV.KIMI, http.client.HTTPMessage()))

    def test_rejected_key_and_bad_bodies_on_the_search_endpoint(self):
        """搜索接口的 401 / 403 没有 body（Web Search Basic 页；10-21 实测 401 的 Content-Length 是 0）：不读、不抛，记 http_401。
        200 却没有 search_results 列表：形状不对。"""
        with mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
            out, seen, log = self.search(queries_reply("q1"), ("raw", 401, b""), max_uses=1)
            rb.assert_not_called()
        self.assertEqual((out["urls"], out["error"], len(seen)), ([], "query 1: http_401", 2))
        out, _, log = self.search(queries_reply("q1"), ("json", 200, {"results": []}), max_uses=1)
        self.assertEqual((out["error"], log[1]["error"]), ("query 1: bad_response_body", "bad_response_body"))

    def test_query_generation_failures_mean_no_search(self):
        """生成查询词只调一次，失败就没有 URL（不修 JSON、不补查询词），error 以 "queries:" 开头，不发搜索请求。"""
        cases = [(ok("not json"), "queries: reply is not valid JSON"),
                 (ok('{"q": ["a"]}'), 'queries: the reply has no "queries" list'),
                 (ok('{"queries": ["", "  ", 3]}'), "queries: the reply listed no search queries"),
                 (ok('{"queries": ["a"', finish_reason="length"), "queries: reply was truncated (finish_reason=length)"),
                 (("json", 400, FK.error_body("invalid_request_error", "Invalid request")),
                  "queries: search:d1:queries t attempt 1: http_400 (invalid_request_error: Invalid request)"),
                 (("json", 401, FK.REAL_401_FAKE_KEY), "queries: Kimi rejected the API key (HTTP 401)")]
        for reply, err in cases:
            with self.subTest(err=err[:40]):
                out, seen, _ = self.search(reply)
                self.assertEqual((out["urls"], out["queries"], out["error"], out["web_search_requests"], len(seen)),
                                 ([], [], err, 0, 1))

    def test_queries_are_trimmed_deduplicated_and_capped(self):
        out, seen, _ = self.search(queries_reply(" a widgets ", "a widgets", "b", "c", "d"), *[results("https://a.example.org/w")] * 3)
        self.assertEqual(out["queries"], ["a widgets", "b", "c"])
        self.assertEqual([r["body"]["text_query"] for r in seen[1:]], ["a widgets", "b", "c"])

    def test_balance_stops_on_the_query_call_and_on_the_search_endpoint(self):
        body = FK.error_body("exceeded_current_quota_error", "Account balance is insufficient or the account has been disabled")
        out, seen, _ = self.search(("json", 429, body))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 1)
        out, seen, log = self.search(queries_reply("q1", "q2"), ("json", 429, body))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertTrue(str(out).startswith("insufficient balance: Kimi HTTP 429 exceeded_current_quota_error (balance insufficient"))
        self.assertIn("(search:d1 t); the run was stopped without retrying.", str(out))
        self.assertEqual((len(seen), self.sleeps), (2, []))
        self.assertNoKeyIn(str(out), log)


class TestKimiDirection(_FakeServerCase):
    """run_direction（一个子 agent）对着假服务走完：查询词 -> 搜索接口 -> 取页（假的）-> 抽取 -> 代码核对；三次调用都记进
    calls.jsonl 并计入预算（查询词调用的 token、搜索的按次费用、抽取的 token）。"""

    def test_one_direction_end_to_end(self):
        ctx = P.Context("t", "q", "2026-06-20", self.tmp / "c.jsonl", spec=spec("kimi-k2.6", "high"))
        url = "https://stats.example.org/widgets"
        extract = {"points": [{"name": "widgets June 2025", "value_as_written": "1,210", "unit": "widgets",
                               "period_start": "2025-06-01", "period_end": "2025-06-30", "quote": "June 2025: 1,210 widgets"}]}
        self.fake.reset(queries_reply("widgets June 2025"), results(url), ok(json.dumps(extract), use=FK.usage(5000, 400)))
        page = {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                "text": "Widget statistics. June 2025: 1,210 widgets."}
        d = {"id": "d1", "category": "own_history", "hypothesis": "h", "data_to_find": "f", "search_hints": ["widgets"]}
        target = {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30"}
        with mock.patch.object(P, "fetch_page", lambda u, a, q: dict(page)):
            out = P.run_direction(ctx, target, d, 1)
        self.assertNotIn("error", out)
        self.assertEqual(out["search"]["urls"], [url])
        self.assertEqual(out["search"]["queries"], ["widgets June 2025"])
        self.assertEqual(len(out["points"]), 1)
        self.assertEqual([r["path"] for r in self.fake.seen], ["/v1/chat/completions", "/v1/tools/search", "/v1/chat/completions"])
        self.assertIn("widgets", self.fake.seen[0]["body"]["messages"][1]["content"])   # SEARCH_USER 填好的那段在 brief 里
        self.assertEqual(self.fake.seen[2]["body"]["thinking"], {"type": "disabled"})   # 抽取不是 plan / judge / repair
        rows = [json.loads(x) for x in ctx.calls_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([r["arm"] for r in rows], ["search:d1:queries", "search:d1", "extract:d1"])
        want = (1000 * 0.95 + 300 * 4) / 1e6 + 0.002 + (5000 * 0.95 + 400 * 4) / 1e6
        self.assertAlmostEqual(ctx.budget.usd, want, places=6)
        self.assertEqual((ctx.budget.n_calls, ctx.budget.reserved, ctx.budget.aborted), (3, 0.0, ""))
        self.assertNoKeyIn(ctx.calls_path.read_text(encoding="utf-8"), out)


class TestKeyCheck(_FakeServerCase):
    def check(self, *script, sp=None):
        self.fake.reset(*script)
        out = llm.check_key(sp or spec())
        self.assertNoKeyIn(out)
        return out, list(self.fake.seen)

    PAGE = {"object": "list", "data": [
        {"id": "kimi-k3", "object": "model", "created": 1, "owned_by": "moonshot", "context_length": 1_048_576,
         "supports_image_in": True, "supports_video_in": True, "supports_reasoning": True},
        {"id": "kimi-k2.6", "object": "model", "created": 1, "owned_by": "moonshot", "context_length": 262_144,
         "supports_image_in": True, "supports_video_in": True, "supports_reasoning": True}]}

    def test_models_list(self):
        """List Models：GET /v1/models，Authorization: Bearer，回复 {"object": "list", "data": [{"id", "context_length", ...}]}
        （没有分页）。两站的 key 互不通用：国内站的 key 要发到国内站。"""
        out, seen = self.check(("json", 200, self.PAGE))
        self.assertEqual((seen[0]["method"], seen[0]["path"], seen[0]["body"]), ("GET", "/v1/models", None))
        self.assertEqual(seen[0]["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"], out["status"]), (True, True, 2, 200))
        out, seen = self.check(("json", 200, {"object": "list", "data": self.PAGE["data"][1:]}), sp=spec("kimi-k3", "low", region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/v1/models")
        self.assertEqual((out["ok"], out["model_listed"]), (True, False))
        self.assertIn("not in the models list", out["message"])

    def test_rejected_keys_use_the_real_401_bodies(self):
        """2026-10-21 实测（probes/kimi_key_probe.py，没花钱）：不带 key / 假 key 调 GET /v1/models 都是 HTTP 401。"""
        for body in (FK.REAL_401_NO_KEY, FK.REAL_401_FAKE_KEY):
            with self.subTest(type=body["error"]["type"]):
                out, _ = self.check(("json", 401, body))
                self.assertEqual(out, {"provider": "kimi", "model": "kimi-k2.6", "ok": False, "status": 401,
                                       "error": "key_rejected", "message": "Kimi rejected the API key (HTTP 401)"})

    def test_other_outcomes(self):
        out, _ = self.check(("json", 429, FK.error_body("exceeded_current_quota_error", "Account balance is insufficient")))
        self.assertEqual(out["error"], "balance")
        self.assertIn("exceeded_current_quota_error", out["message"])
        out, _ = self.check(("json", 403, FK.error_body("permission_denied_error", "The API you are accessing is not open")))
        self.assertEqual(out["error"], "forbidden")   # v2.10f：403 单独记（不一定是 key 错了）
        self.assertEqual(out["message"], "Kimi rejected the API key or the request (HTTP 403)")
        out, _ = self.check(("raw", 200, b"<html>"))
        self.assertEqual(out["error"], "bad_response_body")
        out, _ = self.check(("redirect", 302, self.fake.url("/x")))
        self.assertEqual(out["error"], "redirect")


class TestModelSpecKimi(unittest.TestCase):
    def test_official_endpoints(self):
        """API 主机：国际站 api.moonshot.ai、国内站 api.moonshot.cn（Chat API / Web Search Basic / List Models 页的 servers）。"""
        self.assertEqual(PV.KIMI.regions, {
            "global": {"chat": "https://api.moonshot.ai/v1/chat/completions", "search": "https://api.moonshot.ai/v1/tools/search",
                       "models": "https://api.moonshot.ai/v1/models"},
            "cn": {"chat": "https://api.moonshot.cn/v1/chat/completions", "search": "https://api.moonshot.cn/v1/tools/search",
                   "models": "https://api.moonshot.cn/v1/models"}})
        self.assertEqual(set(PV.KIMI.region_labels), {"global", "cn"})
        self.assertEqual(PV.KIMI.key_check_request("cn", KEY), ("https://api.moonshot.cn/v1/models", {"Authorization": f"Bearer {KEY}"}))
        self.assertEqual([PV.KIMI.tools_search_request(KEY, "q", limit=n)[1]["limit"] for n in (0, 4, 50)], [1, 4, 20])

    def test_choices_and_public_view(self):
        self.assertEqual(PV.PROVIDERS["kimi"]["models"], ("kimi-k2.6", "kimi-k3"))
        self.assertEqual(PV.PROVIDERS["kimi"]["default_model"], "kimi-k2.6")
        self.assertEqual((PV.MODELS["kimi-k2.6"]["max_output"], PV.MODELS["kimi-k3"]["max_output"]), (262_144, 1_048_576))
        sp = spec("kimi-k3", "medium", region="cn", usd_cap=5)
        self.assertEqual(sp.public(), {"provider": "kimi", "model": "kimi-k3", "region": "cn", "thinking": "medium",
                                       "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high", "*": "low"},
                                       "usd_cap": 5.0, "byok": True, "price_id": "kimi-k3@cn",
                                       "fx": {"cny_per_usd": 6.7192, "source": config.CNY_PER_USD_SOURCE, "date": "2026-10-21"}})
        self.assertEqual(spec().public(), {"provider": "kimi", "model": "kimi-k2.6", "region": "global", "thinking": "off",
                                           "thinking_by_role": {}, "usd_cap": 2.0, "byok": True})
        self.assertNotIn(KEY, repr(sp))
        with self.assertRaises(PV.SpecError):
            spec(region="us")
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("kimi", "gpt-6-luna", KEY)
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("moonshot", "kimi-k2.6", KEY)
        with mock.patch.dict(config.PRICES), self.assertRaises(config.UnknownModel):   # 某个区域没有价格就拒跑
            del config.PRICES["kimi-k2.6@cn"]
            spec(region="cn")


class TestRunWithKimiSpec(_FakeServerCase):
    """prepare_run(spec=Kimi 国内站 K3) -> 图 -> save_run，全部对着假服务：规划一步收到 429 exceeded_current_quota_error 就干净停下；
    state.json 记 provider、price_id、汇率和搜索设置，不记 key；结果目录里没有 key；写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop(self):
        from triangulate.agent import run as R
        sp = spec("kimi-k3", "high", region="cn", usd_cap=1.5)
        q = {"id": "ask_kimi1", "question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20"}
        body = FK.error_body("exceeded_current_quota_error", "Account balance is insufficient or the account has been disabled")
        self.fake.reset(*[("json", 429, body)] * 3)
        with mock.patch.object(R, "RES", self.tmp):
            h = R.prepare_run(q, "web_t", spec=sp)
            out = h["g"].invoke(R.initial_input(q), h["cfg"])
            self.assertFalse(out.get("__interrupt__"))
            st = R.save_run(h, [])
        self.assertEqual([r["path"] for r in self.fake.seen], ["/cn/v1/chat/completions"])
        b = self.fake.seen[0]["body"]
        self.assertEqual((b["model"], b["reasoning_effort"]), ("kimi-k3", "max"))   # plan，网页 high -> max
        self.assertTrue(st["aborted"].startswith("insufficient balance: Kimi HTTP 429 exceeded_current_quota_error"), st["aborted"])
        self.assertEqual((st["provider"], st["model"]), ("kimi", "kimi-k3"))
        rs = st["settings"]["run_spec"]
        self.assertEqual((rs["price_id"], rs["region"], rs["fx"]["cny_per_usd"]), ("kimi-k3@cn", "cn", 6.7192))
        self.assertEqual(st["settings"]["search_queries"], {"max_tokens": S.SEARCH_QUERIES_MAX_TOKENS,
                                                            "endpoint": self.fake.url("/cn/v1/tools/search"), "timeout_seconds": 30})
        self.assertEqual(st["budget"]["usd_cap"], 1.5)
        files = list((self.tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            self.assertNotIn(KEY, f.read_text(encoding="utf-8"), f.name)
        self.assertFalse(sp.has_key)


if __name__ == "__main__":
    unittest.main()
