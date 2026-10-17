"""代码 FETCHER：给一个 URL，拿到「as_of 当天或之前就存在的那一版」页面文字。

1. Wayback CDX 查这个 URL 在 as_of 当天或之前最新的 200 快照，用 id_ 原始形式抓（不带 Wayback 工具栏）。
   跟随重定向后再检查一次：最终 URL 必须还在 web.archive.org 上、能读出 id_ 时间戳、且 <= as_of，否则丢弃。
2. 没有快照：回测（as_of 早于取页当天）一律不用 live 版本——现抓的页面无法证明 as_of 那天就是这个内容
   （审查发现：一个 htmldate 读成 2026-08-17 的预测市场页，正文是取页当天的价格）。
   只有 as_of 就是今天（真实使用）时才用 live 版本：代码要能从 URL 或页面元数据读出日期且 <= as_of，
   正文里也不能有晚于 as_of 的显式日期；标 live_dated。
3. 都不行就丢弃并记原因。
原件和文字存 data/raw/agent/<qid>/（不进 git）；CDX 结果和快照按 URL + 时间戳缓存，重跑不重复打 Wayback。
v2.5：真实使用（as_of = 今天、题目没有登记真值）走 fetch_live：直接抓 live 页，完全不查 Wayback；收下的条件同上面第 2 条。
回测（as_of 早于今天，或登记了真值）仍走 fetch_page，没有改。v2.5.2：fetch_live 每次取页再判断 as_of >= 今天，
已早于今天就改走 fetch_page（不抓 live 页）。
"""
import hashlib
import json
import re
import urllib.parse
from datetime import date, datetime

from ..config import DATA
from . import net
from .evidence import late_dates

