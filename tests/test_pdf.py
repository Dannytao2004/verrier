"""L2（v2.8b）：PDF 用 pypdfium2 取全文；live PDF 的日期先看 URL、再看元数据；抽取员最多收 40 万字符。
测试用的 PDF 在这里手写（不读 data/、results/），不联网、不调模型。"""
import os
import threading
import unittest
from datetime import date
from types import SimpleNamespace
from unittest import mock

from triangulate import config
from triangulate.agent import fetch as F
from triangulate.agent import net
from triangulate.agent import pipeline as P
from tests.test_live import FakeNet, NetCase

AS_OF = date(2026, 10, 16)
META = {"CreationDate": "D:20260915083000+09'00'", "ModDate": "D:20260916090000+09'00'"}


def make_pdf(pages, info=None, encrypt=False) -> bytes:
    """最小 PDF：pages 是每页的文字行列表（空列表 = 只有线条、没有文字的页，像扫描件）；info 写进 /Info；
    encrypt=True 加一个标准加密字典（/U 是随便填的，空密码打不开 = 要密码）。"""
    objs = [b"<< /Type /Catalog /Pages 2 0 R >>", b"", b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    kids = []
    for lines in pages:
        ops = ("BT /F1 12 Tf 72 720 Td 14 TL " + " ".join(f"({x}) Tj T*" for x in lines) + " ET") if lines else "0 0 m 200 200 l S"
        kids.append(len(objs) + 1)
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> "
                    f"/Contents {len(objs) + 2} 0 R >>".encode())
        objs.append(b"<< /Length %d >>\nstream\n" % len(ops) + ops.encode("latin-1") + b"\nendstream")
    objs[1] = f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] /Count {len(kids)} >>".encode()
    trailer = "/Root 1 0 R"
    if info:
        objs.append(("<< " + " ".join(f"/{k} ({v})" for k, v in info.items()) + " >>").encode("latin-1"))
        trailer += f" /Info {len(objs)} 0 R"
    if encrypt:
        objs.append(b"<< /Filter /Standard /V 1 /R 2 /O <" + os.urandom(32).hex().encode() + b"> /U <"
                    + bytes(32).hex().encode() + b"> /P -4 >>")
        trailer += f" /Encrypt {len(objs)} 0 R /ID [<{'00' * 16}> <{'00' * 16}>]"
    out, offs = bytearray(b"%PDF-1.4\n"), []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    x = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1) + b"".join(b"%010d 00000 n \n" % o for o in offs)
    out += f"trailer\n<< /Size {len(objs) + 1} {trailer} >>\nstartxref\n{x}\n%%EOF\n".encode()
    return bytes(out)


THREE = make_pdf([["Visitors in September 2026: 35,518", "Second line 12.5%"], [], ["Page three 1,234"]], info=META)


