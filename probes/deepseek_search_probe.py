"""探针：DeepSeek 的 Anthropic 兼容接口能不能做服务端网页搜索，返回长什么样。

只打印结构（块类型、结果条数、标题和网址、token 用量），不打印 key。原始返回存到 probes/out/（不进 git）。
用法：TRIANGULATE_KEY_FILE=<key 文件> python probes/deepseek_search_probe.py
"""
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from triangulate.config import read_key  # noqa: E402
from triangulate.llm import urlopen_no_redirect  # noqa: E402  不跟随跳转（v2.6g，D9）：3xx 和别的 HTTP 错误一样处理，key 不发到别的地址

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).resolve().parent / "out"
URL = "https://api.deepseek.com/anthropic/v1/messages"
body = {
    "model": "deepseek-flash",
    "max_tokens": 1024,
    "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}],
    "messages": [{"role": "user", "content": "Use web search to find official sources for Yellowstone National Park "
                  "monthly recreation visits in 2024 and 2025. Reply with the list of URLs you found, one per line."}],
}
req = urllib.request.Request(URL, data=json.dumps(body).encode("utf-8"), method="POST", headers={
    "Content-Type": "application/json", "x-api-key": read_key(), "anthropic-version": "2023-06-01"})
t0 = time.time()
try:
    with urlopen_no_redirect(req, timeout=600) as r:
        status, raw = r.status, r.read()
except urllib.error.HTTPError as e:
    status, raw = e.code, e.read()
print(f"http {status}, {time.time() - t0:.1f}s")
OUT.mkdir(exist_ok=True)
(OUT / "deepseek_search_probe.json").write_bytes(raw)
try:
    d = json.loads(raw)
except json.JSONDecodeError:
    print(raw[:500])
    sys.exit(1)
if status != 200:
    print(json.dumps(d, ensure_ascii=False)[:800])
    sys.exit(1)
print("model:", d.get("model"), "| stop:", d.get("stop_reason"), "| usage:", d.get("usage"))
for b in d.get("content", []):
    t = b.get("type")
    if t == "server_tool_use":
        print("[server_tool_use]", json.dumps(b.get("input"), ensure_ascii=False))
    elif t == "web_search_tool_result":
        c = b.get("content")
        if isinstance(c, list):
            print(f"[web_search_tool_result] {len(c)} results; fields: {sorted(c[0].keys()) if c else []}")
            for x in c:
                print("   -", x.get("title"), "|", x.get("url"), "| page_age:", x.get("page_age"))
        else:
            print("[web_search_tool_result] error:", c)
    elif t == "text":
        print("[text]", b.get("text", "")[:600])
    else:
        print(f"[{t}]")
