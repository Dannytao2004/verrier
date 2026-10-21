"""v2.10e：GLM adapter（Z.ai 国际站 api.z.ai / 智谱开放平台国内站 open.bigmodel.cn）。全部对着 127.0.0.1 上的假服务
（tests/fake_glm.py）跑：真实走 urllib + urlopen_no_redirect，请求头、请求体、HTTPError 的 body 都是真的；不联网、不需要真 key、
不读 key 文件。

JSON 调用：OpenAI 兼容的非流式 Chat Completions；搜索：一次 JSON 调用生成查询词 + 每个查询词 POST /web_search。
每一项对照的官方文档写在各个测试的说明里（链接见 PROVIDERS.md 第 12 节）。
"""
import http.client
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import fake_glm as FG
from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import prompts as PR
from triangulate.agent import search as S

KEY = "0123456789abcdef0123456789abcdef.GLMuserSecret01"   # 形状同 GLM 的 key（id.secret）
SYSTEM = "You are a careful analyst. Reply with one JSON object."
MSGS = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "Estimate widgets in June 2026. Reply {\"a\": 1}."}]
BRIEF = "Find official widget statistics for June 2026.\n\nAfter searching, reply with at most 4 URLs, most useful first."
FX = config.CNY_PER_USD
EXTRA = config.THINKING_EXTRA_TOKENS


def spec(model="glm-5.2", thinking="off", key=KEY, **kw):
    return PV.ModelSpec("glm", model, key, thinking=thinking, **kw)


def ok(content='{"a": 1}', **kw):
    return ("json", 200, FG.completion(content, **kw))


def queries_reply(*qs, **kw):
    return ok(json.dumps({"queries": list(qs)}), **kw)


def results(*urls):
    return ("json", 200, FG.search_results(*urls))


def err(status, code, message, wrapped=True, headers=None):
    item = ("json", status, FG.error_body(code, message, wrapped=wrapped))
    return item + (headers,) if headers else item


