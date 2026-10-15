"""离线报告：只读保存下来的模型回复和 calls.jsonl，重算一切（同种子同结果），不发任何请求。

进 git 的输出（不含题目文字和答案值）：results/summary.json、results/per_question.json、results/report_tables.md、
docs/graphs/index.html、demo 的状态和图。只留本地的：results/realfp/states/*.json、docs/graphs/realfp/*.html。
"""
import collections
import html
import json
import math
import statistics

from .arms import check_naive
from .config import CALLS, GRAPHS, GRAPHS_LOCAL, MODEL, RESULTS, RESULTS_LOCAL
from .data import load_backtest
from .engine import evaluate_structured
from .viewer import render_index, render_page

DEMO_ID = "demo_cn_hdt_2024"
DEMO = {"id": DEMO_ID, "question": "Estimate the number of heavy-duty trucks sold in China in calendar year 2024",
        "answer_unit": "", "unit_hint": "a count of heavy-duty trucks", "strict": False}
DEMO_RAW = RESULTS / "demo" / "raw_structured.json"
DEMO_STATE = RESULTS / "demo" / "state.json"


def safe(qid: str) -> str:
    return qid.replace(":", "_")


def raw_path(arm: str, qid: str):
    return RESULTS_LOCAL / "raw" / arm / f"{safe(qid)}.json"


def _load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _write(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1, default=_json_default), encoding="utf-8")


def _json_default(x):
    if isinstance(x, float) and not math.isfinite(x):
        return None
    return str(x)


