"""v2.12b 离线回放（不调模型）：把 results/agent 下所有存档里被接受的单位裁定，重新过一遍 _dropped（单位里的倍数漏乘），
列出会被打回重裁的方法。用法：./.venv/Scripts/python.exe probes/replay_unit_dropped.py"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from triangulate.agent import unit_review as UR  # noqa: E402


def points(st: dict) -> dict:
    by_id = {}

    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("id"), str) and o["id"].startswith("p") and "quote" in o and "unit" in o:
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
    n_rev = n_hit = 0
    for path in sorted(glob.glob("results/agent/*/*/state.json")):
        name = os.path.relpath(os.path.dirname(path), "results/agent").replace("\\", "/")
        try:
            st = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        by_id = points(st)
        for r in st.get("judge_rounds") or []:
            for ur in r.get("unit_reviews") or []:
                for rec in ur["methods"]:
                    acc = [a for a in rec.get("arbiter") or [] if a.get("reply") and a.get("problem") == ""]
                    if not acc:
                        continue
                    n_rev += 1
                    rep = acc[-1]["reply"]
                    named = {x["name"]: f for x in rep.get("inputs") or [] if isinstance(x, dict) and x.get("name") in by_id
                             and (f := UR._named_multiplier(by_id[x["name"]])) != 1}
                    if d := UR._dropped(rep, named):
                        n_hit += 1
                        nm = d.split(":")[0].replace("input ", "")
                        got = [x["unit"] for x in rep["inputs"] if x.get("name") == nm]
                        print(f"{name} {rec.get('label') or rec.get('method')} | {nm} {by_id[nm]['unit']!r} "
                              f"{by_id[nm].get('value_as_written')!r} -> arbiter {got} | result {rep.get('result_unit')}")
    print(f"accepted unit reviews: {n_rev}  would be re-asked: {n_hit}")


if __name__ == "__main__":
    main()
