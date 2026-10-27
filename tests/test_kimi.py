"""v2.10d：Kimi adapter（Moonshot AI 开放平台：国际站 api.moonshot.ai / 国内站 api.moonshot.cn）。全部对着 127.0.0.1 上的
假服务（tests/fake_kimi.py）跑：真实走 urllib + urlopen_no_redirect，请求头、请求体、HTTPError 的 body 都是真的；不联网、
不需要真 key、不读 key 文件。

JSON 调用：OpenAI 兼容的流式 Chat Completions。v2.10h（用户 10-21：只用各家自带的联网搜索）：只剩 K3（K2.6 删掉）；搜索 =
Responses API（POST /v1/responses）自带的 web_search 工具，不再有「生成查询词 + /v1/tools/search」。
每一项对照的官方文档写在各个测试的说明里（链接见 PROVIDERS.md 第 11、16 节）。
"""
import json
import tempfile
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
SEARCH_OUT = config.MAX_TOKENS["search"] + EXTRA   # K3 永远在想：搜索也带思考余量


def spec(model="kimi-k3", thinking="low", key=KEY, **kw):
    return PV.ModelSpec("kimi", model, key, thinking=thinking, **kw)


def ok(content='{"a": 1}', **kw):
    return ("raw", 200, FK.sse(content, **kw))


