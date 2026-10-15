"""最小探针：一次极短的 JSON 调用，看延迟、finish_reason 和 token。日志写到 probes/ping_calls.jsonl。"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from triangulate.llm import LLM  # noqa: E402

llm = LLM(calls_path=Path(__file__).resolve().parent / "ping_calls.jsonl")
t = time.time()
out, text, err = llm.json_call([{"role": "user", "content": 'Reply with JSON {"ok": true}'}],
                               arm="ping", qid="ping", attempt=1, max_tokens=50)
print(out, err, round(time.time() - t, 2))
