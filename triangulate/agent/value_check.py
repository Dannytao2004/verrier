"""v2.8o：观测点的数由抽取员读（number / low / high，见 evidence.read_reading），算之前逐个交给模型核对（用户 10-18 的设计）。

1. 只核对裁判方法实际用到、还没核对过的点（value_check == "pending"），一个点一次调用，并行；模型只回 true / false。
2. false：带着被否的读数让模型从同一个 quote 重新读这个数（scale_word 不变），再核对；最多重读 MAX_REREADS 次。
3. 仍不过：这个点记为 failed，算的时候当作不存在（用到它的方法报错，原因交给修正轮）。
核对调用本身失败（出错、超预算）时不拦，照抽取员读的数算（同单位核对），记为 error。
只有代码解析不了的写法（单词、分数、区间）才用抽取员读的数、才核对；阿拉伯数字写法由代码解析（pipeline.verify_point），
旧运行的点、市场数据的点也没有 value_check，不核对。"""
import re
from concurrent.futures import ThreadPoolExecutor

from ..config import MAX_TOKENS
from . import evidence as ev
from .pipeline import BudgetExceeded, dumps
from .prompts import VALUE_CHECK_SYSTEM, VALUE_CHECK_USER, VALUE_REREAD_SYSTEM, VALUE_REREAD_USER

MAX_REREADS = 3
MAX_WORKERS = 16
_PID = re.compile(r"p\d+")


def _ids(x, out: set):
    """方法参数里引用的所有点 id（formula_mc 的 inputs、序列方法的 target_history 等，不管写在哪一层）。"""
    if isinstance(x, dict):
        for v in x.values():
            _ids(v, out)
    elif isinstance(x, list):
        for v in x:
            _ids(v, out)
    elif isinstance(x, str) and _PID.fullmatch(x):
        out.add(x)
    return out


def _ask(llm, system, user, role, qid, key):
    try:
        return llm.ask(system, user, role=role, qid=qid, max_tokens=MAX_TOKENS[key])
    except BudgetExceeded as e:
        return None, str(e)


def _match(llm, qid: str, p: dict, reading: dict):
    """True / False；调用失败返回 (None, 原因)。"""
    # 倍数词由代码乘（evidence.split_multiplier），模型只看去掉倍数词的写法（v2.8o 探针：倍数交给它判，三类读错都放行了）
    written = ev.written_number(p.get("value_as_written", ""), p.get("scale_word", ""))
    user = VALUE_CHECK_USER.replace("__POINT__", dumps({"quote": p.get("quote", ""), "written": written, "reading": reading}))
    out, err = _ask(llm, VALUE_CHECK_SYSTEM, user, f"value_check:{p['id']}", qid, "value_check")
    if out is None or not isinstance(out.get("match"), bool):
        return None, err or f"reply without a true/false match: {dumps(out)[:200]}"
    return out["match"], ""


def check_point(llm, qid: str, p: dict) -> dict:
    """核对一个点；返回记录 {id, status: ok / failed / error, tries, 通过时的 value / low / high / reading}。不改 p。"""
    rec, reading = {"id": p["id"], "tries": []}, p["reading"]
    for k in range(1 + MAX_REREADS):
        if k:
            user = (VALUE_REREAD_USER.replace("__NAME__", str(p.get("name", ""))).replace("__UNIT__", str(p.get("unit", "")))
                    .replace("__QUOTE__", str(p.get("quote", "")))
                    .replace("__WRITTEN__", ev.written_number(p.get("value_as_written", ""), p.get("scale_word", "")))
                    .replace("__PREVIOUS__", dumps(reading)))
            out, err = _ask(llm, VALUE_REREAD_SYSTEM, user, f"value_reread:{p['id']}", qid, "value_reread")
            try:
                if out is None:
                    raise ValueError(err or "no reply")
                got = ev.read_reading(out, p.get("value_as_written", ""), p.get("scale_word", ""), _fmt(p))
            except ValueError as e:
                rec["tries"].append({"reread_error": str(e)[:200]})
                continue
            reading = got[4]
        ok, err = _match(llm, qid, p, reading)
        if ok is None:
            rec["tries"].append({"reading": reading, "error": str(err)[:200]})
            return {**rec, "status": "error"}
        rec["tries"].append({"reading": reading, "match": ok})
        if ok:
            if k:
                v, lo, hi, _, _ = ev.read_reading(reading, p.get("value_as_written", ""), p.get("scale_word", ""), _fmt(p))
                rec.update(value=v, value_low=lo, value_high=hi)
            return {**rec, "status": "ok", "reading": reading}
    return {**rec, "status": "failed"}


def _fmt(p: dict) -> str:
    """v2.17a：点所在页面的数字写法（pipeline.verify_point 记的 number_format；英式页面的点没有这个键）。"""
    return (p.get("number_format") or {}).get("format", "en")


def _apply(p: dict, rec: dict):
    p["value_check"], p["value_check_tries"] = rec["status"], rec["tries"]
    if rec["status"] == "ok" and "value" in rec:   # 重读后才通过：用重读的数（原来的读数留在 reading_from_extractor）
        p["reading_from_extractor"], p["reading"] = p["reading"], rec["reading"]
        p["value"] = rec["value"]
        p.pop("value_low", None), p.pop("value_high", None)
        if rec["value_low"] is not None:
            p["value_low"], p["value_high"] = rec["value_low"], rec["value_high"]


def review(llm, qid: str, jr: dict, pts: list) -> list:
    """核对 jr["methods"] 用到的、还没核对过的点（并行），结果写回点（value_check / value_check_tries，重读后通过的改 value）。
    返回给修正轮的错误：现在的方法用到、但核对没过的点（包括之前几次 check 里没过的）。"""
    by_id = {p["id"]: p for p in pts}
    used = sorted(_ids(jr.get("methods") or [], set()) & set(by_id), key=lambda i: int(i[1:]))
    todo = [by_id[i] for i in used if by_id[i].get("value_check") == "pending" and by_id[i].get("reading")]
    if todo:
        with ThreadPoolExecutor(min(MAX_WORKERS, len(todo))) as ex:
            recs = list(ex.map(lambda p: check_point(llm, qid, p), todo))
        for p, rec in zip(todo, recs):
            _apply(p, rec)
        jr.setdefault("value_checks", []).append(recs)
    return [f'data point {i} ("{str(by_id[i].get("name", ""))[:80]}"): its number could not be confirmed against its quote '
            f'(value_as_written "{by_id[i].get("value_as_written", "")}") after {MAX_REREADS} re-reads, so code removed it; '
            f'use another data point or an assumption instead' for i in used if by_id[i].get("value_check") == "failed"]


def usable(points) -> list:
    """算的时候用的点：核对没过的去掉。"""
    return [p for p in points if p.get("value_check") != "failed"]
