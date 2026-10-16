"""Jev 对照臂（v2.2，可选）：TypeSafe 的 System One 模型，只走官方端点 POST https://api.typesafe.ai/v1/systemone。

只在离散目标、而且配置了 key 文件时运行：环境变量 TYPESAFE_KEY_FILE 指向一个文件，里面一行 TYPESAFE_API_KEY=...。
没设这个变量就跳过，记为 not_configured。key 只在调用时读进内存，不打印、不写日志、不进 state。
compute 之后由代码把保留的数据点写成一份英文证据简报（目标定义、可能的结果、每个点一行「name = value unit, period, source
domain, date」），问 Jev 一个 choice 问题（官方建议：能算的在代码里算、一个判断一个问题），它给出的分布单独存成一臂，
不和 agent 的答案合并。

请求和回复格式按官方文档 https://docs.typesafe.ai/api（2026-10-15 查看）：
请求 {"model": "jev-latest", "state": <text>, "questions": {"outcome": {"type": "choice", "instructions": ..., "criteria": {label: 描述}}}}；
回复 answers.outcome = {type, choice, probabilities（覆盖全部选项、和为 1）, confidence}，另有 usage.{input_tokens, output_tokens}。
价格按 https://docs.typesafe.ai/models（2026-10-15 查看）：输入 $0.042 / 百万 token，输出免费。
"""
import http.client
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

from . import discrete as D

API_URL = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"
KEY_ENV = "TYPESAFE_KEY_FILE"
KEY_NAME = "TYPESAFE_API_KEY"
USD_PER_M_INPUT = 0.042
PRICE_SOURCE = "https://docs.typesafe.ai/models (viewed 2026-10-15): $0.042 per million input tokens, output tokens free"
QUESTION = "outcome"
TIMEOUT_S = 90
RETRY_STATUS = {429, 529, 500, 502, 503, 504}
MAX_POINTS = 150
INSTRUCTIONS = ("Using only the information in the state, decide which of the listed mutually exclusive outcomes the target "
                "described in the state will resolve to. The evidence lines are the only facts available up to the "
                "information cutoff.")


class JevError(RuntimeError):
    pass


def key_file():
    v = os.environ.get(KEY_ENV, "").strip()
    return Path(v) if v else None


