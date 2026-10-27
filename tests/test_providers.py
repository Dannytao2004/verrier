"""v2.10a：provider adapter 层（目前只有 DeepSeek）和每次运行的 ModelSpec。全部离线：假 urlopen、假 key，不读 key 文件。

- 没有 ModelSpec 的默认路径（命令行、回测、基线）：请求（URL、请求头、请求体字节）和 calls.jsonl 行与 HEAD ec3e929 逐字节相同
  （tests/golden/deepseek_requests_head.json），有意的差别是 402 现在抛 BalanceExhausted，以及 v2.11c 起成功的搜索的返回值多一个
  candidates（CANDIDATES 里的 4 个 case；请求、日志不变）；
- 有 ModelSpec 的 DeepSeek 运行：请求体和默认路径相同，只是 key / 模型 / 思考档位按 spec；
- 价格：没有价格的模型拒跑；方向数按模型价格缩放；
- 余额不足：整次运行干净停下；key 不进任何写盘的文件和错误文字；Jev 对照臂在自带 key 的运行里不跑。
"""
import copy
import json
import pickle
import tempfile
import unittest
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

from tests import golden_deepseek as GD
from triangulate import config, llm
from triangulate import providers as PV
from triangulate.agent import pipeline as P
from triangulate.agent import search as S

KEY = "sk-user-0123456789ABCDEF"
GOLDEN = Path(__file__).resolve().parent / "golden" / "deepseek_requests_head.json"
OK_CHAT = ("ok", 200, GD._chat('{"a": 1}'))
OK_SEARCH = ("ok", 200, GD.SEARCH_BODY)
INTENDED = {"json_402", "search_402"}   # 402：HEAD 是 TransportError / 返回 http_402，现在抛 BalanceExhausted（v2.10a 有意改的）
# v2.11c（计划 D3，决定 17）：成功的搜索的返回值多一个 candidates（各查询词的全部结果 URL），只有这 4 个 case 的返回值里有搜索结果。
# 请求、日志照旧逐字节比；返回值去掉 candidates 这一个键以后也逐字节比。context_ask_and_search 的返回值是 [ask 的结果, 搜索的结果]
CANDIDATES = {"search_ok": None, "search_ok_defaults": None, "search_retry_503": None, "context_ask_and_search": 1}
# 金样本 SEARCH_BODY 的 candidates：块里没有 id，按先进先出配查询词；第二块是 max_uses_exceeded 错误
GOLDEN_CANDIDATES = {"provider": "deepseek", "by_query": [
    {"query": "widgets June 2025 official", "urls": ["https://stats.example.org/w", "https://b.example.org/x"]},
    {"query": "widgets 2024", "urls": [], "error": "max_uses_exceeded"}]}


def _without_candidates(case: dict) -> tuple:
    """(去掉 candidates 之后的 case, 去掉的 candidates)：只动 CANDIDATES 里写明的那一个返回值。"""
    case = copy.deepcopy(case)
    i = CANDIDATES[case["case"]]
    res = case["result"] if i is None else case["result"][i]
    return case, res.pop("candidates")


def spec(model="deepseek-flash", thinking="off", key=KEY, **kw):
    return PV.ModelSpec("deepseek", model, key, thinking=thinking, **kw)


class TestGoldenDefaultPath(unittest.TestCase):
    def test_default_path_is_byte_identical_to_head(self):
        old = json.loads(GOLDEN.read_text(encoding="utf-8"))
        new = GD.capture()
        self.assertEqual(old["model"], new["model"])
        self.assertEqual([c["case"] for c in old["cases"]], [c["case"] for c in new["cases"]])
        for o, n in zip(old["cases"], new["cases"]):
            with self.subTest(case=o["case"]):
                self.assertEqual(GD.dumps(o["requests"]), GD.dumps(n["requests"]))   # URL、请求头、请求体字节、超时
                self.assertEqual(o["log"], n["log"])                                 # calls.jsonl 行（at / latency 除外）
                if o["case"] in INTENDED:
                    self.assertEqual(n["result"]["raised"], "BalanceExhausted")
                    self.assertTrue(n["result"]["is_transport_error"])   # 基线只接 TransportError：照旧跳过这道题
                    self.assertIn("insufficient balance", n["result"]["message"])
                elif o["case"] in CANDIDATES:
                    n2, cand = _without_candidates(n)
                    self.assertEqual(cand, GOLDEN_CANDIDATES)
                    self.assertEqual(GD.dumps(o), GD.dumps(n2))
                else:
                    self.assertEqual(GD.dumps(o), GD.dumps(n))
        self.assertNotIn("candidates", GD.dumps([c for c in new["cases"] if c["case"] not in CANDIDATES]))
        self.assertTrue(any(r["body"] for c in new["cases"] for r in c["requests"]))


