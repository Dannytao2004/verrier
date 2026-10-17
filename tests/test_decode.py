"""S9：页面解码（C1 的解码部分、N28）和 zstd 解压。纯函数，不读 data/、results/，不联网。"""
import unittest
from unittest import mock

from triangulate.agent.fetch import _decode, _to_text
from triangulate.agent.net import decompress

JP = "住民基本台帳人口移動報告。移動者の市区町村間移動者数は35万6713人と、前年同月に比べ343人減少しました。"


def page(meta: str = "", body: str = JP * 3) -> str:
    return f"<html><head>{meta}<title>t</title></head><body><p>{body}</p></body></html>"


class TestZstd(unittest.TestCase):
    def test_zstd_magic_is_decompressed(self):
        from compression import zstd
        raw = page().encode("utf-8")
        self.assertEqual(decompress(zstd.compress(raw), {}), raw)   # 缓存里没有 Content-Encoding，只靠魔数
        self.assertEqual(decompress(zstd.compress(raw), {"Content-Encoding": "zstd"}), raw)

    def test_bad_zstd_is_returned_as_is(self):
        bad = b"\x28\xb5\x2f\xfd" + b"not really zstd"
        self.assertEqual(decompress(bad, {}), bad)

    def test_other_bodies_unchanged(self):
        import gzip
        self.assertEqual(decompress(b"<p>x</p>", {}), b"<p>x</p>")
        self.assertEqual(decompress(gzip.compress(b"<p>x</p>"), {}), b"<p>x</p>")


