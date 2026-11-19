"""v2.15d 量级闸门：和一次不联网直接问的粗估比，差 RATIO 倍以上就定向修正一次。

三方审计（金融科技 / VC / 刑侦，2026-11-19）的共识：最伤可信度的是量级错了不报警（中国利润 58,009、美国零售 766,401、
德国新车 249、BCG 101 人），各条路线共用同一个读错的点时，路线之间的打架检查查不出来，要有外部参照。存档离线重放
（agent 估计对同题已存的直接问回复）：2 倍阈值抓到 13/13 次翻车，误报 0（阈值是在这批样本上定的）。

粗估只决定「要不要复查」：不进任何计算，报错里也不写它的数（只写偏高还是偏低、差几倍以上），免得裁判照着它凑数。
修正只触发一次（第一次检查发现偏了时）；修完还偏就在终稿末尾写一句（代码写的），数照出（v2.8l 不准不出数）。
粗估调用失败、单位换不过来、离散目标、没钉单位时，闸门不起作用，原因记在 state 里。"""
import math

from ..config import MAX_TOKENS
from ..prompts import NAIVE_SYSTEM
from . import assumptions as A
from . import qty as Q
from .pipeline import BudgetExceeded

RATIO = 2.0
ROLE = "magnitude"


def _fmt(v) -> str:
    """和 graph._fmt_num 相同（graph 会 import 本模块，这里不反向 import）。"""
    if v is None or not isinstance(v, (int, float)) or not math.isfinite(v):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:.4g}"


def reference_prompt(question: str, as_of: str, target: dict) -> str:
    unit = target.get("unit_canonical") or ""
    return (f"Question: {question}\nInformation cutoff: {as_of}\n"
            f"Estimate exactly this quantity: {target.get('what', '')} (period {target.get('period_start', '')} to "
            f"{target.get('period_end', '')}).\nTarget unit: \"{unit}\"")


def reference(ctx, question: str, as_of: str, target: dict) -> dict:
    """一次不联网直接问（NAIVE_SYSTEM，关思考），换成目标的 unit_canonical。每次运行只问一次（缓存在 ctx 上）。"""
    cached = getattr(ctx, "_magnitude_ref", None)
    if cached is not None:
        return cached
    unit = target.get("unit_canonical") or ""
    if not unit:
        rec = {"status": "skipped", "note": "no pinned unit"}
    else:
        try:
            out, err = ctx.llm.ask(NAIVE_SYSTEM, reference_prompt(question, as_of, target), role=ROLE, qid=ctx.qid,
                                   max_tokens=MAX_TOKENS[ROLE])
        except BudgetExceeded as e:
            out, err = None, f"budget: {e}"
        except Exception as e:  # noqa: BLE001  粗估出任何意外都只让闸门不起作用，不能让整题崩掉（同 markets、jev）
            out, err = None, f"{type(e).__name__}: {e}"[:200]
        rec = _parse(out, err, unit)
    ctx._magnitude_ref = rec
    return rec


def _parse(out, err, unit: str) -> dict:
    if out is None:
        return {"status": "error", "note": str(err)[:200]}
    est, u = out.get("estimate"), str(out.get("unit") or "")
    if isinstance(est, bool) or not isinstance(est, (int, float)) or not math.isfinite(est) or est <= 0:
        return {"status": "invalid", "note": f"estimate {est!r} is not a positive number", "reply": out}
    f, why = (1.0, "") if u == unit else Q.convert_factor(u, unit)
    if f is None:
        return {"status": "unit_unreconciled", "note": why[:200], "reply": out}
    return {"status": "ok", "estimate": est * f, "unit": unit, "reply": out}


def _direction(est: float, ref: float) -> str:
    return "above" if est > ref else "below"


def off(est, ref) -> bool:
    return bool(est) and bool(ref) and max(est / ref, ref / est) > RATIO


def _input_text(d: dict, by_id: dict, kept_a: dict) -> str:
    """一个输入写成一句话：p317 = 12,103 person；a5 = 0.85 % = 0.0085 as a fraction。"""
    iid = d.get("id")
    if d.get("kind") == "assumption" and iid in kept_a:
        a = kept_a[iid]
        frac = f" = {a['value'] / 100:g} as a fraction" if a.get("is_pct") else ""
        return f"{iid} = {a['value']:g} {a.get('unit', '')}{frac}".rstrip()
    if d.get("kind") == "point" and iid in by_id:
        p = by_id[iid]
        u = str(p.get("unit") or "")
        frac = f" = {p['value'] / 100:g} as a fraction" if A.is_pct(u) else ""
        return f"{iid} = {_fmt(p.get('value'))} {u}{frac}".rstrip()
    return f"{d.get('name')} = {_fmt(d.get('p10'))} ({d.get('kind')})"


def check(ref: dict, combined, methods: list, by_id: dict, kept_a: dict) -> tuple:
    """(这次检查的记录, 交给修正轮的问题清单)。combined：能用的方法合并后的中心值；methods：能用的方法（compute 的结果）。
    合并值偏了才报；点名自己也偏了的方法（都不偏时点名全部能用的方法）。"""
    if (ref or {}).get("status") != "ok":
        return {"status": "not_checked", "reference": ref}, []
    r = ref["estimate"]
    rec = {"status": "off" if off(combined, r) else "ok", "reference": ref, "estimate": combined,
           "ratio": (combined / r) if combined else None}
    if rec["status"] != "off":
        return rec, []
    named = [m for m in methods if off(m.get("estimate"), r)] or list(methods)
    lines = [f"method {m.get('label') or m.get('id')} ({m.get('method')}): magnitude check: it gives {_fmt(m.get('estimate'))}, "
             f"more than {RATIO:g}x {_direction(m['estimate'], r)} an independent rough estimate of the target made without "
             f"this evidence. Re-check the scale of every input (code reads them as: "
             + "; ".join(_input_text(d, by_id, kept_a) for d in m.get("inputs_detail") or []) +
             "). Change an input only if its evidence shows it is wrong; if every input is right, keep the method."
             for m in named if m.get("estimate")]
    return rec, lines


def final_record(ref: dict, central) -> dict:
    if (ref or {}).get("status") != "ok":
        return {"status": "not_checked", "reference": ref}
    r = ref["estimate"]
    return {"status": "off" if off(central, r) else "ok", "reference": ref, "estimate": central,
            "ratio": (central / r) if central else None}


def final_note(rec: dict) -> str:
    """终稿末尾的一句（代码写的）。只写偏高还是偏低、差几倍，不写粗估的数。"""
    if (rec or {}).get("status") != "off" or not rec.get("ratio"):
        return ""
    x = rec["ratio"]
    k = x if x >= 1 else 1 / x
    return (f"Magnitude check: this estimate is about {k:,.1f} times {'above' if x >= 1 else 'below'} an independent rough "
            "estimate made without the evidence; one targeted repair did not close the gap, so check the inputs above.")