class _FakeServerCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = FG.FakeGLM()

    @classmethod
    def tearDownClass(cls):
        cls.fake.close()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.sleeps = []
        patches = [mock.patch.object(PV.GLMAdapter, "regions", self.fake.regions()),
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
            s = t if isinstance(t, str) else json.dumps(t, default=str, ensure_ascii=False)
            self.assertNotIn(KEY, s)
            self.assertNotIn(KEY.split(".")[1], s)


class TestChatRequest(_FakeServerCase):
    def test_chat_completions_request(self):
        """Chat Completion API：POST {base}/chat/completions（通用端点 /api/paas/v4，不是 Coding Plan 的 /api/coding/paas/v4），
        Authorization: Bearer；response_format json_object（enum 只有 text / json_object）；max_tokens（没有 max_completion_tokens）；
        非流式（stream false）。temperature / top_p / do_sample 不发：默认 temperature 1.0、top_p 0.95 就是官方推荐值（迁移指南：
        两个只调一个）。GLM-5.2 关思考：thinking {"type": "disabled"}，不发 reasoning_effort（只在 enabled 时生效）。"""
        out, seen, log = self.chat(ok())
        self.assertEqual(out, ({"a": 1}, '{"a": 1}', None))
        r = seen[0]
        self.assertEqual((r["method"], r["path"]), ("POST", "/api/paas/v4/chat/completions"))
        self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual(r["headers"]["content-type"], "application/json")
        for h in ("x-api-key", "anthropic-version"):
            self.assertNotIn(h, r["headers"])
        b = r["body"]
        self.assertEqual(list(b), ["model", "messages", "thinking", "response_format", "max_tokens", "stream"])
        self.assertEqual((b["model"], b["messages"]), ("glm-5.2", MSGS))   # GLM 收 system 角色，原样
        self.assertEqual((b["thinking"], b["response_format"], b["max_tokens"], b["stream"]),
                         ({"type": "disabled"}, {"type": "json_object"}, 12000, False))
        for banned in ("temperature", "top_p", "do_sample", "max_completion_tokens", "reasoning_effort", "tools", "tool_choice",
                       "stream_options", "request_id", "user_id", "store"):
            self.assertNotIn(banned, b)
        self.assertNotIn("thinking", log[0])
        self.assertEqual((log[0]["model"], log[0]["ok"]), ("glm-5.2", True))

    def test_thinking_per_model_and_role(self):
        """Deep Thinking 指南 / Chat Completion API（ChatThinking、reasoning_effort）：
        GLM-5.3：只能 enabled（disabled 报错），reasoning_effort 只有 low / high / max（默认 max）；网页 low -> low、medium -> high、
        high -> max，plan / judge / repair 以外用 low（迁移提示：原来 disabled 的改成 enabled + low）。
        GLM-5.2：能 disabled；reasoning_effort 的 low / medium 映射成 high、xhigh 映射成 max：网页 low、medium 发 high，high 发 max。
        GLM-4.7 系列：enabled（强制思考）/ disabled，没有 reasoning_effort。开思考的调用 max_tokens +24,000。"""
        dis, en = {"type": "disabled"}, {"type": "enabled"}
        cases = [  # (模型, 网页档位, arm, thinking, reasoning_effort, 有没有思考余量)
            ("glm-5.3", "low", "plan", en, "low", True),
            ("glm-5.3", "medium", "judge:r1", en, "high", True),
            ("glm-5.3", "high", "judge:r2:repair", en, "max", True),
            ("glm-5.3", "high", "extract:d1", en, "low", True),
            ("glm-5.3", "medium", "final", en, "low", True),
            ("glm-5.2", "off", "plan", dis, None, False),
            ("glm-5.2", "low", "plan", en, "high", True),
            ("glm-5.2", "medium", "judge:r1", en, "high", True),
            ("glm-5.2", "high", "judge:r2:repair", en, "max", True),
            ("glm-5.2", "high", "audit", dis, None, False),
            ("glm-4.7-flashx", "off", "judge:r1", dis, None, False),
            ("glm-4.7-flashx", "low", "plan", en, None, True),
            ("glm-4.7-flashx", "high", "judge:r1", en, None, True),
            ("glm-4.7-flashx", "high", "extract:d1", dis, None, False),
        ]
        for model, level, arm, thinking, effort, extra in cases:
            with self.subTest(model=model, level=level, arm=arm):
                _, seen, log = self.chat(ok(), sp=spec(model, level), arm=arm, max_tokens=4000)
                b = seen[0]["body"]
                self.assertEqual(b["thinking"], thinking)
                self.assertEqual(b.get("reasoning_effort"), effort)
                if effort is None:
                    self.assertNotIn("reasoning_effort", b)
                self.assertEqual(list(b)[:3], ["model", "messages", "thinking"])
                self.assertEqual(b["max_tokens"], 4000 + (EXTRA if extra else 0))
                self.assertEqual(log[0].get("thinking"), (effort or "enabled") if extra else None)
        self.assertEqual(PV.thinking_levels("glm-5.3"), ("low", "medium", "high"))
        self.assertEqual(PV.thinking_levels("glm-5.2"), ("off", "low", "medium", "high"))
        self.assertEqual(PV.thinking_levels("glm-4.7-flashx"), ("off", "low", "medium", "high"))
        self.assertFalse(PV.MODELS["glm-4.7-flashx"]["thinking_depth"])   # 网页把 low / medium / high 合并成「开」
        with self.assertRaises(PV.SpecError):
            spec("glm-5.3", "off")
        with self.assertRaises(ValueError):   # 防御：5.3 不会发 disabled
            PV.GLM.chat_request("glm-5.3", KEY, MSGS, max_tokens=10, effort=None)
        self.assertEqual(spec("glm-5.3", "high").thinking_by_role(), {"plan": "max", "judge": "max", "repair": "max", "*": "low"})
        self.assertEqual(spec("glm-5.2", "low").thinking_by_role(), {"plan": "high", "judge": "high", "repair": "high"})
        self.assertEqual(spec("glm-4.7-flashx", "medium").thinking_by_role(),
                         {"plan": "enabled", "judge": "enabled", "repair": "enabled"})

    def test_headroom_is_capped_at_the_models_max_output(self):
        """Core Parameters：max_tokens 最大 131,072（三个模型相同）。"""
        _, seen, _ = self.chat(ok(), sp=spec("glm-5.3", "low"), arm="plan", max_tokens=120_000)
        self.assertEqual(seen[0]["body"]["max_tokens"], 131_072)
        self.assertEqual({m: PV.MODELS[m]["max_output"] for m in PV.PROVIDERS["glm"]["models"]},
                         dict.fromkeys(PV.PROVIDERS["glm"]["models"], 131_072))

    def test_region_and_messages(self):
        """国内站的请求发到国内站的地址（假服务上是 /cn/...）。messages 原样发：文档没要求 assistant 的 content 非空（不像 Kimi /
        Claude），所以 AgentLLM.ask 重问时的空 assistant 消息照原样发。"""
        _, seen, _ = self.chat(ok(), sp=spec(region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/api/paas/v4/chat/completions")
        empty = MSGS + [{"role": "assistant", "content": ""}, {"role": "user", "content": "Reply again with one valid JSON object."}]
        _, seen, _ = self.chat(ok(), msgs=empty)
        self.assertEqual(seen[0]["body"]["messages"], empty)


class TestChatReply(_FakeServerCase):
    def test_reply_without_the_reasoning(self):
        """Deep Thinking 指南的回复示例：最终答案在 message.content，思考在 message.reasoning_content；只解析 content，思考内容不进
        返回值、不进日志。"""
        content = '{"answer": "widgets", "n": 3, "notes": "x"}'
        out, _, log = self.chat(ok(content, reasoning="SECRET-REASONING about widgets"))
        self.assertEqual(out, ({"answer": "widgets", "n": 3, "notes": "x"}, content, None))
        self.assertNotIn("SECRET-REASONING", json.dumps(log))

    def test_usage_is_metered_with_cache_hits(self):
        """usage：prompt_tokens 是全部输入，prompt_tokens_details.cached_tokens 是其中命中缓存的（按 Cached Input 价），其余按 Input 价，
        completion_tokens 按 Output 价。国际站 GLM-5.3 / 5.2：$1.4 / cached $0.26 / $4.4；4.7-FlashX：$0.07 / $0.01 / $0.4。
        国内站：GLM-5.3 ¥8 / ¥2 / ¥28，4.7-FlashX ¥0.5 / ¥0.1 / ¥3，按 2026-10-21 中间价 6.7192 折成 USD。"""
        u = FG.usage(prompt=12_000, completion=900, cached=4_000)
        cases = [(spec("glm-5.3", "low"), (8_000 * 1.4 + 4_000 * 0.26 + 900 * 4.4) / 1e6),
                 (spec("glm-5.2"), (8_000 * 1.4 + 4_000 * 0.26 + 900 * 4.4) / 1e6),
                 (spec("glm-4.7-flashx"), (8_000 * 0.07 + 4_000 * 0.01 + 900 * 0.4) / 1e6),
                 (spec("glm-5.3", "low", region="cn"), (8_000 * 8 + 4_000 * 2 + 900 * 28) / 1e6 / FX),
                 (spec("glm-4.7-flashx", region="cn"), (8_000 * 0.5 + 4_000 * 0.1 + 900 * 3) / 1e6 / FX)]
        for sp, want in cases:
            with self.subTest(model=sp.model, region=sp.region):
                _, _, log = self.chat(ok(use=u), sp=sp)
                rec = log[0]
                self.assertAlmostEqual(rec["usd"], round(want, 6))
                self.assertEqual((rec["finish_reason"], rec["prompt_tokens"], rec["cached_tokens"], rec["completion_tokens"]),
                                 ("stop", 12_000, 4_000, 900))
                self.assertNotIn("reasoning_tokens", rec)   # API 参考的 usage 没有这个字段：没有就不记
                self.assertEqual(rec["model"], sp.model)    # 日志里是模型名；计价 id 只用来查价格
        self.assertAlmostEqual(PV.glm_usage_cost({"prompt_tokens": 1000, "completion_tokens": 10}, "glm-5.2"),
                               (1000 * 1.4 + 10 * 4.4) / 1e6)   # 没有 prompt_tokens_details：全按 input 价
        u2 = {**FG.usage(), "completion_tokens_details": {"reasoning_tokens": 120}}
        _, _, log = self.chat(ok(use=u2))
        self.assertEqual(log[0]["reasoning_tokens"], 120)

    def test_finish_reasons(self):
        """finish_reason（API 参考：stop / tool_calls / length / sensitive / model_context_window_exceeded / network_error）：
        length、model_context_window_exceeded = 输出没写完，报截断（不解析）；sensitive = 被内容安全审核拦截；其余照原样报，不解析。"""
        for fr in ("length", "model_context_window_exceeded"):
            with self.subTest(finish_reason=fr):
                out, seen, log = self.chat(ok('{"a": ', finish_reason=fr))
                self.assertEqual(out, (None, '{"a": ', f"reply was truncated (finish_reason={fr})"))
                self.assertEqual((log[0]["error"], log[0]["finish_reason"], len(seen)), ("truncated", fr, 1))
        out, _, log = self.chat(ok(finish_reason="sensitive"))
        self.assertEqual(out[2], "reply was stopped by content moderation (finish_reason=sensitive)")
        self.assertEqual(log[0]["error"], "sensitive")
        for fr in ("network_error", "tool_calls", None):
            with self.subTest(finish_reason=fr):
                out, seen, log = self.chat(ok(finish_reason=fr))
                self.assertEqual((out[0], out[2], len(seen)), (None, f"reply ended with finish_reason={fr}", 1))
                self.assertEqual(log[0]["error"], "unexpected_finish")

    def test_json_is_not_repaired_and_bad_bodies_are_retried(self):
        """用户决定 4：不做 JSON 修补（不剥代码块）。回复的骨架不对（没有 choices、message 不是对象）按 bad_response_body 重试。"""
        out, _, log = self.chat(ok('```json\n{"a": 1}\n```'))
        self.assertEqual((out[0], out[2]), (None, "reply is not valid JSON"))
        self.assertEqual(log[0]["error"], "invalid_json")
        out, _, _ = self.chat(ok("[1, 2]"))
        self.assertEqual(out[2], "reply is not a JSON object")
        out, seen, log = self.chat(("json", 200, {"id": "x", "choices": []}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual((log[0]["error"], log[0]["will_retry"]), ("bad_response_body", True))
        out, seen, _ = self.chat(*[("json", 200, {"choices": [{"index": 0, "message": "x"}]})] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual(len(seen), 3)


class TestChatErrors(_FakeServerCase):
    def test_balance_stops_without_retrying(self):
        """错误码页（两站）：HTTP 429 + 业务码 1113 = 余额不足或没有资源包（国内站：账户已欠费），重试没用 -> BalanceExhausted，
        不重试。错误 body 两种形状都认：错误码页的 {"error": {"code": "1113"}}（字符串）和 API 参考 Error schema 的 {"code": 1113}
        （整数、没有外层 error）。"""
        bodies = [err(429, 1113, "Insufficient balance or no resource package. Please recharge."),
                  err(429, 1113, "您的账户已欠费，请充值后重试", wrapped=False),
                  err(429, 1113, "Insufficient balance", headers={"Retry-After": "5"})]
        for item in bodies:
            with self.subTest(body=item[2]):
                out, seen, log = self.chat(item)
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertIsInstance(out, llm.TransportError)
                self.assertEqual(len(seen), 1)
                self.assertTrue(str(out).startswith("insufficient balance: GLM HTTP 429 code 1113 (insufficient balance or no "
                                                    "resource package) (judge:r1 t attempt 1); the run was stopped"), str(out))
                self.assertIn("z.ai/manage-apikey/billing or bigmodel.cn", str(out))
                self.assertNotIn("recharge", str(out))   # 不含服务端原文
                self.assertNotIn("欠费", str(out))
                self.assertEqual(log[0]["error"], "http_429")
                self.assertEqual(self.sleeps, [])
                self.assertNoKeyIn(str(out), log)

    def test_usage_limit_and_plan_codes_also_stop(self):
        """错误码页：1308 / 1310 / 1316–1321 是用量上限（要到服务端给的重置时间才恢复），1309 / 1311 / 1314 / 1315 是套餐过期、
        套餐不含这个模型、套餐类型的 key：重试都没用，整次运行停下；套餐类的说明里提示要用 Standard API Key。
        v2.10f：这两类的说明开头不写成 insufficient balance（审查发现）；1313（公平使用策略的频率限制）按限流重试。"""
        for code in ("1308", "1310", "1316", "1317", "1318", "1319", "1320", "1321"):
            with self.subTest(code=code):
                out, seen, _ = self.chat(err(429, code, "Usage limit reached"))
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertEqual(len(seen), 1)
                self.assertTrue(str(out).startswith(f"usage limit reached: GLM HTTP 429 {PV.GLM_LIMIT_CODES[code]}"), str(out))
                self.assertNotIn("insufficient balance", str(out))
        for code in ("1309", "1311", "1314", "1315"):
            with self.subTest(code=code):
                out, seen, _ = self.chat(err(429, code, "Your GLM Coding Plan package has expired"))
                self.assertIsInstance(out, llm.BalanceExhausted)
                self.assertEqual(len(seen), 1)
                self.assertTrue(str(out).startswith("key or plan not accepted: GLM HTTP 429 code"), str(out))
                self.assertIn("this app needs a Standard API Key", str(out))
        self.assertEqual(self.sleeps, [])
        self.assertNotIn("1313", PV.GLM_BALANCE_CODES)
        self.assertNotIn("1313", PV.GLM_LIMIT_CODES)
        fair = "Request frequency limited under the fair usage policy"
        out, seen, _ = self.chat(err(429, 1313, fair), ok())   # 1313：限流，退避后重试成功
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertEqual(self.sleeps, [2])
        self.sleeps.clear()
        out, seen, log = self.chat(*[err(429, 1313, fair)] * 3)   # 3 次仍是 1313：传输错误（照原样报），不是余额不足
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertIn(f"(code 1313: {fair})", str(out))
        self.assertEqual(PV.GLM.stop_prefix("HTTP 429 " + PV.GLM_BALANCE_CODES["1113"]),
                         "insufficient balance")

    def test_rate_limits_and_overload_are_retried(self):
        """429 的 1302（限流）、1305（过载）是临时的：退避重试（服务端给了 Retry-After 就至少等那么久）；500 的 1234（网络错误）同样重试。
        3 次仍失败报传输错误，异常文字带业务码和 message（GLM 的错误没有 type：「(code 1305: ...)」）。"""
        out, seen, _ = self.chat(err(429, 1302, "Rate limit reached for requests", headers={"Retry-After": "7"}), ok())
        self.assertEqual((out[0], len(seen)), ({"a": 1}, 2))
        self.assertIn(7.0, self.sleeps)
        self.sleeps.clear()
        out, seen, _ = self.chat(err(500, 1234, "Network error, error id: x, please try again later"), ok())
        self.assertEqual((out[0], len(seen), self.sleeps), ({"a": 1}, 2, [2]))
        over = "The service may be temporarily overloaded, please try again later"
        out, seen, log = self.chat(*[err(429, 1305, over, wrapped=False)] * 3)
        self.assertIsInstance(out, llm.TransportError)
        self.assertNotIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 3)
        self.assertIn(f"http_429 (code 1305: {over})", str(out))
        self.assertEqual((log[-1]["server_error_code"], log[-1]["server_error"]), ("1305", over))
        self.assertNotIn("server_error_type", log[-1])

    def test_other_errors_are_reported_as_they_are(self):
        """400（1210 / 1214 参数不对、1211 模型不存在、1261 prompt 超长、1301 内容安全）不重试、不当成余额问题；业务码和 message 前
        200 字进日志和异常文字。401 / 403（1000 / 1001 / 1220）= key 被拒，不读 body。"""
        cases = [(400, 1214, "Parameter `reasoning_effort` is invalid. Please check the documentation.", True),
                 (400, 1211, "Unknown Model, please check the model code.", False),
                 (400, 1261, "Prompt too long", True),
                 (400, 1301, "System detected potentially unsafe or sensitive content in input or generation.", True)]
        for status, code, msg, wrapped in cases:
            with self.subTest(code=code):
                out, seen, log = self.chat(err(status, code, msg, wrapped=wrapped))
                self.assertIsInstance(out, llm.TransportError)
                self.assertNotIsInstance(out, llm.BalanceExhausted)
                self.assertEqual(len(seen), 1)
                self.assertEqual((log[0]["error"], log[0]["server_error_code"], log[0]["server_error"]),
                                 (f"http_{status}", str(code), msg))
                self.assertIn(f"(code {code}: {msg})", str(out))
        for status, body in ((401, FG.REAL_401_FAKE_KEY), (401, FG.REAL_401_FAKE_KEY_CN),
                             (403, FG.error_body(1220, "You do not have permission to access API"))):
            with self.subTest(status=status), mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
                out, _, log = self.chat(("json", status, body))
                rb.assert_not_called()
                self.assertIsInstance(out, llm.KeyRejected)
                # v2.10f：403 不一定是 key 错了：写成「key 或这个请求被拒」（GLM 的 403 不读 body）
                self.assertEqual(str(out), "GLM rejected the API key (HTTP 401)" if status == 401
                                 else "GLM rejected the API key or the request (HTTP 403)")
                self.assertNotIn("server_error", log[0])

    def test_error_body_shapes(self):
        """glm_error：两种形状、字符串 / 整数 code 都认；不是 JSON、没有 code 和 message 的返回 None。"""
        self.assertEqual(PV.glm_error(b'{"error":{"code":"1214","message":"bad"}}'), ("1214", "bad"))
        self.assertEqual(PV.glm_error(b'{"code":1214,"message":"bad"}'), ("1214", "bad"))
        self.assertEqual(PV.glm_error(b'{"error":{"message":"no code"}}'), (None, "no code"))
        for raw in (b"", b"<html>", b"[1]", b'{"id": "x"}'):
            self.assertIsNone(PV.glm_error(raw))
        self.assertIsNone(PV.GLM.balance_exhausted(429, b'{"error":{"message":"no code"}}'))
        self.assertIsNone(PV.GLM.balance_exhausted(400, b'{"error":{"code":"1113","message":"x"}}'))   # 只认 429
        self.assertEqual(llm.server_error_detail({"server_error_code": "1214", "server_error": "bad"}), " (code 1214: bad)")
        # 其余 provider 的说明文字不变（有 server_error_type 这个键）
        self.assertEqual(llm.server_error_detail({"server_error_type": "", "server_error_code": "x", "server_error": "m"}), "")

    def test_redirects_are_not_followed(self):
        out, seen, _ = self.chat(("redirect", 301, self.fake.url("/api/coding/paas/v4/chat/completions")))
        self.assertIsInstance(out, llm.TransportError)
        self.assertEqual([r["path"] for r in seen], ["/api/paas/v4/chat/completions"])


class TestGLMCost(unittest.TestCase):
    """Pricing 页（国际站 USD：https://docs.z.ai/guides/overview/pricing；国内站 CNY：https://docs.bigmodel.cn/cn/guide/start/pricing，
    2026-10-21）。搜索：国际站 Built-in Tools 的 Web Search $0.01 / use，国内站 Search-Std ¥0.01 / 次。"""

    def test_prices_match_the_pricing_pages(self):
        want = {"glm-5.3": ("USD", (0.26, 1.4, 4.4)), "glm-5.2": ("USD", (0.26, 1.4, 4.4)),
                "glm-4.7-flashx": ("USD", (0.01, 0.07, 0.4)), "glm-5.3@cn": ("CNY", (2, 8, 28)),
                "glm-5.2@cn": ("CNY", (2, 8, 28)), "glm-4.7-flashx@cn": ("CNY", (0.1, 0.5, 3))}
        for pid, (cur, listed) in want.items():
            with self.subTest(price_id=pid):
                p = config.price(pid)
                r = 1.0 if cur == "USD" else 1 / FX
                self.assertEqual((p["provider"], p["currency"], p["prompt_cache"], p["checked"]), ("glm", cur, "implicit", "2026-10-21"))
                self.assertEqual((p["listed"]["hit"], p["listed"]["miss"], p["listed"]["out"], p["listed"]["search_fee"]),
                                 (*listed, 0.01))
                for got, base in zip(p["peak"], listed):
                    self.assertAlmostEqual(got, base * r)
                self.assertEqual(p["peak"], p["offpeak"])
                self.assertAlmostEqual(p["search_fee_usd"], 0.01 * r)
                self.assertNotIn("cache_write_5m", p)   # 隐式缓存，没有写入价
                self.assertEqual(p["source"], config.GLM_PRICING if cur == "USD" else config.GLM_PRICING_CN)
                self.assertEqual("fx" in p, cur == "CNY")

    def test_directions_scale_with_glm_prices(self):
        """「一个方向」的估价：GLM 自动缓存，但这个 agent 的命中率没测过，输入全按 input 价算，加 4 次 × 每次搜索费。
        $2 上限：国际站 5.3 / 5.2 9 个方向，4.7-FlashX 10 个；国内站（折算后更便宜）都是 10 个（页数上限 40 / 4）。"""
        pr = P.Budget.DIRECTION_PROFILE

        def cost(m):
            p = config.price(m)
            hit, miss, out = p["peak"]
            if m.startswith("glm"):
                hit = miss
            fee = p.get("search_fee_usd", 0.01)
            return (pr["hit"] * hit + pr["miss"] * miss + pr["out"] * out) / 1e6 + pr["searches"] * fee
        flash = cost("deepseek-flash")
        ids = ("glm-5.3", "glm-5.2", "glm-4.7-flashx", "glm-5.3@cn", "glm-5.2@cn", "glm-4.7-flashx@cn")
        for m in ids:
            with self.subTest(price_id=m):
                self.assertAlmostEqual(P.Budget.typical_direction_usd(m), 0.06 * cost(m) / flash)
        self.assertEqual({m: P.Budget.for_model(m, usd=2.0).directions for m in ids},
                         {"glm-5.3": 9, "glm-5.2": 9, "glm-4.7-flashx": 10, "glm-5.3@cn": 10, "glm-5.2@cn": 10,
                          "glm-4.7-flashx@cn": 10})
        self.assertEqual(P.Budget().directions, 10)   # DeepSeek 默认路径不变

    def test_reservations_and_the_context_budget(self):
        """预扣：输入按 input 价（没有写入价）；国内站按折算后的价格。Context 按 spec.price_id 计价；搜索的预扣按「生成查询词」那次调用
        发出的 max_tokens（5.3 永远在想：+24,000）加 (2 × max_uses + 2) 次搜索费。"""
        # v2.10f：别家的 tokenizer 没测过，输入按 1 个字符 1 个 token 预扣（DeepSeek 照旧 2 个字符）
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "glm-5.3"), (100_000 * 1.4 + 1000 * 4.4) / 1e6)
        self.assertAlmostEqual(P.Budget.llm_reserve(100_000, 1000, "glm-5.3@cn"), (100_000 * 8 + 1000 * 28) / 1e6 / FX)
        ctx = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("glm-5.3", "high", region="cn"))
        self.assertEqual((ctx.budget.model, ctx.budget.usd_cap), ("glm-5.3@cn", 2.0))
        self.assertEqual(ctx.budget.search_tokens, S.SEARCH_QUERIES_MAX_TOKENS + EXTRA)
        self.assertAlmostEqual(ctx.budget.search_reserve(),
                               (30_000 * 8 + ctx.budget.search_tokens * 28) / 1e6 / FX + 8 * 0.01 / FX)
        ctx2 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("glm-5.2", "high"))
        self.assertEqual(ctx2.budget.search_tokens, S.SEARCH_QUERIES_MAX_TOKENS)   # 搜索不是 plan / judge / repair：5.2 关思考
        self.assertAlmostEqual(ctx2.budget.search_reserve(), (30_000 * 1.4 + 2000 * 4.4) / 1e6 + 8 * 0.01)

    def test_search_fee_by_region(self):
        self.assertAlmostEqual(PV.search_fee_usd("glm-5.2"), 0.01)
        self.assertAlmostEqual(PV.search_fee_usd("glm-5.3@cn"), 0.01 / FX)
        self.assertEqual(spec("glm-5.3", "low", region="cn").price_id, "glm-5.3@cn")
        self.assertEqual(spec().price_id, "glm-5.2")


class TestGLMSearch(_FakeServerCase):
    QS = ("widgets June 2026 national statistics office", "widget production 2025 annual report", "widget exports customs data")

    def test_queries_then_web_search(self):
        """同 Kimi：一次 JSON 调用（SEARCH_QUERIES_* 包着同一段搜索 prompt）生成查询词，再逐个 POST {base}/web_search（Web Search API：
        国际站 search_engine 必填、enum 只有 search-prime；search_query 必填；count 1–50，默认 10）。搜索不是 plan / judge / repair：
        5.2 关思考。结果的 link（和 title）按名次交替合并。"""
        a1, a2, b1, c1 = (f"https://{h}.example.org/w" for h in ("a1", "a2", "b1", "c1"))
        out, seen, log = self.search(queries_reply(*self.QS), results(a1, a2), results(b1, a1), results(c1))
        q = seen[0]
        self.assertEqual((q["method"], q["path"]), ("POST", "/api/paas/v4/chat/completions"))
        self.assertEqual(q["body"]["messages"], [{"role": "system", "content": PR.SEARCH_QUERIES_SYSTEM},
                                                 {"role": "user", "content": PR.SEARCH_QUERIES_USER.format(n=3, brief=BRIEF)}])
        self.assertEqual((q["body"]["thinking"], q["body"]["max_tokens"], q["body"]["response_format"]),
                         ({"type": "disabled"}, S.SEARCH_QUERIES_MAX_TOKENS, {"type": "json_object"}))
        self.assertEqual(len(seen), 4)
        for r, text in zip(seen[1:], self.QS):
            self.assertEqual((r["method"], r["path"]), ("POST", "/api/paas/v4/web_search"))
            self.assertEqual(r["headers"]["authorization"], f"Bearer {KEY}")
            self.assertEqual(r["body"], {"search_engine": "search-prime", "search_query": text, "count": 4})
        self.assertEqual(out["urls"], [a1, b1, c1, a2])
        self.assertEqual(out["queries"], list(self.QS))
        self.assertEqual((out["web_search_requests"], out["n_result_urls"], out["n_text_urls"]), (3, 5, 0))
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.03)
        self.assertAlmostEqual(out["usd"], (1000 * 1.4 + 300 * 4.4) / 1e6)
        self.assertNotIn("Title of", json.dumps(out))   # 标题解析出来但不往外传
        self.assertNotIn("error", out)
        self.assertEqual(log[0]["arm"], "search:d1:queries")
        for i, rec in enumerate(log[1:], 1):
            self.assertEqual((rec["arm"], rec["kind"], rec["query_n"], rec["ok"], rec["web_search_requests"], rec["usd"],
                              rec["usd_search_fee_assumed"]), ("search:d1", "search", i, True, 1, 0.0, 0.01))
        self.assertNoKeyIn(out, log)

    def test_china_endpoint_and_query_length(self):
        """国内站 Web Search API：search_query（必填，maxLength 70，建议不超过 70 个字符）、search_engine（必填，search_std = 基础版
        ¥0.01 / 次）、search_intent（必填；false = 跳过意图识别、直接搜）、count。超过 70 个字符的查询词截到 70 以内（按空格；中文直接截）。
        5.3 的查询词调用用 low（永远在想，+24,000 余量）。"""
        long_en = "official widget production statistics June 2026 national bureau monthly release table"   # 85 个字符
        long_zh = "国家统计局" * 20
        out, seen, log = self.search(queries_reply(long_en, long_zh, "widgets 2026"), *[results("https://a.example.org/w")] * 3,
                                     sp=spec("glm-5.3", "high", region="cn"))
        self.assertEqual([r["path"] for r in seen], ["/cn/api/paas/v4/chat/completions"] + ["/cn/api/paas/v4/web_search"] * 3)
        b = seen[0]["body"]
        self.assertEqual((b["thinking"], b["reasoning_effort"], b["max_tokens"]),
                         ({"type": "enabled"}, "low", S.SEARCH_QUERIES_MAX_TOKENS + EXTRA))
        bodies = [r["body"] for r in seen[1:]]
        # 前 70 个字符停在 "monthly" 中间（加上 "monthly" 是 71 个），截到它前面的空格
        self.assertEqual(bodies[0], {"search_query": "official widget production statistics June 2026 national bureau",
                                     "search_engine": "search_std", "search_intent": False, "count": 4})
        self.assertEqual(bodies[1]["search_query"], long_zh[:70])
        self.assertEqual(bodies[2]["search_query"], "widgets 2026")
        self.assertTrue(all(len(x["search_query"]) <= 70 for x in bodies))
        self.assertEqual(out["queries"], [long_en, long_zh, "widgets 2026"])   # 返回的是生成的查询词（进 state.json 审计）
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 3 * 0.01 / FX)
        self.assertEqual(log[0]["thinking"], "low")
        self.assertEqual(PV.GLM.tools_search_request(KEY, long_en, limit=4, region="global")[1]["search_query"], long_en)
        self.assertEqual([PV.GLM.tools_search_request(KEY, "q", limit=n)[1]["count"] for n in (0, 4, 80)], [1, 4, 50])

    def test_billing_and_failures(self):
        """国内站价格页：搜索工具按实际调用次数计费（国际站价格页按次）。文档没说空结果免费，所以每个 HTTP 200 都按一次记（含空结果、
        形状不对的），失败的请求不记。一个查询词失败不影响其余的，失败原因合在 error 里（400 的业务码和 message 照原样）。"""
        x = "https://x.example.org/w"
        out, seen, log = self.search(queries_reply(*self.QS), ("json", 200, {"id": "s", "search_result": []}),
                                     err(400, 1214, "Parameter count is invalid. Please check the documentation."), results(x))
        self.assertEqual((out["urls"], out["web_search_requests"], len(seen)), ([x], 2, 4))
        self.assertAlmostEqual(out["usd_search_fee_assumed"], 0.02)
        self.assertEqual(out["error"], "query 2: http_400 (code 1214: Parameter count is invalid. Please check the documentation.)")
        self.assertEqual((log[1]["web_search_requests"], log[1]["usd_search_fee_assumed"], log[1]["n_result_urls"]), (1, 0.01, 0))
        self.assertEqual((log[2]["ok"], log[2]["error"], log[2]["server_error_code"]), (False, "http_400", "1214"))
        self.assertNotIn("usd", log[2])
        out, _, log = self.search(queries_reply("q1"), ("json", 200, {"id": "s"}), max_uses=1)
        self.assertEqual((out["urls"], out["error"], out["web_search_requests"]), ([], "query 1: bad_response_body", 1))
        self.assertEqual((log[1]["error"], log[1]["usd"], log[1]["usd_search_fee_assumed"]), ("bad_response_body", 0.0, 0.01))

    def test_rejected_key_rate_limits_and_balance_on_the_search_endpoint(self):
        """搜索接口的 401：不读 body、不抛，记 http_401（同其他 provider 的搜索）。429 1302 重试；429 1113：整次运行停下。"""
        with mock.patch.object(llm, "read_error_body", wraps=llm.read_error_body) as rb:
            out, seen, _ = self.search(queries_reply("q1"), ("json", 401, FG.REAL_401_FAKE_KEY), max_uses=1)
            rb.assert_not_called()
        self.assertEqual((out["urls"], out["error"], len(seen)), ([], "query 1: http_401", 2))
        out, seen, _ = self.search(queries_reply("q1"), err(429, 1302, "Rate limit reached for requests"),
                                   results("https://a.example.org/w"), max_uses=1)
        self.assertEqual((len(seen), out["urls"], self.sleeps), (3, ["https://a.example.org/w"], [3]))
        self.sleeps.clear()
        out, seen, log = self.search(queries_reply("q1", "q2"), err(429, 1113, "Insufficient balance or no resource package."))
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertTrue(str(out).startswith("insufficient balance: GLM HTTP 429 code 1113"), str(out))
        self.assertIn("(search:d1 t); the run was stopped without retrying.", str(out))
        self.assertEqual((len(seen), self.sleeps), (2, []))
        self.assertNoKeyIn(str(out), log)
        out, seen, _ = self.search(err(429, 1113, "Insufficient balance"))   # 生成查询词那一步就没钱了
        self.assertIsInstance(out, llm.BalanceExhausted)
        self.assertEqual(len(seen), 1)

    def test_query_generation_failures_mean_no_search(self):
        """生成查询词只调一次，失败就没有 URL（不修 JSON、不补查询词），error 以 "queries:" 开头，不发搜索请求。"""
        cases = [(ok("not json"), "queries: reply is not valid JSON"),
                 (ok('{"q": ["a"]}'), 'queries: the reply has no "queries" list'),
                 (ok('{"queries": ["a"', finish_reason="length"), "queries: reply was truncated (finish_reason=length)"),
                 (ok('{"queries": ["a"]}', finish_reason="sensitive"),
                  "queries: reply was stopped by content moderation (finish_reason=sensitive)"),
                 (err(400, 1210, "Invalid API parameter, please check the documentation."),
                  "queries: search:d1:queries t attempt 1: http_400 (code 1210: Invalid API parameter, please check the documentation.)"),
                 (("json", 401, FG.REAL_401_FAKE_KEY), "queries: GLM rejected the API key (HTTP 401)")]
        for reply, msg in cases:
            with self.subTest(err=msg[:40]):
                out, seen, _ = self.search(reply)
                self.assertEqual((out["urls"], out["queries"], out["error"], out["web_search_requests"], len(seen)),
                                 ([], [], msg, 0, 1))


