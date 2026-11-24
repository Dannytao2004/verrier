"""v2.16 固定回归按组跑（口径：results/experiments/v216_reg_2026-11-24/PLAN.md「执行方式」）：一组 3 次并行；DeepSeek 谷价、
而且 20 分钟后仍是谷价时才开组（高峰就等）；已有 state.json 的跳过。开组时的代码版本（git describe）记进 batch.log。
用法：.venv/Scripts/python.exe probes/run_v216_groups.py <组号 1-5>   （TRIANGULATE_THINKING 必须为空）"""
import os
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "probes"))
from triangulate import config  # noqa: E402
from run_v216_reg import OUT, RUNS, log, run_one  # noqa: E402

GROUPS = {1: ["fc_kr_births_2026_07 off", "fc_de_cars_2026_09 off", "bcg_us off"],
          2: ["fc_tw_births_2026_09 off", "sponsor_strict off", "fc_ca_rail_2026_07 think"],
          3: ["fc_lhr_pax_2026_09 off", "fc_jp_births_2026_07 off", "fc_de_cars_2026_09 think"],
          4: ["fc_pola_teu_2026_09 off", "fc_es_transit_2026_08 off", "fc_us_starts_2026_08 off"],
          5: ["fc_ca_rail_2026_07 off", "fc_hk_visitors_2026_09 off", "fc_kr_online_2026_08 off"]}
MARGIN = timedelta(minutes=20)


def main(g: int):
    if os.environ.get("TRIANGULATE_THINKING"):
        raise SystemExit("TRIANGULATE_THINKING must be unset: run_one sets it per run")
    by_name = {r["name"]: r for r in RUNS}
    runs = [by_name[n] for n in GROUPS[g]]
    OUT.mkdir(parents=True, exist_ok=True)
    while True:
        now = datetime.now(timezone.utc)
        if not config.is_peak(now) and not config.is_peak(now + MARGIN):
            break
        time.sleep(60)
    code = subprocess.run(["git", "describe", "--tags", "--match", "v2.*", "--always", "--dirty"], cwd=ROOT, capture_output=True,
                          text=True).stdout.strip()
    log({"event": "group_start", "group": g, "runs": GROUPS[g], "code": code})
    ts = [threading.Thread(target=run_one, args=(r,)) for r in runs]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    log({"event": "group_end", "group": g})


if __name__ == "__main__":
    main(int(sys.argv[1]))
