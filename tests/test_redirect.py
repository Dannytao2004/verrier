"""S10（v2.6g，N30、E4、D9）：带 key 的 HTTP 请求不跟随跳转。

urllib 默认把 POST 的 301/302/303 改成 GET 跟到 Location，并把 Authorization / x-api-key 原样带过去
（urllib.request.HTTPRedirectHandler.redirect_request：新请求的头 = 原请求的头去掉 content-length / content-type）。
这里在 127.0.0.1 上起两个本地 HTTP 服务：A 当作配置的端点，路径 /r<code> 回 <code> 跳转、Location 指向 B，路径 /ok 回 200；
B 是跳转目标，记下收到的每个请求。断言：四个带 key 的客户端遇到 3xx 都不重试、B 一个请求都没收到；
llm.LLM.json_call、search_direct.DirectClient.call 抛 TransportError，agent/jev.JevClient.ask 抛 JevError，
agent/search.Searcher.search 照旧不抛异常、返回带 error = "http_3xx" 的结果（结构和别的 HTTP 错误相同）；200 照常解析。
只连 127.0.0.1；不读 key 文件（key 是写死的假字符串）；calls.jsonl 写到临时目录，不碰 data/、results/。"""
import json
import socketserver
import tempfile
import threading
import unittest
import urllib.request
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from unittest import mock

from triangulate import llm, search_direct as SD
from triangulate.agent import jev as J, search as S

KEY = "sk-redirect-test-0001"
CODES = (301, 302, 303, 307, 308)
CRIT = {"A": "The target resolves to: A", "B": "The target resolves to: B"}
# 一个 200 回复同时满足四个客户端：chat/completions 的 choices、Anthropic 接口的 content、Jev 的 answers
OK_BODY = {"choices": [{"message": {"content": '{"ok": 1}'}, "finish_reason": "stop"}],
           "content": [{"type": "text", "text": "https://example.org/a-page"}], "stop_reason": "end_turn",
           "answers": {"outcome": {"type": "choice", "choice": "B", "probabilities": {"A": 0.25, "B": 0.75}}},
           "model": "fake", "usage": {"input_tokens": 10, "output_tokens": 2}}


