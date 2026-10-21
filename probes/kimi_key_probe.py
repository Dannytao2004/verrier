"""v2.10d 探针（不花钱）：对真实的 Kimi 接口发不带 key / 带明显是假的 key 的请求，看 401 的形状，并确认 llm.check_key 的处理。
  1. 国际站 GET https://api.moonshot.ai/v1/models：不带 key、带假 key；
  2. 国内站 GET https://api.moonshot.cn/v1/models：带假 key（两站的 key 互不通用，看返回是否相同）；
  3. 国际站 POST /v1/tools/search、POST /v1/chat/completions：带假 key（鉴权就被拒，不会执行搜索或生成）；
  4. llm.check_key：国际站、国内站各一次（假 key，Authorization: Bearer，和正式代码同一条路）。
不读 .env、不读任何 key 文件；结果写到 probes/out/kimi_key_probe.json（gitignore）。
用法：.venv/Scripts/python.exe probes/kimi_key_probe.py
"""
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate import llm, providers as PV  # noqa: E402

FAKE_KEY = "sk-FAKE-not-a-real-kimi-key-000000"
OUT = ROOT / "probes" / "out" / "kimi_key_probe.json"
KEEP = ("content-type", "content-length", "retry-after", "x-msh-track-id", "x-msh-chat-id", "msh-trace-mode")


def send(url: str, headers: dict, body=None) -> dict:
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="GET" if body is None else "POST",
                                 headers={**headers, **({"Content-Type": "application/json"} if body is not None else {})})
    try:
        with llm.urlopen_no_redirect(req, timeout=30) as r:
            return {"status": r.status, "body": r.read()[:500].decode("utf-8", "replace")}
    except urllib.error.HTTPError as e:
        raw = e.read()[:500].decode("utf-8", "replace")
        keep = {k.lower(): v for k, v in e.headers.items() if k.lower() in KEEP}
        e.close()
        return {"status": e.code, "headers": keep, "body": raw}


def main():
    g, cn = PV.KIMI.regions["global"], PV.KIMI.regions["cn"]
    fake = {"Authorization": f"Bearer {FAKE_KEY}"}
    out = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "global_models_no_key": send(g["models"], {}),
           "global_models_fake_key": send(g["models"], fake),
           "cn_models_fake_key": send(cn["models"], fake),
           "global_tools_search_fake_key": send(g["search"], fake, {"text_query": "test", "limit": 1, "timeout_seconds": 5}),
           "global_chat_fake_key": send(g["chat"], fake, {"model": "kimi-k2.6", "messages": [{"role": "user", "content": "hi"}],
                                                         "thinking": {"type": "disabled"}, "max_completion_tokens": 1}),
           "check_key_global": llm.check_key(PV.ModelSpec("kimi", "kimi-k2.6", FAKE_KEY)),
           "check_key_cn": llm.check_key(PV.ModelSpec("kimi", "kimi-k3", FAKE_KEY, region="cn", thinking="low"))}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
