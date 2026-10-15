"""依赖图与敏感度。

节点：target、path、input（含 missing 占位）。边：input -used_by-> path，path -aggregated_into-> target。
输入节点状态：sourced_verified | sourced_unverified | assumption | missing | contradicted
（本探针没有检索，sourced_verified / contradicted 只保留在词表里，不会出现）。

敏感度（每个输入）：其他输入固定在中位数，该输入从 low 移到 high，最终估计的 log10 变化量。
「最终估计」在这里用确定性代理：各有效路径在该组输入下的点值，在 log 空间取中位数（与聚合口径一致）。
"""
import math

from .mc import log_median

INPUT_STATUSES = ("sourced_verified", "sourced_unverified", "assumption", "missing", "contradicted")


def _final(formulas: dict, env: dict, target_factor: float):
    vals = []
    for f in formulas.values():
        try:
            v = f.eval(env) / target_factor
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
        if math.isfinite(v) and v > 0:
            vals.append(v)
    return log_median(vals) if vals else None


def _point(f, env, target_factor):
    try:
        v = f.eval(env) / target_factor
    except (ValueError, ZeroDivisionError, OverflowError):
        return None
    return v if math.isfinite(v) and v > 0 else None


def sensitivity(ranges_si: dict, formulas: dict, target_factor: float) -> dict:
    """ranges_si: name -> (low_si, high_si)；formulas: path_id -> Formula（只含进入聚合的有效路径）。
    返回 name -> {"final": 带符号的 Δlog10(最终估计) 或 None, "path_max": 单条路径上最大的 |Δlog10| 或 None}。"""
    med = {k: math.sqrt(lo * hi) for k, (lo, hi) in ranges_si.items()}
    out = {}
    for name, (lo, hi) in ranges_si.items():
        users = {pid: f for pid, f in formulas.items() if name in f.names}
        if not users:
            out[name] = {"final": None, "path_max": None}
            continue
        env_lo, env_hi = dict(med, **{name: lo}), dict(med, **{name: hi})
        f_lo, f_hi = _final(formulas, env_lo, target_factor), _final(formulas, env_hi, target_factor)
        final = math.log10(f_hi) - math.log10(f_lo) if f_lo and f_hi else None
        deltas = []
        for f in users.values():
            a, b = _point(f, env_lo, target_factor), _point(f, env_hi, target_factor)
            if a and b:
                deltas.append(abs(math.log10(b) - math.log10(a)))
        out[name] = {"final": final, "path_max": max(deltas) if deltas else None}
    return out


def build_graph(state: dict) -> dict:
    res = state["result"]
    nodes = [{
        "id": "target", "kind": "target", "label": "target",
        "status": "estimated" if res.get("central") is not None else "failed",
        "definition": state["target"].get("definition", ""), "unit": state["target"]["unit"],
        "central": res.get("central"), "p10": res.get("p10"), "p90": res.get("p90"),
        "n_valid_paths": res.get("n_valid_paths", 0), "outliers": res.get("outliers", []),
    }]
    edges = []
    for p in state["paths"]:
        nodes.append({
            "id": f"path:{p['id']}", "kind": "path", "label": f"{p['id']} {p.get('method', '')}".strip(),
            "status": p["status"], "method": p.get("method"), "description": p.get("description", ""),
            "formula": p.get("formula"), "output_unit": p.get("output_unit"), "issues": p.get("issues", []),
            "median": p.get("median"), "p10": p.get("p10"), "p90": p.get("p90"),
            "log10_vs_central": p.get("log10_vs_central"), "n_dependents": 1,
        })
        edges.append({"source": f"path:{p['id']}", "target": "target", "kind": "aggregated_into",
                      "included": p["status"] in ("valid", "outlier")})
        for name in p.get("uses", []):
            edges.append({"source": f"input:{name}", "target": f"path:{p['id']}", "kind": "used_by"})
    for i in state["inputs"]:
        nodes.append({
            "id": f"input:{i['name']}", "kind": "input", "label": i["name"], "status": i["status"],
            "description": i.get("description", ""), "value": i.get("value"), "low": i.get("low"),
            "high": i.get("high"), "unit": i.get("unit"), "provenance": i.get("provenance"),
            "issues": i.get("issues", []), "count_nouns": i.get("count_nouns", []),
            "used_by": i.get("used_by", []), "n_dependents": len(i.get("used_by", [])),
            "sensitivity": i.get("sensitivity"), "sensitivity_path_max": i.get("sensitivity_path_max"),
        })
    return {"nodes": nodes, "edges": edges}
