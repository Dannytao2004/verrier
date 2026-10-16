"""两个 arm：naive（直接报数）和 structured（提结构，Python 算）。两边都是「首次调用 + 输出无效时带错误清单重试一次」。

运行时只做调用、校验、保存原始回复；打分和聚合由 report 从保存的回复离线重算。
"""
import math

from .config import MAX_TOKENS
from .engine import evaluate_structured
from .prompts import NAIVE_SYSTEM, RETRY, STRUCTURED_SYSTEM, USER, unit_display
from .units import UnitError, UnitMismatch, convert, dims_str, parse_unit


def check_naive(reply, target_unit: str, strict_target: bool = True):
    """返回 (status, estimate_in_target_unit 或 None, problems)。status: ok | invalid_output | unit_unreconciled。"""
    if not isinstance(reply, dict):
        return "invalid_output", None, ["reply is not a JSON object"]
    est, unit = reply.get("estimate"), reply.get("unit", "")
    if isinstance(est, bool) or not isinstance(est, (int, float)) or not math.isfinite(est) or est <= 0:
        return "invalid_output", None, [f'"estimate" must be a positive JSON number, got {est!r}']
    if unit is None:
        unit = ""
    target = parse_unit(target_unit, strict=strict_target)
    try:
        u = parse_unit(unit)
    except UnitError as e:
        return "unit_unreconciled", None, [f'"unit" {unit!r} cannot be parsed ({e}); use the target unit {target_unit!r}']
    try:
        return "ok", convert(float(est), u, target), []
    except UnitMismatch:
        return "unit_unreconciled", None, [f'"unit" {unit!r} has dimension {dims_str(u.dims)} but the target unit '
                                           f'{target_unit!r} has dimension {dims_str(target.dims)}']


def _messages(system: str, q: dict):
    user = USER.format(question=q["question"], unit_display=unit_display(q["answer_unit"], q.get("unit_hint", "")))
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def _run(llm, q: dict, arm: str, system: str, check, max_tokens: int) -> dict:
    msgs = _messages(system, q)
    record = {"qid": q["id"], "arm": arm, "target_unit": q["answer_unit"], "attempts": []}
    for attempt in (1, 2):
        reply, text, err = llm.json_call(msgs, arm=arm, qid=q["id"], attempt=attempt, max_tokens=max_tokens)
        problems = [err] if err else check(reply)
        record["attempts"].append({"attempt": attempt, "reply": reply,
                                   "unparsed_text": text if reply is None else None, "problems": problems})
        if not problems or attempt == 2:
            break
        msgs = msgs + [{"role": "assistant", "content": text or "{}"},
                       {"role": "user", "content": RETRY.format(problems="\n".join(f"- {p}" for p in problems))}]
    record["final_attempt"] = len(record["attempts"])
    return record


def run_naive(llm, q: dict) -> dict:
    strict = q.get("strict", True)
    return _run(llm, q, "naive", NAIVE_SYSTEM,
                lambda r: check_naive(r, q["answer_unit"], strict)[2], max_tokens=MAX_TOKENS["naive"])


def run_structured(llm, q: dict) -> dict:
    strict = q.get("strict", True)

    def check(reply):
        return evaluate_structured(reply, q["answer_unit"], q["id"], strict_target=strict, n=200)["errors"]
    return _run(llm, q, "structured", STRUCTURED_SYSTEM, check, max_tokens=MAX_TOKENS["structured"])
