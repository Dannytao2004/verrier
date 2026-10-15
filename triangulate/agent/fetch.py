"""代码 FETCHER：给一个 URL，拿到「as_of 当天或之前就存在的那一版」页面文字。

1. Wayback CDX 查这个 URL 在 as_of 当天或之前最新的 200 快照，用 id_ 原始形式抓（不带 Wayback 工具栏）。
   跟随重定向后再检查一次最终快照时间戳 <= as_of。
2. 没有快照：只有当代码能从 URL 或页面元数据里读出日期、且最晚的那个日期 <= as_of 时，才允许用 live 版本，标 live_dated。
3. 都不行就丢弃并记原因。
原件和文字存 data/raw/agent/<qid>/（不进 git）；CDX 结果和快照按 URL + 时间戳缓存，重跑不重复打 Wayback。
"""
import hashlib
import json
import re
import urllib.parse
from datetime import date, datetime

from ..config import DATA
from . import net

RAW_AGENT = DATA / "raw" / "agent"
CACHE = RAW_AGENT / "_cache"
CDX = "https://web.archive.org/cdx/search/cdx"
SNAP_TS = re.compile(r"/web/(\d{14})id_/")
URL_DATE = re.compile(r"(?<!\d)((?:19|20)\d{2})[/_-]?(0[1-9]|1[0-2])[/_-]?(0[1-9]|[12]\d|3[01])?(?!\d)")
TEXT_TYPES = ("text/html", "application/xhtml", "text/plain", "text/csv")


def _key(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def clean_url(u: str) -> str:
    """去掉 #fragment；Wayback 链接还原成原始 URL。"""
    u = u.split("#", 1)[0]
    m = re.match(r"https?://web\.archive\.org/web/\d{1,14}[a-z_]*/(https?://.+)", u)
    return m.group(1) if m else u


def select_snapshot(rows: list, as_of: date):
    """CDX json 行（第一行是表头）里挑时间戳 <= as_of 当天的最新 200 快照；没有就 None。纯函数，便于测试。"""
    if not rows or len(rows) < 2:
        return None
    head = rows[0]
    best = None
    lim = as_of.strftime("%Y%m%d") + "235959"
    for r in rows[1:]:
        d = dict(zip(head, r))
        ts = d.get("timestamp", "")
        if len(ts) == 14 and ts.isdigit() and ts <= lim and d.get("statuscode", "200") == "200":
            if best is None or ts > best["timestamp"]:
                best = d
    return best


def ts_date(ts: str) -> date:
    return datetime.strptime(ts[:8], "%Y%m%d").date()


def cdx_lookup(url: str, as_of: date):
    ck = CACHE / "cdx" / f"{_key(url + '|' + as_of.isoformat())}.json"
    if ck.exists():
        rows = json.loads(ck.read_text(encoding="utf-8"))
    else:
        q = urllib.parse.urlencode({"url": url, "to": as_of.strftime("%Y%m%d"), "output": "json", "limit": "-5",
                                    "filter": "statuscode:200", "fl": "timestamp,original,statuscode,mimetype"})
        rows = None
        for _ in range(2):
            status, body, _, _ = net.get(f"{CDX}?{q}", timeout=90)
            if status == 200:
                rows = json.loads(body) if body.strip() else []
                break
        if rows is None:
            raise RuntimeError(f"cdx http {status}")
        ck.parent.mkdir(parents=True, exist_ok=True)
        ck.write_text(json.dumps(rows), encoding="utf-8")
    return select_snapshot(rows, as_of)


def html_to_text(html: str) -> str:
    import trafilatura
    t = trafilatura.extract(html, include_tables=True, include_comments=False, favor_recall=True,
                            deduplicate=False) or ""
    if len(t) < 300:
        try:
            import lxml.html
            doc = lxml.html.fromstring(html)
            for bad in doc.xpath("//script|//style|//noscript"):
                bad.drop_tree()
            alt = re.sub(r"\n\s*\n+", "\n", doc.text_content())
            if len(alt.strip()) > len(t):
                t = alt
        except Exception:  # noqa: BLE001
            pass
    return t.strip()


def page_dates(url: str, html: str) -> list:
    """URL 里的日期 + htmldate 找到的原始日期和最新日期。"""
    out = []
    for m in URL_DATE.finditer(urllib.parse.urlsplit(url).path):
        try:
            out.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3) or 1)))
        except ValueError:
            pass
    try:
        from htmldate import find_date
        for orig in (True, False):
            d = find_date(html, original_date=orig, outputformat="%Y-%m-%d", extensive_search=False)
            if d:
                out.append(date.fromisoformat(d))
    except Exception:  # noqa: BLE001
        pass
    return out


