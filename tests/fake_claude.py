"""v2.10b：127.0.0.1 上的假 Anthropic Messages API，给 tests/test_claude.py 用。不联网、不需要真 key。

按脚本依次回复，记下每个请求（方法、路径含查询串、请求头小写、JSON body）。脚本的每一项：
  ("json", status, obj[, headers])   JSON body（错误回复就是官方 Errors 页的形状）
  ("sse", events[, status])          流式回复：events 是 [(事件名, data dict), ...]，按官方 Streaming 页的格式逐个写出
  ("raw", status, body_bytes[, headers])
  ("redirect", status, location)
脚本用完以后的请求回 500（测试里应该当作失败）。用 regions() 换掉 providers.ClaudeAdapter.regions，客户端就连到这里。
"""
import json
import socketserver
import threading
from http.server import BaseHTTPRequestHandler

# 2026-10-20 / 10-21 对 https://api.anthropic.com/v1/models 不带 key、带假 key 实测的回复（HTTP 401，x-should-retry: false）
REAL_401_NO_KEY = {"type": "error", "error": {"type": "authentication_error", "message": "x-api-key header is required"},
                   "request_id": "req_011CgEsvKywoum2W5i36Eb1K"}
REAL_401_FAKE_KEY = {"type": "error", "error": {"type": "authentication_error", "message": "invalid x-api-key"},
                     "request_id": "req_011CgEsvLPWP8tUmD8K39fBt"}


def error_body(etype: str, message: str, **extra) -> dict:
    """官方 Errors 页的错误形状：{"type": "error", "error": {"type", "message"}, "request_id"}。"""
    return {"type": "error", "error": {"type": etype, "message": message, **extra}, "request_id": "req_fake_0001"}


def sse_message(blocks, stop_reason="end_turn", usage=None, model="claude-opus-5-5", stop_details=None, pings=1,
                start_usage=None):
    """一条完整的流式回复。blocks：[("thinking", ""), ("text", "..."), ...]；文字分两段 text_delta 发，思考按 display omitted
    的样子（空的 thinking_delta + 一个 signature_delta）。usage 放在 message_delta（累计值），start_usage 放在 message_start。"""
    ev = [("message_start", {"type": "message_start", "message": {
        "id": "msg_fake", "type": "message", "role": "assistant", "content": [], "model": model, "stop_reason": None,
        "stop_sequence": None, "usage": start_usage or {"input_tokens": 0, "output_tokens": 1}}})]
    for i, (kind, text) in enumerate(blocks):
        if kind == "thinking":
            ev.append(("content_block_start", {"type": "content_block_start", "index": i,
                                               "content_block": {"type": "thinking", "thinking": "", "signature": ""}}))
            ev.append(("content_block_delta", {"type": "content_block_delta", "index": i,
                                               "delta": {"type": "thinking_delta", "thinking": text}}))
            ev.append(("content_block_delta", {"type": "content_block_delta", "index": i,
                                               "delta": {"type": "signature_delta", "signature": "EqQBsig"}}))
        else:
            ev.append(("content_block_start", {"type": "content_block_start", "index": i,
                                               "content_block": {"type": "text", "text": ""}}))
            for _ in range(pings):
                ev.append(("ping", {"type": "ping"}))
            half = len(text) // 2
            for part in (text[:half], text[half:]):
                ev.append(("content_block_delta", {"type": "content_block_delta", "index": i,
                                                   "delta": {"type": "text_delta", "text": part}}))
        ev.append(("content_block_stop", {"type": "content_block_stop", "index": i}))
    delta = {"stop_reason": stop_reason, "stop_sequence": None}
    if stop_details is not None:
        delta["stop_details"] = stop_details
    ev.append(("message_delta", {"type": "message_delta", "delta": delta, "usage": usage or {"output_tokens": 15}}))
    ev.append(("message_stop", {"type": "message_stop"}))
    return ev


def encode_sse(events) -> bytes:
    return b"".join(f"event: {name}\ndata: {json.dumps(data)}\n\n".encode("utf-8") for name, data in events)


class _Handler(BaseHTTPRequestHandler):
    def _serve(self):
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        srv = self.server
        with srv.lock:
            srv.seen.append({"method": self.command, "path": self.path,
                             "headers": {k.lower(): v for k, v in self.headers.items()},
                             "body": json.loads(raw) if raw else None})
            item = srv.script.pop(0) if srv.script else ("json", 500, error_body("api_error", "script exhausted"))
        kind = item[0]
        if kind == "sse":
            events, status = item[1], (item[2] if len(item) > 2 else 200)
            self.send_response(status)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            for name, data in events:   # 一个事件一次 flush：客户端按块读
                self.wfile.write(encode_sse([(name, data)]))
                self.wfile.flush()
            return
        if kind == "redirect":
            self.send_response(item[1])
            self.send_header("Location", item[2])
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        status = item[1]
        body = json.dumps(item[2]).encode("utf-8") if kind == "json" else item[2]
        headers = item[3] if len(item) > 3 else {}
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    do_GET = do_POST = _serve

    def log_message(self, *args):
        pass


class _Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


class FakeClaude:
    def __init__(self):
        self.srv = _Server(("127.0.0.1", 0), _Handler)
        self.srv.seen, self.srv.script, self.srv.lock = [], [], threading.Lock()
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()

    @property
    def seen(self):
        return self.srv.seen

    def reset(self, *script):
        with self.srv.lock:
            self.srv.seen.clear()
            self.srv.script[:] = list(script)

    def url(self, path: str) -> str:
        return f"http://127.0.0.1:{self.srv.server_address[1]}{path}"

    def regions(self) -> dict:
        return {"global": {"chat": self.url("/v1/messages"), "search": self.url("/v1/messages"),
                           "models": self.url("/v1/models")}}

    def close(self):
        self.srv.shutdown()
        self.srv.server_close()