def found(text="https://a.example.org/w", **kw):
    return ("json", 200, FK.search_response(text, **kw))


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
        K3：顶层 reasoning_effort（永远在想；省略时 max），不发 thinking。"""
        out, seen, log = self.chat(ok())
        self.assertEqual(out, ({"a": 1}, '{"a": 1}', None))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/chat/completions"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        for h in ("x-api-key", "anthropic-version"):
            self.assertNotIn(h, r["headers"])
        b = r["body"]
        self.assertEqual(list(b), ["model", "messages", "reasoning_effort", "response_format", "max_completion_tokens", "stream",
                                   "stream_options"])
        self.assertEqual((b["model"], b["messages"]), ("kimi-k3", MSGS))   # Kimi 收 system 角色，原样
        self.assertEqual((b["reasoning_effort"], b["response_format"], b["max_completion_tokens"], b["stream"], b["stream_options"]),
                         ("low", {"type": "json_object"}, 12000 + EXTRA, True, {"include_usage": True}))
        for banned in ("temperature", "top_p", "n", "presence_penalty", "frequency_penalty", "max_tokens", "thinking",
                       "tools", "tool_choice", "prompt_cache_options", "store"):
            self.assertNotIn(banned, b)
        self.assertEqual((log[0]["model"], log[0]["ok"], log[0]["thinking"]), ("kimi-k3", True, "low"))

    def test_thinking_per_role(self):
        """K3（Reasoning Effort 页）：永远在想，顶层 reasoning_effort 只有 low / high / max（省略时 max），不发 thinking；网页档位
        low -> low、medium -> high、high -> max（调研的映射），plan / judge / repair 以外用 low。思考 token 和正文共用
        max_completion_tokens（Thinking 指南）：每个调用都 +24,000。"""
        cases = [("low", "plan", "low"), ("medium", "judge:r1", "high"), ("high", "judge:r2:repair", "max"),
                 ("high", "audit", "low"), ("medium", "final", "low")]
        for level, arm, want in cases:
            with self.subTest(level=level, arm=arm):
                out, seen, log = self.chat(ok(), sp=spec(thinking=level), arm=arm, max_tokens=4000)
                b = seen[0]["body"]
                self.assertEqual(b["reasoning_effort"], want)
                self.assertNotIn("thinking", b)
                self.assertEqual(b["max_completion_tokens"], 4000 + EXTRA)
                self.assertEqual(log[0]["thinking"], want)
        self.assertEqual(PV.thinking_levels("kimi-k3"), ("low", "medium", "high"))
        with self.assertRaises(PV.SpecError):
            spec(thinking="off")
        with self.assertRaises(ValueError):   # 防御：K3 不会不带 reasoning_effort
            PV.KIMI.chat_request("kimi-k3", KEY, MSGS, max_tokens=10, effort=None)
        self.assertEqual(spec(thinking="high").thinking_by_role(), {"plan": "max", "judge": "max", "repair": "max", "*": "low"})

    def test_headroom_is_capped_at_the_models_max_output(self):
        _, seen, _ = self.chat(ok(), max_tokens=1_040_000)
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
        K3 价格（国际站）：miss $3、5 分钟写入 $3、命中 $0.30、输出 $15。国内站：CNY 价按 2026-10-21 中间价 6.7192 折成 USD。"""
        u = FK.usage(prompt=12_000, completion=900, cached=4_000, write=7_000)
        cases = [(spec(), (1_000 * 3.00 + 4_000 * 0.30 + 7_000 * 3.00 + 900 * 15.00) / 1e6),
                 (spec(region="cn"), (1_000 * 20 + 4_000 * 2 + 7_000 * 20 + 900 * 100) / 1e6 / FX)]
        for sp, want in cases:
            with self.subTest(region=sp.region):
                _, _, log = self.chat(ok(use=u), sp=sp)
                rec = log[0]
                self.assertAlmostEqual(rec["usd"], round(want, 6))
                self.assertEqual((rec["finish_reason"], rec["prompt_tokens"], rec["cached_tokens"], rec["cache_write_tokens"],
                                  rec["completion_tokens"]), ("stop", 12_000, 4_000, 7_000, 900))
                self.assertNotIn("reasoning_tokens", rec)   # Chat API 的 usage 没有这个字段：没有就不记
                self.assertEqual(rec["model"], sp.model)    # 日志里是模型名；计价 id 只用来查价格
        # 没有 prompt_tokens_details 时用顶层 cached_tokens；有 completion_tokens_details.reasoning_tokens 时记下
        self.assertAlmostEqual(PV.kimi_usage_cost({"prompt_tokens": 1000, "cached_tokens": 400, "completion_tokens": 10}, "kimi-k3"),
                               (600 * 3.00 + 400 * 0.30 + 10 * 15.00) / 1e6)
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
        want = P.Budget.llm_reserve(sum(len(m["content"]) for m in MSGS), sent["max_completion_tokens"], "kimi-k3")
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
    """Pricing 页（国际站 USD、国内站 CNY，2026-10-21）。v2.10h：Responses 里 web_search 的单价两站的 WebSearch Pricing 页都没列：
    按每次 $0.01 的假设记（config.KIMI_WEB_SEARCH_FEE_ASSUMED_USD，两站相同、不折算）。"""

    def test_prices_match_the_pricing_pages(self):
        want = {"kimi-k3": ("USD", (0.30, 3.00, 15.00), 3.00, 6.00), "kimi-k3@cn": ("CNY", (2.00, 20.00, 100.00), 20.00, 40.00)}
        self.assertEqual(sorted(p for p in config.PRICES if p.startswith("kimi")), sorted(want))   # K2.6 已删
        for pid, (cur, listed, w5, w1) in want.items():
            with self.subTest(price_id=pid):
                p = config.price(pid)
                r = 1.0 if cur == "USD" else 1 / FX
                self.assertEqual((p["provider"], p["currency"], p["prompt_cache"], p["checked"]), ("kimi", cur, "implicit", "2026-10-21"))
                self.assertEqual((p["listed"]["hit"], p["listed"]["miss"], p["listed"]["out"]), listed)
                self.assertNotIn("search_fee", p["listed"])   # 没有官方价，不写成「原价」
                for got, base in zip(p["peak"], listed):
                    self.assertAlmostEqual(got, base * r)
                self.assertEqual(p["peak"], p["offpeak"])
                self.assertEqual((p["search_fee_usd"], p["search_fee_assumed"]), (0.01, True))
                self.assertAlmostEqual(p["cache_write_5m"], w5 * r)
                self.assertAlmostEqual(p["cache_write_1h"], w1 * r)
                self.assertTrue(p["source"].startswith("https://platform.kimi." + ("ai" if cur == "USD" else "com")))
                self.assertEqual("fx" in p, cur == "CNY")
        self.assertEqual(config.price("kimi-k3@cn")["fx"], {"cny_per_usd": 6.7192, "source": config.CNY_PER_USD_SOURCE,
                                                            "date": "2026-10-21"})

    def test_directions_scale_with_kimi_prices(self):
        """「一个方向」的估价：Kimi 自动缓存，但这个 agent 的命中率没测过，输入全按 miss（K3 的 5 分钟写入价同 miss）算，
        加 4 次 × 每次搜索费（假设的 $0.01）。$2 上限：两站都是 4 个方向。"""
        pr = P.Budget.DIRECTION_PROFILE

        def cost(m):
            p = config.price(m)
            hit, miss, out = p["peak"]
            if m.startswith("kimi"):
                hit = miss = max(miss, p.get("cache_write_5m", miss))
            fee = p.get("search_fee_usd", 0.01)
            return (pr["hit"] * hit + pr["miss"] * miss + pr["out"] * out) / 1e6 + pr["searches"] * fee
        flash = cost("deepseek-flash")
        ids = ("kimi-k3", "kimi-k3@cn")
        for m in ids:
            with self.subTest(price_id=m):
                self.assertAlmostEqual(P.Budget.typical_direction_usd(m), 0.06 * cost(m) / flash)
        self.assertEqual({m: P.Budget.for_model(m, usd=2.0).directions for m in ids}, {"kimi-k3": 4, "kimi-k3@cn": 4})
        self.assertEqual(P.Budget().directions, 10)   # DeepSeek 默认路径不变

    def test_reservations_and_the_context_budget(self):
        """预扣：输入按 miss 和 5 分钟写入价中较高的；国内站按折算后的价格。Context 按 spec.price_id 计价。v2.10h：搜索的预扣同其他
        自带搜索的 provider：输入按 p99 的 72,000 token、输出按发出的 max_output_tokens（K3 永远在想：+24,000）、(2 × max_uses + 2) 次搜索费。"""
        # v2.10f：别家的 tokenizer 没测过，输入按 1 个字符 1 个 token 预扣（DeepSeek 照旧 2 个字符）
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "kimi-k3"), (100_000 * 3 + 1000 * 15) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "kimi-k3@cn"), (100_000 * 20 + 1000 * 100) / 1e6 / FX)
        ctx = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec(thinking="high", region="cn"))
        self.assertEqual((ctx.budget.model, ctx.budget.usd_cap), ("kimi-k3@cn", 3.0))   # v2.13b：默认上限 $3
        self.assertEqual((ctx.budget.search_tokens, ctx.budget.search_input_tokens), (SEARCH_OUT, 72_000))
        self.assertAlmostEqual(ctx.budget.search_reserve(), (72_000 * 20 + SEARCH_OUT * 100) / 1e6 / FX + 8 * 0.01)
        ctx2 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec())
        self.assertAlmostEqual(ctx2.budget.search_reserve(), (72_000 * 3 + SEARCH_OUT * 15) / 1e6 + 8 * 0.01)

    def test_responses_usage_is_split_like_chat_usage(self):
        """Responses 页 Usage fields：cached_tokens、cache_write_tokens 和未缓存的部分互斥、相加等于 input_tokens（同 Chat API）。K3 的
        5 分钟写入价恰好等于 miss 价，这里用一个写入价不同的假价格确认写入那部分确实按写入价算。"""
        fake = dict(config.price("kimi-k3"), peak=(0.5, 2.0, 10.0), cache_write_5m=7.0)
        with mock.patch.dict(config.PRICES, {"kimi-fake": fake}):
            u = {"input_tokens": 1_000, "input_tokens_details": {"cached_tokens": 100, "cache_write_tokens": 300}, "output_tokens": 50}
            self.assertAlmostEqual(PV.kimi_responses_cost(u, "kimi-fake"), (600 * 2.0 + 100 * 0.5 + 300 * 7.0 + 50 * 10.0) / 1e6)
            self.assertEqual(PV.kimi_responses_cost({}, "kimi-fake"), 0.0)   # usage 是 null 时按 0

    def test_search_fee_and_other_providers_unchanged(self):
        self.assertEqual((PV.search_fee_usd("kimi-k3"), PV.search_fee_usd("kimi-k3@cn")), (0.01, 0.01))
        self.assertEqual(PV.KIMI.search_fee_usd, config.KIMI_WEB_SEARCH_FEE_ASSUMED_USD)
        for m, fee in (("deepseek-flash", 0.01), ("claude-opus-5-5", 0.01), ("gpt-6-luna", 0.01)):
            self.assertEqual(PV.search_fee_usd(m), fee)
        self.assertEqual(spec().price_id, "kimi-k3")
        self.assertEqual(spec(region="cn").price_id, "kimi-k3@cn")
        self.assertEqual(PV.ModelSpec("deepseek", "deepseek-flash", KEY).price_id, "deepseek-flash")


