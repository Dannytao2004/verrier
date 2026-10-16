"""离线复核：连续值模式的保存运行，用指定的一份代码重算 compute。不调模型、不联网，只写 stdout 和 probes/out/。

1. 原有的 7 次检查（开发集 4 次、留出测试 3 次）：重算的中心估计和保存值逐位相同（identical: 7/7）。
2. 全量回归表：results/agent/**/state.json 里每个有方法的连续值运行（跳过离散、答案已公布、提前停、compute 那一轮没有方法的）。
   每次运行取 compute 用的那一轮裁判方法（compute.methods_from_round），去掉输入核对没过的方法（audit_failed），
   重新校验假设，再跑 compute.run（消融运行和 graph 的 compute 节点一样，只允许 ablation.ALLOWED_METHODS）。
   每行：qid/tag、中心、P10、P90、P90/P10、basis；forecast.QUESTIONS 里有登记真值的题再加 % 误差和是否覆盖。
   这张表用来比较两份代码对同一输入的重算结果，不是「重算 vs 保存值」（旧运行是用当时的代码算的，本来就可能不同）。
3. 终稿 lint：每个保存运行的 final.text 里 "[n]"、"[unknown placeholder]"、"no basis" 的出现次数；
   合计给两种口径：含有它的终稿数、总出现次数。

用法（解释器 .venv/Scripts/python.exe）：
  probes/recheck_continuous.py [输出 json 路径]           原有用法；这个 json 里只有 7 次检查的行
  probes/recheck_continuous.py --code <代码根目录>         用另一份代码重算（git archive <tag> triangulate | tar -x -C 目录）
  probes/recheck_continuous.py --json probes/out/x.json    全部结果写成 json（只允许写到 probes/out/ 下）
  probes/recheck_continuous.py --diff a.json b.json        按 qid/tag 比较两份 --json 的回归表，有差异时退出码 1
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "probes" / "out"
AGENT = ROOT / "results" / "agent"

RUNS = [("fc_yell_2026_08", "v21b"), ("fc_yell_2026_09", "v21b"), ("fc_jnto_2026_08", "v21d"),
        ("fc_kr_births_2026_07", "v21d"), ("fc_tw_births_2026_09", "test1"), ("fc_lhr_pax_2026_09", "test1"),
        ("fc_jp_births_2026_07", "test1")]
LINT = ("[n]", "[unknown placeholder]", "no basis")

AS = C = AB = None   # load_code() 按 --code 导入
QUESTIONS = []


def load_code(code_root: Path) -> Path:
    """把 code_root 放到 sys.path 最前面再导入 triangulate（同 compare_continuous_paths.py），返回实际导入的包目录。"""
    global AS, C, AB, QUESTIONS
    sys.path.insert(0, str(code_root))
    import triangulate
    from triangulate.agent import ablation, assumptions, compute
    from triangulate.forecast import QUESTIONS as qs
    AS, C, AB, QUESTIONS = assumptions, compute, ablation, qs
    return Path(triangulate.__file__).resolve().parent


def compute_round(st: dict):
    """compute 用的那一轮裁判（round == compute.methods_from_round 且有方法）；没有就是 None。"""
    comp = st.get("compute") or {}
    return next((j for j in st.get("judge_rounds") or []
                 if j.get("round") == comp.get("methods_from_round") and j.get("methods")), None)


def recompute(st: dict) -> dict:
    jr = compute_round(st)
    if jr is None:
        raise ValueError("no judge round with methods")
    bad = jr.get("audit_failed") or {}
    methods = [m for i, m in enumerate(jr["methods"]) if str(i) not in bad]
    target = st["plan"]["target"]
    av = AS.validate(jr.get("assumptions") or [], target)
    only = AB.ALLOWED_METHODS if st.get("ablation") else None   # 同 graph 的 compute 节点：消融运行只允许这些方法
    return C.run(methods, {p["id"]: p for p in st.get("points") or []}, target, assumptions=av, only_methods=only)


def skip_reason(st: dict) -> str:
    """回归表不收的运行返回原因；收的返回空串。"""
    target = (st.get("plan") or {}).get("target") or {}
    if not target:
        return "no_target"
    if target.get("outcome_type") == "discrete":
        return "discrete"
    pub = st.get("published") or {}
    if pub.get("early_stop"):
        return "early_stop"
    if pub.get("status") == "published" or ((st.get("compute") or {}).get("result") or {}).get("basis") == "published":
        return "published"
    if compute_round(st) is None:
        return "no_methods"
    return ""


def table_row(key: str, st: dict, answers: dict) -> dict:
    row = {"key": key, "qid": st.get("qid")}
    try:
        r = recompute(st)["result"]
    except Exception as e:   # 某份代码对某个 state 报错：记下来，表照样出
        row["error"] = f"{type(e).__name__}: {e}"[:200]
        return row
    c, lo, hi = r.get("central"), r.get("p10"), r.get("p90")
    ans = answers.get(st.get("qid"))
    row.update(central=c, p10=lo, p90=hi, p90_p10=hi / lo if lo and hi else None, basis=r.get("basis"), answer=ans,
               pct_err=None if ans is None or c is None else c / ans - 1,
               covered=None if ans is None or c is None else lo <= ans <= hi)
    return row


def _n(x) -> str:
    return "-" if x is None else f"{x:,.0f}" if abs(x) >= 100 else f"{x:.4g}"


def print_table(rows: list):
    w = max([len(r["key"]) for r in rows] + [7])
    print(f"{'qid/tag':<{w}}  {'central':>12}  {'P10':>12}  {'P90':>12}  {'P90/P10':>7}  {'basis':<17}  {'err':>7}  covered")
    for r in rows:
        if "error" in r:
            print(f"{r['key']:<{w}}  ERROR {r['error']}")
            continue
        err = "-" if r["pct_err"] is None else f"{r['pct_err']:+.1%}"
        cov = "-" if r["covered"] is None else "yes" if r["covered"] else "no"
        ratio = "-" if r["p90_p10"] is None else f"{r['p90_p10']:.3f}"
        print(f"{r['key']:<{w}}  {_n(r['central']):>12}  {_n(r['p10']):>12}  {_n(r['p90']):>12}  {ratio:>7}  "
              f"{str(r['basis']):<17}  {err:>7}  {cov}")


def diff(a: Path, b: Path) -> int:
    """按 key（qid/tag）比较两份 --json 输出的 rows；打印有差异的行，有差异返回 1。"""
    ra = {r["key"]: r for r in json.loads(a.read_text(encoding="utf-8"))["rows"]}
    rb = {r["key"]: r for r in json.loads(b.read_text(encoding="utf-8"))["rows"]}
    n = 0
    for k in sorted(set(ra) | set(rb)):
        if k not in ra or k not in rb:
            n += 1
            print(f"{k}: only in {a if k in ra else b}")
            continue
        d = [(f, ra[k].get(f), rb[k].get(f)) for f in sorted(set(ra[k]) | set(rb[k]))
             if json.dumps(ra[k].get(f)) != json.dumps(rb[k].get(f))]
        if d:
            n += 1
            print(f"{k}: " + "; ".join(f"{f} {x!r} -> {y!r}" for f, x, y in d))
    print(f"rows: {len(ra)} vs {len(rb)}; differing: {n}")
    return 1 if n else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="offline recompute of saved continuous runs")
    ap.add_argument("out", nargs="?", help="original usage: write the 7 identical-check rows here")
    ap.add_argument("--code", type=Path, default=ROOT, help="code root to import triangulate from")
    ap.add_argument("--json", type=Path, help="write all rows as json (must be under probes/out/)")
    ap.add_argument("--diff", nargs=2, type=Path, metavar=("A_JSON", "B_JSON"), help="compare two --json outputs")
    a = ap.parse_args(argv)
    if a.diff:
        return diff(*a.diff)
    if a.json is not None and OUT_DIR.resolve() not in a.json.resolve().parents:
        ap.error("--json must be a path under probes/out/")
    pkg = load_code(a.code.resolve())
    print(f"code: {pkg}")

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
    if a.out:
        Path(a.out).write_text(json.dumps(rows, indent=1), encoding="utf-8")
    print(f"identical: {sum(r['identical'] for r in rows)}/{len(rows)}")

    answers = {q["id"]: q["answer_value"] for q in QUESTIONS if q.get("answer_value") is not None}
    table, skipped, lint_rows = [], {}, []
    for p in sorted(AGENT.glob("**/state.json")):
        key = p.parent.relative_to(AGENT).as_posix()
        st = json.loads(p.read_text(encoding="utf-8"))
        why = skip_reason(st)
        if why:
            skipped.setdefault(why, []).append(key)
        else:
            table.append(table_row(key, st, answers))
        text = (st.get("final") or {}).get("text")
        if isinstance(text, str) and text:
            lint_rows.append({"key": key, **{s: text.count(s) for s in LINT}})

    print(f"\nregression table: {len(table)} continuous runs with methods")
    print_table(table)
    print("skipped: " + "; ".join(f"{k} {len(v)} ({', '.join(v)})" for k, v in sorted(skipped.items())))

    totals = {s: {"finals": sum(r[s] > 0 for r in lint_rows), "occurrences": sum(r[s] for r in lint_rows)} for s in LINT}
    print(f"\nfinal-text lint: {len(lint_rows)} saved finals (finals with no hits not listed)")
    for r in lint_rows:
        if any(r[s] for s in LINT):
            print(f"  {r['key']}: " + ", ".join(f"{s} {r[s]}" for s in LINT))
    print("lint totals: " + "; ".join(f"{s!r} in {t['finals']}/{len(lint_rows)} finals, {t['occurrences']} in total"
                                      for s, t in totals.items()))

    if a.json is not None:
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(json.dumps({"code": str(pkg), "identical": rows, "rows": table, "skipped": skipped,
                                      "lint": {"runs": lint_rows, "totals": totals}}, indent=1, ensure_ascii=False),
                          encoding="utf-8")
        print(f"json: {a.json}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
