"""S9 / S9b：页面解码（C1 的解码部分、N28；v2.6f1 起用 w3lib）和 zstd 解压。纯函数，不读 data/、results/，不联网。"""
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
    """v2.6f1：解码交给 w3lib.encoding.html_to_unicode（BOM → 头 → meta → 自动探测 → utf-8），这里只钉住我们依赖的行为。"""
    NO_DETECT = mock.patch("charset_normalizer.from_bytes", side_effect=AssertionError("detector called"))

    def test_header_charset_with_quotes(self):   # N28
        # 几乎全 ASCII 的 Shift_JIS 正文：按 utf-8 解是能过阈值的乱码，只能靠头里的 charset 解对；探测 mock 成报错
        html = page(body="Population report " * 40 + "東京都")
        with self.NO_DETECT:
            for ct in ('text/html; charset="Shift_JIS"', "text/html; charset=Shift_JIS"):
                with self.subTest(ct=ct):
                    self.assertEqual(_decode(html.encode("shift_jis"), {"Content-Type": ct}), html)

    def test_header_wins_over_meta(self):
        html = page('<meta charset="Shift_JIS">')
        self.assertEqual(_decode(html.encode("utf-8"), {"Content-Type": "text/html; charset=utf-8"}), html)

    def test_meta_charset_and_http_equiv(self):
        for meta in ('<meta charset="Shift_JIS">', "<meta charset=shift_jis>",
                     '<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">'):
            html = page(meta)
            self.assertEqual(_decode(html.encode("shift_jis"), {"Content-Type": "text/html"}), html, meta)

    def test_meta_wins_over_clean_utf8(self):
        # 浏览器的顺序：meta 排在自动探测前面。几乎全 ASCII 的 Shift_JIS 页按 utf-8 解只有很少的 U+FFFD（v2.6e 当成能解码，日文成了乱码）
        html = page('<meta charset="Shift_JIS">', "Population report " * 40 + "東京都")
        b = html.encode("shift_jis")
        self.assertLess(b.decode("utf-8", "replace").count("\ufffd"), 0.01 * len(b))
        self.assertEqual(_decode(b, {}), html)

    def test_meta_not_ascii_compatible_is_ignored(self):
        # WHATWG：meta 是在 ASCII 字节里读到的，声明 utf-16/32、EBCDIC 必然是错的，按自动探测（这里是 utf-8）解；
        # w3lib 本身会照这些声明解成乱码，这是 fetch._decode 在 w3lib 外补的第一条。idna 不支持 replace，不能让取页崩（第二条）
        ascii_body = "<p>Heathrow handled 6,912,345 passengers in July 2026, up +2.1% on last year.</p>" * 6
        for meta in ('<meta charset="utf-16">', '<meta http-equiv="Content-Type" content="text/html; charset=UTF-16LE">',
                     '<meta charset="utf-32">', '<meta charset="cp037">', '<meta charset="idna">'):
            for body in (ascii_body, JP * 3):
                html = page(meta, body)
                with self.subTest(meta=meta, ascii=body is ascii_body):
                    self.assertEqual(_decode(html.encode("utf-8"), {"Content-Type": "text/html"}), html)

    def test_utf8_bom_is_stripped(self):
        # w3lib 去掉 BOM（v2.6f 以前 BOM 字符留在开头）；html_to_text 之后的正文不受影响
        self.assertEqual(_decode(b"\xef\xbb\xbf" + page().encode("utf-8"), {"Content-Type": "text/html"}), page())

    def test_utf16_bom(self):
        # 全 ASCII 的正文：没有 BOM 一步就按 utf-8 解，只有 BOM 的 2 个 U+FFFD、字符之间夹着 NUL，能过阈值；探测 mock 成报错
        with self.NO_DETECT:
            for body in ("Passengers rose 2.1% to 6,912,345 in July 2026. " * 3, JP * 3):
                with self.subTest(n=len(body)):
                    self.assertEqual(_decode(page(body=body).encode("utf-16"), {"Content-Type": "text/html"}), page(body=body))

    def test_unknown_header_charset_falls_through(self):
        self.assertEqual(_decode(page().encode("utf-8"), {"Content-Type": "text/html; charset=x-no-such-codec"}), page())

    def test_clean_utf8_does_not_call_detector(self):
        with self.NO_DETECT:
            self.assertEqual(_decode(page().encode("utf-8"), {"Content-Type": "text/html"}), page())

    def test_detector_for_undeclared_non_utf8(self):
        self.assertEqual(_decode(page().encode("shift_jis"), {"Content-Type": "text/html"}), page())

    def test_shift_jis_label_decodes_as_cp932(self):
        # w3lib 按 WHATWG 把 shift_jis 换成超集 cp932：「～」「－」这类字符照浏览器的显示（v2.6f 解成「〜」「−」）
        html = page(body="期間：1月～3月、増減－343人")
        self.assertEqual(_decode(html.encode("cp932"), {"Content-Type": "text/html; charset=Shift_JIS"}), html)

    def test_undeclared_utf8_with_a_few_bad_bytes_stays_utf8(self):
        # v2.6f2：没有声明、夹了几个坏字节的 utf-8 页仍按 utf-8（坏字节处出 U+FFFD），不交给探测；
        # v2.6f1 要求整页严格合法，这种页会被猜成 mac_* 之类，「−2.1%」的负号变成乱码
        text = "<p>Passenger numbers fell −2.1% to 6,912,345 – “the weakest July” €.</p>" * 12
        b = page(body=text).encode("utf-8")
        b = b[:300] + b"\xff" + b[300:600] + b"\xfe\xfd" + b[600:]
        with self.NO_DETECT:
            got = _decode(b, {"Content-Type": "text/html"})
        self.assertEqual(got, b.decode("utf-8", "replace"))
        self.assertIn("−2.1%", got)

    def test_single_quoted_header_charset_is_not_a_charset(self):
        # 和浏览器一致：charset='Shift_JIS'（单引号）不是合法的 MIME 参数写法，不当作声明；几乎全 ASCII 的页按 utf-8 解
        # （v2.6e 也是这样；v2.6f 的手写正则曾认它）。改成认单引号要另写解析，按用户的要求不在 w3lib 外再加规则
        b = page(body="Population report " * 40 + "東京都").encode("shift_jis")
        self.assertEqual(_decode(b, {"Content-Type": "text/html; charset='Shift_JIS'"}), b.decode("utf-8", "replace"))

    def test_meta_utf7_ignored(self):
        # w3lib 不认 utf-7 这个 label（WHATWG 也没有）：「+2.1%」不会被 utf-7 解坏。升级 w3lib 时这条是防线
        for meta in ('<meta charset="utf-7">', '<meta charset="u7">'):
            html = page(meta, "<p>Heathrow handled 6,912,345 passengers in July 2026, up +2.1% on last year.</p>" * 6)
            with self.subTest(meta=meta):
                got = _decode(html.encode("utf-8"), {"Content-Type": "text/html"})
                self.assertEqual(got, html)
                self.assertIn("+2.1%", got)

    def test_meta_only_in_first_4kb(self):
        # 干净的 utf-8 页、正文有非 ASCII 字符：前 4 KB 内的 meta（latin-1，w3lib 按 WHATWG 换成 cp1252）照用，4 KB 之后的不看
        text = "<p>Fares rose 3.4% – to €12.50 per trip.</p>" * 3
        pad = "<!-- pad -->" * 400
        far = f'<html><head>{pad}<meta charset="iso-8859-1"></head><body>{text}</body></html>'.encode("utf-8")
        near = f'<html><head><meta charset="iso-8859-1">{pad}</head><body>{text}</body></html>'.encode("utf-8")
        self.assertGreater(far.find(b"<meta"), 4096)
        self.assertLess(near.find(b"<meta"), 4096)
        self.assertEqual(_decode(far, {"Content-Type": "text/html"}), far.decode("utf-8"))
        self.assertEqual(_decode(near, {"Content-Type": "text/html"}), near.decode("cp1252", "replace"))


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
        # v2.8b 起 PDF 交给 pypdfium2（tests/test_pdf.py），这里换成别的二进制类型
        text, why = _to_text(b"PK\x03\x04 ...", {"Content-Type": "application/zip"})
        self.assertIsNone(text)
        self.assertEqual(why, "unsupported content type application/zip")


if __name__ == "__main__":
    unittest.main()