class TestDecodeOrder(unittest.TestCase):
    def test_header_charset_with_quotes(self):   # N28
        # 只有头里有 charset（没有 meta），探测 mock 成报错：头里的 charset 认不出来就只剩 utf-8 一步。
        # 几乎全 ASCII 的正文按 utf-8 解是能过阈值的乱码；日文正文按 utf-8 解不干净、会去调探测。两种都只能靠头里的 charset 解对
        with mock.patch("trafilatura.utils.detect_encoding", side_effect=AssertionError("detector called")):
            for body in ("Population report " * 40 + "東京都", JP * 3):
                html = page(body=body)
                for ct in ('text/html; charset="Shift_JIS"', "text/html; charset='Shift_JIS'", "text/html; charset=Shift_JIS"):
                    with self.subTest(ct=ct, n=len(body)):
                        self.assertEqual(_decode(html.encode("shift_jis"), {"Content-Type": ct}), html)

    def test_header_wins_over_meta(self):
        html = page('<meta charset="Shift_JIS">')
        self.assertEqual(_decode(html.encode("utf-8"), {"Content-Type": "text/html; charset=utf-8"}), html)

    def test_meta_charset_and_http_equiv(self):
        for meta in ('<meta charset="Shift_JIS">', "<meta charset=shift_jis>",
                     '<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">'):
            html = page(meta)
            self.assertEqual(_decode(html.encode("shift_jis"), {"Content-Type": "text/html"}), html, meta)

    def test_meta_only_in_first_4kb(self):
        # 干净的 utf-8 页、正文有非 ASCII 字符：照 meta（latin-1）解和不看 meta（utf-8）解，结果不一样
        text = "<p>Fares rose 3.4% – to €12.50 per trip.</p>" * 3
        pad = "<!-- pad -->" * 400
        far = f'<html><head>{pad}<meta charset="iso-8859-1"></head><body>{text}</body></html>'.encode("utf-8")
        near = f'<html><head><meta charset="iso-8859-1">{pad}</head><body>{text}</body></html>'.encode("utf-8")
        self.assertGreater(far.find(b"<meta"), 4096)
        self.assertLess(near.find(b"<meta"), 4096)
        self.assertNotEqual(far.decode("utf-8"), far.decode("latin-1"))
        self.assertEqual(_decode(far, {"Content-Type": "text/html"}), far.decode("utf-8"))      # 4 KB 之后的 meta 不看
        self.assertEqual(_decode(near, {"Content-Type": "text/html"}), near.decode("latin-1"))  # 对照：前 4 KB 内的照用

    def test_meta_utf16_utf32_ebcdic_ignored(self):
        # meta 是在 ASCII 字节里匹配到的，声明这些编码一定是错的：结果要和 v2.6e（不看 meta，utf-8 replace）逐字相同
        ascii_body = "<p>Heathrow handled 6,912,345 passengers in July 2026, up +2.1% on last year.</p>" * 6
        for meta in ('<meta charset="utf-16">', '<meta http-equiv="Content-Type" content="text/html; charset=UTF-16LE">',
                     '<meta charset="utf16">', '<meta charset="utf-32">', '<meta charset="cp037">'):
            for body in (ascii_body, JP * 3):
                b = page(meta, body).encode("utf-8")
                with self.subTest(meta=meta, ascii=body is ascii_body):
                    self.assertEqual(_decode(b, {"Content-Type": "text/html"}), b.decode("utf-8", "replace"))

    def test_meta_utf7_ignored(self):
        # utf-7 会把「+2.1%」解成「�1%」；不看这个 meta，结果和 v2.6e 逐字相同
        for meta in ('<meta charset="utf-7">', '<meta charset="u7">'):
            for body in ("<p>Passengers rose +2.1% to 6,912,345 in July 2026.</p>",
                         "<p>Heathrow handled 6,912,345 passengers in July 2026, up +2.1% on last year.</p>" * 6):
                b = page(meta, body).encode("utf-8")
                with self.subTest(meta=meta, n=len(body)):
                    self.assertEqual(_decode(b, {"Content-Type": "text/html"}), b.decode("utf-8", "replace"))
                    text, why = _to_text(b, {"Content-Type": "text/html"})
                    self.assertEqual(why, "")
                    self.assertIn("+2.1%", text)

    def test_ascii_compatible_meta_labels_still_used(self):
        from triangulate.agent.fetch import _ascii_compatible
        for lab in ("Shift_JIS", "cp932", "euc-jp", "iso-2022-jp", "gbk", "gb2312", "GB18030", "big5", "euc-kr",
                    "windows-1252", "iso-8859-1", "windows-1251", "koi8-r", "utf-8"):
            self.assertTrue(_ascii_compatible(lab), lab)
        for lab in ("utf-16", "UTF-16LE", "utf-16be", "utf-32", "utf-7", "cp037", "cp500", "x-no-such-codec"):
            self.assertFalse(_ascii_compatible(lab), lab)

    def test_meta_wins_over_clean_utf8(self):
        # 几乎全是 ASCII 的 Shift_JIS 页：按 utf-8 解只有很少的 U+FFFD（旧版当成能解码，日文成了乱码）；meta 排在 utf-8 前面
        html = page('<meta charset="Shift_JIS">', "Population report " * 40 + "東京都")
        b = html.encode("shift_jis")
        self.assertLess(b.decode("utf-8", "replace").count("�"), 0.01 * len(b))
        self.assertEqual(_decode(b, {}), html)

    def test_utf8_bom_kept_like_before(self):
        b = b"\xef\xbb\xbf" + page().encode("utf-8")
        self.assertEqual(_decode(b, {"Content-Type": "text/html"}), b.decode("utf-8", "replace"))   # 和旧版逐字相同

    def test_utf16_bom(self):
        # 探测 mock 成报错。全 ASCII 的正文：没有 BOM 一步就按 utf-8 解，只有 BOM 的 2 个 U+FFFD、字符之间夹着 NUL，能过阈值
        # （v2.6e 就这样放行）；日文正文按 utf-8 解不干净、会去调探测。两种都只能靠 BOM 解对
        with mock.patch("trafilatura.utils.detect_encoding", side_effect=AssertionError("detector called")):
            for body in ("Passengers rose 2.1% to 6,912,345 in July 2026. " * 3, JP * 3):
                with self.subTest(n=len(body)):
                    self.assertEqual(_decode(page(body=body).encode("utf-16"), {"Content-Type": "text/html"}), page(body=body))

    def test_unknown_or_unusable_declared_charset_falls_through(self):
        b = page().encode("utf-8")
        self.assertEqual(_decode(b, {"Content-Type": "text/html; charset=x-no-such-codec"}), page())
        html = page('<meta charset="idna">')   # idna 不支持 errors="replace"，会抛 UnicodeError；不能让页面里的 meta 弄崩取页
        self.assertEqual(_decode(html.encode("utf-8"), {}), html)

    def test_clean_utf8_does_not_call_detector(self):
        with mock.patch("trafilatura.utils.detect_encoding", side_effect=AssertionError("detector called")):
            self.assertEqual(_decode(page().encode("utf-8"), {"Content-Type": "text/html"}), page())

    def test_detector_for_undeclared_non_utf8(self):
        b = page().encode("shift_jis")
        self.assertEqual(_decode(b, {"Content-Type": "text/html"}), page())

    def test_only_first_known_guess_is_used(self):
        b = "Le nombre a augmenté de 3,4 %. ".encode("cp1252") * 20
        with mock.patch("trafilatura.utils.detect_encoding", return_value=["no-such-codec", "cp1252", "latin-1"]):
            self.assertEqual(_decode(b, {}), b.decode("cp1252"))
        # 第一个认识的猜测解出来不干净也照用（之后由 _to_text 判 undecodable），不往后找能解干净的 latin-1
        self.assertNotEqual(b.decode("ascii", "replace"), b.decode("latin-1"))
        with mock.patch("trafilatura.utils.detect_encoding", return_value=["ascii", "latin-1"]):
            self.assertEqual(_decode(b, {}), b.decode("ascii", "replace"))
        with mock.patch("trafilatura.utils.detect_encoding", return_value=[]):
            self.assertEqual(_decode(b, {}), b.decode("utf-8", "replace"))   # 探测不出：旧版的 utf-8 replace


class TestToText(unittest.TestCase):
    def test_shift_jis_meta_page_now_has_text(self):
        html = page('<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">')
        text, why = _to_text(html.encode("shift_jis"), {"Content-Type": "text/html"})
        self.assertEqual(why, "")
        self.assertIn("35万6713人", text)

    def test_binary_still_undecodable(self):
        import os
        for _ in range(5):
            text, why = _to_text(os.urandom(4000), {"Content-Type": "text/html"})
            self.assertIsNone(text)
            self.assertEqual(why, "undecodable content (binary or unsupported encoding)")

    def test_wrong_header_charset_still_undecodable(self):
        # 头说 utf-8、字节其实是 Shift_JIS：头排第一，照旧判 undecodable（不改成探测）
        text, why = _to_text(page().encode("shift_jis"), {"Content-Type": "text/html; charset=utf-8"})
        self.assertIsNone(text)
        self.assertIn("undecodable", why)

    def test_content_type_check_unchanged(self):
        text, why = _to_text(b"%PDF-1.7 ...", {"Content-Type": "application/pdf"})
        self.assertIsNone(text)
        self.assertEqual(why, "unsupported content type application/pdf")


if __name__ == "__main__":
    unittest.main()
