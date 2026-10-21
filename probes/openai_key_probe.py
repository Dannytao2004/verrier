"""v2.10c 探针（不花钱）：对真实的 https://api.openai.com/v1/models 发两次 GET，看 401 的形状，并确认 llm.check_key 的处理。
  1. 不带 key：直接用 urllib 发，记状态码、几个响应头、body 原文；
  2. 带一把明显是假的 key：先直接发一次记 body 原文（OpenAI 会在 message 里回显打了码的 key 片段，这把是假的，可以看），
     再走 llm.check_key（Authorization: Bearer，和正式代码同一条路），记它返回的 dict。
不读 .env、不读任何 key 文件；结果写到 probes/out/openai_key_probe.json（gitignore）。
用法：.venv/Scripts/python.exe probes/openai_key_probe.py
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

FAKE_KEY = "sk-proj-FAKE-not-a-real-key-000000"
OUT = ROOT / "probes" / "out" / "openai_key_probe.json"


def raw_get(headers: dict) -> dict:
    url = PV.OPENAI.key_check_request("global", "x")[0]
    req = urllib.request.Request(url, method="GET", headers=headers)
    try:
        with llm.urlopen_no_redirect(req, timeout=30) as r:
            return {"status": r.status, "body": r.read()[:500].decode("utf-8", "replace")}
    except urllib.error.HTTPError as e:
        body = e.read()[:500].decode("utf-8", "replace")
        keep = {k: v for k, v in e.headers.items() if k.lower() in ("content-type", "retry-after", "x-request-id")}
        e.close()
        return {"status": e.code, "headers": keep, "body": body}


def main():
    out = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "no_key": raw_get({}),
           "fake_key_raw": raw_get({"Authorization": f"Bearer {FAKE_KEY}"}),
           "check_key_fake_key": llm.check_key(PV.ModelSpec("gpt", "gpt-6-luna", FAKE_KEY, thinking="off"))}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
