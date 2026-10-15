"""realFP 读取、答案解析和确定性选题。

id = "<split>:<index>"（官方 JSON 没有 id 字段，index 是该 split 列表里的 0 起下标）。
"""
import json
import random
import re

from .config import BACKTEST_FULL, BACKTEST_IDS, N_QUESTIONS, RAW, SELECT_SEED, SELECT_SPLIT
from .units import UnitError, parse_unit

SPLITS = ("train", "val", "test")
ANSWER_RE = re.compile(r"^\s*(\$)?\s*(-?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*(.*?)\s*$")


def load_split(split: str) -> list:
    return json.loads((RAW / f"{split}_realfp.json").read_text(encoding="utf-8"))


def parse_answer(text: str):
    """'3.20E+13' -> (3.2e13, '')；'1800 L' -> (1800, 'L')；'$75120' -> (75120, 'USD')。
    返回 (value, unit_str, reason)；不合格时 value 为 None，reason 说明原因。"""
    m = ANSWER_RE.match(text or "")
    if not m:
        return None, None, "answer not numeric"
    dollar, num, unit = m.groups()
    value = float(num)
    if dollar:
        if unit:
            return None, None, "dollar plus extra unit"
        unit = "USD"
    if not (value > 0):
        return None, None, "answer not positive (log error undefined)"
    try:
        parse_unit(unit, strict=True)
    except UnitError as e:
        return None, None, f"unit not parseable: {e}"
    return value, unit, ""


def eligibility(split: str = SELECT_SPLIT):
    rows = load_split(split)
    ok, rejected = [], []
    for i, row in enumerate(rows):
        qid = f"{split}:{i}"
        value, unit, reason = parse_answer(row.get("answer", ""))
        if value is None:
            rejected.append({"id": qid, "answer_raw": row.get("answer"), "reason": reason})
        else:
            ok.append({"id": qid, "question": row["question"], "answer_raw": row["answer"],
                       "answer_value": value, "answer_unit": unit})
    return ok, rejected


def select(n: int = N_QUESTIONS, seed: int = SELECT_SEED, split: str = SELECT_SPLIT) -> dict:
    ok, rejected = eligibility(split)
    ok.sort(key=lambda r: int(r["id"].split(":")[1]))
    picked = random.Random(seed).sample(ok, n)
    meta = {"split": split, "seed": seed, "n": n, "n_split": len(ok) + len(rejected),
            "n_eligible": len(ok), "n_rejected": len(rejected),
            "rule": "random.Random(seed).sample(eligible sorted by index, n); eligible = numeric positive answer "
                    "whose unit parses strictly with triangulate.units"}
    BACKTEST_FULL.write_text(json.dumps({"meta": meta, "questions": picked}, ensure_ascii=False, indent=1), encoding="utf-8")
    BACKTEST_IDS.write_text(json.dumps({"meta": meta, "ids": [q["id"] for q in picked],
                                        "rejected": [{"id": r["id"], "reason": r["reason"]} for r in rejected]},
                                       ensure_ascii=False, indent=1), encoding="utf-8")
    return meta


def load_backtest() -> list:
    """优先读本地完整文件；没有就按已提交的 id 从原件重建（原件需先下载，见 DATA.md）。"""
    if not BACKTEST_FULL.exists():
        ids = json.loads(BACKTEST_IDS.read_text(encoding="utf-8"))["ids"]
        ok, _ = eligibility(SELECT_SPLIT)
        by_id = {r["id"]: r for r in ok}
        qs = [by_id[i] for i in ids]
        return qs
    return json.loads(BACKTEST_FULL.read_text(encoding="utf-8"))["questions"]
