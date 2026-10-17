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
FFFD_MAX = 0.01   # U+FFFD 超过全文 1% 判 undecodable（_to_text）


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


def _sniff(body: bytes):
    """没有任何声明时的自动探测：按 utf-8 解、U+FFFD 不超过 FFFD_MAX 就用 utf-8（夹了几个坏字节的 utf-8 页仍按 utf-8，
    v2.6f1 要求整页严格合法时，这种页会被 charset_normalizer 猜成 mac_iceland 之类、负号「−」变成乱码）；否则用
    charset_normalizer 的最佳猜测（猜不出返回 None，html_to_unicode 退回 utf-8）。"""
    if _clean(body.decode("utf-8", "replace")):
        return "utf-8"
    from charset_normalizer import from_bytes
    best = from_bytes(body).best()
    return best.encoding if best else None


def _decode(body: bytes, headers: dict) -> str:
    """字节 → 文字。v2.6f1 起交给现成的库 w3lib.encoding.html_to_unicode（Scrapy 的编码模块），按浏览器的顺序：
    BOM → HTTP 头的 charset → <meta> / xml 声明 → 自动探测（_sniff）→ utf-8；编码别名按 WHATWG 换成超集
    （shift_jis → cp932、gb2312 → gb18030、latin-1 → cp1252 等），UTF BOM 会被去掉。解不对的字节变成 U+FFFD，
    由 _to_text 按 FFFD_MAX 判 undecodable。
    w3lib 之外只补两条：(1) 编码只来自 <meta> 且和 ASCII 不兼容（utf-16/32、EBCDIC）时按 WHATWG 的规定不用它，改走自动探测
    （meta 是在 ASCII 字节里读到的，这种声明必然是错的）；(2) 声明的编码不支持 errors="replace"（如 idna）时不崩，同样改走自动探测。"""
    from w3lib.encoding import html_body_declared_encoding, html_to_unicode, http_content_type_encoding, read_bom
    ct = headers.get("Content-Type") or None
    try:
        enc, text = html_to_unicode(ct, body, auto_detect_fun=_sniff)
    except (UnicodeError, LookupError):
        enc, text = None, None
    from_meta = read_bom(body)[0] is None and http_content_type_encoding(ct) is None and html_body_declared_encoding(body)
    if text is None or (from_meta and b"<html>".decode(enc, "replace") != "<html>"):
        text = body.decode(_sniff(body) or "utf-8", "replace")
    return text


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
