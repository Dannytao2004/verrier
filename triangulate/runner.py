"""在线部分：对 20 题跑两个 arm（以及 finance demo），只保存原始回复。已有结果的题默认跳过（防止误重跑）。"""
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from .arms import run_naive, run_structured
from .config import MAX_CONCURRENCY
from .data import load_backtest
from .llm import LLM, KeyRejected
from .report import DEMO, DEMO_RAW, raw_path


def _save(p, rec):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")


def run_backtest(force: bool = False, limit: int | None = None):
    qs = load_backtest()[:limit] if limit else load_backtest()
    tasks = [(arm, q) for q in qs for arm in ("naive", "structured") if force or not raw_path(arm, q["id"]).exists()]
    if not tasks:
        print("all raw replies already saved; use --force to re-run (this costs money and changes results)")
        return
    llm = LLM()
    fns = {"naive": run_naive, "structured": run_structured}
    done = 0
    with ThreadPoolExecutor(MAX_CONCURRENCY) as ex:
        futs = {ex.submit(fns[arm], llm, q): (arm, q["id"]) for arm, q in tasks}
        try:
            for fut in as_completed(futs):
                arm, qid = futs[fut]
                rec = fut.result()
                _save(raw_path(arm, qid), rec)
                done += 1
                last = rec["attempts"][-1]
                print(f"[{done}/{len(tasks)}] {arm:10s} {qid:9s} attempts={len(rec['attempts'])} "
                      f"problems={len(last['problems'])}", flush=True)
        except KeyRejected:
            for f in futs:
                f.cancel()
            raise


def run_demo(force: bool = False):
    if DEMO_RAW.exists() and not force:
        print("demo reply already saved; use --force to re-run")
        return
    rec = run_structured(LLM(), DEMO)
    _save(DEMO_RAW, rec)
    print(f"demo attempts={len(rec['attempts'])} problems={rec['attempts'][-1]['problems']}")
