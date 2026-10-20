"""探针：DeepSeek 思考模式（OpenAI 格式）加 JSON 输出的真实返回（v2.9 准备，2026-10-19）。

文档没说清的三件事，这里实测：
  1. thinking enabled + response_format json_object 能不能一起用，content 是不是合法 JSON；
  2. 思考 token 算不算进 max_tokens（小 max_tokens 时 finish_reason 会不会变 length）；
  3. usage 里思考 token 记在哪个字段，计费按什么算。
只打印结构和计数，不打印 key，不存回复正文以外的东西。结果写 probes/out/thinking_probe.json。
用法：TRIANGULATE_KEY_FILE=... ./.venv/Scripts/python.exe probes/thinking_probe.py
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.config import API_URL, MODEL, read_key  # noqa: E402

SYSTEM = "You are a careful analyst. Reply with one JSON object only."
USER = ("A port handled 960,464 TEU in July 2025 and 1,028,000 TEU in July 2026. "
        "Return json: {\"yoy_pct\": number rounded to 1 decimal, \"reasoning_steps\": integer count of steps you used}.")

CASES = [
    ("disabled", None, 2000),
    ("enabled", "low", 2000),
    ("enabled", "high", 2000),
    ("enabled", "high", 150),   # 小 max_tokens：看思考是否挤占输出上限
]


def call(key, thinking, effort, max_tokens):
    payload = {"model": MODEL, "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": USER}],
               "thinking": {"type": thinking}, "response_format": {"type": "json_object"},
               "temperature": 0, "max_tokens": max_tokens, "stream": False}
    if effort:
        payload["reasoning_effort"] = effort
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            status, raw = r.status, r.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    out = {"thinking": thinking, "effort": effort, "max_tokens": max_tokens, "http": status,
           "latency_s": round(time.time() - t0, 2)}
    try:
        data = json.loads(raw)
    except ValueError:
        out["body"] = "not_json"
        return out
    if status != 200:
        out["server_error"] = str((data.get("error") or {}).get("message", ""))[:300]
        return out
    ch = data["choices"][0]
    msg = ch.get("message") or {}
    content = msg.get("content") or ""
    try:
        parsed = json.loads(content)
        out["content_json_ok"] = isinstance(parsed, dict)
        out["content"] = parsed
    except ValueError:
        out["content_json_ok"] = False
        out["content_head"] = content[:200]
    out.update(response_model=data.get("model"), finish_reason=ch.get("finish_reason"),
               reasoning_chars=len(msg.get("reasoning_content") or ""), message_keys=sorted(msg), usage=data.get("usage"))
    return out


def main():
    key = read_key()
    rows = []
    for c in CASES:
        r = call(key, *c)
        rows.append(r)
        print(json.dumps({k: v for k, v in r.items() if k != "content"}, ensure_ascii=False))
    dst = ROOT / "probes" / "out" / "thinking_probe.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
