# showcase1 打分专用的冻结 engine：commit f1ac7b0 的 triangulate/engine.py 逐字拷贝（只加了这两行注释）。
# 预注册展示集（results/showcase/summary.json）每次打分都用它重算结构化臂；不要改，engine.py 的修改不进这里。
"""structured arm 的计算端：校验模型给的结构 -> 单位换算 -> Monte Carlo -> 聚合 -> 敏感度 -> world model 状态。

errors：会触发一次重试的问题（发回给模型）；warnings：只记录。
同一个函数既用于运行时判断要不要重试，也用于 report 时离线重算（同输入、同种子 -> 同结果）。
"""
import math
import numbers

from . import graph as graph_mod
from .config import MC_SAMPLES, MC_SEED
from .expr import FUNCS, NAME_RE, DimError, Formula, FormulaError
from .mc import aggregate, lognormal_median, sample_inputs
from .units import UnitError, dims_str, parse_unit

METHODS = ("top_down", "bottom_up", "proxy")


def _num(x):
    return isinstance(x, numbers.Real) and not isinstance(x, bool) and math.isfinite(x)


def _inputs(spec, errors, warnings):
    out, seen = [], set()
    raw_inputs = spec.get("inputs")
    if not isinstance(raw_inputs, list) or not raw_inputs:
        errors.append('"inputs" must be a non-empty list')
        return out
    for k, raw in enumerate(raw_inputs):
        issues = []
        if not isinstance(raw, dict):
            errors.append(f"inputs[{k}] is not an object")
            continue
        name = raw.get("name")
        if not isinstance(name, str) or not NAME_RE.match(name) or name in FUNCS:
            errors.append(f"inputs[{k}].name {name!r} is not a valid identifier")
            continue
        if name in seen:
            errors.append(f"input {name!r} defined twice")
            continue
        seen.add(name)
        rec = {"name": name, "description": raw.get("description", ""), "value": raw.get("value"),
               "low": raw.get("low"), "high": raw.get("high"), "unit": raw.get("unit", ""),
               "provenance": raw.get("provenance")}
        v, lo, hi = rec["value"], rec["low"], rec["high"]
        if not (_num(v) and _num(lo) and _num(hi)):
            issues.append("value/low/high must all be finite numbers")
        elif not (0 < lo <= v <= hi):
            issues.append(f"need 0 < low <= value <= high, got low={lo}, value={v}, high={hi}")
        try:
            u = parse_unit(rec["unit"] if rec["unit"] is not None else "")
            rec["count_nouns"] = list(u.count_nouns)
            rec["dims"] = dims_str(u.dims)
        except UnitError as e:
            u = None
            issues.append(f"unit: {e}")
        prov = rec["provenance"]
        status = "missing"
        if not isinstance(prov, dict) or prov.get("type") not in ("assumption", "sourced"):
            issues.append('provenance.type must be "assumption" or "sourced"')
        elif prov["type"] == "assumption":
            status = "assumption"
            if not str(prov.get("rationale") or "").strip():
                issues.append("assumption needs a one-line rationale")
        else:
            status = "sourced_unverified"  # 没有检索，模型自报的出处一律未核实
            if not str(prov.get("source") or "").strip():
                issues.append("sourced input needs a source name")
        rec["issues"] = issues
        if issues:
            rec["status"], rec["usable"] = "missing", False
            errors.extend(f"input {name!r}: {m}" for m in issues)
        else:
            rec["status"], rec["usable"] = status, True
            rec["_unit"] = u
            rec["si"] = {"low": lo * u.factor, "high": hi * u.factor, "value": v * u.factor}
            rec["median"] = lognormal_median(lo, hi)
        out.append(rec)
    return out


