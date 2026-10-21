"""v2.10f：五家 provider 各跑完整的网页运行，走真实路径：POST /api/runs -> Registry -> prepare_run -> AgentLLM / Searcher（真实的 adapter、
urllib、urlopen_no_redirect）-> save_run。所有 provider 的 URL 都换成 127.0.0.1 上的一个假服务（按路径和 system prompt 回复，内容同
tests/test_web.py 的 FakeLLM）。key 都是假的；不读 key 文件、不联网。

检查：每家都能跑完（done，估计 1210）、每个请求都带着用户的 key、请求体按各家的规则（采样参数、思考字段、max tokens 不超过模型上限）、
写出的文件和 API 返回里没有 key（半截也没有）、结束后 key 已从内存清掉；搜索阶段余额不足（402 / 429）时网页状态是 failed、error 有说明；
中途花费超过上限时同样 failed；上限放不下一次最小运行的组合在服务端拒跑、一个请求都不发；贵模型第一轮同时在途的搜索放不下时排队跑完
（不再中止）；服务端的错误说明里带着 key（截断位置落在 key 中间）时也不留半截；停在人工确认超时自动结束并清 key。
（审查脚本 e2e_all.py 整理而来。）
"""
import json
import shutil
import socketserver
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


def no_key_file(*a, **k):
    raise AssertionError("a web run must never read the server's key file")


def _key(i: int, provider: str) -> str:
    if provider == "glm":   # GLM 的 key 形状：32 位 hex . 16 位
        return f"{i:02d}a1b2c3d4e5f60718293a4b5c6d7e8f".ljust(32, "0")[:32] + f".ZyXwVuTsRqPoNm{i:02d}"
    return f"sk-e2e{i:02d}-SECRET-{provider}-0123456789abcdefQRSTUV"


class _State:
    """假服务的脚本（每个测试设）：key、模式、搜索延迟、规划给几个方向。"""
    key = None
    mode = "normal"          # normal / broke_search / leaky / huge_usage
    search_delay = 0.0
    n_directions = 3


def _role_of(system):
    from triangulate.agent import prompts as PR
    return {PR.PLAN_SYSTEM: "plan", PR.EXTRACT_SYSTEM: "extract", PR.JUDGE_SYSTEM: "judge:r1", PR.AUDIT_SYSTEM: "audit",
            PR.FINAL_SYSTEM: "final", PR.SEARCH_QUERIES_SYSTEM: "queries"}.get(system)


def _answer(role):
    from tests.test_web import FakeLLM
    if role == "queries":
        return {"queries": ["widgets June 2026 official", "widgets 2025 statistics"]}
    out, _ = FakeLLM().ask("", "", role=role, qid="fake")
    if role == "plan":
        cats = ("own_history", "physical_flow", "attention", "related_series", "administrative", "capacity_consumption")
        out["directions"] = [{"category": cats[i % len(cats)], "hypothesis": f"h{i + 1}", "data_to_find": "f"}
                             for i in range(_State.n_directions)]
    return out


