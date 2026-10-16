"""离线：一次保存运行的用时拆分（规划、搜索、取页、抽取、已公布检查、裁判 / 核对 / 终稿）、取页数和成本。
数据只来自 state.json 和 calls.jsonl（calls 的 at = 开始时刻，latency_s = 用时）；v2.5 起 live 页另有 fetch_at / fetch_s。
阶段在各方向之间是并行的：「合计」是各次用时之和，「跨度」是这一阶段第一次开始到最后一次结束的墙钟时间。
用法：.venv/Scripts/python.exe probes/time_split.py results/agent/<qid>/<tag> [更多运行目录 ...]
"""
import json
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path


def _t(s):
    return datetime.fromisoformat(s)


def split(run_dir: Path) -> dict:
    st = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    calls = [json.loads(x) for x in (run_dir / "calls.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    calls = [c for c in calls if c.get("at") and c.get("latency_s") is not None]
    t0 = _t(st["started_at"].replace("Z", "+00:00")) if "T" in st["started_at"] and "-" in st["started_at"] else None
    if t0 is None:
        t0 = datetime.strptime(st["started_at"], "%Y%m%dT%H%M%SZ").replace(tzinfo=_t(calls[0]["at"]).tzinfo)
    groups = {"plan": ("plan",), "search": ("search:",), "extract": ("extract:",), "published_check": ("published",),
              "judge": ("judge:",), "audit": ("audit",), "final": ("final",)}
    out = {"run": str(run_dir), "wall_s": st["wall_s"], "budget": st["budget"], "phases": {}}
    for name, pre in groups.items():
        cs = [c for c in calls if c["arm"].startswith(pre)]
        if not cs:
            continue
        a = min(_t(c["at"]) for c in cs)
        b = max(_t(c["at"]) + timedelta(seconds=c["latency_s"]) for c in cs)
        out["phases"][name] = {"n": len(cs), "sum_s": round(sum(c["latency_s"] for c in cs), 1),
                               "span_s": round((b - a).total_seconds(), 1),
                               "from_start_s": [round((a - t0).total_seconds(), 1), round((b - t0).total_seconds(), 1)],
                               "roles": dict(Counter(c["arm"].split(":")[0] if not c["arm"].startswith("published") else c["arm"]
                                                     for c in cs))}
    pages = [pg for r in st.get("results") or [] for pg in r.get("pages") or []]
    timed = [pg for pg in pages if pg.get("fetch_at") and pg.get("fetch_s") is not None]
    if timed:
        a = min(_t(pg["fetch_at"]) for pg in timed)
        b = max(_t(pg["fetch_at"]) + timedelta(seconds=pg["fetch_s"]) for pg in timed)
        out["phases"]["fetch"] = {"n": len(timed), "sum_s": round(sum(pg["fetch_s"] for pg in timed), 1),
                                  "max_s": max(pg["fetch_s"] for pg in timed), "span_s": round((b - a).total_seconds(), 1),
                                  "from_start_s": [round((a - t0).total_seconds(), 1), round((b - t0).total_seconds(), 1)]}
    elif "search" in out["phases"] and "extract" in out["phases"]:   # v2.5 以前没记取页用时：搜索结束到最后一次抽取开始
        s_end = out["phases"]["search"]["from_start_s"][1]
        last_x = max(_t(c["at"]) for c in calls if c["arm"].startswith("extract:"))
        out["phases"]["fetch"] = {"note": "not recorded before v2.5; span = last search end -> last extract start",
                                  "span_s": round((last_x - t0).total_seconds() - s_end, 1)}
    out["pages"] = {"n": len(pages), "status": dict(Counter(pg.get("status") for pg in pages)),
                    "dropped_reasons": dict(Counter((pg.get("reason") or "")[:70] for pg in pages if pg.get("status") == "dropped")),
                    "sent_to_extractor": sum(1 for pg in pages if pg.get("chars_sent"))}
    out["directions"] = [{"id": r["direction_id"], "round": r["round"], "wall_s": r.get("wall_s"),
                          "n_pages": len(r.get("pages") or []), "n_points": len(r.get("points") or []),
                          "stopped": r.get("stopped") or r.get("aborted") or r.get("error")} for r in st.get("results") or []]
    pub, pe = st.get("published") or {}, st.get("published_early") or {}
    out["published"] = {k: pub.get(k) for k in ("status", "early_stop", "id", "value", "date", "confirmed_ids")}
    out["published"]["source_url"] = (pub.get("point") or {}).get("source_url")
    out["published_early"] = {k: pe.get(k) for k in ("status", "n_checks", "off")} if pe else None
    return out


if __name__ == "__main__":
    for d in sys.argv[1:]:
        print(json.dumps(split(Path(d)), indent=1, ensure_ascii=False, default=str))
