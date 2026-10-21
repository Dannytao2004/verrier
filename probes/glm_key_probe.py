"""v2.10e 探针（不花钱）：对真实的 GLM 接口（Z.ai 国际站 / 智谱开放平台国内站）发不带 key / 带明显是假的 key 的请求，
看 401 的形状，并确认 llm.check_key 的处理。鉴权就被拒，不会生成、不会搜索、不计费。
  1. 国际站 GET https://api.z.ai/api/paas/v4/models：不带 key、带假 key；国内站 GET https://open.bigmodel.cn/api/paas/v4/models：带假 key；
  2. 两站 POST /chat/completions、POST /web_search：带假 key；
  3. llm.check_key：两站各一次（假 key，Authorization: Bearer，和正式代码同一条路；adapter 还没加时跳过）。
不读 .env、不读任何 key 文件；结果写到 probes/out/glm_key_probe.json（gitignore）。
用法：.venv/Scripts/python.exe probes/glm_key_probe.py
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

FAKE_KEY = "00000000000000000000000000000000.FAKEnotarealkey0"   # 形状同 GLM 的 key（id.secret），但显然是假的
OUT = ROOT / "probes" / "out" / "glm_key_probe.json"
KEEP = ("content-type", "content-length", "retry-after", "x-log-id", "x-request-id")
BASES = {"global": "https://api.z.ai/api/paas/v4", "cn": "https://open.bigmodel.cn/api/paas/v4"}


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
    fake = {"Authorization": f"Bearer {FAKE_KEY}"}
    chat = {"model": "glm-4.7-flashx", "messages": [{"role": "user", "content": "hi"}], "thinking": {"type": "disabled"},
            "max_tokens": 1}
    out = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "global_models_no_key": send(BASES["global"] + "/models", {}),
           "global_models_fake_key": send(BASES["global"] + "/models", fake),
           "cn_models_fake_key": send(BASES["cn"] + "/models", fake),
           "global_chat_fake_key": send(BASES["global"] + "/chat/completions", fake, chat),
           "cn_chat_fake_key": send(BASES["cn"] + "/chat/completions", fake, chat),
           "global_web_search_fake_key": send(BASES["global"] + "/web_search", fake,
                                              {"search_engine": "search-prime", "search_query": "test", "count": 1}),
           "cn_web_search_fake_key": send(BASES["cn"] + "/web_search", fake,
                                          {"search_query": "test", "search_engine": "search_std", "search_intent": False,
                                           "count": 1})}
    if "glm" in PV.ADAPTERS:
        out["check_key_global"] = llm.check_key(PV.ModelSpec("glm", "glm-4.7-flashx", FAKE_KEY))
        out["check_key_cn"] = llm.check_key(PV.ModelSpec("glm", "glm-5.3", FAKE_KEY, region="cn", thinking="low"))
    text = json.dumps(out, ensure_ascii=False, indent=1)
    out["fake_key_echoed"] = FAKE_KEY in text or FAKE_KEY.split(".")[0] in text   # 服务端有没有回显 key（或 key 的 id 段）
    text = json.dumps(out, ensure_ascii=False, indent=1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
