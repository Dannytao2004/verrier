"""v2.12b 离线回放（不调模型、不联网）：results/agent 下所有存档里的点，按现在的 pipeline._pair_unit 重新配对一遍。
存档的点已经过了旧的配对（原文有依据的倍数已挪到数上，unit 里不再有倍数），所以这里只会动「unit 里还写着倍数」的点：
列出它们的计算值怎么变、哪些现在会被丢掉。表头不在存档里，依据一栏按 quote 判（header 给空串），不影响挪不挪。
用法：./.venv/Scripts/python.exe probes/replay_unit_pairing.py"""
import glob
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent.pipeline import _pair_unit  # noqa: E402


def points(st: dict) -> dict:
    by_id = {}

    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("id"), str) and o["id"].startswith("p") and "quote" in o and "unit" in o and "value" in o:
                by_id.setdefault(o["id"], o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(st.get("points"))
    walk(st.get("results"))
    return by_id


def main():
    n_pts, moved, dropped = 0, [], []
    for path in sorted(glob.glob("results/agent/*/*/state.json")):
        run = os.path.relpath(os.path.dirname(path), "results/agent").replace("\\", "/")
        try:
            st = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for pid, p in points(st).items():
            n_pts += 1
            unit = str(p.get("unit") or "")
            if unit == "%" or not ev.unit_multipliers(unit):
                continue
            got = _pair_unit(unit, str(p.get("value_as_written") or ""), str(p.get("scale_word") or ""), ev.norm(str(p.get("quote") or "")), "")
            if isinstance(got, str):
                dropped.append((run, pid, unit, p.get("value_as_written"), got))
            elif got and got[1] != 1:   # 倍数为 1：老存档里代码已乘过、unit 只是去掉倍数，计算值不变
                new_unit, g, sw, basis = got
                moved.append((run, pid, unit, p.get("value_as_written"), p["value"], p["value"] * g, new_unit, sw, basis,
                              str(p.get("quote") or "")[:90]))
    print(f"points: {n_pts}  value changes: {len(moved)}  newly dropped: {len(dropped)}")
    print("by unit:", Counter(m[2] for m in moved).most_common())
    for m in moved:
        print(f"  {m[0]} {m[1]} | {m[2]!r} vw={m[3]!r}: {m[4]:g} -> {m[5]:g} {m[6]!r} sw={m[7]!r} basis={m[8]} | {m[9]!r}")
    for d in dropped:
        print("  DROP", *d)


if __name__ == "__main__":
    main()
