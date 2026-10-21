"""web-v0.9：网页的「自带 key」（BYOK）：GET /api/providers、POST /api/key/check、POST /api/runs 带 key、运行结束清 key、
任何返回和写出的文件里都没有 key、经典界面（/）不能发起运行。不联网、不调真模型、不读 key 文件。

端到端的一组（TestRealPathEndToEnd）走真实的 prepare_run / AgentLLM / Searcher / save_run：DeepSeek 的 URL 换成 127.0.0.1 上的
假服务（按请求路径和 system prompt 回复，回复内容同 tests/test_web.py 的 FakeLLM），key 真的进了请求头，然后检查它没有出现在
任何 API 返回和结果目录的任何文件里，运行结束后 key 已从内存清掉。
"""
import json
import shutil
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from unittest import mock

try:
    import fastapi  # noqa: F401
    import langgraph  # noqa: F401
    HAVE_WEB = True
except ImportError:
    HAVE_WEB = False

KEY = "sk-byok-SECRET-0123456789abcdefQRS"
STATIC = Path(__file__).resolve().parents[1] / "triangulate" / "web" / "static"


def no_key_file(*a, **k):
    raise AssertionError("a web run must never read the server's key file")


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(k)
            yield from walk_strings(v)
    elif isinstance(obj, (list, tuple)):
        for x in obj:
            yield from walk_strings(x)


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class _Client(unittest.TestCase):
    def client(self, reg=None, key_checker=None, res=None):
        """reg 没给时用一个 prepare 直接报错的 Registry：保护失效时测试只会失败，不会真的发起运行、连到真的 API。"""
        from fastapi.testclient import TestClient

        from triangulate.web.app import create_app
        from triangulate.web.runs import Registry

        def refuse(q, tag="", spec=None):
            raise AssertionError("this test must not start a real run")
        tmp = res or Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        return TestClient(create_app(reg or Registry(prepare=refuse, save=refuse), res=tmp, key_checker=key_checker),
                          base_url="http://127.0.0.1")

    def assertNoKey(self, text, key=KEY, what=""):
        self.assertNotIn(key, text, what)
        self.assertNotIn(key[8:24], text, what)   # 半截也不行