class TestKimiSearch(_FakeServerCase):
    """v2.10h：K3 自带的 web_search（Responses 页：POST /v1/responses，tools [{"type": "web_search"}]，服务端先按输入决定要不要搜，
    搜了把结果放进模型的上下文；output 最前面是 web_search_call，include web_search_call.action.sources 才带结果的 url / title）。"""

    def test_responses_web_search_request_and_reply(self):
        """请求：model、input（搜索 prompt 原样，字符串 = 一条 user 消息）、tools 只有 web_search、include sources、reasoning.effort
        （省略时默认 max，所以显式写；搜索不是 plan / judge / repair：low）、max_output_tokens（8192 + 24,000 思考余量）。不发
        tool_choice（只有 auto）、max_tool_calls（没有这个参数）、stream / store / instructions / prompt_cache_options。
        回复：模型文字里的 URL 优先，不够再按 sources 补；查询词是 action.query（服务端实际用的）；计次 = web_search_call 的个数。"""
        src = ("https://b.example.org/x", "https://a.example.org/w", "https://c.example.org/y")
        use = FK.responses_usage(inp=20_000, out=700, cached=5_000, write=10_000, reasoning=300)
        out, seen, log = self.search(found("Best first:\nhttps://a.example.org/w", sources=src, use=use))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/v1/responses"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        b = r["body"]
        self.assertEqual(b, {"model": "kimi-k3", "input": BRIEF, "tools": [{"type": "web_search"}],
                             "include": ["web_search_call.action.sources"], "reasoning": {"effort": "low"},
                             "max_output_tokens": SEARCH_OUT})
        self.assertEqual(list(b), ["model", "input", "tools", "include", "reasoning", "max_output_tokens"])
        self.assertEqual(out["urls"], ["https://a.example.org/w", "https://b.example.org/x", "https://c.example.org/y"])
        self.assertEqual(out["queries"], ["widgets June 2026 official statistics"])
        self.assertEqual((out["web_search_requests"], out["n_result_urls"], out["n_text_urls"]), (1, 3, 1))
        want = (5_000 * 3.00 + 5_000 * 0.30 + 10_000 * 3.00 + 700 * 15.00) / 1e6   # 未缓存 = 20,000 - 5,000 - 10,000
        self.assertAlmostEqual(out["usd"], want)
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.01)
        self.assertNotIn("error", out)
        self.assertNotIn("Title of", json.dumps(out))      # 标题解析出来但不往外传
        self.assertNotIn("SECRET-REASONING", json.dumps(out) + json.dumps(log))
        rec = log[0]
        self.assertEqual((rec["arm"], rec["kind"], rec["ok"], rec["stop"], rec["input_tokens"], rec["cached_tokens"],
                          rec["cache_write_tokens"], rec["output_tokens"], rec["reasoning_tokens"], rec["web_search_requests"],
                          rec["n_result_urls"], rec["usd"], rec["usd_search_fee_assumed"]),
                         ("search:d1", "search", True, "completed", 20_000, 5_000, 10_000, 700, 300, 1, 3, round(want, 6), 0.01))
        parsed = PV.KIMI.search_unpack(FK.search_response(sources=src))
        self.assertEqual(parsed["result_titles"], ["Title of x", "Title of w", "Title of y"])   # sources 的 title 解析出来
        self.assertNoKeyIn(out, log)

    def test_effort_is_low_whatever_the_level_and_the_china_endpoint(self):
        """国内站发到国内站的 /v1/responses；token 按 CNY 价折算，搜索费按假设的 $0.01（不折算）。网页档位只作用于 plan / judge / repair。"""
        use = FK.responses_usage(inp=10_000, out=500, reasoning=100)
        out, seen, log = self.search(found(sources=("https://a.example.org/w",), use=use), sp=spec(thinking="high", region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/v1/responses")
        self.assertEqual((seen[0]["body"]["reasoning"], seen[0]["body"]["max_output_tokens"]), ({"effort": "low"}, SEARCH_OUT))
        self.assertAlmostEqual(out["usd"], (10_000 * 20 + 500 * 100) / 1e6 / FX)
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.01)
        with self.assertRaises(ValueError):   # 防御：K3 的搜索不会不带 reasoning effort
            PV.KIMI.search_request("kimi-k3", KEY, BRIEF, max_tokens=10, max_uses=3, effort=None)

    def test_the_server_may_not_search(self):
        """Responses 页：web_search_call 只有服务端决定要搜时才有（tool_choice 只有 auto，没法强制）。没搜：不计搜索费，URL 只能来自
        模型的文字；照常记一行（stop completed、web_search_requests 0）。"""
        out, _, log = self.search(found("https://memory.example.org/z", searched=False))
        self.assertEqual((out["urls"], out["queries"], out["web_search_requests"], out["usd_search_fee_assumed"]),
                         (["https://memory.example.org/z"], [], 0, 0.0))
        self.assertEqual((log[0]["web_search_requests"], log[0]["n_result_urls"], log[0]["usd_search_fee_assumed"]), (0, 0, 0.0))
        out, _, _ = self.search(found("no links here", searched=False))
        self.assertEqual(out["urls"], [])

    def test_incomplete_and_null_usage(self):
        """status incomplete（incomplete_details.reason = max_output_tokens）：照样用已有的文字和 sources，stop 记原因。usage 可以是 null
        （ResponsesResponse 的 usage oneOf null）：v2.10i 起 token 成本按这次搜索预扣的 token 部分记（72,000 输入 + 32,192 输出，按 K3 的
        预扣单价，约 $0.70；以前记 0，预算会漏掉这次），日志写 usd_basis；搜索照样按 web_search_call 计次。"""
        reply = FK.search_response("", sources=("https://a.example.org/w",), status="incomplete",
                                   incomplete={"reason": "max_output_tokens"})
        reply["usage"] = None
        out, _, log = self.search(("json", 200, reply))
        want = (72_000 * 3.00 + SEARCH_OUT * 15.00) / 1e6
        self.assertAlmostEqual(want, P.Budget.search_tokens_reserve("kimi-k3", P.Budget.SEARCH_INPUT_TOKENS_BYOK, SEARCH_OUT))
        self.assertEqual((out["urls"], out["web_search_requests"]), (["https://a.example.org/w"], 1))
        self.assertAlmostEqual(out["usd"], want)
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.01)
        self.assertEqual((log[0]["stop"], log[0]["ok"], log[0]["usage_missing"], log[0]["usd_basis"], log[0]["usd"]),
                         ("incomplete:max_output_tokens", True, True, "reserve (usage missing)", round(want, 6)))
        for missing in ("absent", {}):   # 整个字段都没有、或是空对象：同样按预扣
            if missing == "absent":
                reply.pop("usage")
            else:
                reply["usage"] = missing
            out, _, log = self.search(("json", 200, reply))
            self.assertAlmostEqual(out["usd"], want)
            self.assertTrue(log[0]["usage_missing"])
        out, _, log = self.search(found())   # 有 usage 的回复照旧按 usage 计价，不带 usage_missing / usd_basis
        self.assertFalse({"usage_missing", "usd_basis"} & set(log[0]))

    def test_errors_on_the_search_endpoint(self):
        """Responses 接口的错误形状 {"error": {message, type, code}}：429 exceeded_current_quota_error -> 整次运行停下（不重试）；
        429 engine_overloaded_error 按 Retry-After 重试；400 照原样记（不重试）；401 不读 body、不抛，记 http_401（同其他 provider 的搜索）；
        3xx 不跟随。"""
        body = FK.error_body("exceeded_current_quota_error", "Account balance is insufficient or the account has been disabled")
        out, seen, log = self.search(("json", 429, body))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertTrue(str(out).startswith("insufficient balance: Kimi HTTP 429 exceeded_current_quota_error (balance insufficient"))
        self.assertIn("(search:d1 t); the run was stopped without retrying.", str(out))
        self.assertEqual((len(seen), self.sleeps), (1, []))
        self.assertNoKeyIn(str(out), log)
        over = FK.error_body("engine_overloaded_error", "The engine is currently overloaded, please try again later")
        out, seen, _ = self.search(("json", 429, over, {"retry-after": "8"}), found())
        self.assertEqual((len(seen), out["urls"], self.sleeps), (2, ["https://a.example.org/w"], [8.0]))
        bad = FK.error_body("invalid_request_error", "search_context_size is not supported")
        out, seen, log = self.search(("json", 400, bad))
        self.assertEqual((out["urls"], out["error"], len(seen)),
                         ([], "http_400 (invalid_request_error: search_context_size is not supported)", 1))
        with mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
            out, seen, _ = self.search(("json", 401, FK.REAL_401_FAKE_KEY))
            rb.assert_not_called()
        self.assertEqual((out["urls"], out["error"], len(seen)), ([], "http_401", 1))
        out, seen, _ = self.search(("redirect", 302, self.fake.url("/elsewhere")))
        self.assertEqual((out["error"], [r["path"] for r in seen]), ("http_302", ["/v1/responses"]))