def _send(client_factory, script, call):
    """用假 urlopen 跑一次，返回 (请求列表, 返回值)。"""
    net = GD._Net()
    net.script = list(script)
    with mock.patch.object(llm, "urlopen_no_redirect", net), mock.patch("time.sleep"), \
            mock.patch.object(llm, "read_key", return_value=KEY), mock.patch.object(S, "read_key", return_value=KEY), \
            mock.patch.object(config, "is_peak", lambda t: False):
        client = client_factory()
        try:
            out = call(client)
        except Exception as e:  # noqa: BLE001
            out = e
    net.close()
    return net.seen, out


class TestSpecPathDeepSeek(unittest.TestCase):
    def _chat(self, sp, arm="judge:r1", max_tokens=12000, thinking=None):
        tmp = Path(tempfile.mkdtemp()) / "c.jsonl"
        with mock.patch.object(llm, "THINKING", thinking or {}):
            seen, out = _send(lambda: llm.LLM(calls_path=tmp, spec=sp), [OK_CHAT],
                              lambda c: c.json_call(GD.MSGS, arm=arm, qid="t", attempt=1, max_tokens=max_tokens))
        return seen, out, GD._norm_log(tmp.read_text(encoding="utf-8").splitlines())

    def test_flash_off_sends_the_same_bytes_as_the_default_path(self):
        for arm, mt in (("judge:r1", 12000), ("plan", 6000), ("extract:d2", 16000), ("final", 4000)):
            with self.subTest(arm=arm):
                a = self._chat(None, arm, mt)
                b = self._chat(spec(), arm, mt)
                self.assertEqual(a, b)
                self.assertEqual(dict(b[0][0]["headers"])["Authorization"], f"Bearer {KEY}")
        logged = []
        sa, ra = _send(lambda: S.Searcher(log=logged.append), [OK_SEARCH], lambda s: s.search("p", role="search:d1", qid="t"))
        sb, rb = _send(lambda: S.Searcher(log=logged.append, spec=spec()), [OK_SEARCH],
                       lambda s: s.search("p", role="search:d1", qid="t"))
        # v2.10g（用户 10-21「保持原本一样即可」）：自带 key 的搜索请求和默认路径逐字相同，不加 thinking
        self.assertEqual(ra, rb)
        self.assertEqual(sa, sb)
        self.assertNotIn("thinking", json.loads(sb[0]["body"]))
        self.assertEqual(GD._norm_log(logged[:1]), GD._norm_log(logged[1:]))
        self.assertEqual(dict(sb[0]["headers"])["X-api-key"], KEY)

    def test_env_thinking_does_not_apply_to_spec_runs(self):
        seen, _, _ = self._chat(spec(), "extract:d1", 16000, thinking={"extract": "high"})
        self.assertEqual(json.loads(seen[0]["body"])["thinking"], {"type": "disabled"})

    def test_thinking_levels_map_to_deepseek_efforts(self):
        # DeepSeek Thinking Mode 文档：只有 low / high / max，medium 按 high 处理
        for level, effort in (("low", "low"), ("medium", "high"), ("high", "high")):
            for arm, mt in (("plan", 6000), ("judge:r2", 12000), ("judge:r2:repair", 12000)):
                with self.subTest(level=level, arm=arm):
                    seen, out, log = self._chat(spec(thinking=level), arm, mt)
                    body = json.loads(seen[0]["body"])
                    self.assertEqual((body["thinking"], body["reasoning_effort"]), ({"type": "enabled"}, effort))
                    self.assertEqual(body["max_tokens"], mt + config.THINKING_EXTRA_TOKENS)
                    self.assertEqual(json.loads(log[0])["thinking"], effort)
            for arm in ("extract:d1", "audit", "unit_arbiter:m1:1", "value_check", "published", "final"):
                with self.subTest(level=level, arm=arm):
                    body = json.loads(self._chat(spec(thinking=level), arm, 4000)[0][0]["body"])
                    self.assertEqual(body["thinking"], {"type": "disabled"})
                    self.assertNotIn("reasoning_effort", body)
                    self.assertEqual(body["max_tokens"], 4000)

    def test_thinking_headroom_is_capped_at_the_models_max_output(self):
        with mock.patch.dict(PV.MODELS, {"deepseek-flash": {**PV.MODELS["deepseek-flash"], "max_output": 20000}}):
            body = json.loads(self._chat(spec(thinking="high"), "judge:r1", 12000)[0][0]["body"])
        self.assertEqual(body["max_tokens"], 20000)

    def test_v4_pro_is_sent_and_priced_as_itself(self):
        seen, out, log = self._chat(spec("deepseek-v4-pro"))
        self.assertEqual(json.loads(seen[0]["body"])["model"], "deepseek-v4-pro")
        u = GD.USAGE
        hit, miss, outp = config.PRICES["deepseek-v4-pro"]["offpeak"]
        want = round((u["prompt_cache_hit_tokens"] * hit + u["prompt_cache_miss_tokens"] * miss
                      + u["completion_tokens"] * outp) / 1e6, 6)
        self.assertEqual(json.loads(log[0])["usd"], want)
        self.assertNotEqual(want, round((256 * 0.003 + 944 * 0.15 + 300 * 0.60) / 1e6, 6))   # 不是 flash 的价


