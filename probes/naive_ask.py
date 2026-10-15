"""复现「直接问」那一组的调用：system / user 消息和参数与 forecast 一样。先打印完整请求（不含 key），再打印回复。
结果不写进 results/，调用日志记到 probes/out/naive_ask_calls.jsonl（不进 git）。

用法：
  python probes/naive_ask.py                       # 原题 fc_yell_2026_08
  python probes/naive_ask.py fc_yell_2026_09       # 原题 9 月
  python probes/naive_ask.py --q "自己改写的英文问题"   # 换问题，其余不变
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from triangulate.arms import _messages  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402
from triangulate.llm import LLM  # noqa: E402
from triangulate.prompts import NAIVE_SYSTEM  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser()
ap.add_argument("qid", nargs="?", default="fc_yell_2026_08")
ap.add_argument("--q", help="replace the question text")
a = ap.parse_args()
q = dict(next(x for x in QUESTIONS if x["id"] == a.qid))
if a.q:
    q["question"] = a.q
msgs = _messages(NAIVE_SYSTEM, q)
print("== request (POST https://api.deepseek.com/chat/completions)")
print(json.dumps({"model": "deepseek-flash", "messages": msgs, "thinking": {"type": "disabled"},
                  "response_format": {"type": "json_object"}, "temperature": 0, "max_tokens": 500},
                 ensure_ascii=False, indent=1))
reply, text, err = LLM(calls_path=Path(__file__).resolve().parent / "out" / "naive_ask_calls.jsonl").json_call(
    msgs, arm="naive_ask", qid=q["id"], attempt=1, max_tokens=500)
print("== reply")
print(text if err is None else f"error: {err}\n{text}")
