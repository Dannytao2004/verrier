"""v2 回测：两道题 x（完整 / 消融 --ablate-own-history）共 4 次运行，在同一个进程里用线程并行。

同一个进程 = 共用 net.LIMITER 和 robots 缓存：Wayback 仍是单连接、两次请求间隔 1.5 秒，其他 host 间隔 >= 1 秒
（robots.txt 的 Crawl-delay 更长就按它），和串行跑时的限速完全一样；并行只让模型调用重叠。
每次运行有自己的 Budget（美元上限 1.00，含按 $0.01 / 次假设的搜索费）和自己的 calls.jsonl。
跑完分别打分：results/agent/summary_<tag>.json 和 summary_<tag>_noown.json。

用法（key 只在这条命令的环境里）：
  TRIANGULATE_KEY_FILE=... .venv/Scripts/python.exe probes/run_v2_backtests.py --tag v2
"""
import argparse
import json
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import run as R  # noqa: E402
from triangulate.forecast import FC, QUESTIONS  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v2")
    ap.add_argument("--arms", choices=["both", "full", "noown"], default="both")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    fc = json.loads((FC / "summary.json").read_text(encoding="utf-8"))
    ablate = {"both": (False, True), "full": (False,), "noown": (True,)}[a.arms]
    jobs = [(q, abl) for abl in ablate for q in QUESTIONS]
    t0 = time.time()

    def one(job):
        q, abl = job
        try:
            st = R.run_question(q, True, a.tag, abl)
            r = (st.get("compute") or {}).get("result") or {}
            return {"id": q["id"], "ablation": abl, "estimate": r.get("central"), "wall_s": st.get("wall_s")}
        except Exception as e:  # noqa: BLE001  一次运行崩了不拖垮另外三次；记下来，修好再单独重跑
            traceback.print_exc()
            return {"id": q["id"], "ablation": abl, "error": f"{type(e).__name__}: {e}"[:300]}

    with ThreadPoolExecutor(len(jobs)) as ex:
        done = list(ex.map(one, jobs))
    print(json.dumps(done, indent=1, ensure_ascii=False), flush=True)
    tags = ([a.tag] if False in ablate else []) + ([R.ablation_tag(a.tag)] if True in ablate else [])
    for t in tags:
        rows = R.score_all(QUESTIONS, t, fc)
        print(t, json.dumps([{k: r.get(k) for k in ("id", "estimate", "pct_err", "covered_80", "n_assumptions_used",
                                                     "assumption_weight_share", "usd_total_assumed", "wall_s")}
                             for r in rows], indent=1, ensure_ascii=False), flush=True)
    print(f"total wall {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