class TestProvidersApi(_Client):
    def setUp(self):
        self.c = self.client()

    def test_catalog_matches_providers_and_models(self):
        """provider、模型、档位都来自 providers.py（不另写一份）；Kimi / GLM 有国际站 / 国内站，其余只有一个区域；默认值。"""
        from triangulate import providers as PV
        with mock.patch("triangulate.config.read_key", no_key_file):
            v = self.c.get("/api/providers").json()
        self.assertEqual([p["id"] for p in v["providers"]], list(PV.PROVIDERS))
        self.assertEqual((v["default_provider"], v["default_usd_cap"], v["usd_cap"]), ("deepseek", 2.0, 2.0))
        self.assertEqual(v["thinking_levels"], ["off", "low", "medium", "high"])
        self.assertEqual(v["reasoning_roles"], ["plan", "judge", "repair"])
        for p in v["providers"]:
            self.assertEqual([m["id"] for m in p["models"]], list(PV.PROVIDERS[p["id"]]["models"]))
            self.assertEqual(p["default_model"], PV.PROVIDERS[p["id"]]["default_model"])
            self.assertEqual(p["region_choice"], p["id"] in ("kimi", "glm"))
            self.assertEqual([r["id"] for r in p["regions"]], list(PV.ADAPTERS[p["id"]].regions))
            for m in p["models"]:
                th = m["thinking"]
                self.assertEqual(th["levels"], list(PV.thinking_levels(m["id"])))
                self.assertEqual(th["can_turn_off"], PV.MODELS[m["id"]]["thinking_off"])
                self.assertEqual(th["default"], "off" if th["can_turn_off"] else "low")
                self.assertEqual(set(m["by_region"]), set(PV.ADAPTERS[p["id"]].regions))
                for region, r in m["by_region"].items():
                    self.assertEqual(r["price_id"], m["id"] if region == "global" else f"{m['id']}@{region}")
                    self.assertEqual(set(r["by_thinking"]), set(th["levels"]))
                    for e in r["by_thinking"].values():
                        self.assertGreater(e["est_usd"], 0)
                        self.assertGreaterEqual(e["directions"], 1)
        no_off = {m["id"] for p in v["providers"] for m in p["models"] if not m["thinking"]["can_turn_off"]}
        self.assertEqual(no_off, {"claude-opus-5-5", "claude-fable-5-1", "gpt-6.1-sol", "gpt-6-astra", "kimi-k3", "glm-5.3"})
        glm = next(p for p in v["providers"] if p["id"] == "glm")
        self.assertIn("Standard API Key", glm["notes"][0]["en"])
        self.assertIn("Coding Plan", glm["notes"][0]["zh"])
        self.assertEqual(glm["key_pages"], PV.GLM.key_pages)
        for s in walk_strings(v):   # 没有任何秘密：没有 key 字段，也不提服务器的 key 文件
            self.assertNotIn("TRIANGULATE_KEY_FILE", s)
            self.assertNotEqual(s, "api_key")

    def test_thinking_sends_what_the_adapter_sends(self):
        """「发什么」直接从 adapter 建的请求体里取，和真实请求相同。"""
        v = self.c.get("/api/providers").json()
        m = {x["id"]: x for p in v["providers"] for x in p["models"]}
        self.assertEqual(m["deepseek-flash"]["thinking"]["sends"]["off"], {"thinking": {"type": "disabled"}})
        self.assertEqual(m["deepseek-flash"]["thinking"]["sends"]["medium"],
                         {"thinking": {"type": "enabled"}, "reasoning_effort": "high"})
        self.assertEqual(m["claude-opus-5-5"]["thinking"]["sends"]["low"],
                         {"thinking": {"type": "adaptive"}, "output_config": {"effort": "low"}})
        self.assertEqual(m["claude-opus-5-5"]["thinking"]["sends_other_roles"],
                         {"thinking": {"type": "adaptive"}, "output_config": {"effort": "low"}})
        self.assertEqual(m["claude-sonnet-5-5"]["thinking"]["sends"]["off"]["thinking"], {"type": "between_tools"})
        self.assertEqual(m["gpt-6-luna"]["thinking"]["sends"]["off"], {"reasoning_effort": "none"})
        self.assertEqual(m["kimi-k3"]["thinking"]["sends"]["high"], {"reasoning_effort": "max"})
        self.assertEqual(m["kimi-k2.6"]["thinking"]["sends"]["high"], {"thinking": {"type": "enabled"}})
        self.assertEqual(m["glm-5.2"]["thinking"]["sends"]["low"]["reasoning_effort"], "high")
        self.assertEqual(m["kimi-k2.6"]["notes"][0]["en"], "No depth levels: low, medium and high all mean thinking on.")
        self.assertIn("cannot be turned off", m["gpt-6-astra"]["notes"][0]["en"])

    def test_estimates_follow_the_cap_and_the_budget(self):
        """方向数 = Budget.for_model(price_id, usd=cap).directions；估计 = RUN_PROFILE 按官方价；第一轮预扣放不下时给提示和最小上限。"""
        from triangulate.agent.pipeline import Budget
        from triangulate.web import catalog as C

        def est(cap, model, region="global", level=None):
            v = self.c.get("/api/providers", params={"usd_cap": cap}).json()
            m = next(x for p in v["providers"] for x in p["models"] if x["id"] == model)
            return m["by_region"][region]["by_thinking"][level or m["thinking"]["default"]]
        flash = est(2, "deepseek-flash")
        self.assertEqual(flash["directions"], Budget.for_model("deepseek-flash", usd=2.0).directions)
        rp = C.RUN_PROFILE
        want = (rp["directions_per_round1_max"] * 10 * Budget.profile_usd("deepseek-flash", Budget.DIRECTION_PROFILE)
                + Budget.profile_usd("deepseek-flash", rp["reasoning"]) + Budget.profile_usd("deepseek-flash", rp["other"]))
        self.assertAlmostEqual(flash["est_usd"], round(want, 2))
        self.assertTrue(0.4 < flash["est_usd"] < 0.9, flash)   # 实测 50 次运行平均 $0.52（峰时价估计偏高一点）
        self.assertFalse(flash["stops_early"])
        self.assertGreater(est(2, "deepseek-flash", level="high")["est_usd"], flash["est_usd"])   # 思考 token 按输出价另计
        opus = est(2, "claude-opus-5-5")
        self.assertEqual((opus["directions"], opus["stops_early"], opus["min_cap_usd"]), (3, True, 7.0))
        self.assertAlmostEqual(opus["round1_search_hold_usd"], 2.53, places=2)   # PROVIDERS.md 9.8：3 x $0.844
        self.assertTrue(opus["over_cap"])
        self.assertFalse(est(7, "claude-opus-5-5")["stops_early"])
        fable = est(2, "claude-fable-5-1")   # 只有 1 个方向，搜索放得下，但抽取一页的预扣（$2.20）就超过上限
        self.assertEqual(fable["directions"], 1)
        self.assertLess(fable["round1_search_hold_usd"], 2)
        self.assertGreater(fable["extract_hold_usd"], 2)
        self.assertTrue(fable["stops_early"])
        self.assertGreaterEqual(fable["min_cap_usd"], fable["extract_hold_usd"])
        cn = est(2, "kimi-k3", "cn")
        self.assertEqual(cn["price_id"], "kimi-k3@cn")

    def test_bad_cap(self):
        for bad in ("0", "-1", "nan", "inf"):
            self.assertEqual(self.c.get("/api/providers", params={"usd_cap": bad}).status_code, 400, bad)
        self.assertEqual(self.c.get("/api/providers", params={"usd_cap": "abc"}).status_code, 422)


