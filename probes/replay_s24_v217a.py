"""v2.17a（BUGS S24）离线重放：数字写法按页面定以后，存档里哪些点的读数变了。不调模型、不联网，不改 results/、data/。

已存运行（results/agent/**/state.json）里每个通过代码核对的点，页面原文在 data/raw/agent/ 有缓存的：按和 pipeline 一样的
截断（MAX_CHARS_TO_EXTRACTOR）判页面写法（evidence.page_number_format），再用旧读法（fmt="en"）和新读法各读一遍
value_as_written（代码读数的点用 parse_value，读数路径的点用 read_reading + 存下的读数），逐条比较。
丢点一侧：dropped_points 里原因以 "number:" 开头的（只存了 value_as_written 前 40 个字符，没有 quote），按新写法重读数字这一步，
看哪些现在读得出来（不是完整的核对）。
用法：.venv/Scripts/python.exe probes/replay_s24_v217a.py [--json probes/out/replay_s24.json]"""
import argparse
import collections
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent.pipeline import MAX_CHARS_TO_EXTRACTOR  # noqa: E402


def page_text(qid: str, url: str, ts):
    k = hashlib.sha1(f"{url}|{ts or 'live'}".encode("utf-8")).hexdigest()[:16]
    f = ROOT / "data" / "raw" / "agent" / qid / f"{k}.txt"
    return f.read_text(encoding="utf-8") if f.exists() else None


def read(p: dict, fmt: str):
    vw, sw = p.get("value_as_written") or "", p.get("scale_word") or ""
    reading = p.get("reading_from_extractor") or p.get("reading")
    try:
        if reading:
            v = ev.read_reading(reading, vw, sw, fmt)
            return ("ok", v[0], v[1], v[2])
        v = ev.parse_value(vw, sw, fmt)
        return ("ok", v[0], v[1])
    except ValueError as e:
        return ("error", str(e)[:90])


def main(out_json=None):
    fmt_cache, stats = {}, collections.Counter()
    by_fmt = collections.Counter()
    changed, dropped_rows = [], []
    for f in sorted((ROOT / "results" / "agent").glob("*/*/state.json")):
        st = json.loads(f.read_text(encoding="utf-8"))
        qid = st.get("qid") or f.parent.parent.name
        for p in st.get("points") or []:
            url, ts = p.get("source_url") or "", p.get("snapshot_ts")
            if not url:
                continue
            key = (qid, url, ts)
            if key not in fmt_cache:
                t = page_text(qid, url, ts)
                fmt_cache[key] = None if t is None else ev.page_number_format(ev.norm(t[:MAX_CHARS_TO_EXTRACTOR]), url)
            nf = fmt_cache[key]
            if nf is None:
                stats["point: no cached page"] += 1
                continue
            by_fmt[nf[0]] += 1
            old, new = read(p, "en"), read(p, nf[0])
            if old == new:
                stats[f"point: same ({nf[0]})"] += 1
            else:
                stats[f"point: CHANGED ({nf[0]})"] += 1
                changed.append({"run": str(f.parent.relative_to(ROOT / "results" / "agent")), "id": p.get("id"),
                                "host": urlsplit(url).hostname, "fmt": nf[0], "lang": nf[1],
                                "written": p.get("value_as_written"), "scale_word": p.get("scale_word"),
                                "old": old, "new": new, "name": (p.get("name") or "")[:70]})
        for r in st.get("results") or []:
            for d in (r or {}).get("dropped_points") or []:
                why = str(d.get("reason") or "")
                if not why.startswith("number:"):
                    continue
                url, ts = d.get("source_url") or "", d.get("snapshot_ts")
                key = (qid, url, ts)
                if key not in fmt_cache:
                    t = page_text(qid, url, ts)
                    fmt_cache[key] = None if t is None else ev.page_number_format(ev.norm(t[:MAX_CHARS_TO_EXTRACTOR]), url)
                nf = fmt_cache[key]
                if nf is None or nf[0] == "en":
                    stats[f"dropped (number): {'no cached page' if nf is None else 'en page, unchanged'}"] += 1
                    continue
                try:
                    v = ev.parse_value(d.get("value_as_written") or "", "", nf[0])
                    stats[f"dropped (number): now readable ({nf[0]})"] += 1
                    dropped_rows.append({"run": str(f.parent.relative_to(ROOT / "results" / "agent")),
                                         "host": urlsplit(url).hostname, "fmt": nf[0], "lang": nf[1],
                                         "written": d.get("value_as_written"), "old_reason": why[:80], "now": v[0]})
                except ValueError:
                    stats[f"dropped (number): still not readable ({nf[0]})"] += 1
    pages = collections.Counter(v[0] for v in fmt_cache.values() if v)
    langs = collections.Counter((v[0], v[1]) for v in fmt_cache.values() if v and v[0] != "en")
    print("pages with cached text by format:", dict(pages))
    print("non-en pages by language:", dict(langs))
    print("points by page format:", dict(by_fmt))
    for k in sorted(stats):
        print(f"  {stats[k]:6d}  {k}")
    print("\nchanged kept points:")
    for c in changed:
        print(f"  [{c['fmt']}/{c['lang']}] {c['run']} {c['id']} {c['host']}: {c['written']!r} {c['old']} -> {c['new']}  ({c['name']})")
    print(f"\ndropped points now readable: {len(dropped_rows)}")
    for d in dropped_rows[:40]:
        print(f"  [{d['fmt']}/{d['lang']}] {d['run']} {d['host']}: {d['written']!r} -> {d['now']:g}  (was: {d['old_reason']})")
    if out_json:
        Path(out_json).write_text(json.dumps({"stats": stats, "pages": pages, "changed": changed, "dropped": dropped_rows},
                                             ensure_ascii=False, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--json")
    main(a.parse_args().json)