class TestModelSpec(unittest.TestCase):
    def assertNoKey(self, cm, key=KEY):
        self.assertNotIn(key.strip(), str(cm.exception))

    def test_defaults_and_public_view(self):
        sp = spec()
        self.assertEqual((sp.provider, sp.model, sp.region, sp.thinking, sp.usd_cap), ("deepseek", "deepseek-flash",
                                                                                       "global", "off", 3.0))   # v2.13b
        pub = sp.public()
        self.assertEqual(pub, {"provider": "deepseek", "model": "deepseek-flash", "region": "global", "thinking": "off",
                               "thinking_by_role": {}, "usd_cap": 3.0, "byok": True})   # v2.13b：默认上限 $3
        self.assertEqual(spec(thinking="High").public()["thinking_by_role"], {"plan": "high", "judge": "high", "repair": "high"})
        for text in (repr(sp), str(sp), json.dumps(pub), f"{sp}"):
            self.assertNotIn(KEY, text)

    def test_bad_settings_are_refused_without_the_key(self):
        bad = [dict(provider="openai"), dict(model="gpt-6-luna"), dict(model="deepseek-chat"), dict(region="cn"),
               dict(thinking="max"), dict(thinking="ultra"), dict(usd_cap=0), dict(usd_cap=-1), dict(usd_cap=float("nan")),
               dict(usd_cap=float("inf")), dict(usd_cap="two"), dict(usd_cap=None)]
        for kw in bad:
            with self.subTest(**{k: str(v) for k, v in kw.items()}):
                args = {"provider": "deepseek", "model": "deepseek-flash", **kw}
                with self.assertRaises(PV.SpecError) as cm:
                    PV.ModelSpec(args.pop("provider"), args.pop("model"), KEY, **args)
                self.assertNoKey(cm)

    def test_model_without_price_is_refused(self):
        extra = {"deepseek-x": {**PV.MODELS["deepseek-flash"], "label": "x"}}
        with mock.patch.dict(PV.MODELS, extra), \
                mock.patch.dict(PV.PROVIDERS, {"deepseek": {**PV.PROVIDERS["deepseek"],
                                                            "models": PV.PROVIDERS["deepseek"]["models"] + ("deepseek-x",)}}):
            with self.assertRaises(config.UnknownModel):
                spec("deepseek-x")

    def test_key_is_trimmed_and_checked(self):
        self.assertEqual(spec(key=f"  {KEY}\r\n").key, KEY)
        for bad in (f"{KEY}\r\nX-Evil: 1", "sk-abc def0123", "sk-ключ-0123456789", "short", "x" * 513, "", None, 12345678):
            with self.subTest(bad=repr(bad)[:20]):
                with self.assertRaises(PV.SpecError) as cm:
                    spec(key=bad)
                if isinstance(bad, str) and bad.strip():
                    self.assertNotIn(bad.strip(), str(cm.exception))
                    self.assertNotIn("0123456789", str(cm.exception))

    def test_key_cannot_be_copied_and_can_be_dropped(self):
        sp = spec()
        for fn in (pickle.dumps, copy.copy, copy.deepcopy):
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(TypeError):
                    fn(sp)
        self.assertEqual(sp.redact(f"error near {KEY}!"), "error near ***!")
        sp.drop_key()
        self.assertFalse(sp.has_key)
        with self.assertRaises(PV.KeyDropped) as cm:
            sp.key
        self.assertNotIn(KEY, str(cm.exception))

    def test_thinking_levels_and_models_that_cannot_turn_thinking_off(self):
        self.assertEqual(PV.thinking_levels("deepseek-flash"), ("off", "low", "medium", "high"))
        always = {**PV.MODELS["deepseek-flash"], "thinking_off": False, "efforts": {"medium": "medium", "high": "high"}}
        with mock.patch.dict(PV.MODELS, {"deepseek-flash": always}):
            self.assertEqual(PV.thinking_levels("deepseek-flash"), ("medium", "high"))
            with self.assertRaises(PV.SpecError):
                spec(thinking="off")
            sp = spec(thinking="high")
            self.assertEqual((sp.effort("judge"), sp.effort("extract"), sp.effort("final")), ("high", "medium", "medium"))
            self.assertEqual(sp.thinking_by_role(), {"plan": "high", "judge": "high", "repair": "high", "*": "medium"})

    def test_web_choices_have_prices_and_adapters(self):
        for name, p in PV.PROVIDERS.items():
            self.assertIn(p["default_model"], p["models"])
            for m in p["models"]:
                with self.subTest(model=m):
                    self.assertEqual(PV.MODELS[m]["provider"], name)
                    self.assertIs(PV.adapter_for_model(m), PV.ADAPTERS[name])
                    pr = config.price(m)
                    self.assertTrue(pr["source"].startswith("https://") and pr["checked"] >= "2026-10-21")
                    self.assertEqual(pr["provider"], name)