class TestPdfToText(unittest.TestCase):
    def test_all_pages_joined_with_blank_lines(self):
        self.assertEqual(F.pdf_to_text(THREE),
                         ("Visitors in September 2026: 35,518\nSecond line 12.5%\n\n\n\nPage three 1,234", ""))

    def test_detected_by_content_type_or_magic(self):
        want = F.pdf_to_text(THREE)
        for headers in ({"Content-Type": "application/pdf"}, {"Content-Type": "application/octet-stream"},
                        {"Content-Type": "text/html"}, {}):
            self.assertEqual(F._to_text(THREE, headers), want, headers)

    def test_dropped_with_reason(self):
        cases = {b"%PDF-1.7 ...": "unreadable PDF: Failed to load document (PDFium: Data format error).",
                 THREE[: len(THREE) // 2]: "unreadable PDF: Failed to load document (PDFium: Data format error).",
                 make_pdf([["secret 1"]], encrypt=True): "encrypted PDF (needs a password)",
                 make_pdf([[], []]): "PDF has no text layer (scanned image?); OCR is not supported"}
        for body, why in cases.items():
            self.assertEqual(F._to_text(body, {"Content-Type": "application/pdf"}), (None, why))
        self.assertEqual(F._to_text(b"<html>error</html>", {"Content-Type": "application/pdf"}),
                         (None, "unreadable PDF: Failed to load document (PDFium: Data format error)."))

    def test_pdfium_called_under_the_lock(self):
        import pypdfium2
        real, seen = pypdfium2.PdfDocument, []

        def spy(*a, **k):
            seen.append(F._PDFIUM_LOCK.locked())
            return real(*a, **k)

        with mock.patch.object(pypdfium2, "PdfDocument", spy):
            F.pdf_to_text(THREE)
            F.pdf_dates("https://x.example.org/report.pdf", THREE)
        self.assertEqual(seen, [True, True])
        out = []
        threads = [threading.Thread(target=lambda: out.append(F.pdf_to_text(THREE))) for _ in range(8)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(out, [F.pdf_to_text(THREE)] * 8)


class TestPdfDates(unittest.TestCase):
    def test_url_date_first_then_metadata(self):
        self.assertEqual(F.pdf_dates("https://www.jnto.go.jp/statistics/data/20260910.pdf", THREE), [date(2026, 9, 10)])
        self.assertEqual(F.pdf_dates("https://stat.example.org/report.pdf?id=7", THREE),
                         [date(2026, 9, 15), date(2026, 9, 16)])
        self.assertEqual(F.pdf_dates("https://stat.example.org/report.pdf", make_pdf([["x 1"]])), [])


class TestFetchPdf(NetCase):
    def test_live_pdf(self):
        nodate = make_pdf([["Visitors in September 2026: 35,518"]])
        later = make_pdf([["Visitors 35,518"]], info={"CreationDate": "D:20261020000000Z"})
        bodies = {"/stats/20261001.pdf": THREE, "/stats/report.pdf": THREE, "/nodate.pdf": nodate, "/later.pdf": later,
                  "/locked.pdf": make_pdf([["x 1"]], encrypt=True)}
        fake = FakeNet(lambda u: (200, bodies[u.split("example.org", 1)[1]], {"Content-Type": "application/pdf"}))
        self.use(fake, 0.01)
        got = {k: F.fetch_live(f"https://a.example.org{k}", AS_OF, "t", today=AS_OF) for k in bodies}
        self.assertEqual({k: (r["status"], r["page_date"], r["reason"]) for k, r in got.items()},
                         {"/stats/20261001.pdf": ("live_dated", "2026-10-01", ""),
                          "/stats/report.pdf": ("live_dated", "2026-09-16", ""),
                          "/nodate.pdf": ("dropped", None, "live page has no readable date"),
                          "/later.pdf": ("dropped", None, "live page dated 2026-10-20 > as_of"),
                          "/locked.pdf": ("dropped", None, "encrypted PDF (needs a password)")})
        rec = got["/stats/report.pdf"]
        self.assertEqual(rec["text"], F.pdf_to_text(THREE)[0])
        self.assertEqual((self.tmp / "t" / rec["raw_path"].split("/")[-1]).read_bytes(), THREE)
        self.assertEqual(F.fetch_live("https://a.example.org/r.xlsx", AS_OF, "t", today=AS_OF)["reason"],
                         "binary file type not supported in MVP")

    def test_snapshot_pdf(self):
        orig = "https://stat.example.org/report.pdf"
        snap = "https://web.archive.org/web/20261001000000id_/" + orig
        fake = FakeNet(lambda u: (200, THREE, {"Content-Type": "application/pdf"}) if u == snap else (404, b"", {}))
        self.use(fake, 0.01)
        with mock.patch.object(F, "cdx_lookup", return_value={"timestamp": "20261001000000", "original": orig}), \
                mock.patch.dict(net.HOST_INTERVAL, {"web.archive.org": 0.01}):
            rec = F.fetch_page(orig, AS_OF, "t", today=date(2026, 10, 20))
        self.assertEqual((rec["status"], rec["page_date"], rec["reason"]), ("snapshot", "2026-10-01", ""))
        self.assertEqual(rec["text"], F.pdf_to_text(THREE)[0])


class TestDirectionWithPdf(NetCase):
    def test_live_direction_verifies_a_quote_from_a_pdf(self):
        """一个方向从头走到尾（假搜索、假网络、假抽取员）：live 取到 PDF -> 全文给抽取员 -> quote 在 PDF 文字里核对通过。"""
        from tests.test_live import _Searcher, _ctx
        self.use(FakeNet(lambda u: (200, make_pdf([["Visitor arrivals, September 2026", "Total visitors: 3,266,800"]]),
                                    {"Content-Type": "application/pdf"})), 0.01)
        ctx = _ctx(True, as_of=date.today().isoformat())
        point = {"name": "visitor arrivals, September 2026", "value_as_written": "3,266,800", "scale_word": "",
                 "unit": "visitors", "period_start": "2026-09-01", "period_end": "2026-09-30", "quote": "Total visitors: 3,266,800"}
        ctx.llm = SimpleNamespace(ask=lambda system, user, **kw: ({"points": [point] if "Total visitors: 3,266,800" in user else []}, None))
        ctx.searcher = _Searcher(["https://stat.example.org/data/20261010.pdf"])
        target = {"what": "visitor arrivals", "unit": "visitor", "period_start": "2026-09-01", "period_end": "2026-09-30"}
        out = P.run_direction(ctx, target, {"id": "d1", "category": "related_series"}, 1)
        self.assertEqual([(p["status"], p["page_date"], p["n_points_verified"]) for p in out["pages"]], [("live_dated", "2026-10-10", 1)])
        self.assertEqual([(p["value"], p["via"]) for p in out["points"]], [(3266800.0, "live_dated")])


class TestExtractorGetsLongPages(unittest.TestCase):
    def test_up_to_400k_chars_and_16k_tokens(self):
        asked = []

        def ask(system, user, **kw):
            asked.append((len(user), kw["max_tokens"]))
            return {"points": []}, None

        ctx = SimpleNamespace(leak_patterns=[], as_of=AS_OF, qid="t", llm=SimpleNamespace(ask=ask))
        target = {"what": "x", "unit": "visitor", "period_start": "2026-09-01", "period_end": "2026-09-30"}
        pages = []
        for n in (30_000, 450_000):
            out = {"pages": [], "points": [], "dropped_points": []}
            P._process_page(ctx, target, {"id": "d1"}, 1, {"url": "https://x.org/a", "status": "snapshot"}, "y" * n, out, False)
            pages.append({k: out["pages"][0][k] for k in ("chars_sent", "truncated")})
        self.assertEqual(pages, [{"chars_sent": 30_000, "truncated": False}, {"chars_sent": 400_000, "truncated": True}])
        self.assertEqual([m for _, m in asked], [config.MAX_TOKENS["extract"]] * 2)
        self.assertEqual(config.MAX_TOKENS["extract"], 16000)
        self.assertGreater(asked[1][0], 400_000)
        self.assertLess(asked[1][0], 410_000)
        self.assertEqual(net.MAX_BYTES, 64_000_000)


if __name__ == "__main__":
    unittest.main()