class TestKimiDirection(_FakeServerCase):
    """run_direction（一个子 agent）对着假服务走完：自带的 web_search（Responses）-> 取页（假的）-> 抽取 -> 代码核对；两次调用都记进
    calls.jsonl 并计入预算（搜索的 token 和假设的按次费用、抽取的 token）。"""

    def test_one_direction_end_to_end(self):
        ctx = P.Context("t", "q", "2026-06-20", self.tmp / "c.jsonl", spec=spec(thinking="high"))
        url = "https://stats.example.org/widgets"
        extract = {"points": [{"name": "widgets June 2025", "value_as_written": "1,210", "unit": "widgets",
                               "period_start": "2025-06-01", "period_end": "2025-06-30", "quote": "June 2025: 1,210 widgets"}]}
        self.fake.reset(found(url, query="widgets June 2025", sources=(url,)), ok(json.dumps(extract), use=FK.usage(5000, 400)))
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
        self.assertEqual([r["path"] for r in self.fake.seen], ["/v1/responses", "/v1/chat/completions"])
        self.assertIn("widgets", self.fake.seen[0]["body"]["input"])   # SEARCH_USER 填好的那段原样是 input
        self.assertNotIn(PR.SEARCH_USER[:40], json.dumps(self.fake.seen[1]["body"]))   # 抽取不经过搜索 prompt
        self.assertEqual(self.fake.seen[1]["body"]["reasoning_effort"], "low")   # 抽取不是 plan / judge / repair
        rows = [json.loads(x) for x in ctx.calls_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([r["arm"] for r in rows], ["search:d1", "extract:d1"])
        want = (9000 * 3.00 + 600 * 15.00) / 1e6 + 0.01 + (5000 * 3.00 + 400 * 15.00) / 1e6
        self.assertAlmostEqual(ctx.budget.usd, want, places=6)
        self.assertEqual((ctx.budget.n_calls, ctx.budget.reserved, ctx.budget.aborted), (2, 0.0, ""))
        self.assertNoKeyIn(ctx.calls_path.read_text(encoding="utf-8"), out)


class TestKeyCheck(_FakeServerCase):
    def check(self, *script, sp=None):
        self.fake.reset(*script)
        out = llm.check_key(sp or spec())
        self.assertNoKeyIn(out)
        return out, list(self.fake.seen)

    PAGE = {"object": "list", "data": [
        {"id": "kimi-k2.6", "object": "model", "created": 1, "owned_by": "moonshot", "context_length": 262_144,
         "supports_image_in": True, "supports_video_in": True, "supports_reasoning": True},
        {"id": "kimi-k3", "object": "model", "created": 1, "owned_by": "moonshot", "context_length": 1_048_576,
         "supports_image_in": True, "supports_video_in": True, "supports_reasoning": True}]}

    def test_models_list(self):
        """List Models：GET /v1/models，Authorization: Bearer，回复 {"object": "list", "data": [{"id", "context_length", ...}]}
        （没有分页）。两站的 key 互不通用：国内站的 key 要发到国内站。（列表里别的模型照样有，网页只提供 K3。）"""
        out, seen = self.check(("json", 200, self.PAGE))
        self.assertEqual((seen[0]["method"], seen[0]["path"], seen[0]["body"]), ("GET", "/v1/models", None))
        self.assertEqual(seen[0]["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"], out["status"]), (True, True, 2, 200))
        out, seen = self.check(("json", 200, {"object": "list", "data": self.PAGE["data"][:1]}), sp=spec(region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/v1/models")
        self.assertEqual((out["ok"], out["model_listed"]), (True, False))
        self.assertIn("not in the models list", out["message"])

    def test_rejected_keys_use_the_real_401_bodies(self):
        """2026-10-21 实测（probes/kimi_key_probe.py，没花钱）：不带 key / 假 key 调 GET /v1/models 都是 HTTP 401。"""
        for body in (FK.REAL_401_NO_KEY, FK.REAL_401_FAKE_KEY):
            with self.subTest(type=body["error"]["type"]):
                out, _ = self.check(("json", 401, body))
                self.assertEqual(out, {"provider": "kimi", "model": "kimi-k3", "ok": False, "status": 401,
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
        """API 主机：国际站 api.moonshot.ai、国内站 api.moonshot.cn（Chat API / Responses / List Models 页的 servers）。
        v2.10h：搜索发到 /v1/responses（不再有 /v1/tools/search）。"""
        self.assertEqual(PV.KIMI.regions, {
            "global": {"chat": "https://api.moonshot.ai/v1/chat/completions", "search": "https://api.moonshot.ai/v1/responses",
                       "models": "https://api.moonshot.ai/v1/models"},
            "cn": {"chat": "https://api.moonshot.cn/v1/chat/completions", "search": "https://api.moonshot.cn/v1/responses",
                   "models": "https://api.moonshot.cn/v1/models"}})
        self.assertEqual(set(PV.KIMI.region_labels), {"global", "cn"})
        self.assertEqual(PV.KIMI.key_check_request("cn", KEY), ("https://api.moonshot.cn/v1/models", {"Authorization": f"Bearer {KEY}"}))
        for gone in ("search_mode", "tools_search_request", "tools_search_unpack", "search_settings", "reset_header"):
            self.assertFalse(hasattr(PV.KIMI, gone), gone)

    def test_choices_and_public_view(self):
        """v2.10h：K2.6 删掉（用户 10-21：没有自带的搜索），只剩 K3，默认也是 K3。"""
        self.assertEqual(PV.PROVIDERS["kimi"]["models"], ("kimi-k3",))
        self.assertEqual(PV.PROVIDERS["kimi"]["default_model"], "kimi-k3")
        self.assertNotIn("kimi-k2.6", PV.MODELS)
        self.assertEqual(PV.MODELS["kimi-k3"]["max_output"], 1_048_576)
        sp = spec(thinking="medium", region="cn", usd_cap=5)
        self.assertEqual(sp.public(), {"provider": "kimi", "model": "kimi-k3", "region": "cn", "thinking": "medium",
                                       "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high", "*": "low"},
                                       "usd_cap": 5.0, "byok": True, "price_id": "kimi-k3@cn",
                                       "fx": {"cny_per_usd": 6.7192, "source": config.CNY_PER_USD_SOURCE, "date": "2026-10-21"}})
        self.assertEqual(spec().public(), {"provider": "kimi", "model": "kimi-k3", "region": "global", "thinking": "low",
                                           "thinking_by_role": {"plan": "low", "judge": "low", "repair": "low", "*": "low"},
                                           "usd_cap": 3.0, "byok": True})
        self.assertNotIn(KEY, repr(sp))
        for bad in (lambda: spec(region="us"), lambda: PV.ModelSpec("kimi", "gpt-6-luna", KEY),
                    lambda: PV.ModelSpec("moonshot", "kimi-k3", KEY, thinking="low"),
                    lambda: PV.ModelSpec("kimi", "kimi-k2.6", KEY)):
            with self.assertRaises(PV.SpecError):
                bad()
        with mock.patch.dict(config.PRICES), self.assertRaises(config.UnknownModel):   # 某个区域没有价格就拒跑
            del config.PRICES["kimi-k3@cn"]
            spec(region="cn")


class TestRunWithKimiSpec(_FakeServerCase):
    """prepare_run(spec=Kimi 国内站 K3) -> 图 -> save_run，全部对着假服务：规划一步收到 429 exceeded_current_quota_error 就干净停下；
    state.json 记 provider、price_id 和汇率，不记 key（v2.10h 起也不再记 search_queries）；结果目录里没有 key；写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop(self):
        from triangulate.agent import run as R
        sp = spec(thinking="high", region="cn", usd_cap=1.5)
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
        self.assertNotIn("search_queries", st["settings"])
        self.assertEqual(st["budget"]["usd_cap"], 1.5)
        files = list((self.tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            self.assertNotIn(KEY, f.read_text(encoding="utf-8"), f.name)
        self.assertFalse(sp.has_key)


if __name__ == "__main__":
    unittest.main()