class TestPricing(unittest.TestCase):
    def test_unknown_model_is_not_priced_as_flash(self):
        t = datetime(2026, 10, 21, tzinfo=timezone.utc)
        with self.assertRaises(config.UnknownModel):
            config.usd_cost({"completion_tokens": 10}, t, "no-such-model-x")
        with self.assertRaises(config.UnknownModel):
            PV.adapter_for_model("no-such-model-x")
        self.assertAlmostEqual(config.usd_cost({"prompt_cache_hit_tokens": 10 ** 6, "prompt_cache_miss_tokens": 10 ** 6,
                                                "completion_tokens": 10 ** 6}, datetime(2026, 10, 18, 2, tzinfo=timezone.utc),
                                               "deepseek-v4-pro"), 0.022 + 0.66 + 1.98)   # 周日 = 闲时

    def test_clients_refuse_unpriced_models_before_reading_the_key(self):
        with mock.patch.object(llm, "read_key") as rk, mock.patch.object(S, "read_key") as rk2:
            with self.assertRaises(config.UnknownModel):
                llm.LLM(model="deepseek-chat")
            with self.assertRaises(config.UnknownModel):
                S.Searcher(log=print, model="deepseek-chat")
        rk.assert_not_called()
        rk2.assert_not_called()

    def test_directions_scale_with_model_price(self):
        self.assertEqual(P.Budget().directions, 10)
        self.assertEqual(P.Budget.typical_direction_usd("deepseek-flash"), 0.06)
        self.assertEqual(P.Budget.for_model("deepseek-flash", usd=1.0).directions, 10)
        pro = P.Budget.typical_direction_usd("deepseek-v4-pro")
        pr, f, p = P.Budget.DIRECTION_PROFILE, config.PRICES["deepseek-flash"]["peak"], config.PRICES["deepseek-v4-pro"]["peak"]

        def cost(x):
            return (pr["hit"] * x[0] + pr["miss"] * x[1] + pr["out"] * x[2]) / 1e6 + pr["searches"] * 0.01
        self.assertAlmostEqual(pro, 0.06 * cost(p) / cost(f))
        self.assertTrue(0.09 < pro < 0.12, pro)
        self.assertEqual(P.Budget.for_model("deepseek-v4-pro", usd=1.0).directions, int(0.6 / pro))
        self.assertEqual(P.Budget.for_model("deepseek-v4-pro", usd=2.0).directions, 10)   # 页数上限 40 / 4
        with self.assertRaises(config.UnknownModel):
            P.Budget.for_model("no-such-model-x")

    def test_reservations_use_the_runs_model(self):
        hit, miss, out = config.PRICES["deepseek-v4-pro"]["peak"]
        self.assertAlmostEqual(P.Budget.llm_reserve(1000, 12000, "deepseek-v4-pro"), (500 * miss + 12000 * out) / 1e6)
        self.assertEqual(P.Budget.llm_reserve(1000, 12000), P.Budget.llm_reserve(1000, 12000, "deepseek-flash"))
        b = P.Budget.for_model("deepseek-v4-pro", usd=2.0)
        self.assertAlmostEqual(b.search_reserve(), (30_000 * miss + config.MAX_TOKENS["search"] * out) / 1e6 + 8 * 0.01)
        self.assertGreater(b.search_reserve(), P.Budget().search_reserve())

    def test_spec_reservation_includes_thinking_headroom(self):
        seen = []

        class B(P.Budget):
            @contextmanager_hold
            def hold(self, amount):
                seen.append(amount)

        sp = spec("deepseek-v4-pro", thinking="high")
        a = P.AgentLLM(Path(tempfile.mkdtemp()) / "c.jsonl", B.for_model("deepseek-v4-pro", usd=2.0), spec=sp)
        with mock.patch.object(P.AgentLLM, "json_call", return_value=({"a": 1}, "", None)):
            a.ask("s", "u", role="judge:r1", qid="t", max_tokens=12000)
            a.ask("s", "u", role="extract:d1", qid="t", max_tokens=16000)
        self.assertAlmostEqual(seen[0], P.Budget.llm_reserve(2, 12000 + config.THINKING_EXTRA_TOKENS, "deepseek-v4-pro"))
        self.assertAlmostEqual(seen[1], P.Budget.llm_reserve(2, 16000, "deepseek-v4-pro"))

    def test_context_budget_follows_the_spec(self):
        with mock.patch.object(llm, "read_key", return_value=KEY), mock.patch.object(S, "read_key", return_value=KEY):
            c0 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl")
        c1 = P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=spec("deepseek-v4-pro", usd_cap=3.5))
        self.assertEqual((c0.budget.usd_cap, c0.budget.model, c0.spec, c0.llm.spec, c0.searcher.spec), (1.0, None, None, None, None))
        self.assertEqual((c1.budget.usd_cap, c1.budget.model, c1.llm.model, c1.searcher.model),
                         (3.5, "deepseek-v4-pro", "deepseek-v4-pro", "deepseek-v4-pro"))
        self.assertIs(c1.llm.spec, c1.spec)
        self.assertIsNone(c1.llm._key)   # key 只在 spec 里
        self.assertIsNone(c1.searcher._key)