def evaluate_structured(spec, target_unit: str, qid: str, *, strict_target: bool = True,
                        question: str = "", n: int = MC_SAMPLES, seed=MC_SEED) -> dict:
    errors, warnings = [], []
    target = parse_unit(target_unit, strict=strict_target)
    state = {"qid": qid, "question": question,
             "target": {"unit": target_unit, "dims": dims_str(target.dims), "definition": ""},
             "inputs": [], "paths": [], "errors": errors, "warnings": warnings,
             "mc": {"samples": n, "seed": f"{seed}:{qid}", "input_distribution": "lognormal, low/high = P10/P90"}}
    if not isinstance(spec, dict):
        errors.append("reply is not a JSON object")
        state["result"] = {"central": None, "p10": None, "p90": None, "unit": target_unit, "n_valid_paths": 0, "outliers": []}
        state["graph"] = graph_mod.build_graph(state)
        return state
    tgt = spec.get("target") if isinstance(spec.get("target"), dict) else {}
    state["target"]["definition"] = str(tgt.get("definition") or "")
    if not state["target"]["definition"]:
        warnings.append("target.definition missing")

    inputs = _inputs(spec, errors, warnings)
    by_name = {i["name"]: i for i in inputs}

    raw_paths = spec.get("paths")
    if not isinstance(raw_paths, list):
        errors.append('"paths" must be a list')
        raw_paths = []
    if len(raw_paths) != 3:
        errors.append(f"expected exactly 3 paths, got {len(raw_paths)}")
    paths, formulas, seen = [], {}, set()
    missing = {}
    for k, raw in enumerate(raw_paths):
        if not isinstance(raw, dict):
            errors.append(f"paths[{k}] is not an object")
            continue
        pid = str(raw.get("id") or f"p{k + 1}")
        if pid in seen:
            pid = f"{pid}_{k + 1}"
        seen.add(pid)
        p = {"id": pid, "method": raw.get("method"), "description": raw.get("description", ""),
             "formula": raw.get("formula"), "output_unit": raw.get("output_unit", ""), "issues": [], "uses": []}
        if p["method"] not in METHODS:
            warnings.append(f"path {pid}: method {p['method']!r} not one of {METHODS}")
        try:
            f = Formula(p["formula"])
        except FormulaError as e:
            p["issues"].append(f"formula: {e}")
            f = None
        if f is not None:
            p["uses"] = sorted(f.names)
            undefined = [x for x in p["uses"] if x not in by_name]
            for x in undefined:
                missing.setdefault(x, []).append(pid)
                p["issues"].append(f"uses undefined input {x!r}")
            unusable = [x for x in p["uses"] if x in by_name and not by_name[x]["usable"]]
            if unusable:
                p["issues"].append(f"uses invalid input(s) {unusable}")
            if not undefined and not unusable:
                try:
                    d = f.dims({x: by_name[x]["_unit"].dims for x in p["uses"]})
                    p["dims"] = dims_str(d)
                    if d != target.dims:
                        p["issues"].append(f"dimension mismatch: formula gives {dims_str(d)}, target is {dims_str(target.dims)}")
                except (DimError, FormulaError) as e:
                    p["issues"].append(f"units: {e}")
                try:
                    ou = parse_unit(p["output_unit"] or "")
                    if "dims" in p and dims_str(ou.dims) != p["dims"]:
                        warnings.append(f"path {pid}: declared output_unit {p['output_unit']!r} ({dims_str(ou.dims)}) "
                                        f"differs from computed {p['dims']}; computed one is used")
                except UnitError:
                    warnings.append(f"path {pid}: output_unit {p['output_unit']!r} not parseable (ignored)")
        # 输入本身的错误已经记过，这里只把路径特有的问题发回模型
        errors.extend(f"path {pid}: {m}" for m in p["issues"] if not m.startswith("uses invalid"))
        p["status"] = "invalid" if p["issues"] else "valid"
        if p["status"] == "valid":
            formulas[pid] = f
        paths.append(p)

    for name, users in missing.items():
        inputs.append({"name": name, "description": "", "value": None, "low": None, "high": None, "unit": None,
                       "provenance": None, "status": "missing", "usable": False,
                       "issues": [f"referenced by {', '.join(users)} but not defined"]})
    for i in inputs:
        i["used_by"] = [p["id"] for p in paths if i["name"] in p["uses"]]
        i["n_dependents"] = len(i["used_by"])

    # ---------- Monte Carlo ----------
    needed = sorted({x for f in formulas.values() for x in f.names})
    ranges = {x: (by_name[x]["si"]["low"], by_name[x]["si"]["high"]) for x in needed}
    samples = sample_inputs(ranges, n, f"{seed}:{qid}")
    path_samples = {pid: [v / target.factor for v in f.eval_vec(samples, n)] for pid, f in formulas.items()}
    agg = aggregate(path_samples)
    for p in paths:
        s = agg["paths"].get(p["id"])
        if s is None:
            continue
        p.update(median=s["median"], p10=s["p10"], p90=s["p90"], n_nonfinite=s["n_nonfinite"],
                 n_nonpositive=s["n_nonpositive"], log10_vs_central=s.get("log10_vs_central"))
        if p["id"] not in agg["used"]:
            p["status"] = "invalid"
            p["issues"].append("path median is not a positive finite number")
        elif p["id"] in agg["outliers"]:
            p["status"] = "outlier"
    used = {pid: formulas[pid] for pid in agg["used"]}
    meds = [agg["paths"][pid]["median"] for pid in agg["used"]]
    state["result"] = {
        "central": agg["central"], "p10": agg["p10"], "p90": agg["p90"], "unit": target_unit,
        "n_valid_paths": len(agg["used"]), "outliers": agg["outliers"],
        "path_spread_oom": (math.log10(max(meds)) - math.log10(min(meds))) if meds else None,
    }

    # ---------- 敏感度 ----------
    sens = graph_mod.sensitivity(ranges, used, target.factor) if used else {}
    for i in inputs:
        s = sens.get(i["name"], {})
        i["sensitivity"], i["sensitivity_path_max"] = s.get("final"), s.get("path_max")
        i.pop("_unit", None)
    state["inputs"], state["paths"] = inputs, paths
    state["graph"] = graph_mod.build_graph(state)
    return state