def _clean(obj):
    """把 inf/nan 换成 None，保证输出是标准 JSON。"""
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    if isinstance(obj, dict):
        return {k: _clean(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_clean(v) for v in obj]
    return obj


def errors_for(est, ans):
    if est is None or not (est > 0):
        return None, math.inf
    s = math.log10(est / ans)
    return s, abs(s)


def fp_score(abs_err: float) -> float:
    """官方 eval_utils.accuracy_metric 在 y, y_hat > 0 时的形式：max(0, 3 - |log10(y / y_hat)|) / 3。"""
    return 0.0 if not math.isfinite(abs_err) else max(0.0, 3 - abs_err) / 3


def final_reply(raw):
    if not raw or not raw.get("attempts"):
        return None
    return raw["attempts"][-1]["reply"]


def score_question(q: dict):
    nraw, sraw = _load(raw_path("naive", q["id"])), _load(raw_path("structured", q["id"]))
    ans = q["answer_value"]
    row = {"id": q["id"], "unit": q["answer_unit"]}
    # naive
    if nraw is None:
        row["naive"] = {"status": "not_run"}
    else:
        status, est, problems = check_naive(final_reply(nraw), q["answer_unit"])
        signed, err = errors_for(est, ans)
        row["naive"] = {"status": status, "estimate": est, "signed_log10_err": signed, "abs_log10_err": err,
                        "within_1_oom": err <= 1, "fp_score": fp_score(err), "attempts": len(nraw["attempts"]),
                        "problems": problems}
    # structured
    state = None
    if sraw is None:
        row["structured"] = {"status": "not_run"}
    else:
        state = evaluate_structured(final_reply(sraw), q["answer_unit"], q["id"], question=q["question"])
        r = state["result"]
        est = r["central"]
        signed, err = errors_for(est, ans)
        covered = est is not None and r["p10"] <= ans <= r["p90"]
        st = "ok" if est is not None else ("invalid_output" if final_reply(sraw) is None else "no_valid_path")
        statuses = collections.Counter(i["status"] for i in state["inputs"])
        row["structured"] = {
            "status": st, "estimate": est, "p10": r["p10"], "p90": r["p90"], "signed_log10_err": signed,
            "abs_log10_err": err, "within_1_oom": err <= 1, "fp_score": fp_score(err), "covered_80": covered,
            "n_valid_paths": r["n_valid_paths"], "outliers": r["outliers"], "path_spread_oom": r["path_spread_oom"],
            "path_medians_log10_err": {p["id"]: errors_for(p.get("median"), ans)[0] for p in state["paths"]
                                       if p["status"] in ("valid", "outlier")},
            "path_methods": {p["id"]: p.get("method") for p in state["paths"]},
            "n_inputs": len(state["inputs"]), "input_status": dict(statuses), "attempts": len(sraw["attempts"]),
            "remaining_errors": state["errors"],
        }
    return row, state


def call_stats(prefix_filter=None):
    if not CALLS.exists():
        return {}
    recs = [json.loads(line) for line in CALLS.read_text(encoding="utf-8").splitlines() if line.strip()]
    out = {}
    groups = collections.defaultdict(list)
    for r in recs:
        key = "demo" if r["qid"].startswith("demo") else r["arm"]
        groups[key].append(r)
    groups["all"] = recs
    for k, rs in groups.items():
        lat = sorted(r["latency_s"] for r in rs if r.get("latency_s") is not None)
        out[k] = {
            "calls": len(rs), "ok": sum(1 for r in rs if r.get("ok")), "retry_calls": sum(1 for r in rs if r.get("attempt") == 2),
            "prompt_tokens": sum(r.get("prompt_tokens", 0) for r in rs),
            "completion_tokens": sum(r.get("completion_tokens", 0) for r in rs),
            "usd": round(sum(r.get("usd", 0) or 0 for r in rs), 6),
            "latency_median_s": statistics.median(lat) if lat else None,
            "latency_max_s": max(lat) if lat else None,
            "finish_reasons": dict(collections.Counter(str(r.get("finish_reason")) for r in rs)),
        }
    return out


def _arm_summary(rows, arm):
    rs = [r[arm] for r in rows if r[arm]["status"] != "not_run"]
    if not rs:
        return {"n": 0}
    errs = [r["abs_log10_err"] for r in rs]
    out = {"n": len(rs), "median_abs_log10_err": statistics.median(errs),
           "share_within_1_oom": sum(r["within_1_oom"] for r in rs) / len(rs),
           "fp_score": sum(r["fp_score"] for r in rs) / len(rs),
           "n_failed": sum(1 for r in rs if r["status"] != "ok"),
           "failures": dict(collections.Counter(r["status"] for r in rs if r["status"] != "ok")),
           "n_retried": sum(1 for r in rs if r["attempts"] > 1)}
    if arm == "structured":
        out["coverage_80"] = sum(r["covered_80"] for r in rs) / len(rs)
        out["n_with_outlier_path"] = sum(1 for r in rs if r["outliers"])
    return out


def _f(x, nd=2):
    if x is None:
        return "—"
    if isinstance(x, float) and math.isinf(x):
        return "∞"
    return f"{x:.{nd}f}" if isinstance(x, float) else str(x)


def tables_md(summary, rows):
    n, s = summary["naive"], summary["structured"]
    lines = ["| arm | n | median abs log10 err | within 1 OOM | fp_score | 80% coverage | failed | retried |",
             "|---|---|---|---|---|---|---|---|"]
    lines.append(f"| naive | {n['n']} | {_f(n['median_abs_log10_err'])} | {n['share_within_1_oom']:.0%} | {n['fp_score']:.3f} | n/a | {n['n_failed']} | {n['n_retried']} |")
    lines.append(f"| structured | {s['n']} | {_f(s['median_abs_log10_err'])} | {s['share_within_1_oom']:.0%} | {s['fp_score']:.3f} | {s['coverage_80']:.0%} | {s['n_failed']} | {s['n_retried']} |")
    both = summary["both_estimated"]
    lines += ["", f"Both arms estimated: {both['n']} questions; median abs log10 err naive {_f(both['naive_median'])}, "
              f"structured {_f(both['structured_median'])}. Paired: structured better {summary['paired']['structured_better']}, "
              f"equal {summary['paired']['equal']}, worse {summary['paired']['structured_worse']}.", ""]
    lines += ["| id | unit | naive signed log10 err | structured signed log10 err | structured 80% covers | valid paths | path spread (OOM) | outlier paths | inputs (assumption/sourced_unverified/missing) | retries n/s |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        a, b = r["naive"], r["structured"]
        st = b.get("input_status", {})
        lines.append(
            f"| {r['id']} | {r['unit'] or '(pure)'} | {_f(a.get('signed_log10_err')) if a.get('status') == 'ok' else a.get('status')} | "
            f"{_f(b.get('signed_log10_err')) if b.get('status') == 'ok' else b.get('status')} | "
            f"{'yes' if b.get('covered_80') else 'no'} | {b.get('n_valid_paths', '—')} | {_f(b.get('path_spread_oom'))} | "
            f"{', '.join(b.get('outliers', [])) or '—'} | {st.get('assumption', 0)}/{st.get('sourced_unverified', 0)}/{st.get('missing', 0)} | "
            f"{a.get('attempts', '—')}/{b.get('attempts', '—')} |")
    c = summary["calls"]
    lines += ["", "| calls group | calls | ok | retry calls | prompt tokens | completion tokens | USD (est.) | median latency s | max latency s | finish_reason |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for k in ("naive", "structured", "demo", "all"):
        if k in c:
            v = c[k]
            lines.append(f"| {k} | {v['calls']} | {v['ok']} | {v['retry_calls']} | {v['prompt_tokens']} | {v['completion_tokens']} | "
                         f"{v['usd']:.4f} | {_f(v['latency_median_s'], 1)} | {_f(v['latency_max_s'], 1)} | {v['finish_reasons']} |")
    return "\n".join(lines) + "\n"


def build_demo():
    raw = _load(DEMO_RAW)
    if raw is None:
        return None
    state = evaluate_structured(final_reply(raw), DEMO["answer_unit"], DEMO_ID, strict_target=False, question=DEMO["question"])
    _write(DEMO_STATE, _clean(state))
    extra = (f"Question: {html.escape(DEMO['question'])}<br>Not scored: no ground truth is used. "
             f"Attempts: {len(raw['attempts'])}. All inputs come from model knowledge; none is verified.")
    (GRAPHS / f"{DEMO_ID}.html").write_text(render_page(_clean(state), "Finance demo: heavy-duty trucks sold in China, 2024",
                                                         extra, back_link="index.html"), encoding="utf-8")
    return state


def build():
    qs = load_backtest()
    rows = []
    for q in qs:
        row, state = score_question(q)
        rows.append(row)
        if state is not None:
            local = dict(state, answer={"value": q["answer_value"], "unit": q["answer_unit"], "raw": q["answer_raw"]},
                         naive=row["naive"], scores=row["structured"])
            _write(RESULTS_LOCAL / "states" / f"{safe(q['id'])}.json", _clean(local))
            a, b = row["naive"], row["structured"]
            extra = (f"Question: {html.escape(q['question'])}<br>realFP answer: <b>{html.escape(q['answer_raw'])}</b> "
                     f"&middot; structured |log10 err| {_f(b['abs_log10_err'])} &middot; 80% covers: {'yes' if b['covered_80'] else 'no'}"
                     f" &middot; naive estimate {_f(a.get('estimate'), 3) if a.get('estimate') else a.get('status')}"
                     f" (|log10 err| {_f(a.get('abs_log10_err'))})")
            GRAPHS_LOCAL.mkdir(parents=True, exist_ok=True)
            (GRAPHS_LOCAL / f"{safe(q['id'])}.html").write_text(
                render_page(_clean(state), f"realFP {q['id']}", extra, back_link="../index.html"), encoding="utf-8")
    demo = build_demo()
    both = [r for r in rows if r["naive"].get("status") == "ok" and r["structured"].get("status") == "ok"]
    ran = [r for r in rows if r["naive"].get("status") != "not_run" and r["structured"].get("status") != "not_run"]
    summary = {
        "model": MODEL, "n_questions": len(qs),
        "naive": _arm_summary(rows, "naive"), "structured": _arm_summary(rows, "structured"),
        "both_estimated": {"n": len(both),
                           "naive_median": statistics.median([r["naive"]["abs_log10_err"] for r in both]) if both else None,
                           "structured_median": statistics.median([r["structured"]["abs_log10_err"] for r in both]) if both else None},
        "paired": {"structured_better": sum(1 for r in ran if r["structured"]["abs_log10_err"] < r["naive"]["abs_log10_err"]),
                   "equal": sum(1 for r in ran if r["structured"]["abs_log10_err"] == r["naive"]["abs_log10_err"]),
                   "structured_worse": sum(1 for r in ran if r["structured"]["abs_log10_err"] > r["naive"]["abs_log10_err"])},
        "calls": call_stats(),
        "demo": None if demo is None else {"central": demo["result"]["central"], "p10": demo["result"]["p10"],
                                           "p90": demo["result"]["p90"], "n_valid_paths": demo["result"]["n_valid_paths"],
                                           "outliers": demo["result"]["outliers"]},
    }
    if summary["naive"].get("n") and summary["structured"].get("n"):
        summary["stop_rule_triggered"] = not (summary["structured"]["median_abs_log10_err"] < summary["naive"]["median_abs_log10_err"])
    _write(RESULTS / "summary.json", _clean(summary))
    _write(RESULTS / "per_question.json", _clean(rows))
    md = tables_md(summary, rows) if summary["naive"].get("n") and summary["structured"].get("n") else ""
    (RESULTS / "report_tables.md").write_text(md, encoding="utf-8")
    idx_rows = [{"id": r["id"], "file": f"{safe(r['id'])}.html", "unit": r["unit"],
                 "naive_err": r["naive"].get("abs_log10_err") if r["naive"].get("status") == "ok" else None,
                 "structured_err": r["structured"].get("abs_log10_err") if r["structured"].get("status") == "ok" else None,
                 "covered": ("yes" if r["structured"].get("covered_80") else "no") if r["structured"].get("status") != "not_run" else None,
                 "n_valid_paths": r["structured"].get("n_valid_paths", 0), "outliers": r["structured"].get("outliers", [])}
                for r in rows]
    note = (f"Model {html.escape(MODEL)}. Colours show input status, node size shows sensitivity. "
            "No retrieval is used yet, so inputs are assumptions or unverified model citations.")
    GRAPHS.mkdir(parents=True, exist_ok=True)
    (GRAPHS / "index.html").write_text(render_index(idx_rows, [(f"{DEMO_ID}.html", DEMO["question"])] if demo else [], note),
                                       encoding="utf-8")
    return summary, md