def contextmanager_hold(fn):
    """把一个只记录金额的 hold 包成上下文管理器（不检查上限）。"""
    from contextlib import contextmanager

    @contextmanager
    def wrapper(self, amount):
        fn(self, amount)
        yield
    return wrapper


class TestBalanceStop(unittest.TestCase):
    def _ctx(self, sp=None):
        with mock.patch.object(llm, "read_key", return_value=KEY), mock.patch.object(S, "read_key", return_value=KEY):
            return P.Context("t", "q", "2026-06-20", Path(tempfile.mkdtemp()) / "c.jsonl", spec=sp)

    def test_balance_exhausted_is_a_transport_error_for_the_baselines(self):
        self.assertTrue(issubclass(llm.BalanceExhausted, llm.TransportError))

    def test_ask_stops_the_whole_run(self):
        for sp in (None, spec()):
            with self.subTest(spec=bool(sp)):
                ctx = self._ctx(sp)
                net = GD._Net()
                net.script = [("http", 402, b"")]
                with mock.patch.object(llm, "urlopen_no_redirect", net), mock.patch("time.sleep"):
                    with self.assertRaises(P.BudgetExceeded) as cm:
                        ctx.llm.ask("s", "u", role="plan", qid="t")
                net.close()
                self.assertEqual(len(net.seen), 1)   # 不重试、不带错误重问
                self.assertIn("insufficient balance", str(cm.exception))
                self.assertTrue(ctx.budget.aborted.startswith("insufficient balance: DeepSeek HTTP 402"))
                with self.assertRaises(P.BudgetExceeded):   # 之后的调用都不再发
                    with ctx.budget.hold(0.0):
                        pass

    def test_search_402_stops_the_direction_and_the_run(self):
        ctx = self._ctx(spec())
        net = GD._Net()
        net.script = [("http", 402, b"")]
        d = {"id": "d1", "category": "own_history", "hypothesis": "h", "data_to_find": "f"}
        target = {"what": "widgets", "unit": "widgets", "period_start": "2026-06-01", "period_end": "2026-06-30"}
        with mock.patch.object(llm, "urlopen_no_redirect", net), mock.patch("time.sleep"), \
                mock.patch.object(P, "fetch_page", side_effect=AssertionError("no page should be fetched")):
            out = P.run_direction(ctx, target, d, 1)
            out2 = P.run_direction(ctx, target, {**d, "id": "d2"}, 1)
        net.close()
        self.assertIn("insufficient balance", out["aborted"])
        self.assertEqual((out["pages"], out2["pages"], len(net.seen)), ([], [], 1))
        self.assertIn("insufficient balance", out2["aborted"])
        self.assertNotIn("error", out)

    def test_error_strings_never_carry_the_key(self):
        ctx = self._ctx(spec())

        class Leaky:
            def search(self, *a, **k):
                raise ValueError(f"Invalid header value b'Bearer {KEY}'")
        ctx.searcher = Leaky()
        out = P.run_direction(ctx, {"what": "w"}, {"id": "d1", "category": "own_history"}, 1)
        self.assertIn("***", out["error"])
        self.assertNotIn(KEY, out["error"])
        net = GD._Net()
        net.script = [("http", 401, KEY.encode())]
        with mock.patch.object(llm, "urlopen_no_redirect", net):
            with self.assertRaises(llm.KeyRejected) as cm:
                ctx.llm.json_call(GD.MSGS, arm="plan", qid="t", attempt=1)
        net.close()
        self.assertEqual(str(cm.exception), "DeepSeek rejected the API key (HTTP 401)")
        self.assertNotIn(KEY, ctx.calls_path.read_text(encoding="utf-8"))


