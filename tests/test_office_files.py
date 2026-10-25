"""v2.12h：Office 表格和文档（xlsx、xls、docx）转成文字，live 文件的日期取 URL 或 docProps/core.xml。
存档里被「binary file type not supported in MVP」丢掉的 Office 文件：香港运输署 table82.xls、NHS 英格兰急诊时间序列、
INEGI 出口公报、Pizza-Market-Profiler-2020.docx 等 11 页（179 次运行）。不联网、不写 data/raw（NetCase 换成临时目录）。"""
import io
import unittest
import zipfile
from datetime import date, datetime

import openpyxl

from triangulate.agent import fetch as F
from triangulate.agent import net
from tests.test_live import FakeNet, NetCase

AS_OF = date(2026, 10, 16)
XLSX_CT = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
DOCX_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _core(created="", modified="") -> str:
    tag = lambda t, v: f'<dcterms:{t} xsi:type="dcterms:W3CDTF">{v}</dcterms:{t}>' if v else ""
    return ('<?xml version="1.0"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/'
            'core-properties" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'{tag("created", created)}{tag("modified", modified)}</cp:coreProperties>')


def _with_core(body: bytes, core: str) -> bytes:
    """openpyxl 保存时把 modified 改成当前时间：换掉 docProps/core.xml，测试里的日期才是写死的。"""
    src, out = zipfile.ZipFile(io.BytesIO(body)), io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for n in src.namelist():
            z.writestr(n, core if n == "docProps/core.xml" else src.read(n))
    return out.getvalue()


def make_xlsx(rows, created="2026-09-30T08:00:00Z", modified="2026-10-02T09:00:00Z", title="Table 82") -> bytes:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = title
    for r in rows:
        ws.append(r)
    b = io.BytesIO()
    wb.save(b)
    return _with_core(b.getvalue(), _core(created, modified))


def make_docx(paragraphs, table=(), created="2020-01-15T10:00:00Z") -> bytes:
    body = "".join(f"<w:p><w:r><w:t>{p}</w:t></w:r></w:p>" for p in paragraphs)
    if table:
        body += "<w:tbl>" + "".join("<w:tr>" + "".join(f"<w:tc><w:p><w:r><w:t>{c}</w:t></w:r></w:p></w:tc>" for c in row)
                                    + "</w:tr>" for row in table) + "</w:tbl>"
    parts = {
        "[Content_Types].xml": ('<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                                '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                                '<Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" '
                                'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                                '</Types>'),
        "_rels/.rels": ('<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
                        'officeDocument" Target="word/document.xml"/></Relationships>'),
        "word/document.xml": f'<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="{W}"><w:body>{body}</w:body></w:document>',
        "docProps/core.xml": _core(created),
    }
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w") as z:
        for n, s in parts.items():
            z.writestr(n, s)
    return b.getvalue()


ROWS = [["Visitor arrivals", None, None], ["Month", "Visitors", "Share"], [datetime(2026, 8, 1), 3266800, 0.123],
        ["Total", 1234567.5, None]]
XLSX = make_xlsx(ROWS)
DOCX = make_docx(["Pizza Market Profiler 2020"], [["Slices per year", "3 billion"]])


class TestKind(unittest.TestCase):
    def test_by_content_type_url_or_zip_contents(self):
        self.assertEqual(F.office_kind(XLSX, {"Content-Type": XLSX_CT}), "xlsx")
        self.assertEqual(F.office_kind(XLSX, {"Content-Type": "application/octet-stream"}, "https://a.org/t.xlsx"), "xlsx")
        self.assertEqual(F.office_kind(XLSX, {}, "https://a.org/download?id=7"), "xlsx")   # 只认 zip 包里的 xl/workbook.xml
        self.assertEqual(F.office_kind(DOCX, {"Content-Type": DOCX_CT}), "docx")
        self.assertEqual(F.office_kind(F.OLE_MAGIC + b"\0" * 100, {}, "https://www.td.gov.hk/table82.xls"), "xls")

    def test_wrong_bytes_are_not_office(self):
        self.assertEqual(F.office_kind(b"<html>x</html>", {"Content-Type": XLSX_CT}), "")
        self.assertEqual(F.office_kind(b"PK\x03\x04junk", {}, "https://a.org/t.xlsx"), "")
        self.assertEqual(F.office_kind(b"not ole", {}, "https://a.org/t.xls"), "")
        self.assertEqual(F.office_kind(XLSX, {}, "https://a.org/t.docx"), "")          # 后缀说 docx，包里是表格：不认
        self.assertEqual(F.office_kind(b"<html>", {"Content-Type": "text/html"}, "https://a.org/p"), "")


class TestToText(unittest.TestCase):
    def test_xlsx_rows(self):
        text, why = F.office_to_text(XLSX, "xlsx")
        self.assertEqual(why, "")
        self.assertEqual(text, "## Table 82\n| Visitor arrivals |\n| Month | Visitors | Share |\n| 2026-08-01 | 3266800 | 0.123 |\n"
                               "| Total | 1234567.5 |")

    def test_docx_paragraphs_and_table(self):
        self.assertEqual(F.office_to_text(DOCX, "docx"), ("Pizza Market Profiler 2020\n| Slices per year | 3 billion |", ""))

    def test_broken_or_empty(self):
        self.assertEqual(F.office_to_text(b"PK\x03\x04junk", "xlsx")[0], None)
        self.assertIn("unreadable xls", F.office_to_text(F.OLE_MAGIC + b"\0" * 100, "xls")[1])
        self.assertEqual(F.office_to_text(make_xlsx([]), "xlsx"), (None, "xlsx has no text"))

    def test_cell_formats(self):
        self.assertEqual([F._cell(v) for v in (None, 5.0, 0.1 + 0.2, 1234567.891, datetime(2026, 8, 1, 13, 5), "a\n b", True)],
                         ["", "5", "0.3", "1234567.891", "2026-08-01 13:05:00", "a b", "True"])


class TestDates(unittest.TestCase):
    def test_url_first_then_core_properties(self):
        self.assertEqual(F.office_dates("https://a.org/2026/09/15/t.xlsx", XLSX, "xlsx"), [date(2026, 9, 15)])
        self.assertEqual(F.office_dates("https://a.org/t.xlsx", XLSX, "xlsx"), [date(2026, 9, 30), date(2026, 10, 2)])
        self.assertEqual(F.office_dates("https://a.org/t.xlsx", make_xlsx(ROWS, "", ""), "xlsx"), [])
        self.assertEqual(F.office_dates("https://a.org/t.xls", F.OLE_MAGIC, "xls"), [])
        # 都没有时用 HTTP 头的 Last-Modified（香港运输署 table82.xls 的真实响应头）
        lm = {"Last-Modified": "Tue, 29 Sep 2026 03:04:44 GMT"}
        self.assertEqual(F.office_dates("https://www.td.gov.hk/table82.xls", F.OLE_MAGIC, "xls", lm), [date(2026, 9, 29)])
        self.assertEqual(F.office_dates("https://a.org/t.xlsx", XLSX, "xlsx", lm), [date(2026, 9, 30), date(2026, 10, 2)])
        self.assertEqual(F.office_dates("https://a.org/t.xls", F.OLE_MAGIC, "xls", {"Last-Modified": "garbage"}), [])
        self.assertEqual(F.page_published("https://www.td.gov.hk/table82.xls", F.OLE_MAGIC, lm, AS_OF), date(2026, 9, 29))

    def test_page_published_uses_created(self):
        self.assertEqual(F.page_published("https://a.org/t.xlsx", XLSX, {}, AS_OF), date(2026, 9, 30))
        self.assertEqual(F.page_published("https://a.org/p.docx", DOCX, {}, AS_OF), date(2020, 1, 15))


class TestQuoteFromATableRow(unittest.TestCase):
    def test_row_quote_verifies(self):
        """抽取员抄表格的一行当引文：引文核对（verify_point）在转出来的文字里找得到这一行和这个数。"""
        from triangulate.agent import evidence as ev
        from triangulate.agent import pipeline as P
        text = F.office_to_text(XLSX, "xlsx")[0]
        raw = {"name": "Visitor arrivals, August 2026", "value_as_written": "3266800", "scale_word": "", "unit": "visitors",
               "period_start": "2026-08-01", "period_end": "2026-08-31", "quote": "| 2026-08-01 | 3266800 | 0.123 |"}
        p, why = P.verify_point(raw, ev.norm(text), AS_OF, None, date(2026, 9, 30), url="https://a.org/t.xlsx")
        self.assertEqual((why, p["value"] if p else None), ("", 3266800.0))


class TestFetchOffice(NetCase):
    def test_live_files(self):
        later = make_xlsx(ROWS, "2026-10-01T00:00:00Z", "2026-10-20T00:00:00Z")
        bodies = {"/t.xlsx": (XLSX, XLSX_CT), "/p.docx": (DOCX, DOCX_CT), "/later.xlsx": (later, XLSX_CT),
                  "/nodate.xlsx": (make_xlsx(ROWS, "", ""), "application/octet-stream")}
        fake = FakeNet(lambda u: (200, bodies[u.split("example.org", 1)[1]][0], {"Content-Type": bodies[u.split("example.org", 1)[1]][1]}))
        self.use(fake, 0.01)
        got = {k: F.fetch_live(f"https://a.example.org{k}", AS_OF, "t", today=AS_OF) for k in bodies}
        self.assertEqual({k: (r["status"], r["page_date"], r["reason"]) for k, r in got.items()},
                         {"/t.xlsx": ("live_dated", "2026-10-02", ""), "/p.docx": ("live_dated", "2020-01-15", ""),
                          "/later.xlsx": ("dropped", None, "live page dated 2026-10-20 > as_of"),
                          "/nodate.xlsx": ("dropped", None, "live page has no readable date")})
        rec = got["/t.xlsx"]
        self.assertEqual(rec["text"], F.office_to_text(XLSX, "xlsx")[0])
        self.assertEqual(rec["page_published"], "2026-09-30")
        self.assertEqual((self.tmp / "t" / rec["raw_path"].split("/")[-1]).read_bytes(), XLSX)
        for still in ("https://a.example.org/r.zip", "https://a.example.org/r.pptx", "https://a.example.org/r.doc"):
            self.assertEqual(F.fetch_live(still, AS_OF, "t", today=AS_OF)["reason"], "binary file type not supported in MVP")

    def test_snapshot_xlsx(self):
        from unittest import mock
        orig = "https://stat.example.org/table.xlsx"
        snap = "https://web.archive.org/web/20261001000000id_/" + orig
        fake = FakeNet(lambda u: (200, XLSX, {"Content-Type": XLSX_CT}) if u == snap else (404, b"", {}))
        self.use(fake, 0.01)
        with mock.patch.object(F, "cdx_lookup", return_value={"timestamp": "20261001000000", "original": orig}), \
                mock.patch.dict(net.HOST_INTERVAL, {"web.archive.org": 0.01}):
            rec = F.fetch_page(orig, AS_OF, "t", today=date(2026, 10, 20))
        self.assertEqual((rec["status"], rec["page_date"], rec["reason"]), ("snapshot", "2026-10-01", ""))
        self.assertIn("| 2026-08-01 | 3266800 | 0.123 |", rec["text"])


if __name__ == "__main__":
    unittest.main()
