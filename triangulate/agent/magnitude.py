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
    try:
        f, why = (1.0, "") if u == unit else Q.convert_factor(u, unit)
    except Exception as e:  # noqa: BLE001  pint 的其他异常也只让闸门不起作用（v2.15f 审查）
        f, why = None, f"{type(e).__name__}: {e}"
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
        return _point_text(by_id[iid])
    return f"{d.get('name')} = {_fmt(d.get('p10'))} ({d.get('kind')})"


def _point_text(p: dict) -> str:
    """点按代码算的时候用的单位写（v2.13a 起是 unit_calc，没有就是 unit）；两者不同时括号里注明原来记的单位。"""
    u = str(p.get("unit") or "")
    uc = str(p.get("unit_calc") or "") or u
    frac = f" = {p['value'] / 100:g} as a fraction" if A.is_pct(uc) else ""
    note = f" (recorded unit {u})" if u and u != uc else ""
    return f"{p['id']} = {_fmt(p.get('value'))} {uc}{frac}{note}".rstrip()


def _inputs(m: dict, by_id: dict, kept_a: dict) -> str:
    """一个方法的输入，每个一句；series 这类方法没有逐项输入（inputs_detail），列它用到的点（最多 8 个）。"""
    if m.get("inputs_detail"):
        return "; ".join(_input_text(d, by_id, kept_a) for d in m["inputs_detail"])
    ids = [i for i in m.get("used_ids") or [] if i in by_id][:8]
    return "; ".join(_point_text(by_id[i]) for i in ids) or "no inputs recorded"


def _result_unit(m: dict) -> str:
    """代码按什么单位读这个方法的结果、换到目标单位乘了多少（compute 的 unit_check）。美国零售 test3：点记的是
    millions of USD，方法的单位被定成 USD、倍数 1，结果小了 10^6；只写输入的话裁判看不出来（v2.15g，存档重放）。"""
    uc = m.get("unit_check") or {}
    if not uc.get("unit"):
        return ""
    f = uc.get("factor")
    return (f"; code reads this method's result in {uc['unit']} and converts it to the target unit {uc.get('target_unit')}"
            + (f" with factor {f:g}" if isinstance(f, (int, float)) else ""))


def check(ref: dict, combined, methods: list, by_id: dict, kept_a: dict) -> tuple:
    """(这次检查的记录, 交给修正轮的问题清单)。combined：能用的方法合并后的中心值；methods：能用的方法（compute 的结果）。
    合并值偏了才报，点名全部能用的方法（v2.15g：只点名自己也偏的方法，等于告诉裁判粗估落在没点名那条的 1/2 到 2 倍之间；
    现在只说合并值偏高还是偏低、差 2 倍以上），每条写出代码读到的输入和结果单位。"""
    if (ref or {}).get("status") != "ok":
        return {"status": "not_checked", "reference": ref}, []
    r = ref["estimate"]
    rec = {"status": "off" if off(combined, r) else "ok", "reference": ref, "estimate": combined,
           "ratio": (combined / r) if combined else None}
    if rec["status"] != "off":
        return rec, []
    lines = [f"method {m.get('label') or m.get('id')} ({m.get('method')}): magnitude check: the combined estimate of the "
             f"usable methods ({_fmt(combined)}) is more than {RATIO:g}x {_direction(combined, r)} an independent rough "
             f"estimate of the target made without this evidence; this method gives {_fmt(m.get('estimate'))}. Re-check the "
             f"scale of every input (code reads them as: {_inputs(m, by_id, kept_a)}){_result_unit(m)}. Change an input or "
             "unit only if its evidence shows it is wrong; if everything is right, keep the method."
             for m in methods if m.get("estimate")]
    return rec, lines


def final_record(ref: dict, central, repair_sent: bool = False) -> dict:
    """repair_sent：闸门的报错真的随一次修正发给了裁判（v2.15f：第一次偏出在最后一次修正之后时没发出去）。"""
    if (ref or {}).get("status") != "ok" or not central:
        return {"status": "not_checked", "reference": ref, "repair_sent": repair_sent}
    r = ref["estimate"]
    return {"status": "off" if off(central, r) else "ok", "reference": ref, "estimate": central, "ratio": central / r,
            "repair_sent": repair_sent}


def final_note(rec: dict) -> str:
    """终稿末尾的一句（代码写的）。只写偏高还是偏低、差几倍，不写粗估的数。"""
    if (rec or {}).get("status") != "off" or not rec.get("ratio"):
        return ""
    x = rec["ratio"]
    k = x if x >= 1 else 1 / x
    tried = ("one targeted repair did not close the gap" if rec.get("repair_sent") else
             "the judge was not asked to re-check it (it was found after the repair rounds, or no method passed every check)")
    return (f"Magnitude check: this estimate is about {k:,.1f} times {'above' if x >= 1 else 'below'} an independent rough "
            f"estimate made without the evidence; {tried}, so check the inputs above.")