class TestKeyCheckApi(_Client):
    def test_check_against_fake_server(self):
        """POST /api/key/check -> llm.check_key -> 这家的 models 列表（这里是假服务）；返回 ok / 被拒，不含 key。"""
        from tests import fake_claude as FC
        from triangulate import providers as PV
        fake = FC.FakeClaude()
        self.addCleanup(fake.close)
        c = self.client()
        with mock.patch.object(PV.DeepSeekAdapter, "regions", {"global": {"models": fake.url("/models")}}), \
                mock.patch("triangulate.config.read_key", no_key_file):
            fake.reset(("json", 200, {"object": "list", "data": [{"id": "deepseek-flash", "object": "model"}]}))
            r = c.post("/api/key/check", json={"provider": "deepseek", "api_key": "  " + KEY + "\n"})
            self.assertEqual(r.status_code, 200, r.text)
            self.assertEqual((r.json()["ok"], r.json()["model_listed"]), (True, True))
            self.assertEqual(fake.seen[0]["headers"]["authorization"], f"Bearer {KEY}")   # 去掉了首尾空白
            self.assertNoKey(r.text)
            fake.reset(("raw", 401, b"Authentication Fails (governor)"))
            r = c.post("/api/key/check", json={"provider": "deepseek", "api_key": KEY})
            self.assertEqual((r.status_code, r.json()["ok"], r.json()["error"]), (200, False, "key_rejected"))
            self.assertNoKey(r.text)

    def test_validation_and_key_dropped(self):
        seen = []

        def checker(spec):
            seen.append(spec)
            self.assertTrue(spec.has_key)
            return {"provider": spec.provider, "model": spec.model, "region": spec.region, "ok": True, "message": "echo " + spec.key}
        c = self.client(key_checker=checker)
        r = c.post("/api/key/check", json={"provider": "glm", "region": "cn", "api_key": KEY})
        self.assertEqual(r.status_code, 200)
        self.assertEqual((r.json()["model"], r.json()["region"]), ("glm-5.2", "cn"))   # 没给模型：这家的默认模型
        self.assertNoKey(r.text)                              # 兜底：校验函数返回的文字里有 key 也会换成 ***
        self.assertEqual(r.json()["message"], "echo ***")
        self.assertFalse(seen[0].has_key)                     # 校验完就清掉
        for body in ({"provider": "deepseek"}, {"provider": "deepseek", "api_key": "  "}, {"provider": "nope", "api_key": KEY},
                     {"provider": "deepseek", "region": "cn", "api_key": KEY}, {"provider": "claude", "model": "kimi-k3", "api_key": KEY},
                     {"provider": "deepseek", "api_key": KEY + "é"}):
            r = c.post("/api/key/check", json=body)
            self.assertEqual(r.status_code, 400, body)
            self.assertNoKey(r.text)
        self.assertEqual(len(seen), 1)


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestRunsByok(_Client):
    def setUp(self):
        from tests import test_web as TW
        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        from triangulate.web.runs import Registry
        self.TW = TW
        self.tmp = Path(tempfile.mkdtemp())
        for p in (mock.patch.object(P, "fetch_page", TW.fake_fetch),
                  mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}),
                  mock.patch("triangulate.config.read_key", no_key_file)):
            p.start()
            self.addCleanup(p.stop)
        self.gate = threading.Event()
        self.gate.set()
        self.reg = Registry(prepare=TW.make_prepare(self.tmp, self.gate), max_active=1)
        self.c = self.client(self.reg, res=self.tmp)
        self.addCleanup(self._wait_all)
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def _wait_all(self):
        self.gate.set()
        for r in self.reg.runs.values():
            t = time.time()
            while r.status in ("planning", "running") and time.time() - t < 10:
                time.sleep(0.05)

    def body(self, **kw):
        return {"question": "How many widgets in June 2026?", "as_of": "2026-06-20", "api_key": KEY, **kw}

    def responses_have_no_key(self, *extra):
        texts = [self.c.get("/api/runs").text, *extra]
        texts += [self.c.get(f"/api/runs/{rid}").text for rid in self.reg.runs]
        for t in texts:
            self.assertNoKey(t)

    def test_missing_key_is_refused(self):
        from triangulate.web.runs import NEED_KEY
        no_key = {k: v for k, v in self.body().items() if k != "api_key"}
        for b in (no_key, {**no_key, "api_key": None}, {**no_key, "api_key": ""}, {**no_key, "api_key": "   "}):
            r = self.c.post("/api/runs", json=b)
            self.assertEqual(r.status_code, 400, b)
            self.assertEqual(r.json()["detail"], NEED_KEY)
        self.assertIn("API key", NEED_KEY)
        self.assertIn("key 文件", NEED_KEY)
        self.assertEqual(self.c.get("/api/runs").json()["runs"], [])

    def test_bad_settings_are_400_without_echo(self):
        for extra in ({"provider": "nope"}, {"provider": "claude", "model": "deepseek-flash"}, {"provider": "gpt", "model": "gpt-6-astra",
                                                                                               "thinking": "off"},
                      {"provider": "kimi", "region": "eu"}, {"usd_cap": 0}, {"usd_cap": "lots"}, {"usd_cap": True},
                      {"thinking": "max"}, {"provider": 1}, {"api_key": "short"}, {"api_key": KEY + " tail"}, {"api_key": 12345678},
                      {"question": ""}, {"as_of": "2999-01-01"}, {"question": 5}):
            r = self.c.post("/api/runs", json=self.body(**extra))
            self.assertEqual(r.status_code, 400, (extra, r.text))
            self.assertNoKey(r.text, what=str(extra))
        for raw, ctype in ((f'{{"api_key": "{KEY}", '.encode(), "application/json"), (f'"{KEY}"'.encode(), "application/json"),
                           (json.dumps(self.body()).encode(), "text/plain"), (json.dumps([self.body()]).encode(), "application/json")):
            r = self.c.post("/api/runs", content=raw, headers={"Content-Type": ctype})
            self.assertEqual(r.status_code, 422, r.text)
            self.assertNoKey(r.text)                  # FastAPI 默认的 422 会回显 body（input）；这里换掉了
        self.assertEqual(self.reg.runs, {})

    def test_defaults_and_settings_reach_the_run(self):
        r = self.c.post("/api/runs", json=self.body(provider="kimi", region="cn", model="kimi-k3", thinking="high", usd_cap=3.5))
        self.assertEqual(r.status_code, 200, r.text)
        st = self.TW.wait_for(self.c, r.json()["id"], ("awaiting_approval", "failed"))
        sp = st["run_spec"]
        self.assertEqual((sp["provider"], sp["model"], sp["region"], sp["thinking"], sp["usd_cap"], sp["price_id"]),
                         ("kimi", "kimi-k3", "cn", "high", 3.5, "kimi-k3@cn"))
        self.assertEqual(st["usd_cap"], 3.5)          # 预算用这次运行的上限
        self.assertTrue(st["key_in_memory"])          # 停在人工确认：批准后还要用，key 还在
        self.assertNoKey(json.dumps(st))
        self.c.post(f"/api/runs/{st['id']}/cancel")
        self.TW.wait_for(self.c, st["id"], ("cancelled",))
        r = self.c.post("/api/runs", json={"question": "q", "as_of": "2026-06-20", "api_key": KEY})   # 什么都不选：DeepSeek 默认
        sp = r.json()["run_spec"]
        self.assertEqual((sp["provider"], sp["model"], sp["region"], sp["thinking"], sp["usd_cap"]),
                         ("deepseek", "deepseek-flash", "global", "off", 2.0))

    def test_full_run_drops_key_and_writes_no_key(self):
        rid = self.c.post("/api/runs", json=self.body(provider="claude", model="claude-sonnet-5-5", thinking="medium")).json()["id"]
        st = self.TW.wait_for(self.c, rid, ("awaiting_approval", "failed"))
        self.assertEqual(st["status"], "awaiting_approval", st.get("error"))
        run = self.reg.get(rid)
        self.assertTrue(run._spec.has_key)
        self.c.post(f"/api/runs/{rid}/approve", json={})
        st = self.TW.wait_for(self.c, rid, ("done", "failed"))
        self.assertEqual(st["status"], "done", st.get("error"))
        self.assertFalse(st["key_in_memory"])
        self.assertFalse(run._spec.has_key)
        out = self.tmp / st["qid"] / st["tag"]
        state = json.loads((out / "state.json").read_text(encoding="utf-8"))
        self.assertEqual(state["provider"], "claude")
        self.assertEqual({k: state["settings"]["run_spec"][k] for k in ("provider", "model", "region", "thinking", "usd_cap")},
                         {"provider": "claude", "model": "claude-sonnet-5-5", "region": "global", "thinking": "medium", "usd_cap": 2.0})
        self.assertNotIn("api_key", json.dumps(state))
        for f in self.tmp.rglob("*"):
            if f.is_file():
                self.assertNoKey(f.read_text(encoding="utf-8"), what=str(f))
        res = st["result"]
        self.responses_have_no_key(self.c.get("/api/result", params=res).text, self.c.get("/api/saved").text,
                                   self.c.get("/api/graph", params=res).text,
                                   self.c.get("/api/file", params={**res, "name": "ledger.md"}).text)

    def test_key_in_model_output_is_redacted_everywhere(self):
        """兜底：key 万一出现在模型回复里（这里假模型把它写进方向的假设），状态视图、运行结束后的视图、写出的文件里都是 ***。"""
        TW = self.TW

        class Leaky(TW.FakeLLM):
            def ask(self, system, user, *, role, qid, **k):
                out, err = super().ask(system, user, role=role, qid=qid, **k)
                if role == "plan":
                    out["directions"][0]["hypothesis"] = f"leak {KEY} leak"
                return out, err
        with mock.patch.object(TW, "FakeLLM", Leaky):
            rid = self.c.post("/api/runs", json=self.body()).json()["id"]
            st = TW.wait_for(self.c, rid, ("awaiting_approval",))
            self.assertEqual(st["directions_proposed"][0]["hypothesis"], "leak *** leak")
            self.c.post(f"/api/runs/{rid}/approve", json={})
            st = TW.wait_for(self.c, rid, ("done", "failed"))
        self.assertFalse(st["key_in_memory"])
        self.assertIn("leak *** leak", json.dumps(st))   # 清 key 之前已存的文字过了一遍 redact_obj
        for f in self.tmp.rglob("*"):
            if f.is_file():
                self.assertNoKey(f.read_text(encoding="utf-8"), what=str(f))
        self.responses_have_no_key()

    def test_cancel_and_failures_drop_the_key(self):
        from triangulate.web.runs import Busy, Registry
        TW = self.TW
        rid = self.c.post("/api/runs", json=self.body()).json()["id"]
        TW.wait_for(self.c, rid, ("awaiting_approval",))
        self.c.post(f"/api/runs/{rid}/cancel")
        st = TW.wait_for(self.c, rid, ("cancelled",))
        self.assertFalse(st["key_in_memory"])
        self.assertFalse(self.reg.get(rid)._spec.has_key)

        def boom(q, tag="", spec=None):   # 出错文字里带着 key，而且 key 跨在 500 字截断的位置上
            raise RuntimeError("x" * 470 + spec.key + " tail")   # "RuntimeError: " 14 字 + 470：截断后会留下 key 的前 16 个字符
        reg = Registry(prepare=boom)
        sp = TW.byok_spec(key=KEY)
        run = reg.start("q", "2026-06-20", spec=sp)
        t = time.time()
        while run.status == "planning" and time.time() - t < 5:
            time.sleep(0.02)
        v = run.status_view()
        self.assertEqual(v["status"], "failed")
        self.assertTrue(v["error"].startswith("RuntimeError: xxx"))
        self.assertNoKey(v["error"])
        self.assertNotIn(KEY[:12], v["error"])   # 先 redact 再截断：没有留下半截 key
        self.assertTrue(v["error"].endswith("x*** tail"), v["error"][-20:])
        self.assertFalse(sp.has_key)

        with self.assertRaises(ValueError):            # 没有 spec：拒跑
            reg.start("q", "2026-06-20")
        sp2 = TW.byok_spec(key=KEY)
        with self.assertRaises(ValueError):            # 题目不合法：没登记，key 也清掉
            reg.start("  ", "2026-06-20", spec=sp2)
        self.assertFalse(sp2.has_key)
        self.gate.clear()                              # 名额占满（max_active=1）：Busy，key 清掉
        first = self.reg.start("q1", "2026-06-20", spec=TW.byok_spec(key=KEY))
        sp3 = TW.byok_spec(key=KEY)
        with self.assertRaises(Busy):
            self.reg.start("q2", "2026-06-20", spec=sp3)
        self.assertFalse(sp3.has_key)
        self.assertTrue(first._spec.has_key)
        self.gate.set()


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestClassicPageCannotStartRuns(_Client):
    def test_classic_page_is_browse_only(self):
        c = self.client()
        js = (STATIC / "app.js").read_text(encoding="utf-8")
        self.assertNotIn('post("/api/runs"', js)             # 只剩 approve / cancel 的 POST
        self.assertNotIn('id="q"', js)
        self.assertNotIn('id="go"', js)
        self.assertIn('href="/verrier#console"', js)
        self.assertIn("approve", js)
        self.assertNotIn("新问题", c.get("/").text)
        self.assertEqual(c.post("/api/runs", json={"question": "q"}).status_code, 400)   # 接口本身也不收没有 key 的运行

    def test_console_form(self):
        js = (STATIC / "verrier_console.js").read_text(encoding="utf-8")
        for s in ('"/api/providers?usd_cap="', '"/api/key/check"', 'type="password" id="cxKey"', 'id="cxRemember"', "sessionStorage",
                  'sset("local", n, v && keep ? v : null)', 'sset("session", n, v && !keep ? v : null)', "api_key: key",
                  'id="cxProv"', 'id="cxReg"', 'id="cxModel"', 'id="cxThink"', 'id="cxCap"', 'value="2.00"', ' disabled"'):
            self.assertIn(s, js)
        self.assertNotIn("TRIANGULATE_KEY_FILE", js)          # 旧的「需要 key 文件、上限 $1.00」说明已换掉
        self.assertNotIn("US$1.00", js)
        html = (STATIC / "verrier_console.html").read_text(encoding="utf-8")
        for s in (".cx-cfg{", ".cx-cfg-g{", ".cx-est{", ".cx-keyrow{"):
            self.assertIn(s, html)


