"""预测市场工具（Polymarket，公开只读接口，不登录）。

1. Gamma public-search 按关键词搜市场；代码只留「题目包含全部关键词」且创建时间 <= as_of 的市场（最多 3 个）。
2. 对每个市场的第一个 outcome token 取 CLOB prices-history，只用 <= as_of 当天结束的价格点，取最后一个。
绝大多数题不会有对应市场，返回空是正常结果。返回的数据点由代码生成，不经过模型，标 verified_by=api。
"""
import json
import urllib.parse
from datetime import date, datetime, time, timezone

from . import net

GAMMA = "https://gamma-api.polymarket.com/public-search"
CLOB = "https://clob.polymarket.com/prices-history"


def _created(m: dict):
    for k in ("createdAt", "startDate"):
        v = m.get(k)
        if v:
            try:
                return datetime.fromisoformat(v.replace("Z", "+00:00")).date()
            except ValueError:
                pass
    return None


def match_markets(events: list, keywords: list, as_of: date, cap: int = 3) -> list:
    kws = [k.lower() for k in keywords if k and k.strip()]
    out = []
    for e in events or []:
        for m in e.get("markets") or []:
            q = (m.get("question") or "").lower()
            c = _created(m)
            if kws and all(k in q for k in kws) and c is not None and c <= as_of:
                out.append(m)
    return out[:cap]


def search_markets(keywords: list, as_of: date) -> dict:
    rec = {"keywords": keywords, "markets": [], "points": [], "note": ""}
    if not keywords:
        rec["note"] = "no market keywords from plan"
        return rec
    q = urllib.parse.urlencode({"q": " ".join(keywords), "limit_per_type": 20})
    try:
        status, body, _, _ = net.get(f"{GAMMA}?{q}", timeout=30)
    except net.Blocked:
        rec["note"] = "gamma search blocked by robots.txt"
        return rec
    except Exception as e:  # noqa: BLE001
        rec["note"] = f"gamma search error {type(e).__name__}"
        return rec
    if status != 200:
        rec["note"] = f"gamma search http {status}"
        return rec
    events = (json.loads(body) or {}).get("events") or []
    found = match_markets(events, keywords, as_of)
    rec["n_events_returned"] = len(events)
    end_ts = int(datetime.combine(as_of, time(23, 59, 59), tzinfo=timezone.utc).timestamp())
    for m in found:
        mrec = {"question": (m.get("question") or "")[:200], "slug": m.get("slug"), "created": str(_created(m))}
        try:
            tokens = json.loads(m.get("clobTokenIds") or "[]")
            outcomes = json.loads(m.get("outcomes") or "[]")
        except ValueError:
            tokens, outcomes = [], []
        if not tokens:
            mrec["note"] = "no clob token"
            rec["markets"].append(mrec)
            continue
        qs = urllib.parse.urlencode({"market": tokens[0], "startTs": end_ts - 30 * 86400, "endTs": end_ts,
                                     "fidelity": 1440})
        try:
            status, body, _, _ = net.get(f"{CLOB}?{qs}", timeout=30)
            hist = (json.loads(body) or {}).get("history") or [] if status == 200 else []
        except Exception:  # noqa: BLE001
            hist = []
        hist = [h for h in hist if isinstance(h, dict) and h.get("t", 1e18) <= end_ts]
        if hist:
            last = max(hist, key=lambda h: h["t"])
            d = datetime.fromtimestamp(last["t"], timezone.utc).date().isoformat()
            name = f"Prediction market price of '{outcomes[0] if outcomes else 'first outcome'}' for: {mrec['question']}"
            rec["points"].append({"name": name[:240], "value": float(last["p"]), "value_as_written": str(last["p"]),
                                  "scale_word": "", "unit": "probability", "period_start": d, "period_end": d,
                                  "published_at_if_visible": d, "quote": name[:200], "verified_by": "api",
                                  "source_url": f"https://polymarket.com/event/{mrec['slug']}", "via": "api"})
        mrec["n_price_points_le_as_of"] = len(hist)
        rec["markets"].append(mrec)
    if not found:
        rec["note"] = "no matching market created on or before as_of"
    return rec