def read_key(path: Path) -> str:
    """只取 KEY_NAME 这一行；报错信息里不带任何 key 内容。"""
    if not path.is_file():
        raise JevError(f"key file not found: {path} (set {KEY_ENV})")
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip().removeprefix("export ").strip()
        if line.startswith(KEY_NAME + "="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
    raise JevError(f"{KEY_NAME} not set in {path}")


def _fmt(v) -> str:
    if not isinstance(v, (int, float)) or not math.isfinite(v):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 1000 else f"{v:.6g}"


def evidence_brief(target: dict, points: list, as_of: str) -> str:
    """给 Jev 的证据简报（英文纯文本）。只用保留的点；数字由代码格式化，日期差由代码算好。"""
    unit = target.get("unit", "")
    lines = [f"Information cutoff: {as_of}. Every fact below was available on or before this date.",
             f"Target: {target.get('what', '')} (unit: {unit}; target period {target.get('period_start') or '?'} to "
             f"{target.get('period_end') or '?'}).", ]
    try:
        days = (date.fromisoformat(str(target.get("period_end"))[:10]) - date.fromisoformat(as_of)).days
        lines.append(f"Days from the information cutoff to the end of the target period (computed by code): {days}.")
    except ValueError:
        pass
    if target.get("caveats"):
        lines.append(f"Definition notes: {target['caveats']}")
    lines.append("Possible outcomes (mutually exclusive):")
    for o in target.get("outcomes") or []:
        lines.append(f"- {o['label']}" + D.value_text(o, unit))   # 合并尾部带 or lower / or higher（v2.3.1）
    lines.append("Evidence (name = value unit, period, source domain, date available):")
    for p in points[:MAX_POINTS]:
        dom = urllib.parse.urlsplit(p.get("source_url") or "").netloc or "unknown source"
        avail = p.get("page_date") or p.get("published_at_if_visible") or "date unknown"
        lines.append(f"- {p.get('name', '')} = {_fmt(p.get('value'))} {p.get('unit', '')}, period "
                     f"{p.get('period_start') or '?'}..{p.get('period_end') or '?'}, source {dom}, {avail}")
    if len(points) > MAX_POINTS:
        lines.append(f"({len(points) - MAX_POINTS} further evidence lines omitted.)")
    return "\n".join(lines)


def criteria(target: dict) -> dict:
    unit = target.get("unit", "")
    return {o["label"]: f"The target resolves to: {o['label']}" + D.value_text(o, unit) for o in target.get("outcomes") or []}


def request_body(state_text: str, crit: dict) -> dict:
    return {"model": MODEL, "state": state_text,
            "questions": {QUESTION: {"type": "choice", "instructions": INSTRUCTIONS, "criteria": crit}}}


def parse_answer(data, labels: list) -> dict:
    """官方回复 -> {model, choice, probabilities, confidence, usage}。分布必须覆盖全部 label、每个在 [0, 1]、和约为 1。"""
    try:
        ans = data["answers"][QUESTION]
        probs = ans["probabilities"]
    except (KeyError, TypeError) as e:
        raise JevError(f"response has no answers.{QUESTION}.probabilities ({type(e).__name__})") from None
    if not isinstance(probs, dict) or set(probs) != set(labels):
        raise JevError(f"probabilities do not cover exactly the outcomes: got {sorted(probs) if isinstance(probs, dict) else probs!r}")
    vals = {k: float(v) for k, v in probs.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
    if len(vals) != len(labels) or not all(math.isfinite(v) and 0 <= v <= 1 for v in vals.values()):
        raise JevError("probabilities must be numbers in [0, 1]")
    s = sum(vals.values())
    if abs(s - 1) > 0.02:
        raise JevError(f"probabilities sum to {s:.3f}, not 1")
    usage = data.get("usage") if isinstance(data.get("usage"), dict) else {}
    return {"model": data.get("model"), "choice": ans.get("choice"), "probabilities": {k: vals[k] / s for k in labels},
            "confidence": ans.get("confidence"), "usage": {k: usage.get(k) for k in ("input_tokens", "output_tokens")}}


def _urllib_post(url: str, body: bytes, headers: dict, timeout: float) -> tuple:
    req = urllib.request.Request(url, data=body, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if hasattr(e, "read") else b""


class JevClient:
    """标准库 HTTP 客户端。post(url, body, headers, timeout) -> (status, raw bytes) 可以换成假的（测试用）。"""

    def __init__(self, key: str, post=None, tries: int = 3, sleep=time.sleep):
        self._key, self._post, self.tries, self._sleep = key, post or _urllib_post, tries, sleep

    def ask(self, state_text: str, crit: dict) -> dict:
        body = json.dumps(request_body(state_text, crit), ensure_ascii=False).encode("utf-8")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self._key}"}
        status, raw, t0 = None, b"", time.time()
        for attempt in range(1, self.tries + 1):
            try:
                status, raw = self._post(API_URL, body, headers, TIMEOUT_S)
            except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException) as e:   # IncompleteRead 等不是 OSError
                status, raw = None, f"{type(e).__name__}".encode()
            if status in RETRY_STATUS or status is None:
                if attempt < self.tries:
                    self._sleep(2 ** attempt)
                    continue
            break
        latency = round(time.time() - t0, 2)
        if status in (401, 403):
            raise JevError(f"TypeSafe rejected the API key (HTTP {status})")
        if status != 200:
            raise JevError(f"HTTP {status if status is not None else 'error ' + raw.decode(errors='replace')[:40]}")
        try:
            data = json.loads(raw)
        except ValueError:
            raise JevError("response body is not JSON") from None
        out = parse_answer(data, list(crit))
        out.update(http=status, attempts=attempt, latency_s=latency)
        return out


def run_arm(target: dict, points: list, as_of: str, qid: str = "", log=None, client=None) -> dict:
    """Jev 对照臂。不抛异常：未配置 / 出错都记在返回的 dict 里（status = ok / not_configured / error / skipped）。"""
    out = {"arm": "jev", "endpoint": API_URL, "model_requested": MODEL, "pooled_with_agent": False}
    if client is None:
        kf = key_file()
        if kf is None:
            return {**out, "status": "not_configured", "note": f"{KEY_ENV} is not set; Jev arm skipped"}
        try:
            client = JevClient(read_key(kf))
        except JevError as e:
            return {**out, "status": "error", "error": str(e)}
    if not points:
        return {**out, "status": "skipped", "note": "no kept data points to brief"}
    brief = evidence_brief(target, points, as_of)
    crit = criteria(target)
    out.update(brief=brief, brief_chars=len(brief), n_points_in_brief=min(len(points), MAX_POINTS), criteria=crit)
    try:
        ans = client.ask(brief, crit)
    except JevError as e:
        out.update(status="error", error=str(e)[:300])
        if log:
            log({"arm": "jev", "qid": qid, "ok": False, "error": str(e)[:200]})
        return out
    tin = ans["usage"].get("input_tokens")
    usd = None if not isinstance(tin, (int, float)) else tin * USD_PER_M_INPUT / 1e6
    out.update(status="ok", usd_estimated=usd, price_usd_per_m_input=USD_PER_M_INPUT, price_source=PRICE_SOURCE, **ans)
    if log:   # calls.jsonl：只记计量字段，不记简报内容、不记 key；没有 "usd" 键，所以不计入 DeepSeek 的预算
        log({"arm": "jev", "qid": qid, "ok": True, "model": ans.get("model"), "http": ans.get("http"),
             "latency_s": ans.get("latency_s"), "input_tokens": tin, "output_tokens": ans["usage"].get("output_tokens"),
             "usd_jev_estimated": usd})
    return out
