"""离线示例：v2.12 的合并与区间（决定 5）对 v2.11g 的规则，编造的 2 / 3 / 4 个方法，和一道已存题的重算。不调模型、不联网。
同一份输入在两份代码里各跑一次（旧代码先导出：git archive v2.11g triangulate | tar -x -C probes/out/_old_v2.11g）：
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe probes/combine_examples.py <代码根目录>          打印一份代码的结果（json）
  PYTHONIOENCODING=utf-8 ./.venv/Scripts/python.exe probes/combine_examples.py --compare <旧根> <新根>  两份并排
编造的输入只给 combine 用到的字段；旧规则不认识的字段（used_ids、series_auto 的校准区间）它会忽略。
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORED = "results/agent/fc_nhs_ae_2026_09/v211_reg"   # 有登记真值、4 个方法（其中一个 series_naive）的已存运行


def bt(*errs):
    return [{"year": 2023 + i, "log_err": e} for i, e in enumerate(errs)]


CASES = {
    # 2 个方法：两条数据路线、信号不同（METHODS_ZH 4.1 的 ex3）
    "two": [{"id": "m1", "method": "yoy_scaling", "estimate": 1.32e6, "used_ids": ["p1", "p2", "p3"], "backtest": bt(0.04, -0.03)},
            {"id": "m2", "method": "ratio", "estimate": 1.41e6, "used_ids": ["p1", "p7", "p8", "p9"], "backtest": bt(-0.05, 0.06)}],
    # 3 个方法：yoy 和 ratio 用同一条信号（输入相同 -> 一块），formula_mc 靠假设（ex1 的后三个）
    "three": [{"id": "m1", "method": "yoy_scaling", "estimate": 59800.0, "used_ids": ["p1", "p4", "p5"], "backtest": bt(-0.01, 0.02, 0.0)},
              {"id": "m2", "method": "ratio", "estimate": 60500.0, "used_ids": ["p1", "p4", "p5"], "backtest": bt(0.01, -0.02, 0.03)},
              {"id": "m3", "method": "formula_mc", "estimate": 75000.0, "used_ids": ["p9"], "used_assumptions": ["a1", "a2"],
               "backtest": [], "mc": {"p10": 50000.0, "p90": 112000.0}}],
    # 4 个方法：series_auto（模型路径，校准行 comb_ETYL_mean|L13|h2）、yoy_scaling、Fermi 公式、分析师 consensus（公式 = 那个点）
    "four": [{"id": "m1", "method": "series_auto", "estimate": 7476.0, "used_ids": [f"p{i}" for i in range(1, 20)], "backtest": [],
              "series_auto": {"interval": {"q10_ln": -0.201385, "q90_ln": 0.160597, "calibration_row": "comb_ETYL_mean|L13|h2",
                                           "table": "bench-d12f86e0-1013c974"}}},
             {"id": "m2", "method": "yoy_scaling", "estimate": 7650.0, "used_ids": ["p19", "p30", "p31"], "backtest": bt(0.03, -0.02, 0.04)},
             {"id": "m3", "method": "formula_mc", "estimate": 8100.0, "used_ids": ["p40"], "used_assumptions": ["a1", "a2", "a3"],
              "backtest": [], "mc": {"p10": 5800.0, "p90": 11300.0}},
             {"id": "m4", "method": "formula_mc", "estimate": 7900.0, "used_ids": ["p50"], "backtest": [],
              "mc": {"p10": 6583.0, "p90": 9480.0}}],
}
KEYS = ("central", "p10", "p90", "sigma_ln", "basis", "weights", "weight_rule", "weight_basis")


def one(code: Path) -> dict:
    sys.path.insert(0, str(code))
    from triangulate.agent import methods as M
    sys.path.insert(0, str(ROOT / "probes"))
    import recheck_continuous as R
    R.load_code(code)
    out = {}
    for name, rs in CASES.items():
        c = M.combine([dict(r) for r in rs])
        out[name] = {k: c.get(k) for k in KEYS} | {k: c[k] for k in ("combination", "interval", "member_sigma") if k in c}
    st = json.loads((ROOT / STORED / "state.json").read_text(encoding="utf-8"))
    new = R.recompute(st)
    res = new["result"]
    out["stored"] = {"run": STORED, "answer": next(q["answer_value"] for q in R.QUESTIONS if q["id"] == st["qid"]),
                     "methods": [{k: m.get(k) for k in ("id", "label", "method", "estimate", "error", "used_ids", "used_assumptions",
                                                       "baseline_only")} for m in new["methods"]],
                     "result": {k: res.get(k) for k in KEYS} | {k: res[k] for k in ("combination", "interval", "baseline",
                                                                                     "member_sigma") if k in res}}
    return out


def fmt(x):
    return "-" if x is None else f"{x:,.0f}" if abs(x) >= 100 else f"{x:.4g}"


def compare(old_root: str, new_root: str):
    runs = {}
    for tag, root in (("old", old_root), ("new", new_root)):
        p = subprocess.run([sys.executable, __file__, root], capture_output=True, text=True, encoding="utf-8")
        if p.returncode:
            raise SystemExit(p.stderr)
        runs[tag] = json.loads(p.stdout)
    for name in list(CASES) + ["stored"]:
        o, n = runs["old"][name], runs["new"][name]
        ro, rn = (o["result"], n["result"]) if name == "stored" else (o, n)
        print(f"## {name}" + (f" ({o['run']}, answer {fmt(o['answer'])})" if name == "stored" else ""))
        if name == "stored":
            for mo, mn in zip(o["methods"], n["methods"]):
                print(f"  {mn['id']} {mn['method']}: old {fmt(mo['estimate'])}, new {fmt(mn['estimate'])}"
                      + (f" (baseline only {fmt(mn['baseline_only']['estimate'])})" if mn.get("baseline_only") else "")
                      + f"; inputs {mn.get('used_ids')} / {mn.get('used_assumptions')}")
        for tag, r in (("old", ro), ("new", rn)):
            w = ", ".join(f"{k} {v:.3f}" for k, v in (r.get("weights") or {}).items())
            print(f"  {tag}: central {fmt(r['central'])}, 80% [{fmt(r['p10'])}, {fmt(r['p90'])}], basis {r['basis']}, "
                  f"rule {r['weight_rule']}, weights {w}")
        cb = rn.get("combination") or {}
        for b in cb.get("blocks") or []:
            print(f"    {b['id']} = {'+'.join(b['members'])}: {fmt(b['value'])}, rule {b['rule']}, sigma {b['sigma_ln']:.3f} "
                  f"({b['sigma_source']}), shared {b['shared_inputs']}")
        iv = rn.get("interval") or {}
        print(f"    interval: {iv.get('rule')}; rms {iv.get('sigma_blocks_rms')}, Birge {iv.get('birge_ratio')}, "
              f"flags {iv.get('flags')}, sigma {iv.get('sigma_ln')}")
        if name == "stored":
            print(f"    baseline: {rn.get('baseline')}")
            a = o["answer"]
            print(f"    error: old {ro['central'] / a - 1:+.2%}, new {rn['central'] / a - 1:+.2%}; covered old "
                  f"{ro['p10'] <= a <= ro['p90']}, new {rn['p10'] <= a <= rn['p90']}")
        print()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "--compare":
        compare(sys.argv[2], sys.argv[3])
    else:
        print(json.dumps(one(Path(sys.argv[1]).resolve()), default=str))
