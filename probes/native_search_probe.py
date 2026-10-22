"""v2.10h 探针（不花钱）：用正式代码建的搜索请求（adapter.search_request，请求头和请求体同真实运行），带明显是假的 key 发到
Kimi K3 的 Responses 接口（国际站 / 国内站 POST /v1/responses + web_search）和 GLM 的 Chat Completions 接口（Z.ai / 智谱
POST /chat/completions + web_search 工具）。鉴权就被拒（401），不会生成、不会搜索、不计费。看的是：接口在不在（401 而不是 404）、
不跟随跳转、401 的 body 形状（正式代码对 401 不读 body，这里只为记录）、有没有回显 key。
不读 .env、不读任何 key 文件；结果写到 probes/out/native_search_probe.json（gitignore）。
用法：.venv/Scripts/python.exe probes/native_search_probe.py
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

FAKES = {"kimi": "sk-FAKE-not-a-real-kimi-key-000000", "glm": "00000000000000000000000000000000.FAKEnotarealkey0"}
OUT = ROOT / "probes" / "out" / "native_search_probe.json"
KEEP = ("content-type", "content-length", "retry-after", "x-msh-track-id", "x-log-id", "x-request-id")
PROMPT = "Find the official monthly widget statistics page. After searching, reply with at most 2 URLs."


def send(url: str, headers: dict, payload: dict, fake: str) -> dict:
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), method="POST", headers=headers)
    try:
        with llm.urlopen_no_redirect(req, timeout=30) as r:
            out = {"status": r.status, "body": r.read()[:500].decode("utf-8", "replace")}
    except urllib.error.HTTPError as e:
        raw = e.read()[:500].decode("utf-8", "replace")
        out = {"status": e.code, "headers": {k.lower(): v for k, v in e.headers.items() if k.lower() in KEEP}, "body": raw}
        e.close()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        out = {"status": None, "error": type(e).__name__}
    out["echoes_key"] = fake in json.dumps(out) or fake[-12:] in json.dumps(out)
    out["body"] = str(out.get("body", "")).replace(fake, "***")
    return out


def main():
    res = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for provider, model, level in (("kimi", "kimi-k3", "low"), ("glm", "glm-5.2", "off"), ("glm", "glm-5.3", "low")):
        ad = PV.ADAPTERS[provider]
        for region in ad.regions:
            sp = PV.ModelSpec(provider, model, FAKES[provider], region=region, thinking=level)
            effort, max_tokens = sp.tokens_for("search", 8192)
            headers, payload = ad.search_request(model, sp.key, PROMPT, max_tokens=max_tokens, max_uses=3, effort=effort,
                                                 region=region)
            shown = {k: v for k, v in payload.items() if k not in ("input", "messages")}
            res[f"{provider}_{model}_{region}"] = {"url": ad.search_url(region), "body_sent_minus_prompt": shown,
                                                   **send(ad.search_url(region), headers, payload, FAKES[provider])}
            sp.drop_key()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