RAW_AGENT = DATA / "raw" / "agent"
CACHE = RAW_AGENT / "_cache"
CDX = "https://web.archive.org/cdx/search/cdx"
SNAP_TS = re.compile(r"/web/(\d{14})id_/")
URL_DATE = re.compile(r"(?<!\d)((?:19|20)\d{2})[/_-]?(0[1-9]|1[0-2])[/_-]?(0[1-9]|[12]\d|3[01])?(?!\d)")
TEXT_TYPES = ("text/html", "application/xhtml", "text/plain", "text/csv")
CHARSET = re.compile(r"charset=[\"']?([\w-]+)", re.I)   # HTTP 头；N28：charset="Shift_JIS" 这种带引号的也认
META_CHARSET = re.compile(rb"<meta[^>]+charset\s*=\s*[\"']?\s*([\w-]+)", re.I)   # <meta charset=…> 和 http-equiv 的 content 都认
PRINTABLE_ASCII = bytes(range(0x20, 0x7F))   # _ascii_compatible 用：95 个可打印 ASCII 字节
# UTF-8 BOM 用 utf-8 解（BOM 字符留在开头，和旧版按 utf-8 解的结果相同）；UTF-16 由 codec 按 BOM 认字节序
BOMS = ((b"\xef\xbb\xbf", "utf-8"), (b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16"))
FFFD_MAX = 0.01   # U+FFFD 超过全文 1% 判 undecodable（_to_text）；_decode 的 utf-8 一步用同一个阈值


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
            d = find_date(html, original_date=orig, outputformat="%Y-%m-%d", extensive_search=True)
            if d:
                out.append(date.fromisoformat(d))
    except Exception:  # noqa: BLE001
        pass
    return out


def _clean(s: str) -> bool:
    return s.count("\ufffd") <= FFFD_MAX * max(len(s), 1)


def _ascii_compatible(enc: str) -> bool:
    """meta 一步用：meta 是 bytes 正则在 ASCII 字节里匹配到的，声明 UTF-16/32、EBCDIC 就一定是错的（WHATWG 的 prescan
    也是 meta 写 UTF-16 就按 UTF-8）；UTF-7 会把正文里的「+2.1%」解坏。照这些声明解只会把旧版能解对的页解坏。
    判据：这个编码解可打印 ASCII 必须原样。"""
    try:
        return PRINTABLE_ASCII.decode(enc) == PRINTABLE_ASCII.decode("ascii")
    except (LookupError, UnicodeError):
        return False


def _decode(body: bytes, headers: dict) -> str:
    """字节 → 文字。顺序：HTTP 头的 charset（允许引号）→ BOM → 前 4 KB 的 <meta charset> / http-equiv →
    utf-8（U+FFFD 不超过 FFFD_MAX 才用）→ 自动探测（trafilatura.utils.detect_encoding，内部是 charset_normalizer；
    只用第一个 Python 认识的猜测）→ 都不行返回 utf-8 replace 的结果，由 _to_text 判 undecodable。
    声明的编码 Python 不认识就看下一步；meta 给的编码和 ASCII 不兼容（_ascii_compatible）也不用。
    头里有 Python 认识的 charset 的页面、没有任何声明且按 utf-8 本来就干净的页面，结果和旧版相同。"""
    m = CHARSET.search(headers.get("Content-Type", "") or "")
    declared = [m.group(1)] if m else []
    declared += [enc for bom, enc in BOMS if body.startswith(bom)][:1]
    m = META_CHARSET.search(body[:4096])
    if m and _ascii_compatible(m.group(1).decode("ascii")):
        declared.append(m.group(1).decode("ascii"))
    for enc in declared:
        try:
            return body.decode(enc, "replace")
        except (LookupError, UnicodeError):
            continue
    utf8 = body.decode("utf-8", "replace")
    if _clean(utf8):
        return utf8
    from trafilatura.utils import detect_encoding
    for enc in detect_encoding(body):
        try:
            return body.decode(enc, "replace")
        except (LookupError, UnicodeError):
            continue
    return utf8


def _to_text(body: bytes, headers: dict) -> tuple:
    ct = (headers.get("Content-Type", "") or "").lower()
    if ct and not ct.startswith(TEXT_TYPES):
        return None, f"unsupported content type {ct.split(';')[0]}"
    raw = _decode(body, headers)
    if not _clean(raw):
        return None, "undecodable content (binary or unsupported encoding)"
    if ct.startswith(("text/plain", "text/csv")):
        return raw, ""
    return html_to_text(raw), ""


def fetch_page(url: str, as_of: date, qid: str, allow_live=None, today=None) -> dict:
    """返回页面记录：status in {snapshot, live_dated, dropped}；成功时带 text（只在内存里，落盘到 data/raw）。
    allow_live 默认 = as_of >= 今天（只有真实使用时才收 live 页）。"""
    today = today or date.today()
    if allow_live is None:
        allow_live = as_of >= today
    url = clean_url(url)
    rec = {"url": url, "status": "dropped", "reason": "", "snapshot_ts": None, "page_date": None}
    rec["reason"] = _unsupported(url)
    if rec["reason"]:
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
                headers = json.loads(cache.with_suffix(".json").read_text(encoding="utf-8"))
                body = net.decompress(cache.with_suffix(".bin").read_bytes(), headers)
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
        on_wayback = urllib.parse.urlsplit(final or "").netloc.lower() == "web.archive.org"
        if status == 200 and not (m and on_wayback):
            rec["reason"] = "snapshot redirect not verifiable (final URL has no Wayback id_ timestamp)"
            return rec
        real_ts = m.group(1) if m else ts
        if status == 200 and ts_date(real_ts) <= as_of:
            text, why = _to_text(body, headers)
            if text is None:
                rec["reason"] = why
                return rec
            rec.update(status="snapshot", snapshot_ts=real_ts, page_date=ts_date(real_ts).isoformat())
            return _store(rec, out_dir, body, text)
        rec["reason"] = f"snapshot fetch failed (http {status})" if status != 200 else f"snapshot redirected to {real_ts} > as_of"
    # 没有快照：回测不用 live 版本；真实使用时 live 版本只在能读出日期且 <= as_of、正文没有更晚日期时允许
    if not allow_live:
        rec["reason"] = (rec["reason"] or "no snapshot <= as_of") + "; live pages not used in backtests (as_of before fetch day)"
        return rec
    return _live(rec, out_dir, url, as_of, today, rec["reason"] or "no snapshot <= as_of", lambda u: net.get(u, timeout=45))


def fetch_live(url: str, as_of: date, qid: str, today=None) -> dict:
    """v2.5 真实使用（pipeline 在 ctx.live_fetch 时用它，代替 fetch_page）：直接抓 live 页，不调 cdx_lookup、不请求
    web.archive.org。超时短、不重试（net.get_live）；robots、每个 host 的限速照旧。收下的条件与 fetch_page 的 live 分支相同：
    读得出日期且 <= as_of、正文没有晚于 as_of 的显式日期；标 live_dated。
    v2.5.2：真实使用只在 prepare_run 时判断一次，所以这里每次取页再判断：取页这天 as_of 已早于今天（运行跨过午夜、
    网页上隔天才批准）就不抓 live 页，按回测走 fetch_page 的快照路径（同 v2.4.1 每次取页的 allow_live）。"""
    today = today or date.today()
    if as_of < today:
        return {**fetch_page(url, as_of, qid, today=today), "live_skipped": "as_of before fetch day: snapshot path"}
    url = clean_url(url)
    rec = {"url": url, "status": "dropped", "reason": _unsupported(url), "snapshot_ts": None, "page_date": None}
    if rec["reason"]:
        return rec
    out_dir = RAW_AGENT / qid
    out_dir.mkdir(parents=True, exist_ok=True)
    return _live(rec, out_dir, url, as_of, today, "", net.get_live)


def _unsupported(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        return "not an http url"
    if url.lower().split("?")[0].endswith((".pdf", ".xls", ".xlsx", ".zip", ".doc", ".docx", ".ppt", ".pptx")):
        return "binary file type not supported in MVP"
    return ""


def _live(rec: dict, out_dir, url: str, as_of: date, today: date, pre: str, get) -> dict:
    """抓 live 页并检查：http 200、文字类型、读得出日期且 <= as_of、正文没有晚于 as_of 的显式日期。
    pre = 丢弃原因的前缀（fetch_page：快照为什么没用上；fetch_live：空）。"""
    def why(msg):
        return f"{pre}; {msg}" if pre else msg
    try:
        status, body, headers, final = get(url)
    except net.Blocked:
        rec["reason"] = why("live fetch blocked by robots.txt")
        return rec
    except Exception as e:  # noqa: BLE001
        rec["reason"] = why(f"live fetch error {type(e).__name__}")
        return rec
    if status != 200:
        rec["reason"] = why(f"live http {status}")
        return rec
    text, w = _to_text(body, headers)
    if text is None:
        rec["reason"] = why(w)
        return rec
    dates = page_dates(final, _decode(body, headers))
    if not dates:
        rec["reason"] = why("live page has no readable date")
        return rec
    latest = max(dates)
    if latest > as_of:
        rec["reason"] = why(f"live page dated {latest} > as_of")
        return rec
    late = late_dates(text, as_of, today)
    if late:
        rec["reason"] = why(f"live page text mentions {late[-1]} > as_of")
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
