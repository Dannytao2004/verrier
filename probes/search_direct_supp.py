"""补充运行（不在预注册里，不进成功标准）：arm (3) 联网直接答，只把 max_tokens 从 4096 提到 32000，其他不变。

起因：正式运行（results/forecast/raw/search_direct/，提交 428ba24）两题都在第 1 次调用里搜了 6 次后撞上 max_tokens=4096，
没有最后的文字；4096 是实现时定的，预注册没有规定。每题只跑一次，结果不论好坏都报告。已有保存的记录就跳过。
用法：TRIANGULATE_KEY_FILE=<key 文件> .venv/Scripts/python.exe probes/search_direct_supp.py
"""
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from triangulate.forecast import FC, QUESTIONS  # noqa: E402
from triangulate.llm import TransportError  # noqa: E402
from triangulate.report import _write  # noqa: E402
from triangulate.search_direct import DirectClient, run_search_direct  # noqa: E402

ARM, MAX_TOKENS = "search_direct_supp", 32000
lock = threading.Lock()


def log(rec):
    with lock, (FC / "calls.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(dict(rec, arm=ARM), ensure_ascii=False) + "\n")


def one(q):
    out = FC / "raw" / ARM / f"{q['id']}.json"
    if out.exists():
        return
    try:
        rec = run_search_direct(client, q, max_tokens=MAX_TOKENS)
    except TransportError as e:
        print(f"[skip] {ARM} {q['id']}: {e}", flush=True)
        return
    rec.update(arm=ARM, supplementary=True, reason=__doc__.splitlines()[0])
    _write(out, rec)
    print(f"{ARM} {q['id']} attempts={len(rec['attempts'])} status={rec['status']} estimate={rec['estimate']}", flush=True)


client = DirectClient(log)
qs = [q for q in QUESTIONS if q.get("set") == "live"]
with ThreadPoolExecutor(len(qs)) as ex:
    list(ex.map(one, qs))
