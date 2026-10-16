"""探针：arm (3) 的请求（system + web_search）在 DeepSeek Anthropic 兼容接口上能不能跑通、返回长什么样。
用一道和展示集无关的题，只打印结构和计量，记录存 probes/out/（不进 git）。
用法：TRIANGULATE_KEY_FILE=<key 文件> .venv/Scripts/python.exe probes/search_direct_probe.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from triangulate.search_direct import DirectClient, run_search_direct  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)
logs = []
q = {"id": "probe_chicago_pop", "as_of": "2026-10-16", "answer_unit": "", "strict": False,
     "unit_hint": "a count of people",
     "question": "Assume today is 2026-10-16. Estimate the resident population of the city of Chicago on April 1, 2020, "
                 "as counted in the 2020 United States Census."}
rec = run_search_direct(DirectClient(logs.append), q)
(OUT / "search_direct_probe.json").write_text(json.dumps({"record": rec, "calls": logs}, indent=1, ensure_ascii=False),
                                              encoding="utf-8")
print("status", rec["status"], "estimate", rec["estimate"], "attempts", rec["final_attempt"], "usd", rec["usd"],
      "search_fee", rec["usd_search_fee_assumed"])
for a in rec["attempts"]:
    print(a["attempt"], a["stop_reason"], "queries", a["queries"], "n_results", len(a["results"]),
          "thinking", a["n_thinking_blocks"], "tokens in/cache/out", a["input_tokens"], a["cache_read_input_tokens"],
          a["output_tokens"], "problems", a["problems"])
    print("final_text:", a["final_text"][:300])
print("calls:", [{k: c.get(k) for k in ("http", "ok", "error", "latency_s")} for c in logs])