class _Handler(BaseHTTPRequestHandler):
    def _serve(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n:
            self.rfile.read(n)
        self.server.seen.append((self.command, self.path, {k.lower(): v for k, v in self.headers.items()}))
        if self.path.startswith("/r"):
            self.send_response(int(self.path[2:]))
            self.send_header("Location", self.server.location)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        body = json.dumps(OK_BODY).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    do_GET = do_POST = _serve

    def log_message(self, *args):
        pass


class _Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """不用 http.server.HTTPServer：它的 server_bind 会调 socket.getfqdn（反查主机名）。"""
    daemon_threads = True


def _start(location: str = "") -> _Server:
    srv = _Server(("127.0.0.1", 0), _Handler)
    srv.seen, srv.location = [], location
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class TestKeyNotForwardedOnRedirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.B = _start()
        cls.A = _start(location=f"http://127.0.0.1:{cls.B.server_address[1]}/landing")

    @classmethod
    def tearDownClass(cls):
        for srv in (cls.A, cls.B):
            srv.shutdown()
            srv.server_close()

    def setUp(self):
        self.A.seen.clear()
        self.B.seen.clear()

    def url(self, path: str) -> str:
        return f"http://127.0.0.1:{self.A.server_address[1]}/{path}"

    def assert_sent_once_to_a_only(self, header: str, value: str):
        """A（配置的端点）收到正好一个带 key 的 POST；B（跳转目标）什么都没收到。"""
        self.assertEqual([(m, h.get(header)) for m, _, h in self.A.seen], [("POST", value)])
        self.assertEqual(self.B.seen, [])

    def test_plain_urlopen_would_forward_the_key(self):
        """对照组：同一套本地服务下，标准库默认的 urlopen 跟随跳转，B 收到带 key 的 GET。证明下面的断言不是空过。"""
        for code in (301, 302, 303):
            with self.subTest(code=code):
                self.setUp()
                req = urllib.request.Request(self.url(f"r{code}"), data=b"{}", method="POST",
                                             headers={"Authorization": f"Bearer {KEY}"})
                with urllib.request.urlopen(req, timeout=10) as r:
                    self.assertEqual(r.status, 200)
                self.assertEqual([(m, h.get("authorization")) for m, _, h in self.B.seen], [("GET", f"Bearer {KEY}")])

    def test_llm_json_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            client = object.__new__(llm.LLM)   # 不走 __init__：不读 key 文件
            client.model, client.calls_path, client._key = "fake", Path(tmp) / "calls.jsonl", KEY
            for code in CODES:
                with self.subTest(code=code):
                    self.setUp()
                    with mock.patch.object(llm, "API_URL", self.url(f"r{code}")), mock.patch("time.sleep") as sleep:
                        with self.assertRaises(llm.TransportError) as cm:
                            client.json_call([{"role": "user", "content": "x"}], arm="judge:r1", qid="t", attempt=1)
                    self.assertIn(f"judge:r1 t attempt 1: http_{code} redirect not followed", str(cm.exception))
                    sleep.assert_not_called()   # 不重试
                    self.assert_sent_once_to_a_only("authorization", f"Bearer {KEY}")
            logged = [json.loads(x) for x in (Path(tmp) / "calls.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual([(r["http"], r["error"], r["ok"]) for r in logged], [(c, f"http_{c}", False) for c in CODES])
        self.assertNotIn(KEY, json.dumps(logged))

    def test_searcher_search(self):
        logged = []
        s = object.__new__(S.Searcher)   # 不走 __init__：不读 key 文件
        s.model, s._key, s._log = "fake", KEY, logged.append
        for code in CODES:
            with self.subTest(code=code):
                self.setUp()
                with mock.patch.object(S, "SEARCH_URL", self.url(f"r{code}")), mock.patch("time.sleep") as sleep:
                    out = s.search("p", role="search:d1", qid="t")
                # 返回结构和别的 HTTP 错误相同（不抛异常，run_direction 照旧记下 error）
                self.assertEqual(out, {"queries": [], "urls": [], "error": f"http_{code}", "web_search_requests": 0,
                                       "usd": 0.0, "usd_search_fee_assumed": 0.0})
                sleep.assert_not_called()
                self.assert_sent_once_to_a_only("x-api-key", KEY)
        self.assertEqual([r["error"] for r in logged], [f"http_{c}" for c in CODES])
        self.assertNotIn(KEY, json.dumps(logged))

    def test_direct_client_call(self):
        logged = []
        d = object.__new__(SD.DirectClient)   # 不走 __init__：不读 key 文件
        d.model, d._key, d._log = "fake", KEY, logged.append
        for code in CODES:
            with self.subTest(code=code):
                self.setUp()
                with mock.patch.object(SD, "SEARCH_URL", self.url(f"r{code}")), mock.patch("time.sleep") as sleep:
                    with self.assertRaises(llm.TransportError) as cm:
                        d.call({"model": "fake"}, qid="t", attempt=1)
                self.assertIn(f"search_direct t attempt 1: http_{code} redirect not followed", str(cm.exception))
                sleep.assert_not_called()
                self.assert_sent_once_to_a_only("x-api-key", KEY)
        self.assertEqual([r["error"] for r in logged], [f"http_{c}" for c in CODES])
        self.assertNotIn(KEY, json.dumps(logged))

    def test_jev_client_ask(self):
        sleeps = []
        client = J.JevClient(KEY, sleep=sleeps.append)   # 默认的 _urllib_post，真实走本地 HTTP
        for code in CODES:
            with self.subTest(code=code):
                self.setUp()
                with mock.patch.object(J, "API_URL", self.url(f"r{code}")):
                    with self.assertRaises(J.JevError) as cm:
                        client.ask("state", CRIT)
                self.assertIn(f"HTTP {code} redirect not followed", str(cm.exception))
                self.assertNotIn(KEY, str(cm.exception))
                self.assert_sent_once_to_a_only("authorization", f"Bearer {KEY}")
        self.assertEqual(sleeps, [])

    def test_200_still_parsed(self):
        ok = self.url("ok")
        with tempfile.TemporaryDirectory() as tmp:
            client = object.__new__(llm.LLM)
            client.model, client.calls_path, client._key = "deepseek-flash", Path(tmp) / "calls.jsonl", KEY
            with mock.patch.object(llm, "API_URL", ok):
                out, _, err = client.json_call([{"role": "user", "content": "x"}], arm="judge:r1", qid="t", attempt=1)
        self.assertEqual((out, err), ({"ok": 1}, None))
        s = object.__new__(S.Searcher)
        s.model, s._key, s._log = "deepseek-flash", KEY, lambda rec: None
        with mock.patch.object(S, "SEARCH_URL", ok):
            self.assertEqual(s.search("p", role="search:d1", qid="t")["urls"], ["https://example.org/a-page"])
        d = object.__new__(SD.DirectClient)
        d.model, d._key, d._log = "deepseek-flash", KEY, lambda rec: None
        with mock.patch.object(SD, "SEARCH_URL", ok):
            self.assertEqual(d.call({"model": "fake"}, qid="t", attempt=1)["stop_reason"], "end_turn")
        with mock.patch.object(J, "API_URL", ok):
            self.assertEqual(J.JevClient(KEY).ask("state", CRIT)["probabilities"], {"A": 0.25, "B": 0.75})
        self.assertEqual([(m, p, h.get("authorization") or h.get("x-api-key")) for m, p, h in self.A.seen],
                         [("POST", "/ok", f"Bearer {KEY}"), ("POST", "/ok", KEY), ("POST", "/ok", KEY),
                          ("POST", "/ok", f"Bearer {KEY}")])
        self.assertEqual(self.B.seen, [])


if __name__ == "__main__":
    unittest.main()