class _Handler(BaseHTTPRequestHandler):
    def _json(self, status, obj):
        raw = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def _sse(self, chunks):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        for c in chunks:
            self.wfile.write(c.encode())
            self.wfile.flush()

    def do_GET(self):
        self._json(200, {"object": "list", "data": [{"id": "x"}]})

    def _search(self, path, body):
        """搜索接口（模型自己搜的四种 + 两种搜索接口）。broke_search 模式：按各家文档的余额不足回复。"""
        broke = _State.mode == "broke_search"
        big = _State.mode == "huge_usage"
        usage_in = 3_000_000 if big else 9000
        if path.startswith("/claude/"):
            if broke:
                return self._json(402, {"type": "error", "error": {"type": "billing_error", "message": "billing"}})
            return self._json(200, {"id": "m", "type": "message", "role": "assistant", "stop_reason": "end_turn", "content": [
                {"type": "server_tool_use", "id": "s1", "name": "web_search", "input": {"query": "widgets"}},
                {"type": "web_search_tool_result", "tool_use_id": "s1", "content": [
                    {"type": "web_search_result", "url": "https://a.org/1", "title": "A"},
                    {"type": "web_search_result", "url": "https://b.org/2", "title": "B"}]},
                {"type": "text", "text": "https://a.org/1\nhttps://b.org/2"}],
                "usage": {"input_tokens": usage_in, "cache_read_input_tokens": 0, "output_tokens": 400,
                          "server_tool_use": {"web_search_requests": 2}}})
        if path.endswith("/anthropic/v1/messages"):
            if broke:
                return self._json(402, {"error": {"message": "Insufficient Balance"}})
            return self._json(200, {"stop_reason": "end_turn", "content": [
                {"type": "web_search_tool_result", "content": [{"type": "web_search_result", "url": "https://a.org/1"}]},
                {"type": "text", "text": "https://a.org/1"}],
                "usage": {"input_tokens": usage_in, "output_tokens": 400, "server_tool_use": {"web_search_requests": 2}}})
        if path.endswith("/v1/responses"):
            if broke:
                return self._json(429, {"error": {"message": "You exceeded your current quota", "type": "insufficient_quota",
                                                  "param": None, "code": "credit_balance_exhausted"}})
            return self._json(200, {"id": "r", "status": "completed", "output": [
                {"type": "web_search_call", "status": "completed",
                 "action": {"type": "search", "queries": ["widgets"], "sources": [{"type": "url", "url": "https://a.org/1"}]}},
                {"type": "message", "content": [{"type": "output_text", "text": "https://a.org/1",
                                                 "annotations": [{"type": "url_citation", "url": "https://b.org/2", "title": "B"}]}]}],
                "usage": {"input_tokens": usage_in, "input_tokens_details": {"cached_tokens": 0}, "output_tokens": 400,
                          "output_tokens_details": {"reasoning_tokens": 100}}})
        if path.endswith("/tools/search"):
            if broke:
                return self._json(429, {"error": {"message": "Account balance is insufficient", "type": "exceeded_current_quota_error"}})
            return self._json(200, {"search_results": [{"url": "https://a.org/1", "title": "A"}, {"url": "https://b.org/2", "title": "B"}]})
        if broke:   # GLM /web_search
            return self._json(429, {"error": {"code": "1113", "message": "Insufficient balance or no resource package. Please recharge."}})
        return self._json(200, {"id": "w", "search_result": [{"link": "https://a.org/1", "title": "A"}, {"link": "https://b.org/2", "title": "B"}]})

    def do_POST(self):
        srv = self.server
        raw = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        body = json.loads(raw)
        path = self.path
        rec = {"path": path, "headers": {k.lower(): v for k, v in self.headers.items()}, "body": body}
        with srv.lock:
            srv.seen.append(rec)
        is_search = ((path.startswith("/claude/") and "tools" in body) or path.endswith("/anthropic/v1/messages")
                     or path.endswith("/v1/responses") or path.endswith("/tools/search") or path.endswith("/web_search"))
        if is_search:
            rec["role"] = "search"
            if _State.search_delay:
                time.sleep(_State.search_delay)
            return self._search(path, body)
        system = body.get("system") if path.startswith("/claude/") else (body.get("messages") or [{}])[0].get("content")
        role = rec["role"] = _role_of(system)
        if role is None:
            return self._json(400, {"error": {"message": "unexpected system prompt", "type": "invalid_request_error"}})
        if _State.mode == "leaky" and role == "audit":
            # 假设某家在 401 / 403 以外的错误里回显了 key，而且 200 字的截断落在 key 中间
            msg = "x" * 185 + " key=" + _State.key + " end"
            if path.startswith("/claude/"):
                return self._json(400, {"type": "error", "error": {"type": "invalid_request_error", "message": msg}})
            if path.startswith("/glm/"):
                return self._json(400, {"error": {"code": "1210", "message": msg}})
            return self._json(400, {"error": {"message": msg, "type": "invalid_request_error", "code": "bad"}})
        text = json.dumps(_answer(role))
        if path.startswith("/claude/"):
            ev = [("message_start", {"type": "message_start", "message": {"id": "m", "type": "message", "role": "assistant",
                                                                          "content": [], "stop_reason": None,
                                                                          "usage": {"input_tokens": 1200, "output_tokens": 1}}}),
                  ("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}}),
                  ("content_block_stop", {"type": "content_block_stop", "index": 0}),
                  ("content_block_start", {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}}),
                  ("content_block_delta", {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": text}}),
                  ("content_block_stop", {"type": "content_block_stop", "index": 1}),
                  ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 150}}),
                  ("message_stop", {"type": "message_stop"})]
            return self._sse([f"event: {n}\ndata: {json.dumps(d)}\n\n" for n, d in ev])
        if path.startswith("/kimi/"):
            chunks = [{"choices": [{"index": 0, "delta": {"role": "assistant", "reasoning_content": "hmm"}}]},
                      {"choices": [{"index": 0, "delta": {"content": text}}]},
                      {"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]},
                      {"choices": [], "usage": {"prompt_tokens": 1200, "completion_tokens": 150,
                                                "prompt_tokens_details": {"cached_tokens": 200}}}]
            return self._sse([f"data: {json.dumps(c)}\n\n" for c in chunks] + ["data: [DONE]\n\n"])
        usage = {"prompt_tokens": 1200, "completion_tokens": 150}
        if path.startswith("/ds/"):
            usage.update(prompt_cache_hit_tokens=200, prompt_cache_miss_tokens=1000)
        else:
            usage["prompt_tokens_details"] = {"cached_tokens": 200}
        return self._json(200, {"id": "c", "object": "chat.completion", "model": body["model"],
                                "choices": [{"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": "stop"}],
                                "usage": usage})

    def log_message(self, *a):
        pass


class _Srv(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


@unittest.skipUnless(HAVE_WEB, "fastapi / langgraph not installed (use .venv)")
class _E2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = _Srv(("127.0.0.1", 0), _Handler)
        cls.srv.seen, cls.srv.lock = [], threading.Lock()
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def setUp(self):
        from fastapi.testclient import TestClient

        from tests import test_web as TW
        from triangulate import providers as PV
        from triangulate.agent import graph as G
        from triangulate.agent import pipeline as P
        from triangulate.agent import run as R
        from triangulate.web.app import create_app
        from triangulate.web.runs import Registry
        self.TW = TW
        base = f"http://127.0.0.1:{self.srv.server_address[1]}"
        regs = {
            PV.DeepSeekAdapter: {"global": {"chat": base + "/ds/chat/completions", "search": base + "/ds/anthropic/v1/messages",
                                            "models": base + "/ds/models"}},
            PV.ClaudeAdapter: {"global": {"chat": base + "/claude/v1/messages", "search": base + "/claude/v1/messages",
                                          "models": base + "/claude/v1/models"}},
            PV.OpenAIAdapter: {"global": {"chat": base + "/gpt/v1/chat/completions", "search": base + "/gpt/v1/responses",
                                          "models": base + "/gpt/v1/models"}},
            PV.KimiAdapter: {r: {"chat": base + f"/kimi/{r}/v1/chat/completions", "search": base + f"/kimi/{r}/v1/tools/search",
                                 "models": base + f"/kimi/{r}/v1/models"} for r in ("global", "cn")},
            PV.GLMAdapter: {r: {"chat": base + f"/glm/{r}/chat/completions", "search": base + f"/glm/{r}/web_search",
                                "models": base + f"/glm/{r}/models"} for r in ("global", "cn")},
        }
        self.tmp = Path(tempfile.mkdtemp())
        patches = [mock.patch.object(cls, "regions", v) for cls, v in regs.items()]
        patches += [mock.patch.object(R, "RES", self.tmp), mock.patch.object(P, "fetch_page", TW.fake_fetch),
                    mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "x"}),
                    mock.patch("triangulate.config.read_key", no_key_file), mock.patch("triangulate.llm.read_key", no_key_file),
                    mock.patch("triangulate.agent.search.read_key", no_key_file),
                    mock.patch("triangulate.agent.jev.key_file", no_key_file)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        _State.mode, _State.search_delay, _State.n_directions, _State.key = "normal", 0.0, 3, None
        self.addCleanup(setattr, _State, "mode", "normal")
        self.reg = Registry(max_active=1, approval_timeout_s=self.approval_timeout_s)
        self.c = TestClient(create_app(self.reg, res=self.tmp), base_url="http://127.0.0.1")
        self.addCleanup(self._wait_all)
        self.addCleanup(shutil.rmtree, self.tmp, True)

    approval_timeout_s = 600

    def _wait_all(self):
        for r in self.reg.runs.values():
            t = time.time()
            while r.status in ("planning", "running") and time.time() - t < 20:
                time.sleep(0.05)

    def start(self, i, prov, model, region, think, cap, approve=True):
        key = _key(i, prov)
        _State.key = key
        with self.srv.lock:
            self.srv.seen.clear()
        r = self.c.post("/api/runs", json={"question": f"How many widgets were sold in June 2026? case {i}", "as_of": "2026-06-20",
                                           "provider": prov, "model": model, "region": region, "thinking": think, "usd_cap": cap,
                                           "api_key": key})
        if r.status_code != 200:
            return key, r, None
        rid = r.json()["id"]
        st = self.TW.wait_for(self.c, rid, ("awaiting_approval", "failed"), timeout=60)
        if approve and st["status"] == "awaiting_approval":
            self.c.post(f"/api/runs/{rid}/approve", json={})
            st = self.TW.wait_for(self.c, rid, ("done", "failed"), timeout=120)
        return key, r, st

    def texts(self, st):
        """这次运行的所有 API 返回和结果目录里的所有文件。"""
        rid = st["id"]
        out = {"status": self.c.get(f"/api/runs/{rid}").text, "list": self.c.get("/api/runs").text}
        if st.get("result"):
            res = st["result"]
            for name, path, params in (("result", "/api/result", res), ("saved", "/api/saved", None), ("graph", "/api/graph", res),
                                       ("ledger", "/api/file", {**res, "name": "ledger.md"}),
                                       ("graph.html", "/api/file", {**res, "name": "graph.html"})):
                out[name] = self.c.get(path, params=params).text
        d = self.tmp / st["qid"] / st["tag"]
        for f in d.rglob("*") if d.exists() else []:
            if f.is_file():
                out[f.name] = f.read_text(encoding="utf-8")
        return out

    def assertNoKey(self, texts, key):
        frags = {key, key[:9], key[3:20], key[-12:]}
        for name, t in texts.items():
            for fr in frags:
                self.assertNotIn(fr, t, (name, fr))

    def state(self, st):
        return json.loads((self.tmp / st["qid"] / st["tag"] / "state.json").read_text(encoding="utf-8"))


class TestEveryProviderRunsToTheEnd(_E2E):
    CASES = [("deepseek", "deepseek-flash", "global", "high", 2.0),
             ("claude", "claude-haiku-5-5", "global", "off", 2.0),
             ("claude", "claude-sonnet-5-5", "global", "off", 2.0),
             ("claude", "claude-opus-5-5", "global", "high", 20.0),
             ("gpt", "gpt-6-luna", "global", "off", 2.0),
             ("gpt", "gpt-6.1-sol", "global", "medium", 20.0),
             ("kimi", "kimi-k2.6", "global", "off", 2.0),
             ("kimi", "kimi-k3", "cn", "high", 20.0),
             ("glm", "glm-5.2", "global", "off", 2.0),
             ("glm", "glm-5.3", "cn", "low", 5.0),
             ("glm", "glm-4.7-flashx", "global", "high", 2.0)]

    def test_successful_runs(self):
        from triangulate import providers as PV
        for i, (prov, model, region, think, cap) in enumerate(self.CASES):
            with self.subTest(case=f"{prov}/{model}/{region}/{think}/${cap}"):
                key, r, st = self.start(i, prov, model, region, think, cap)
                self.assertEqual(r.status_code, 200, r.text)
                self.assertEqual(st["status"], "done", st.get("error"))
                self.assertAlmostEqual(st["compute"]["central"], 1210.0)
                self.assertFalse(st["key_in_memory"])
                self.assertIsNone(st["error"])
                seen = list(self.srv.seen)
                self.assertIsNone(next((x for x in seen if x.get("role") is None), None))
                for x in seen:   # 每个请求都带着用户的 key
                    self.assertIn(key, x["headers"].get("authorization", "") + x["headers"].get("x-api-key", ""), x["path"])
                roles = {x["role"] for x in seen}
                want = {"plan", "search", "extract", "judge:r1", "final"} | ({"queries"} if prov in ("kimi", "glm") else set())
                self.assertTrue(want <= roles, roles)
                max_out = PV.MODELS[model]["max_output"]
                for x in seen:
                    b = x["body"]
                    sent = b.get("max_tokens") or b.get("max_completion_tokens") or b.get("max_output_tokens") or 0
                    self.assertLessEqual(sent, max_out, (x["role"], sent))
                    if prov in ("claude", "kimi", "glm"):   # 用户决定 5：这几家不发 temperature
                        self.assertNotIn("temperature", b, x["role"])
                    if prov == "gpt" and x["role"] != "search":   # GPT：只有 reasoning_effort = none 时发 temperature 0
                        self.assertEqual("temperature" in b, b.get("reasoning_effort") == "none", x["role"])
                        self.assertIs(b["store"], False)
                    if prov == "deepseek" and x["role"] == "search":   # v2.10g：DeepSeek 搜索保持 v2.9b 原样（用户 10-21），不带 thinking
                        self.assertNotIn("thinking", b)
                state = self.state(st)
                self.assertEqual((state["provider"], state["settings"]["run_spec"]["model"]), (prov, model))
                self.assertTrue(state["budget"]["waited_for_room"] >= 0)
                self.assertEqual(state["budget"]["aborted"], "")
                self.assertNoKey(self.texts(st), key)


class TestStopsAreVisible(_E2E):
    def test_balance_runs_out_during_search(self):
        """搜索阶段余额不足（各家文档写的回复：DeepSeek 402、Claude 402 billing_error、OpenAI 429 credit_balance_exhausted、
        Kimi 429 exceeded_current_quota_error、GLM 429 1113）：网页状态是 failed，error 写明余额不足（审查发现：以前是 done、error 为空），
        state.json 的 aborted 有原因，终稿写明运行被停下，运行列表里也看得到。"""
        _State.mode = "broke_search"
        cases = [("deepseek", "deepseek-flash", "global", "off", "insufficient balance: DeepSeek HTTP 402 Insufficient Balance"),
                 ("claude", "claude-haiku-5-5", "global", "off", "insufficient balance: Claude HTTP 402 billing_error"),
                 ("gpt", "gpt-6-luna", "global", "off",
                  "insufficient balance: OpenAI HTTP 429 credit_balance_exhausted (no prepaid credits left)"),
                 ("kimi", "kimi-k2.6", "global", "off", "insufficient balance: Kimi HTTP 429 exceeded_current_quota_error"),
                 ("glm", "glm-5.2", "cn", "off", "insufficient balance: GLM HTTP 429 code 1113")]
        for i, (prov, model, region, think, want) in enumerate(cases):
            with self.subTest(provider=prov):
                key, r, st = self.start(20 + i, prov, model, region, think, 2.0)
                self.assertEqual(st["status"], "failed", st)
                self.assertTrue(st["error"].startswith(want), st["error"])
                self.assertIn("the run was stopped without retrying", st["error"])
                self.assertIsNone(st["compute"]["central"])
                self.assertFalse(st["key_in_memory"])
                brief = next(x for x in self.c.get("/api/runs").json()["runs"] if x["id"] == st["id"])
                self.assertEqual((brief["status"], brief["error"]), ("failed", st["error"]))
                state = self.state(st)
                self.assertTrue(state["aborted"].startswith(want), state["aborted"])
                self.assertEqual(state["budget"]["aborted"], state["aborted"])
                self.assertTrue(state["final"]["text"].startswith("No estimate: the run was stopped before an estimate could be made "
                                                                  f"({want}"), state["final"]["text"])
                # 不重试：3 个方向同时开搜，每个方向最多发出一个搜索请求（第一个 402 / 429 回来以后，之后的预扣全部拒绝）
                self.assertLessEqual(len([x for x in self.srv.seen if x["role"] == "search"]), 3)
                self.assertNotIn("judge:r1", {x["role"] for x in self.srv.seen})
                self.assertNoKey(self.texts(st), key)

    def test_spending_past_the_cap_mid_run_is_failed(self):
        """服务端报的用量很大（一次搜索 300 万输入 token）：记账后超过上限，之后的预扣都拒绝，没有估计：failed，error 写原因。"""
        _State.mode = "huge_usage"
        key, r, st = self.start(30, "deepseek", "deepseek-flash", "global", "off", 0.5)
        self.assertEqual(st["status"], "failed", st)
        self.assertTrue(st["error"].startswith("usd cap 0.5 exceeded"), st["error"])
        self.assertTrue(self.state(st)["final"]["text"].startswith("No estimate: the run was stopped"))

    def test_cap_that_cannot_cover_a_minimal_run_is_refused(self):
        """审查发现：Opus 5.5 + $2 第一轮就中止（钱已经花了）。现在服务端直接拒跑（400，说明最小上限），一个请求都不发，key 不留。"""
        from triangulate.web import catalog as C
        key, r, st = self.start(31, "claude", "claude-opus-5-5", "global", "low", 2.0)
        self.assertEqual(r.status_code, 400, r.text)
        floor = C.run_floor("claude-opus-5-5", "global", "low")["usd"]
        self.assertIn(f"${C.min_cap(floor):.2f}", r.json()["detail"])
        self.assertIn("cannot cover the worst case of a minimal run", r.json()["detail"])
        self.assertNotIn(key, r.text)
        self.assertEqual(self.srv.seen, [])
        self.assertEqual(self.reg.runs, {})
        for prov, model, think in (("claude", "claude-fable-5-1", "low"), ("gpt", "gpt-6-astra", "low"), ("gpt", "gpt-6.1-sol", "low"),
                                   ("kimi", "kimi-k3", "low")):
            with self.subTest(model=model):
                self.assertEqual(self.start(32, prov, model, "global", think, 2.0)[1].status_code, 400)
        self.assertEqual(self.srv.seen, [])

    def test_expensive_model_queues_instead_of_aborting(self):
        """审查发现：Opus 5.5 在第一轮同时在途的搜索预扣放不下时整次运行中止。现在预扣只是因为在途的调用放不下时等：
        6 个方向、每次搜索预扣约 $1.01、上限 $5：最多 4 个同时在途，其余排队，跑完、不中止。"""
        _State.n_directions, _State.search_delay = 6, 0.3
        key, r, st = self.start(33, "claude", "claude-opus-5-5", "global", "low", 5.0)
        self.assertEqual(r.status_code, 200, r.text)
        self.assertEqual(st["status"], "done", st.get("error"))
        state = self.state(st)
        self.assertEqual(state["budget"]["aborted"], "")
        self.assertEqual(len(state["directions"]), 6)
        self.assertGreater(state["budget"]["waited_for_room"], 0)
        self.assertEqual(sum(1 for x in self.srv.seen if x["role"] == "search"), 6)
        self.assertAlmostEqual(st["compute"]["central"], 1210.0)

    def test_server_message_quoting_the_key_leaves_no_fragment(self):
        """兜底（审查发现）：服务端在 400 的 message 里回显了 key，200 字的截断落在 key 中间。先 redact 再截断：哪里都没有半截 key
        （GLM 的 key 不以 sk- 开头，以前会留下前 10 个字符）。"""
        _State.mode = "leaky"
        for i, (prov, model, region) in enumerate((("glm", "glm-5.2", "global"), ("claude", "claude-haiku-5-5", "global"),
                                                   ("kimi", "kimi-k2.6", "global"))):
            with self.subTest(provider=prov):
                key, r, st = self.start(40 + i, prov, model, region, "off", 2.0)
                self.assertIn(st["status"], ("done", "failed"))
                calls = (self.tmp / st["qid"] / st["tag"] / "calls.jsonl").read_text(encoding="utf-8")
                self.assertIn('"arm": "audit"', calls)
                self.assertNoKey(self.texts(st), key)


class TestApprovalTimeout(_E2E):
    approval_timeout_s = 0.5

    def test_waiting_for_approval_times_out_and_drops_the_key(self):
        """停在人工确认超过时限：按「不批准」结束（cancelled），key 清掉，名额退回，error 写明原因。"""
        key, r, st = self.start(50, "deepseek", "deepseek-flash", "global", "off", 2.0, approve=False)
        self.assertEqual(st["status"], "awaiting_approval")
        self.assertTrue(st["key_in_memory"])
        st = self.TW.wait_for(self.c, st["id"], ("cancelled", "failed"), timeout=10)
        self.assertEqual(st["status"], "cancelled")
        self.assertFalse(st["key_in_memory"])
        self.assertEqual(st["approvals"][-1], {"approved": False, "by": "web-timeout"})
        self.assertIn("not approved within", st["error"])
        self.assertEqual(st["directions"], [])
        self.assertEqual(self.c.post(f"/api/runs/{st['id']}/approve", json={}).status_code, 409)
        self.assertEqual(self.start(51, "deepseek", "deepseek-flash", "global", "off", 2.0, approve=False)[1].status_code, 200)
        self.assertNoKey(self.texts(st), key)

    def test_approving_in_time_cancels_the_timer(self):
        key, r, st = self.start(52, "deepseek", "deepseek-flash", "global", "off", 2.0, approve=False)
        self.assertIsNotNone(self.reg.get(st["id"])._timer)
        self.c.post(f"/api/runs/{st['id']}/approve", json={})
        self.assertIsNone(self.reg.get(st["id"])._timer)   # 批准时计时器停掉
        st = self.TW.wait_for(self.c, st["id"], ("done", "failed"), timeout=60)
        time.sleep(0.7)
        st = self.c.get(f"/api/runs/{st['id']}").json()
        self.assertEqual(st["status"], "done", st.get("error"))
        self.assertEqual([a["by"] for a in st["approvals"]], ["web"])


if __name__ == "__main__":
    unittest.main()
