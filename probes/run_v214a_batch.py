"""v2.14a 试跑（用户 10-27 晚）：sponsor（严格口径，真实使用）+ 台湾 9 月出生数、德国 9 月新车（回测），思考关 / 开各一次，
一个接一个跑；只在 DeepSeek 谷价时段开跑（config.is_peak，高峰就等）。留出测试 4 的两题（英国轿车产量、住宅交易）另由
probes/run_test4.py --round v214a 跑（它自带首发时刻和高峰的门）。口径记录：results/experiments/v214a_batch_2026-10-28/PLAN.md。
用法：.venv/Scripts/python.exe probes/run_v214a_batch.py [--not-before 2026-10-28T10:00:00+00:00]   （TRIANGULATE_THINKING 必须为空：每次运行由本脚本设）"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate import config  # noqa: E402

OUT = ROOT / "results" / "experiments" / "v214a_batch_2026-10-28"
THINK = "plan=high,judge=high,repair=high,audit=low,unit_arbiter=low"   # 同留出测试 3、4 的思考臂
SPONSOR_Q = ("Estimate the number of distinct job postings published in the United States during calendar year 2026 (2026-01-01 to "
             "2026-12-31) for new-graduate roles — summer internships plus full-time entry-level positions for new bachelor's or "
             "master's graduates with 0–1 years of experience, in professional (white-collar) occupations — whose posting text "
             "explicitly states that the employer will sponsor a work visa (for example \"H-1B sponsorship available\" or \"visa "
             "sponsorship provided\"). Count each posting once even if it appears on several job boards. Do not count postings that "
             "do not state sponsorship in their text, even if the employer has sponsored visas before or ticks a \"will sponsor\" box "
             "on a job platform, and do not count postings that rule sponsorship out.")
RUNS = []
for qid in ("fc_tw_births_2026_09", "fc_de_cars_2026_09"):
    for mode in ("off", "think"):
        RUNS.append({"name": f"{qid} {mode}", "mode": mode,
                     "args": ["agent", "--question", qid, "--tag", "v214a" + ("_think" if mode == "think" else ""), "--auto-approve"]})
for mode in ("off", "think"):
    RUNS.append({"name": f"sponsor_strict {mode}", "mode": mode,
                 "args": ["agent", "--ask", SPONSOR_Q, "--as-of", "2026-10-28", "--id", "sponsor_strict_2026",
                          "--tag", "v214a" + ("_think" if mode == "think" else ""), "--auto-approve"]})


def log(rec):
    rec = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), **rec}
    with open(OUT / "batch.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False), flush=True)


def wait_offpeak():
    while config.is_peak(datetime.now(timezone.utc)):
        time.sleep(60)


def main():
    not_before = datetime.fromisoformat(sys.argv[sys.argv.index("--not-before") + 1]) if "--not-before" in sys.argv else None
    while not_before and datetime.now(timezone.utc) < not_before:   # 代码审完、提交以后才开跑：等到指定时刻
        time.sleep(60)
    if os.environ.get("TRIANGULATE_THINKING"):
        raise SystemExit("TRIANGULATE_THINKING must be unset: this script sets it per run")
    OUT.mkdir(parents=True, exist_ok=True)
    for r in RUNS:
        wait_offpeak()
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        if r["mode"] == "think":
            env["TRIANGULATE_THINKING"] = THINK
        log({"event": "start", "run": r["name"], "args": r["args"][:2] + r["args"][2:3] if "--ask" not in r["args"] else ["agent", "--ask", "<SPONSOR_Q>"]})
        t0 = time.time()
        p = subprocess.run([sys.executable, "-m", "triangulate", *r["args"]], cwd=ROOT, env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        (OUT / f"{r['name'].replace(' ', '__')}.out").write_text(p.stdout[-20000:] + "\n--- stderr ---\n" + p.stderr[-20000:],
                                                              encoding="utf-8")
        log({"event": "end", "run": r["name"], "exit": p.returncode, "wall_s": round(time.time() - t0, 1)})


if __name__ == "__main__":
    main()
