"""泄漏检查（v2.9a 实验臂用，2026-10-19）：同一个 deepseek-flash 打开思考后直接问，看它是不是记得回测题的真值。
真值都在 2026 年 8-10 月公布，模型版本 V4.1-Flash-1017 的训练数据可能覆盖到。只读题库，不改已存的基线回复。
用法：TRIANGULATE_THINKING=naive=high TRIANGULATE_KEY_FILE=... ./.venv/Scripts/python.exe probes/leak_naive_thinking.py <qid> ...
结果写 probes/out/leak_naive_thinking.json，调用记录写 probes/out/leak_naive_thinking_calls.jsonl。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate import config  # noqa: E402
from triangulate.arms import run_naive  # noqa: E402
from triangulate.forecast import QUESTIONS  # noqa: E402
from triangulate.llm import LLM  # noqa: E402

OUT = ROOT / "probes" / "out"


def main(qids):
    if not config.THINKING.get("naive"):
        raise SystemExit("set TRIANGULATE_THINKING=naive=high (this probe is about the thinking arm)")
    llm = LLM(calls_path=OUT / "leak_naive_thinking_calls.jsonl")
    by_id = {q["id"]: q for q in QUESTIONS}
    rows = []
    for qid in qids:
        q = by_id[qid]
        rec = run_naive(llm, q)
        last = rec["attempts"][-1]
        est = (last.get("reply") or {}).get("estimate")
        truth = q.get("answer_value")
        pct = (est / truth - 1) if (isinstance(est, (int, float)) and truth) else None
        row = {"qid": qid, "thinking": config.THINKING["naive"], "estimate": est,
               "unit": (last.get("reply") or {}).get("unit"), "truth": truth,
               "pct_err": None if pct is None else round(pct, 4), "problems": last.get("problems")}
        rows.append(row)
        print(json.dumps(row, ensure_ascii=False))
    # 按题合并：多次调用不互相覆盖；结果同时存一份进 results/agent/test2_think_naive.json（受版本管理）
    for dst in (OUT / "leak_naive_thinking.json", ROOT / "results" / "agent" / "test2_think_naive.json"):
        old = {r["qid"]: r for r in json.loads(dst.read_text(encoding="utf-8"))} if dst.exists() else {}
        old.update({r["qid"]: r for r in rows})
        dst.write_text(json.dumps(list(old.values()), indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
