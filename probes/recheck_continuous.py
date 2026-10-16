"""离线复核：连续值模式的 7 次保存运行（开发集 4 次、留出测试 3 次），用当前代码重算 compute，确认中心估计不变。
每次运行取最终那一轮裁判的方法（compute.methods_from_round），去掉输入核对没过的方法（audit_failed），
重新校验假设，再跑 compute.run。不调模型、不联网。

用法：.venv/Scripts/python.exe probes/recheck_continuous.py [输出 json 路径]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from triangulate.agent import assumptions as AS  # noqa: E402
from triangulate.agent import compute as C  # noqa: E402

RUNS = [("fc_yell_2026_08", "v21b"), ("fc_yell_2026_09", "v21b"), ("fc_jnto_2026_08", "v21d"),
        ("fc_kr_births_2026_07", "v21d"), ("fc_tw_births_2026_09", "test1"), ("fc_lhr_pax_2026_09", "test1"),
        ("fc_jp_births_2026_07", "test1")]


def recompute(st: dict) -> dict:
    comp = st["compute"]
    jr = next(j for j in st["judge_rounds"] if j.get("round") == comp.get("methods_from_round") and j.get("methods"))
    bad = jr.get("audit_failed") or {}
    methods = [m for i, m in enumerate(jr["methods"]) if str(i) not in bad]
    target = st["plan"]["target"]
    av = AS.validate(jr.get("assumptions") or [], target)
    return C.run(methods, {p["id"]: p for p in st["points"]}, target, assumptions=av)


def main():
    rows = []
    for qid, tag in RUNS:
        st = json.loads((ROOT / "results" / "agent" / qid / tag / "state.json").read_text(encoding="utf-8"))
        saved = st["compute"]["result"]
        new = recompute(st)["result"]
        row = {"qid": qid, "tag": tag, "saved_central": saved.get("central"), "new_central": new.get("central"),
               "saved_p10": saved.get("p10"), "new_p10": new.get("p10"), "saved_p90": saved.get("p90"), "new_p90": new.get("p90"),
               "identical": saved.get("central") == new.get("central")}
        rows.append(row)
        print(f"{qid}/{tag}: saved {saved.get('central')!r} -> now {new.get('central')!r}  identical={row['identical']}")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(json.dumps(rows, indent=1), encoding="utf-8")
    print(f"identical: {sum(r['identical'] for r in rows)}/{len(rows)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
