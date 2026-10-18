"""冒烟测试（2026-10-17，冻结前）：4 道题，agent（命令行 --ask --auto-approve，tag smoke1）+ 直接问 + 修过的结构化基线，各跑一次。
联网、调模型、要 key 文件（环境变量 TRIANGULATE_KEY_FILE）。agent 结果在 results/agent/<id>/smoke1/，两个基线的回复在 probes/out/smoke/。
用法：.venv/Scripts/python.exe probes/smoke_run.py [baselines]（只重跑两个基线）
第一次跑时基线的 answer_unit 误设成 ""（无量纲），每天的量、质量题基线必然被量纲检查拒掉；之后按题目给了单位。"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.arms import run_naive, run_structured  # noqa: E402
from triangulate.llm import LLM, TransportError  # noqa: E402

OUT = ROOT / "probes" / "out" / "smoke"
TODAY = date.today().isoformat()
QS = [
    {"id": "smoke_pizza", "answer_unit": "tonne/day", "unit_hint": "a mass per day",
     "question": "How many tonnes of pizza do people in Chicago eat on an average day in 2026?"},
    {"id": "smoke_tdr", "answer_unit": "visitor/day", "unit_hint": "a count of visitors per day",
     "question": "What was the average daily number of visitors to Tokyo Disney Resort (Tokyo Disneyland and Tokyo DisneySea combined) in September 2026?"},
    {"id": "smoke_nyc", "answer_unit": "trip/day", "unit_hint": "a count of trips per day",
     "question": "What is the average number of taxi and ride-hail trips per day in New York City in October 2026 (yellow taxis, green "
                 "taxis and high-volume for-hire vehicles combined, as counted by the NYC Taxi & Limousine Commission)?"},
    {"id": "smoke_tea", "answer_unit": "cup/day", "unit_hint": "a count of cups per day",
     "question": "How many cups of tea do people in the United Kingdom drink per day?"},
]


def agent(q):
    cmd = [sys.executable, "-m", "triangulate", "agent", "--ask", q["question"], "--id", q["id"], "--tag", "smoke1", "--auto-approve"]
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    (OUT / f"agent_{q['id']}.log").write_text(p.stdout[-20000:] + "\n--- stderr ---\n" + p.stderr[-20000:], encoding="utf-8")
    return q["id"], "agent", p.returncode


def arm(name, fn, llm, q):
    qq = dict(q, as_of=TODAY, strict=False)
    try:
        rec = fn(llm, qq)
    except TransportError as e:
        return q["id"], name, f"transport: {e}"
    (OUT / f"{name}_{q['id']}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    return q["id"], name, f"attempts={len(rec['attempts'])} problems={len(rec['attempts'][-1]['problems'])}"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    llm = LLM(calls_path=OUT / "calls.jsonl")
    with ThreadPoolExecutor(12) as ex:
        futs = [] if "baselines" in sys.argv else [ex.submit(agent, q) for q in QS]
        futs += [ex.submit(arm, n, f, llm, q) for q in QS for n, f in (("naive", run_naive), ("structured", run_structured))]
        for f in futs:
            print(*f.result(), flush=True)


if __name__ == "__main__":
    main()