class TestRunWithSpec(unittest.TestCase):
    """prepare_run(spec=...) -> 图 -> save_run：余额不足在规划一步就干净停下；state.json 记 provider 等设置，不记 key；
    写完以后 key 从内存里清掉。"""

    def test_end_to_end_balance_stop_and_no_key_on_disk(self):
        from triangulate.agent import run as R
        tmp = Path(tempfile.mkdtemp())
        sp = spec("deepseek-v4-pro", thinking="medium", usd_cap=1.5)
        q = {"id": "ask_spec1", "question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20"}
        net = GD._Net()
        net.script = [("http", 402, b"")] * 5
        with mock.patch.object(R, "RES", tmp), mock.patch.object(llm, "urlopen_no_redirect", net), mock.patch("time.sleep"):
            h = R.prepare_run(q, "web_t", spec=sp)
            self.assertNotIn("spec", h)
            self.assertIs(h["ctx"].spec, sp)
            out = h["g"].invoke(R.initial_input(q), h["cfg"])
            self.assertFalse(out.get("__interrupt__"))
            st = R.save_run(h, [])
        net.close()
        self.assertEqual(len(net.seen), 1)
        self.assertEqual(json.loads(net.seen[0]["body"])["reasoning_effort"], "high")   # plan，medium -> high
        self.assertTrue(st["aborted"].startswith("insufficient balance: DeepSeek HTTP 402"))
        self.assertEqual(st["provider"], "deepseek")
        self.assertEqual(st["model"], "deepseek-v4-pro")
        self.assertEqual(st["settings"]["run_spec"], {"provider": "deepseek", "model": "deepseek-v4-pro", "region": "global",
                                                      "thinking": "medium", "usd_cap": 1.5, "byok": True,
                                                      "thinking_by_role": {"plan": "high", "judge": "high", "repair": "high"}})
        self.assertEqual(st["settings"]["thinking"]["by_role"], {"plan": "high", "judge": "high", "repair": "high"})
        self.assertEqual(st["budget"]["usd_cap"], 1.5)
        files = list((tmp / q["id"] / "web_t").iterdir())
        self.assertTrue({"state.json", "ledger.md", "graph.html", "calls.jsonl"} <= {f.name for f in files})
        for f in files:
            self.assertNotIn(KEY, f.read_text(encoding="utf-8"), f.name)
        self.assertFalse(sp.has_key)   # 运行结束：key 已从内存里清掉
        with self.assertRaises(PV.KeyDropped):
            h["ctx"].llm.json_call(GD.MSGS, arm="plan", qid="t", attempt=1)

    def test_settings_without_spec_are_unchanged(self):
        from triangulate.agent import run as R
        s = R.run_settings()
        self.assertNotIn("run_spec", s)
        self.assertEqual(set(s), {"max_tokens", "budget_defaults", "budget_run", "interval"} | ({"thinking"} if config.THINKING else set()))
        self.assertEqual(set(R.run_settings(spec())), {"max_tokens", "budget_defaults", "budget_run", "interval", "run_spec"})


