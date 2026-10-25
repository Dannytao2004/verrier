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
v2.8b：PDF（Content-Type application/pdf，或正文以 %PDF 开头）用 pypdfium2 取出所有页的文字，页与页之间空一行，不选页、
不限页数；要密码、损坏（包括下载被截断）、没有文字层（扫描件，不做 OCR）的 PDF 丢弃并写明原因。live PDF 的日期先用 URL 里的，
URL 里没有再用 PDF 元数据的 CreationDate / ModDate。
v2.11d：收下的页另存 page_published（页面自己声明的发布日期，page_published()），只给引文没写期间的点兜底；
page_date、live_dates 和收不收页面都不变。
v2.12h：Office 表格和文档（xlsx、xls、docx）转成文字：xlsx 用 openpyxl、xls 用 xlrd，每张表写成「## 表名」加逐行
「| 单元格 | ... |」；docx 用 mammoth 转 HTML 再走 html_to_text。没用 MarkItDown：它多装 18 个包（onnxruntime、magika 等），
读这三种格式用的就是这几个库。live 文件的日期先用 URL 里的，没有再用 docProps/core.xml 的 created / modified（xls 只认 URL）。
zip、pptx、老式 .doc / .ppt 照旧不收（存档里没出现过 pptx，zip 可能是整包数据集）。
"""
import hashlib
import io
import json
import re
import threading
import urllib.parse
import zipfile
from datetime import date, datetime
from itertools import islice

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
# PDFium 不是线程安全的（pypdfium2 文档：「PDFium is inherently not thread-safe」），而方向、live 取页都在各自的线程里：
# 对它的调用（打开、取文字、关闭）一律在这把锁里做
_PDFIUM_LOCK = threading.Lock()
PDF_DATE = re.compile(r"(?:D:)?((?:19|20)\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])")   # PDF 元数据日期 D:YYYYMMDDHHmmSS…
# v2.12h：Office 文件
OFFICE_TYPES = {"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
                "application/vnd.ms-excel": "xls",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx"}
OFFICE_PART = {"xlsx": "xl/workbook.xml", "docx": "word/document.xml"}   # zip 包里证明是这种文件的那一项
OLE_MAGIC = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"   # xls（老式 Excel）的文件头
OFFICE_MAX_ROWS = 5000   # 每张表最多取的行数 [人为约定：再长的表反正会被 pipeline.MAX_CHARS_TO_EXTRACTOR 截掉]
CORE_DATE = re.compile(r"<dcterms:(created|modified)[^>]*>\s*((?:19|20)\d{2})-(\d{2})-(\d{2})")


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


def _url_dates(url: str) -> list:
    out = []
    for m in URL_DATE.finditer(urllib.parse.urlsplit(url).path):
        try:
            out.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3) or 1)))
        except ValueError:
            pass
    return out


def page_dates(url: str, html: str) -> list:
    """URL 里的日期 + htmldate 找到的原始日期和最新日期。"""
    out = _url_dates(url)
    try:
        from htmldate import find_date
        for orig in (True, False):
            d = find_date(html, original_date=orig, outputformat="%Y-%m-%d", extensive_search=True)
            if d:
                out.append(date.fromisoformat(d))
    except Exception:  # noqa: BLE001
        pass
    return out


def _is_pdf(body: bytes, headers: dict) -> bool:
    return (headers.get("Content-Type") or "").lower().startswith("application/pdf") or body.startswith(b"%PDF")


def pdf_to_text(body: bytes) -> tuple:
    """PDF 字节 -> (全文, "")：pypdfium2 逐页取文字，页与页之间空一行。打不开或没有文字 -> (None, 原因)。"""
    import pypdfium2 as pdfium
    with _PDFIUM_LOCK:
        try:
            pdf = pdfium.PdfDocument(body)
        except pdfium.PdfiumError as e:
            if e.err_code == pdfium.raw.FPDF_ERR_PASSWORD:
                return None, "encrypted PDF (needs a password)"
            return None, f"unreadable PDF: {e}"
        try:
            pages = [p.get_textpage().get_text_range().replace("\r\n", "\n").strip() for p in pdf]
        except pdfium.PdfiumError as e:
            return None, f"unreadable PDF: {e}"
        finally:
            pdf.close()
    text = "\n\n".join(pages)
    if not text.strip():
        return None, "PDF has no text layer (scanned image?); OCR is not supported"
    return text, ""


def pdf_dates(url: str, body: bytes) -> list:
    """live PDF 的日期：URL 里的日期；URL 里没有，再用 PDF 元数据的 CreationDate / ModDate（只取年月日）。
    body 必须是 pdf_to_text 能打开的 PDF。"""
    out = _url_dates(url)
    if out:
        return out
    import pypdfium2 as pdfium
    with _PDFIUM_LOCK:
        pdf = pdfium.PdfDocument(body)
        try:
            meta = pdf.get_metadata_dict()
        finally:
            pdf.close()
    for k in ("CreationDate", "ModDate"):
        m = PDF_DATE.match((meta.get(k) or "").strip())
        if m:
            try:
                out.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3))))
            except ValueError:
                pass
    return out


def office_kind(body: bytes, headers: dict, url: str = "") -> str:
    """xlsx / xls / docx，或空串：Content-Type 或 URL 后缀给出种类，再核对文件头（xlsx、docx 是 zip 包且有对应的那一项，
    xls 是 OLE2）；两样都没有时，zip 包里有 xl/workbook.xml / word/document.xml 也认。核对不上就不当 Office 文件。"""
    ct = (headers.get("Content-Type") or "").lower().split(";")[0].strip()
    path = urllib.parse.urlsplit(url or "").path.lower()
    kind = OFFICE_TYPES.get(ct) or next((k for k in ("xlsx", "xls", "docx") if path.endswith("." + k)), "")
    if kind == "xls":
        return kind if body.startswith(OLE_MAGIC) else ""
    if not body.startswith(b"PK\x03\x04"):
        return ""
    try:
        names = set(zipfile.ZipFile(io.BytesIO(body)).namelist())
    except zipfile.BadZipFile:
        return ""
    if kind:
        return kind if OFFICE_PART[kind] in names else ""
    return next((k for k, part in OFFICE_PART.items() if part in names), "")


def _cell(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else f"{v:.15g}"
    if isinstance(v, datetime):
        return v.date().isoformat() if (v.hour, v.minute, v.second) == (0, 0, 0) else v.isoformat(sep=" ")
    if isinstance(v, date):
        return v.isoformat()
    return " ".join(str(v).split())


def _sheet_text(name: str, rows) -> str:
    out = [f"## {name}"]
    for r in rows:
        cells = [_cell(v) for v in r]
        while cells and not cells[-1]:
            cells.pop()
        if any(cells):
            out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) if len(out) > 1 else ""


def _xls_value(c, book):
    import xlrd
    if c.ctype == xlrd.XL_CELL_DATE:
        try:
            return xlrd.xldate_as_datetime(c.value, book.datemode)
        except (ValueError, OverflowError, xlrd.XLDateError):
            return c.value
    return None if c.ctype in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK, xlrd.XL_CELL_ERROR) else c.value


def office_to_text(body: bytes, kind: str) -> tuple:
    """Office 文件字节 -> (文字, "")；打不开或没有文字 -> (None, 原因)。数字原样写出（整数不带 .0，小数最多 15 位有效数字），
    日期写成 ISO。"""
    try:
        if kind == "xlsx":
            import openpyxl
            wb = openpyxl.load_workbook(io.BytesIO(body), read_only=True, data_only=True)
            try:
                parts = [_sheet_text(ws.title, islice(ws.iter_rows(values_only=True), OFFICE_MAX_ROWS))
                         for ws in wb.worksheets if hasattr(ws, "iter_rows")]
            finally:
                wb.close()
        elif kind == "xls":
            import xlrd
            book = xlrd.open_workbook(file_contents=body)
            parts = [_sheet_text(sh.name, ([_xls_value(c, book) for c in sh.row(i)] for i in range(min(sh.nrows, OFFICE_MAX_ROWS))))
                     for sh in book.sheets()]
        else:
            import mammoth
            parts = [html_to_text(mammoth.convert_to_html(io.BytesIO(body)).value or "")]
    except Exception as e:  # noqa: BLE001  各个库的异常类型很多，统一写成原因
        return None, f"unreadable {kind}: {type(e).__name__}"
    text = "\n\n".join(p for p in parts if p.strip())
    if not text.strip():
        return None, f"{kind} has no text"
    return text, ""


def _last_modified(headers):
    from email.utils import parsedate_to_datetime
    v = (headers or {}).get("Last-Modified")
    try:
        return parsedate_to_datetime(v).date() if v else None
    except (TypeError, ValueError):
        return None


def office_dates(url: str, body: bytes, kind: str, headers=None) -> list:
    """live Office 文件的日期：URL 里的日期；没有再用 docProps/core.xml 的 created / modified（xlsx、docx）；都没有再用
    HTTP 头的 Last-Modified（文件型资源的最后修改时间；香港运输署 table82.xls 没有别的日期，Last-Modified 是 9 月发布那天。
    HTML 页不用它：动态页常给当天）。"""
    out = _url_dates(url)
    if out:
        return out
    if kind in OFFICE_PART:
        try:
            core = zipfile.ZipFile(io.BytesIO(body)).read("docProps/core.xml").decode("utf-8", "replace")
        except (KeyError, zipfile.BadZipFile):
            core = ""
        for _, y, m, d in CORE_DATE.findall(core):
            try:
                out.append(date(int(y), int(m), int(d)))
            except ValueError:
                pass
    lm = None if out else _last_modified(headers)
    return [lm] if lm else out


def page_published(url: str, body: bytes, headers: dict, cap: date):
    """v2.11d：页面自己声明的发布日期（pipeline.verify_point 给引文没写期间的点兜底用），只取一层、返回 date 或 None：
    URL 路径里的日期（有几个取最晚的）；否则 HTML 用 htmldate 的结构化原始日期（original_date=True、extensive_search=False，
    不认晚于 cap 的日期），PDF 用元数据的 CreationDate。cap：live 页是 as_of，快照页是快照日期；快照页传原始 URL
    （snap["original"]）和快照正文，不传 web.archive.org 的地址。page_date、live_dates 和收不收页面照旧，这里不参与。"""
    ds = _url_dates(url)
    if ds:
        return max(ds)
    try:   # 取不到就是 None；这一步出意外也不影响取页本身
        if _is_pdf(body, headers):
            import pypdfium2 as pdfium
            with _PDFIUM_LOCK:
                pdf = pdfium.PdfDocument(body)
                try:
                    meta = pdf.get_metadata_dict()
                finally:
                    pdf.close()
            m = PDF_DATE.match((meta.get("CreationDate") or "").strip())
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
        kind = office_kind(body, headers, url)
        if kind:   # v2.12h：Office 文件用 core.xml 的 created（同 PDF 的 CreationDate）；xls 用 HTTP 头的 Last-Modified
            if kind not in OFFICE_PART:
                return _last_modified(headers)
            core = zipfile.ZipFile(io.BytesIO(body)).read("docProps/core.xml").decode("utf-8", "replace")
            hit = next((g for g in CORE_DATE.findall(core) if g[0] == "created"), None)
            return date(int(hit[1]), int(hit[2]), int(hit[3])) if hit else None
        from htmldate import find_date
        # max_date 要给 datetime（给 date 对象 htmldate 会静默换成今天）；取 cap 当天的最后一刻，cap 当天的日期也认
        d = find_date(_decode(body, headers), original_date=True, extensive_search=False, outputformat="%Y-%m-%d",
                      max_date=datetime(cap.year, cap.month, cap.day, 23, 59, 59))
        return date.fromisoformat(d) if d else None
    except Exception:  # noqa: BLE001
        return None


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


def _to_text(body: bytes, headers: dict, url: str = "") -> tuple:
    if _is_pdf(body, headers):
        return pdf_to_text(body)
    kind = office_kind(body, headers, url)   # v2.12h
    if kind:
        return office_to_text(body, kind)
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
            text, why = _to_text(body, headers, orig)
            if text is None:
                rec["reason"] = why
                return rec
            pub = page_published(orig, body, headers, ts_date(real_ts))   # v2.11d：原始 URL + 快照正文，上限 = 快照日期
            rec.update(status="snapshot", snapshot_ts=real_ts, page_date=ts_date(real_ts).isoformat(),
                       page_published=pub.isoformat() if pub else None)
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
    if url.lower().split("?")[0].endswith((".zip", ".doc", ".ppt", ".pptx")):   # v2.12h：xls / xlsx / docx 改成收（office_to_text）
        return "binary file type not supported in MVP"
    return ""


def _live(rec: dict, out_dir, url: str, as_of: date, today: date, pre: str, get) -> dict:
    """抓 live 页并检查：http 200、文字类型或 PDF、读得出日期且 <= as_of、正文没有晚于 as_of 的显式日期。
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
    text, w = _to_text(body, headers, final)
    if text is None:
        rec["reason"] = why(w)
        return rec
    kind = "" if _is_pdf(body, headers) else office_kind(body, headers, final)
    dates = (pdf_dates(final, body) if _is_pdf(body, headers) else office_dates(final, body, kind, headers) if kind
             else page_dates(final, _decode(body, headers)))
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
    pub = page_published(final, body, headers, as_of)   # v2.11d：上限 = as_of
    rec.update(status="live_dated", page_date=latest.isoformat(), live_dates=sorted({d.isoformat() for d in dates}),
               page_published=pub.isoformat() if pub else None, reason="")
    return _store(rec, out_dir, body, text)


def _store(rec: dict, out_dir, body: bytes, text: str) -> dict:
    k = _key(rec["url"] + "|" + (rec.get("snapshot_ts") or "live"))
    (out_dir / f"{k}.raw").write_bytes(body)
    (out_dir / f"{k}.txt").write_text(text, encoding="utf-8")
    rec.update(raw_path=f"data/raw/agent/{out_dir.name}/{k}.raw", text_chars=len(text), text=text)
    return rec
