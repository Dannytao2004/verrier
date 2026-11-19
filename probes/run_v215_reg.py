"""v2.15 固定回归（2026-11-19，口径见 results/experiments/v215_reg_2026-11-19/PLAN.md）：20 次运行，两条线并行，每条线一个接一个；
只在 DeepSeek 谷价时段开跑（config.is_peak，高峰就等）。已经有 state.json 的运行跳过（中途断了可以接着跑，不会重复花钱）。
用法：.venv/Scripts/python.exe probes/run_v215_reg.py   （TRIANGULATE_THINKING 必须为空：每次运行由本脚本设）"""
import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate import config  # noqa: E402

sys.path.insert(0, str(ROOT / "probes"))
from run_v214a_batch import SPONSOR_Q, THINK  # noqa: E402

OUT = ROOT / "results" / "experiments" / "v215_reg_2026-11-19"
AGENT = ROOT / "results" / "agent"
REG = ["fc_kr_births_2026_07", "fc_tw_births_2026_09", "fc_lhr_pax_2026_09", "fc_jp_births_2026_07", "fc_nhs_ae_2026_09",
       "fc_jp_movers_2026_08", "fc_pola_teu_2026_09", "fc_es_transit_2026_08", "fc_ca_rail_2026_07", "fc_de_cars_2026_09",
       "fc_hk_visitors_2026_09", "fc_us_starts_2026_08", "fc_us_gen_2026_07", "fc_kr_online_2026_08"]
THINK_Q = ["fc_ca_rail_2026_07", "fc_tw_births_2026_09", "fc_de_cars_2026_09", "fc_kr_online_2026_08"]
BCG_Q = "how many ng employees in BCG USA in 2026?"

RUNS = [{"name": f"{q} off", "mode": "off", "dir": (q, "v215_reg"),
         "args": ["agent", "--question", q, "--tag", "v215_reg", "--auto-approve"]} for q in REG]
RUNS += [{"name": f"{q} think", "mode": "think", "dir": (q, "v215_reg_think"),
          "args": ["agent", "--question", q, "--tag", "v215_reg_think", "--auto-approve"]} for q in THINK_Q]
RUNS += [{"name": "bcg_us off", "mode": "off", "dir": ("bcg_us_2026", "v215"),
          "args": ["agent", "--ask", BCG_Q, "--as-of", "2026-11-19", "--id", "bcg_us_2026", "--tag", "v215", "--auto-approve"]},
         {"name": "sponsor_strict off", "mode": "off", "dir": ("sponsor_strict_2026", "v215"),
          "args": ["agent", "--ask", SPONSOR_Q, "--as-of", "2026-10-28", "--id", "sponsor_strict_2026", "--tag", "v215",
                   "--auto-approve"]}]
LOCK = threading.Lock()


def log(rec):
    rec = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), **rec}
    with LOCK:
        with open(OUT / "batch.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(json.dumps(rec, ensure_ascii=False), flush=True)


def run_one(r):
    while config.is_peak(datetime.now(timezone.utc)):
        time.sleep(60)
    if (AGENT / r["dir"][0] / r["dir"][1] / "state.json").exists():
        log({"event": "skip", "run": r["name"], "why": "state.json exists"})
        return
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    if r["mode"] == "think":
        env["TRIANGULATE_THINKING"] = THINK
    log({"event": "start", "run": r["name"]})
    t0 = time.time()
    p = subprocess.run([sys.executable, "-m", "triangulate", *r["args"]], cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    (OUT / f"{r['name'].replace(' ', '__')}.out").write_text(p.stdout[-20000:] + "\n--- stderr ---\n" + p.stderr[-20000:],
                                                          encoding="utf-8")
    log({"event": "end", "run": r["name"], "exit": p.returncode, "wall_s": round(time.time() - t0, 1)})


def lane(runs):
    for r in runs:
        run_one(r)


def main():
    if os.environ.get("TRIANGULATE_THINKING"):
        raise SystemExit("TRIANGULATE_THINKING must be unset: this script sets it per run")
    OUT.mkdir(parents=True, exist_ok=True)
    lanes = [threading.Thread(target=lane, args=(RUNS[i::2],)) for i in range(2)]
    for t in lanes:
        t.start()
    for t in lanes:
        t.join()
    log({"event": "done"})


if __name__ == "__main__":
    main()