class TestGLMDirection(_FakeServerCase):
    """run_direction（一个子 agent）对着假服务走完：查询词 -> 搜索接口 -> 取页（假的）-> 抽取 -> 代码核对；三次调用都记进 calls.jsonl
    并计入预算（查询词调用的 token、搜索的按次费用、抽取的 token）。"""

    def test_one_direction_end_to_end(self):
        ctx = P.Context("t", "q", "2026-06-20", self.tmp / "c.jsonl", spec=spec("glm-5.2", "high"))
        url = "https://stats.example.org/widgets"
        extract = {"points": [{"name": "widgets June 2025", "value_as_written": "1,210", "unit": "widgets",
                               "period_start": "2025-06-01", "period_end": "2025-06-30", "quote": "June 2025: 1,210 widgets"}]}
        self.fake.reset(queries_reply("widgets June 2025"), results(url), ok(json.dumps(extract), use=FG.usage(5000, 400)))
        page = {"url": url, "status": "snapshot", "snapshot_ts": "20260601000000", "page_date": "2026-06-01",
                "text": "Widget statistics. June 2025: 1,210 widgets."}
        d = {"id": "d1", "category": "own_history", "hypothesis": "h", "data_to_find": "f", "search_hints": ["widgets"]}
        target = {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30"}
        with mock.patch.object(P, "fetch_page", lambda u, a, q: dict(page)):
            out = P.run_direction(ctx, target, d, 1)
        self.assertNotIn("error", out)
        self.assertEqual(out["search"]["urls"], [url])
        self.assertEqual(len(out["points"]), 1)
        self.assertEqual([r["path"] for r in self.fake.seen],
                         ["/api/paas/v4/chat/completions", "/api/paas/v4/web_search", "/api/paas/v4/chat/completions"])
        self.assertEqual(self.fake.seen[2]["body"]["thinking"], {"type": "disabled"})   # 抽取不是 plan / judge / repair
        rows = [json.loads(x) for x in ctx.calls_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([r["arm"] for r in rows], ["search:d1:queries", "search:d1", "extract:d1"])
        want = (1000 * 1.4 + 300 * 4.4) / 1e6 + 0.01 + (5000 * 1.4 + 400 * 4.4) / 1e6
        self.assertAlmostEqual(ctx.budget.usd, want, places=6)
        self.assertEqual((ctx.budget.n_calls, ctx.budget.reserved, ctx.budget.aborted), (3, 0.0, ""))
        self.assertNoKeyIn(ctx.calls_path.read_text(encoding="utf-8"), out)


class TestKeyCheck(_FakeServerCase):
    def check(self, *script, sp=None):
        self.fake.reset(*script)
        out = llm.check_key(sp or spec())
        self.assertNoKeyIn(out)
        return out, list(self.fake.seen)

    def test_models_list(self):
        """GET {base}/models（Bearer）：两站的文档都没有这个接口，但实测存在（假 key 401）。有效 key 的回复形状没核实：是 OpenAI 的形状
        （data 列表）就看所选模型在不在里面；列表全不全不知道，所以不在里面时 model_listed 是 None，不说「不在列表里」。"""
        page = {"object": "list", "data": [{"id": "glm-5.3", "object": "model"}, {"id": "glm-5.2", "object": "model"}]}
        out, seen = self.check(("json", 200, page))
        self.assertEqual((seen[0]["method"], seen[0]["path"], seen[0]["body"]), ("GET", "/api/paas/v4/models", None))
        self.assertEqual(seen[0]["headers"]["authorization"], f"Bearer {KEY}")
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"], out["status"]), (True, True, 2, 200))
        self.assertEqual(out["message"], "GLM accepted the API key")
        out, seen = self.check(("json", 200, page), sp=spec("glm-4.7-flashx", region="cn"))
        self.assertEqual(seen[0]["path"], "/cn/api/paas/v4/models")
        self.assertEqual((out["ok"], out["model_listed"]), (True, None))
        self.assertIn("whether glm-4.7-flashx is offered was not checked", out["message"])
        out, _ = self.check(("json", 200, {"models": ["glm-5.2"]}))   # 形状不认识：key 照样算通过
        self.assertEqual((out["ok"], out["model_listed"], out["n_models"]), (True, None, 0))

    def test_rejected_keys_use_the_real_401_bodies(self):
        """2026-10-21 实测（probes/glm_key_probe.py，没花钱）：不带 key / 假 key 调 GET /models 都是 HTTP 401（国内站 message 是中文）。"""
        for body in (FG.REAL_401_NO_KEY, FG.REAL_401_FAKE_KEY, FG.REAL_401_FAKE_KEY_CN):
            with self.subTest(code=body["error"]["code"], message=body["error"]["message"]):
                out, _ = self.check(("json", 401, body))
                self.assertEqual(out, {"provider": "glm", "model": "glm-5.2", "ok": False, "status": 401,
                                       "error": "key_rejected", "message": "GLM rejected the API key (HTTP 401)"})

    def test_other_outcomes(self):
        out, _ = self.check(err(429, 1113, "Insufficient balance or no resource package. Please recharge."))
        self.assertEqual(out["error"], "balance")
        self.assertIn("code 1113", out["message"])
        out, _ = self.check(err(429, 1315, "This API Key is limited to enterprise coding package scenarios."))
        self.assertEqual(out["error"], "balance")
        self.assertIn("Standard API Key", out["message"])
        out, _ = self.check(("raw", 200, b"<html>"))
        self.assertEqual(out["error"], "bad_response_body")
        out, _ = self.check(("redirect", 302, self.fake.url("/x")))
        self.assertEqual(out["error"], "redirect")


class TestModelSpecGLM(unittest.TestCase):
    def test_official_endpoints_and_key_note(self):
        """API 主机（两站的 API 参考 servers / HTTP API 页）：国际站 https://api.z.ai/api/paas/v4，国内站 https://open.bigmodel.cn/api/paas/v4。
        只用通用端点，没有 Coding Plan 端点（/api/coding/paas/v4）。网页上的 key 说明：只收 Standard API Key，Coding Plan 的 key 不行。"""
        self.assertEqual(PV.GLM.regions, {
            "global": {"chat": "https://api.z.ai/api/paas/v4/chat/completions", "search": "https://api.z.ai/api/paas/v4/web_search",
                       "models": "https://api.z.ai/api/paas/v4/models"},
            "cn": {"chat": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
                   "search": "https://open.bigmodel.cn/api/paas/v4/web_search",
                   "models": "https://open.bigmodel.cn/api/paas/v4/models"}})
        self.assertNotIn("coding", json.dumps(PV.GLM.regions))
        self.assertEqual(set(PV.GLM.region_labels), {"global", "cn"})
        note = PV.PROVIDERS["glm"]["key_note"]
        self.assertIs(note, PV.GLM.key_note)
        for s in ("Standard API Key", "Coding Plan keys", "are not allowed", "/api/coding/paas/v4", PV.GLM.key_pages["global"],
                  PV.GLM.key_pages["cn"]):
            self.assertIn(s, note)
        self.assertEqual(PV.GLM.key_check_request("cn", KEY),
                         ("https://open.bigmodel.cn/api/paas/v4/models", {"Authorization": f"Bearer {KEY}"}))
        self.assertEqual(PV.GLM.search_settings("global"), {"search_engine": "search-prime"})
        self.assertEqual(PV.GLM.search_settings("cn"), {"search_engine": "search_std", "search_intent": False, "query_max_chars": 70})

    def test_choices_and_public_view(self):
        self.assertEqual(PV.PROVIDERS["glm"]["models"], ("glm-4.7-flashx", "glm-5.2", "glm-5.3"))
        self.assertEqual(PV.PROVIDERS["glm"]["default_model"], "glm-5.2")
        sp = spec("glm-5.3", "medium", region="cn", usd_cap=5)
        self.assertEqual(sp.public(), {"provider": "glm", "model": "glm-5.3", "region": "cn", "thinking": "medium",
                                       "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high", "*": "low"},
                                       "usd_cap": 5.0, "byok": True, "price_id": "glm-5.3@cn",
                                       "fx": {"cny_per_usd": 6.7192, "source": config.CNY_PER_USD_SOURCE, "date": "2026-10-21"}})
        self.assertEqual(spec().public(), {"provider": "glm", "model": "glm-5.2", "region": "global", "thinking": "off",
                                           "thinking_by_role": {}, "usd_cap": 2.0, "byok": True})
        self.assertNotIn(KEY, repr(sp))
        with self.assertRaises(PV.SpecError):
            spec(region="coding")
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("glm", "glm-5.3-flash", KEY, thinking="low")   # 不在网页清单里
        with self.assertRaises(PV.SpecError):
            PV.ModelSpec("zhipu", "glm-5.2", KEY)
        with mock.patch.dict(config.PRICES), self.assertRaises(config.UnknownModel):   # 某个区域没有价格就拒跑
            del config.PRICES["glm-5.2@cn"]
            spec(region="cn")


class TestRunWithGLMSpec(_FakeServerCase):
    """prepare_run(spec=GLM 国内站 5.3) -> 图 -> save_run，全部对着假服务：规划一步收到 429 code 1113 就干净停下；state.json 记 provider、
    price_id、汇率和搜索设置，不记 key；结果目录里没有 key；写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop(self):
        from triangulate.agent import run as R
        sp = spec("glm-5.3", "high", region="cn", usd_cap=1.5)
        q = {"id": "ask_glm1", "question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20"}
        self.fake.reset(*[err(429, 1113, "您的账户已欠费，请充值后重试")] * 3)
        with mock.patch.object(R, "RES", self.tmp):
            h = R.prepare_run(q, "web_t", spec=sp)
            out = h["g"].invoke(R.initial_input(q), h["cfg"])
            self.assertFalse(out.get("__interrupt__"))
            st = R.save_run(h, [])
        self.assertEqual([r["path"] for r in self.fake.seen], ["/cn/api/paas/v4/chat/completions"])
        b = self.fake.seen[0]["body"]
        self.assertEqual((b["model"], b["thinking"], b["reasoning_effort"]), ("glm-5.3", {"type": "enabled"}, "max"))   # plan
        self.assertTrue(st["aborted"].startswith("insufficient balance: GLM HTTP 429 code 1113"), st["aborted"])
        self.assertEqual((st["provider"], st["model"]), ("glm", "glm-5.3"))
        rs = st["settings"]["run_spec"]
        self.assertEqual((rs["price_id"], rs["region"], rs["fx"]["cny_per_usd"]), ("glm-5.3@cn", "cn", 6.7192))
        self.assertEqual(st["settings"]["search_queries"], {"max_tokens": S.SEARCH_QUERIES_MAX_TOKENS,
                                                            "endpoint": self.fake.url("/cn/api/paas/v4/web_search"),
                                                            "search_engine": "search_std", "search_intent": False,
                                                            "query_max_chars": 70})
        self.assertEqual(st["budget"]["usd_cap"], 1.5)
        files = list((self.tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn(KEY, text, f.name)
            self.assertNotIn(KEY.split(".")[1], text, f.name)
        self.assertFalse(sp.has_key)


class TestRetryAfterHeader(unittest.TestCase):
    def test_glm_honors_retry_after_when_present(self):
        """GLM 的文档没写 Retry-After；服务端给了就照它等，没给照常退避（llm.retry_after）。"""
        h = http.client.HTTPMessage()
        h["Retry-After"] = "4"
        self.assertEqual(llm.retry_after(PV.GLM, h), "4")
        self.assertIsNone(llm.retry_after(PV.GLM, http.client.HTTPMessage()))


if __name__ == "__main__":
    unittest.main()