class TestJevDisabledInByokRuns(unittest.TestCase):
    def test_typesafe_is_not_called(self):
        from tests.test_discrete import CUT, HAVE_LG, HIKE, HOLD, TestJevClient, discrete_graph_run
        if not HAVE_LG:
            self.skipTest("langgraph not installed")
        calls = []

        def post(*a):
            calls.append(a)
            return TestJevClient._reply({CUT: 0.05, HOLD: 0.5, HIKE: 0.45})
        st, _ = discrete_graph_run(jev_post=post, spec=spec())
        self.assertEqual(calls, [])
        self.assertEqual(st["jev"]["status"], "skipped")
        self.assertIn("bring-your-own-key", st["jev"]["note"])
        st, _ = discrete_graph_run(jev_post=post)   # 对照：没有 spec 时照旧调用
        self.assertEqual(len(calls), 1)
        self.assertEqual(st["jev"]["status"], "ok")


class TestAdapterErrorBody(unittest.TestCase):
    def test_deepseek_does_not_read_error_bodies(self):
        self.assertEqual(PV.DEEPSEEK.error_body_statuses, frozenset())
        e = urllib.error.HTTPError("u", 429, "x", {}, None)
        self.assertEqual(llm.read_error_body(e), b"")


if __name__ == "__main__":
    unittest.main()