def _decode(body: bytes, headers: dict) -> str:
    ct = headers.get("Content-Type", "") or ""
    m = re.search(r"charset=([\w-]+)", ct, re.I)
    try:
        return body.decode(m.group(1) if m else "utf-8", "replace")
    except LookupError:
        return body.decode("utf-8", "replace")


def _to_text(body: bytes, headers: dict) -> tuple:
    ct = (headers.get("Content-Type", "") or "").lower()
    if ct and not ct.startswith(TEXT_TYPES):
        return None, f"unsupported content type {ct.split(';')[0]}"
    raw = _decode(body, headers)
    if ct.startswith(("text/plain", "text/csv")):
        return raw, ""
    return html_to_text(raw), ""


def fetch_page(url: str, as_of: date, qid: str) -> dict:
    """返回页面记录：status in {snapshot, live_dated, dropped}；成功时带 text（只在内存里，落盘到 data/raw）。"""
    url = clean_url(url)
    rec = {"url": url, "status": "dropped", "reason": "", "snapshot_ts": None, "page_date": None}
    if not url.startswith(("http://", "https://")):
        rec["reason"] = "not an http url"
        return rec
    if url.lower().split("?")[0].endswith((".pdf", ".xls", ".xlsx", ".zip", ".doc", ".docx", ".ppt", ".pptx")):
        rec["reason"] = "binary file type not supported in MVP"
        return rec
    out_dir = RAW_AGENT / qid
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        snap = cdx_lookup(url, as_of)
    except Exception as e:  # noqa: BLE001
        snap, rec["cdx_error"] = None, f"{type(e).__name__}: {e}"[:200]
    if snap:
        ts, orig = snap["timestamp"], snap["original"]
        cache = CACHE / "snap" / f"{_key(ts + orig)}"
        try:
            if cache.with_suffix(".bin").exists():
                body = cache.with_suffix(".bin").read_bytes()
                headers = json.loads(cache.with_suffix(".json").read_text(encoding="utf-8"))
                final = headers.pop("_final_url")
                status = 200
            else:
                status, body, headers, final = net.get(f"https://web.archive.org/web/{ts}id_/{orig}", timeout=90)
                if status == 200:
                    cache.parent.mkdir(parents=True, exist_ok=True)
                    cache.with_suffix(".bin").write_bytes(body)
                    cache.with_suffix(".json").write_text(json.dumps(
                        {"Content-Type": headers.get("Content-Type", ""), "_final_url": final}), encoding="utf-8")
        except net.Blocked:
            status, body, headers, final = 0, b"", {}, ""
        except Exception as e:  # noqa: BLE001
            status, body, headers, final = -1, b"", {}, ""
            rec["fetch_error"] = f"{type(e).__name__}"[:100]
        m = SNAP_TS.search(final or "")
        real_ts = m.group(1) if m else ts
        if status == 200 and ts_date(real_ts) <= as_of:
            text, why = _to_text(body, headers)
            if text is None:
                rec["reason"] = why
                return rec
            rec.update(status="snapshot", snapshot_ts=real_ts, page_date=ts_date(real_ts).isoformat())
            return _store(rec, out_dir, body, text)
        rec["reason"] = f"snapshot fetch failed (http {status})" if status != 200 else f"snapshot redirected to {real_ts} > as_of"
    # 没有快照：live 版本只在能读出日期且 <= as_of 时允许
    try:
        status, body, headers, final = net.get(url, timeout=45)
    except net.Blocked:
        rec["reason"] = (rec["reason"] + "; " if rec["reason"] else "no snapshot <= as_of; ") + "live fetch blocked by robots.txt"
        return rec
    except Exception as e:  # noqa: BLE001
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + f"; live fetch error {type(e).__name__}"
        return rec
    if status != 200:
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + f"; live http {status}"
        return rec
    text, why = _to_text(body, headers)
    if text is None:
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + f"; {why}"
        return rec
    dates = page_dates(final, _decode(body, headers))
    if not dates:
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + "; live page has no readable date"
        return rec
    latest = max(dates)
    if latest > as_of:
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + f"; live page dated {latest} > as_of"
        return rec
    rec.update(status="live_dated", page_date=latest.isoformat(), live_dates=sorted({d.isoformat() for d in dates}),
               reason="")
    return _store(rec, out_dir, body, text)


def _store(rec: dict, out_dir, body: bytes, text: str) -> dict:
    k = _key(rec["url"] + "|" + (rec.get("snapshot_ts") or "live"))
    (out_dir / f"{k}.raw").write_bytes(body)
    (out_dir / f"{k}.txt").write_text(text, encoding="utf-8")
    rec.update(raw_path=f"data/raw/agent/{out_dir.name}/{k}.raw", text_chars=len(text), text=text)
    return rec