# ---------- 真实路径：prepare_run / AgentLLM / Searcher / save_run + 127.0.0.1 上的假 DeepSeek ----------
class _DeepSeekHandler(BaseHTTPRequestHandler):
    """按路径和 system prompt 回复：/chat/completions（OpenAI 兼容形状）、/anthropic/v1/messages（搜索）、/models。
    JSON 调用的内容取自 tests/test_web.py 的 FakeLLM（同一套假数据）；认不出的 system prompt 回 400 并记下。"""

    def _send(self, status, obj):
        raw = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self):
        from tests.test_web import FakeLLM
        from triangulate.agent import prompts as PR
        raw = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        body = json.loads(raw)
        srv = self.server
        rec = {"path": self.path, "headers": {k.lower(): v for k, v in self.headers.items()}, "body": body}
        if self.path == "/anthropic/v1/messages":
            rec["role"] = "search"
            with srv.lock:
                srv.seen.append(rec)
            return self._send(200, {"id": "msg_fake", "type": "message", "role": "assistant", "stop_reason": "end_turn",
                                    "content": [{"type": "server_tool_use", "id": "s1", "name": "web_search", "input": {"query": "widgets"}},
                                                {"type": "web_search_tool_result", "tool_use_id": "s1",
                                                 "content": [{"type": "web_search_result", "url": "https://a.org/1", "title": "A"},
                                                             {"type": "web_search_result", "url": "https://b.org/2", "title": "B"}]},
                                                {"type": "text", "text": "https://a.org/1\nhttps://b.org/2"}],
                                    "usage": {"input_tokens": 900, "cache_read_input_tokens": 0, "output_tokens": 40,
                                              "server_tool_use": {"web_search_requests": 1}}})
        system = (body.get("messages") or [{}])[0].get("content")
        roles = {PR.PLAN_SYSTEM: "plan", PR.EXTRACT_SYSTEM: "extract", PR.JUDGE_SYSTEM: "judge:r1", PR.AUDIT_SYSTEM: "audit",
                 PR.FINAL_SYSTEM: "final"}
        rec["role"] = roles.get(system)
        with srv.lock:
            srv.seen.append(rec)
        if rec["role"] is None:
            return self._send(400, {"error": {"message": "unexpected system prompt", "type": "invalid_request_error"}})
        out, _ = FakeLLM().ask(system, "", role=rec["role"], qid="fake")
        self._send(200, {"id": "c1", "object": "chat.completion", "model": body["model"],
                         "choices": [{"index": 0, "message": {"role": "assistant", "content": json.dumps(out)}, "finish_reason": "stop"}],
                         "usage": {"prompt_tokens": 1200, "prompt_cache_hit_tokens": 200, "prompt_cache_miss_tokens": 1000,
                                   "completion_tokens": 150}})

    def log_message(self, *args):
        pass


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class TestRealPathEndToEnd(_Client):
    def test_real_prepare_run_with_user_key(self):
        import socketserver

        from triangulate import providers as PV
        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        from triangulate.agent import run as R
        from triangulate.web.runs import Registry
        from tests import test_web as TW

        class Srv(socketserver.ThreadingMixIn, socketserver.TCPServer):
            daemon_threads = True
        srv = Srv(("127.0.0.1", 0), _DeepSeekHandler)
        srv.seen, srv.lock = [], threading.Lock()
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        self.addCleanup(srv.server_close)
        self.addCleanup(srv.shutdown)
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        patches = [mock.patch.object(PV.DeepSeekAdapter, "regions", {"global": {"chat": base + "/chat/completions",
                                                                                  "search": base + "/anthropic/v1/messages",
                                                                                  "models": base + "/models"}}),
                   mock.patch.object(R, "RES", tmp), mock.patch.object(P, "fetch_page", TW.fake_fetch),
                   mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}),
                   mock.patch("triangulate.config.read_key", no_key_file), mock.patch("triangulate.llm.read_key", no_key_file),
                   mock.patch("triangulate.agent.search.read_key", no_key_file)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        reg = Registry()   # 默认的 prepare_run / save_run（真实路径）
        c = self.client(reg, res=tmp)
        r = c.post("/api/runs", json={"question": "How many widgets were sold in June 2026?", "as_of": "2026-06-20",
                                      "provider": "deepseek", "model": "deepseek-flash", "thinking": "high", "usd_cap": 1.5,
                                      "api_key": KEY})
        self.assertEqual(r.status_code, 200, r.text)
        rid = r.json()["id"]
        st = TW.wait_for(c, rid, ("awaiting_approval", "failed"))
        self.assertEqual(st["status"], "awaiting_approval", st.get("error"))
        self.assertNoKey(json.dumps(st))
        c.post(f"/api/runs/{rid}/approve", json={})
        st = TW.wait_for(c, rid, ("done", "failed"), timeout=30)
        self.assertEqual(st["status"], "done", st.get("error"))
        self.assertAlmostEqual(st["compute"]["central"], 1210.0)
        self.assertFalse(st["key_in_memory"])
        self.assertFalse(reg.get(rid)._spec.has_key)
        # key 真的用在了请求里（只发给这家的官方 URL；这里换成了假服务）
        seen = srv.seen
        self.assertTrue(seen)
        self.assertIsNone(next((x for x in seen if x["role"] is None), None))
        for x in seen:
            if x["role"] == "search":
                self.assertEqual(x["headers"]["x-api-key"], KEY)
            else:
                self.assertEqual(x["headers"]["authorization"], f"Bearer {KEY}")
        plan = next(x["body"] for x in seen if x["role"] == "plan")
        self.assertEqual((plan["thinking"], plan["reasoning_effort"], plan["max_tokens"], plan["temperature"]),
                         ({"type": "enabled"}, "high", 6000 + 24000, 0))
        ext = next(x["body"] for x in seen if x["role"] == "extract")
        self.assertEqual((ext["thinking"], "reasoning_effort" in ext), ({"type": "disabled"}, False))
        roles = {x["role"] for x in seen}
        self.assertTrue({"plan", "search", "extract", "judge:r1", "final"} <= roles <= {"plan", "search", "extract", "judge:r1", "audit",
                                                                                         "final"}, roles)
        # 结果目录里的每个文件、每个 API 返回都没有 key
        out = tmp / st["qid"] / st["tag"]
        names = {f.name for f in out.iterdir()}
        self.assertTrue({"state.json", "calls.jsonl", "ledger.md", "graph.html"} <= names, names)
        for f in tmp.rglob("*"):
            if f.is_file():
                self.assertNoKey(f.read_text(encoding="utf-8"), what=str(f))
        state = json.loads((out / "state.json").read_text(encoding="utf-8"))
        self.assertEqual(state["settings"]["run_spec"]["thinking_by_role"], {"plan": "high", "judge": "high", "repair": "high"})
        self.assertEqual(state["budget"]["usd_cap"], 1.5)
        self.assertGreater(state["budget"]["usd_total_assumed"], 0)
        calls = [json.loads(x) for x in (out / "calls.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertTrue(calls and all(x.get("ok") for x in calls), calls[:2])
        res = st["result"]
        for t in (c.get("/api/runs").text, c.get(f"/api/runs/{rid}").text, c.get("/api/result", params=res).text,
                  c.get("/api/saved").text, c.get("/api/graph", params=res).text,
                  c.get("/api/file", params={**res, "name": "ledger.md"}).text,
                  c.get("/api/file", params={**res, "name": "graph.html"}).text):
            self.assertNoKey(t)


if __name__ == "__main__":
    unittest.main()
