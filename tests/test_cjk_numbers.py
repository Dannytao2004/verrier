"""v2.6e 中日韩数字和日期（N26、N27、C1 的解析部分）：倍数字 万/萬/만、億/亿/억、兆/조 和复合写法（519万548）、
scale_word 里倍数字后面的单位（万人、兆円）、复合倍数万亿、英文 '000s；日期 YYYY年M月D日 / YYYY년 M월 D일 / 令和・平成・民國 N 年；
期间年份检查认纪年；哨兵登记中日韩的精确写法。纯函数测试，不联网、不调模型、不读 data/ 和 results/。"""
import unittest
from datetime import date

from triangulate.agent import evidence as ev
from triangulate.agent.pipeline import verify_point

# fc_jp_movers_2026_08 缓存页（data/raw/agent/fc_jp_movers_2026_08/0d20a4b15baf2053.txt）里的原句，原样（全角数字）
JP = ("2025年１月～12月の１年間における日本国内の移動状況（日本人及び外国人）をみると、市区町村間移動者数（市区町村間で住所を移し、"
      "転入の届出を行った者の数）は519万548人で、前年に比べ１万7,198人（0.3％）の減少となりました。")
# fc_tw_births_2026_09 缓存页（00a6cbaf771d30fc.txt）里的两句：只写民国纪年，正文没有「2026」
TW = ("內政部今（10日）公布民國115年5月戶口統計資料，截至5月底，台灣總人口數2325萬2641人，與上年同月比較減少10萬2829人。\n"
      "115年5月出生數為6832人，約每6.5分鐘出生一個嬰兒，折合年粗出生率為千分之3.46，較上年同月減少1,601人。")
YEAR_DROP = "period year 2026 does not appear in the page text or URL (likely mis-dated)"
FRAGMENT = "number: value_as_written is only part of a larger CJK number in the quote"
MEGA = "number: ambiguous '兆' before an SI unit: 10^12 or mega-"


def _vp(text, url="https://example.org/x", **kw):
    raw = {"name": "x", "scale_word": "", "unit": "people", "period_start": "2025-01-01", "period_end": "2025-12-31", **kw}
    return verify_point(raw, ev.norm(text), date(2026, 8, 29), None, False, url=url)


class TestParseValueCjk(unittest.TestCase):
    def test_plan_examples(self):
        self.assertEqual(ev.parse_value("519万", ""), (5_190_000.0, False))
        self.assertEqual(ev.parse_value("35万6713", ""), (356_713.0, False))
        self.assertEqual(ev.parse_value("3409万", ""), (34_090_000.0, False))
        self.assertEqual(ev.parse_value("2만4,275", ""), (24_275.0, False))

    def test_compound_forms_are_summed_by_code(self):
        for vw, v in [("519万548", 5_190_548), ("1億2345万", 123_450_000), ("1億2345万6789", 123_456_789),
                      ("1억 2345만 6789", 123_456_789), ("2만 9000", 29_000), ("１万7,198", 17_198), ("10萬4,376", 104_376),
                      ("2325萬2641", 23_252_641), ("3万亿5000亿", 3_500_000_000_000), ("1万亿", 1e12),
                      ("-35万6713", -356_713), ("(35万6713)", -356_713), ("3409万人", 34_090_000)]:
            self.assertEqual(ev.parse_value(vw, ""), (float(v), False), vw)
        self.assertAlmostEqual(ev.parse_value("13.4萬", "")[0], 134_000)
        self.assertAlmostEqual(ev.parse_value("13.48萬", "")[0], 134_800)
        # 模型把倍数字也填进 scale_word：和数字里的第一段一致就不重复乘
        self.assertEqual(ev.parse_value("519万548", "万"), (5_190_548.0, False))
        self.assertEqual(ev.parse_value("3409万", "万人"), (34_090_000.0, False))
        self.assertEqual(ev.parse_value("1億2345万", "億"), (123_450_000.0, False))

    def test_scale_word_with_trailing_unit(self):
        for vw, sw, v in [("315", "万", 3_150_000), ("4,140", "万人", 41_400_000), ("2,995", "万人泊", 29_950_000),
                          ("9.64", "兆円", 9.64e12), ("15.4", "万亿", 1.54e13), ("975", "亿", 9.75e10), ("25", "만", 250_000),
                          ("3", "억 원", 3e8), ("13.4", "萬", 134_000), ("7,348", "000s", 7_348_000), ("7,348", "'000s", 7_348_000)]:
            self.assertAlmostEqual(ev.parse_value(vw, sw)[0], v, msg=f"{vw} {sw}")
            self.assertFalse(ev.parse_value(vw, sw)[1])

    def test_rejected_not_silently_misread(self):
        for vw, sw, msg in [("35万67130", "", "malformed CJK number"), ("5万3万", "", "malformed CJK number"),
                            ("1億12345万", "", "malformed CJK number"), ("1.5万3000", "", "decimal in a multi-part"),
                            ("61万1千", "", "CJK numerals"), ("1千", "", "CJK numerals"), ("三百", "", "no number"),
                            ("3409万 2025", "", "more than one number"), ("3409万", "million", "scale conflict"),
                            ("1億2345万", "万", "scale conflict"), ("2", "成", "unknown scale word"),
                            ("5", "万5", "unknown scale word"), ("5", "万千", "unknown scale word"),
                            ("500兆瓦", "", "ambiguous '兆'"), ("500 兆瓦", "", "ambiguous '兆'"), ("500", "兆瓦", "ambiguous '兆'"),
                            ("3.5", "兆赫", "ambiguous '兆'"), ("12", "兆字节", "ambiguous '兆'"), ("3百万", "", "CJK numerals"),
                            ("15.4万億", "", "two scale characters in a row"), ("15.4萬亿", "", "two scale characters in a row"),
                            ("3万万", "", "two scale characters in a row")]:
            with self.assertRaises(ValueError, msg=vw) as cm:
                ev.parse_value(vw, sw)
            self.assertIn(msg, str(cm.exception), vw)

    def test_percentage_points_are_not_a_numeral(self):
        """「百分点」的「百」不是数词（v2.6d 得 (0.5, False)，第一轮改动曾把它变成报错）。"""
        self.assertEqual(ev.parse_value("0.5百分点", ""), (0.5, False))
        self.assertEqual(ev.parse_value("0.5个百分点", ""), (0.5, False))
        self.assertEqual(ev.parse_value("9.64", "兆円"), (9.64e12, False))   # 兆 + 非 SI 单位照常是 1e12

    def test_english_unchanged(self):
        self.assertEqual(ev.parse_value("881,936", ""), (881_936.0, False))
        self.assertEqual(ev.parse_value("$4.8 million", ""), (4.8e6, False))
        self.assertEqual(ev.parse_value("4.8", "million"), (4.8e6, False))
        self.assertEqual(ev.parse_value("12%", ""), (12.0, True))
        self.assertEqual(ev.parse_value("6832人", ""), (6832.0, False))   # 单位字照旧忽略
        self.assertEqual(ev.parse_value("千分之3.46", ""), (3.46, False))  # 数字前面的字照旧不看（不在本阶段范围）


class TestScaleSupportedCjk(unittest.TestCase):
    def test_glued_to_the_number(self):
        q = ev.norm("関空の通過旅客を含む国際線と国内線の総旅客数は前年比11%増の3409万")
        self.assertEqual(ev.scale_supported("", q, "", "3409万"), "none_needed")
        self.assertEqual(ev.scale_supported("万", q, "", "3409万"), "quote")
        self.assertEqual(ev.scale_supported("万", q, "", "3409"), "quote")
        self.assertEqual(ev.scale_supported("万人", "訪日客は4,140万人だった", "", "4,140"), "quote")
        self.assertEqual(ev.scale_supported("만", "25만 명을 넘어서게 된다", "", "25"), "quote")

    def test_not_supported(self):
        self.assertEqual(ev.scale_supported("万", ev.norm(JP), "", "519"), "")    # 后面还有 548，不能只取 519 万
        self.assertEqual(ev.scale_supported("만", "2만 9000명", "", "2"), "")
        self.assertEqual(ev.scale_supported("万", "2,995万人泊", "", "995"), "")
        self.assertEqual(ev.scale_supported("万", "visitors 315 in total", "(単位:万人)", "315"), "")  # 没有页面级依据
        self.assertEqual(ev.scale_supported("億", "3409万", "", "3409"), "")

    def test_000s_is_a_thousands_header(self):
        ctx = "| September 2025 | | \n| Terminal Passengers (000s) | Sep 2025 | % Change |"
        self.assertEqual(ev.scale_supported("000s", "| Total | 7,348 | 0.8 |", ctx, "7,348"), "page_header")
        self.assertEqual(ev.scale_supported("'000s", "| Total | 7,348 | 0.8 |", "Passengers ('000)", "7,348"), "page_header")
        self.assertEqual(ev.scale_supported("000s", "| Total | 7,348 | 0.8 |", "", "7,348"), "")


class TestVerifyPointCjk(unittest.TestCase):
    def test_jp_movers_level_point_now_kept(self):
        """B1 的主因：表示水平值的 519万548 以前因为「多于一个数字」被丢。"""
        q = "市区町村間移動者数(市区町村間で住所を移し、転入の届出を行った者の数)は519万548人"
        p, why = _vp(JP, quote=q, value_as_written="519万548")
        self.assertEqual(why, "")
        self.assertEqual((p["value"], p["scale_basis"], p["value_as_written"]), (5_190_548.0, "none_needed", "519万548"))
        p, why = _vp(JP, quote="前年に比べ１万7,198人", value_as_written="１万7,198")
        self.assertEqual(p["value"], 17_198.0)
        p, why = _vp(JP, quote=q, value_as_written="519", scale_word="万")
        self.assertIsNone(p)
        self.assertEqual(why, FRAGMENT)
        p, why = _vp(JP, quote=q, value_as_written="519万")
        self.assertIsNone(p)
        self.assertEqual(why, "value_as_written not in quote as a whole number")

    def test_minguo_year_counts_for_the_period_year_check(self):
        kw = dict(quote="115年5月出生數為6832人", value_as_written="6832", period_start="2026-05-01", period_end="2026-05-31")
        p, why = _vp(TW, **kw)
        self.assertEqual((why, p["value"]), ("", 6832.0))
        p, why = _vp(TW.split("\n")[1], **kw)   # 只有不带「民國」的 115年
        self.assertEqual((why, p["value"]), ("", 6832.0))
        p, why = _vp(TW, quote="台灣總人口數2325萬2641人", value_as_written="2325萬2641", period_start="2026-05-31",
                     period_end="2026-05-31")
        self.assertEqual((why, p["value"]), ("", 23_252_641.0))
        p, why = _vp("5月出生數為6832人", **{**kw, "quote": "5月出生數為6832人"})   # 没有任何年份写法：照旧丢，原因文字不变
        self.assertIsNone(p)
        self.assertEqual(why, YEAR_DROP)

    def test_reiwa_needs_the_era_name(self):
        kw = dict(quote="転入者数は35万6920人", value_as_written="35万6920", period_start="2026-03-01", period_end="2026-03-31")
        p, why = _vp("令和8年3月の転入者数は35万6920人", **kw)
        self.assertEqual((why, p["value"]), ("", 356_920.0))
        p, why = _vp("8年3月の転入者数は35万6920人", **kw)   # 不带「令和」的 8年 不认
        self.assertEqual(why, YEAR_DROP)
        p, why = _vp("8年3月の転入者数は35万6920人", url="https://example.org/2026/03", **kw)   # 网址里有年份：照旧通过
        self.assertEqual(why, "")
        p, why = _vp("令和８年３月の転入者数は35万6920人", **kw)   # 全角数字
        self.assertEqual(why, "")

    def test_era_written_period_end_is_still_checked(self):
        """parse_date 现在认纪年写法；period_end 写成「令和8年3月31日」时期间年份检查照样做（按公历 2026 查）。"""
        kw = dict(quote="転入者数は35万6920人", value_as_written="35万6920", period_start="令和8年3月1日", period_end="令和8年3月31日")
        p, why = _vp("令和8年3月の転入者数は35万6920人", **kw)
        self.assertEqual((why, p["period_end"]), ("", "令和8年3月31日"))   # 存的是原文写法，和以前一样不改
        p, why = _vp("3月の転入者数は35万6920人", **kw)
        self.assertEqual(why, YEAR_DROP)
        p, why = _vp("2026年3月の転入者数は35万6920人", **kw)
        self.assertEqual(why, "")


class TestCjkFragment(unittest.TestCase):
    """value_as_written 只是更大的中日韩数字的一截时丢点，不静默读错（审查意见的 3 个例子 + 同一机制的其他写法）。"""
    # fc_jnto_2026_08 缓存页 51b665170aba01d6.txt 里的原句（已存的 v21b_noown 丢弃点 order [3, 2] 的 vw 是 1億3000）
    KK = "地方部における延べ宿泊者数を1億3000万人泊（2025年実績：5873万人泊）とする"

    def _drop(self, text, quote, vw, sw="", why=FRAGMENT):
        p, got = _vp("2025年 " + text, quote=quote, value_as_written=vw, scale_word=sw)
        self.assertIsNone(p, (quote, vw, sw))
        self.assertEqual(got, why, (quote, vw, sw))

    def _keep(self, text, quote, vw, sw, value):
        p, got = _vp("2025年 " + text, quote=quote, value_as_written=vw, scale_word=sw)
        self.assertEqual((got, p and p["value"]), ("", value), (quote, vw, sw))

    def test_review_examples(self):
        self._drop(self.KK, "延べ宿泊者数を1億3000万人泊", "1億3000")            # 后面还有万（v2.6e 第一轮读成 100,003,000）
        self._drop("15.4万亿元", "15.4万亿元", "15.4", "万")                     # 万亿 只填了万（读成 154,000）
        self._drop("1億2345万人", "1億2345万人", "2345", "万")                   # 前面还有 1億（读成 23,450,000）
        self._keep(self.KK, "延べ宿泊者数を1億3000万人泊", "1億3000万", "", 130_000_000.0)
        self._keep("1億2345万人", "1億2345万人", "1億2345万", "", 123_450_000.0)
        self._keep("15.4万亿元", "15.4万亿元", "15.4", "万亿", 1.54e13)

    def test_same_mechanism_other_forms(self):
        self._drop("15.4万亿元", "15.4万亿元", "15.4万")
        self._drop("1億2345万人", "1億2345万人", "2345万")
        self._drop("1억 2345만 명", "1억 2345만 명", "2345만")                   # 韩文段间可以有空格
        self._drop("2만 9000명", "2만 9000명", "2만")
        self._drop("総旅客数は3409万", "総旅客数は3409万", "3409")               # scale_word 空、原文有万（v2.6d 静默得 3409）
        self._drop("519万548人", "519万548人", "548")
        self._drop("前年の4月は61万1千人余り", "前年の4月は61万1千人余り", "61万1")   # 后面还有千（会读成 610,001）
        self._drop("출생아 2만4천275명", "출생아 2만4천275명", "2만4")
        self._drop("装机500兆瓦", "装机500兆瓦", "500", "兆", why=MEGA)
        self._drop("装机500兆瓦", "装机500兆瓦", "500兆", why=MEGA)
        self._keep("跌破10萬 50年後", "跌破10萬 50年後", "10", "萬", 100_000.0)   # 中日文段间不连读（和 _cjk_sum 一致）
        self._keep("3409万 2025年3月", "3409万 2025年3月", "3409万", "", 34_090_000.0)
        self._keep("1億2345万人、うち2345万人", "1億2345万人、うち2345万人", "2345万", "", 23_450_000.0)   # 有一次是完整的数就行
        self._keep("名目GDPは500兆円", "名目GDPは500兆円", "500兆", "", 5e14)

    def test_word_ending_in_scale_char_is_not_a_number(self):
        """하지만 / 다만 / ~지만 里的「만」前面不是数字，不是倍数：后面的数是完整的数（第二轮的规则曾把它们当成一截丢掉）。"""
        self._keep("하지만 24,275명으로 집계됐다", "하지만 24,275명으로 집계됐다", "24,275", "", 24_275.0)
        self._keep("출생아 수는 늘었지만 2만 4275명에 그쳤다", "출생아 수는 늘었지만 2만 4275명에 그쳤다", "2만 4275", "", 24_275.0)
        self._keep("다만 29만 명대를 기록할 전망", "다만 29만 명대를 기록할 전망", "29만", "", 290_000.0)
        self._keep("다만 29만 명대를 기록할 전망", "다만 29만 명대를 기록할 전망", "29", "만", 290_000.0)
        self._drop("3万亿5000亿元", "3万亿5000亿元", "5000亿")   # 前面是「数字 + 万亿」：照样是一截

    def test_scale_supported_uses_the_same_rule(self):
        self.assertEqual(ev.scale_supported("万", "1億2345万人", "", "2345"), "")
        self.assertEqual(ev.scale_supported("万", "15.4万亿元", "", "15.4"), "")
        self.assertEqual(ev.scale_supported("万亿", "15.4万亿元", "", "15.4"), "quote")
        self.assertEqual(ev.scale_supported("万", "315人、1億315万人", "", "315"), "")
        self.assertEqual(ev.scale_supported("兆", "装机500兆瓦", "", "500"), "")
        self.assertEqual(ev.scale_supported("兆", "名目GDPは500兆円", "", "500"), "quote")

    def test_no_cjk_scale_nearby_is_unchanged(self):
        for q, vw, sw in [("Revenue was $4.8 million.", "$4.8", "million"), ("881,936 visitors", "881,936", ""),
                          ("115年5月出生數為6832人", "6832", ""), ("前年に比べ１万7,198人（0.3％）の減少", "0.3%", "")]:
            self.assertEqual(ev.cjk_fragment(ev.norm(q), vw, sw), "", q)
        self.assertEqual(ev.cjk_fragment("abc", "12", ""), "")   # 不在 quote 里：交给 find_value，不在这里报


class TestCjkDates(unittest.TestCase):
    def test_text_dates(self):
        self.assertEqual(ev.text_dates("令和8年3月27日公表 2026年3月27日"), [date(2026, 3, 27)] * 2)
        self.assertEqual(ev.text_dates("2026년 3월 27일 발표"), [date(2026, 3, 27)])
        self.assertEqual(ev.text_dates("民國115年5月20日 / 民国115年5月20日 / 115年5月20日"), [date(2026, 5, 20)] * 3)
        self.assertEqual(ev.text_dates("平成31年4月30日、令和元年5月1日"), [date(2019, 4, 30), date(2019, 5, 1)])
        self.assertEqual(ev.text_dates("２０２６年９月１０日"), [date(2026, 9, 10)])
        self.assertEqual(ev.text_dates("March 5, 2026, then 2026年3月6日, then 2026-03-07"),
                         [date(2026, 3, 5), date(2026, 3, 6), date(2026, 3, 7)])   # 按出现顺序
        self.assertEqual(ev.text_dates("2026年3月の統計、115年5月出生數、8年3月27日、2026年2月30日、2115年5月20日、"
                                       "3000年3月1日、200年3月1日"), [])

    def test_late_dates_see_cjk(self):
        self.assertEqual(ev.late_dates("令和8年9月10日公表、2026년 10월 1일", date(2026, 9, 6), date(2026, 10, 15)),
                         [date(2026, 9, 10), date(2026, 10, 1)])

    def test_parse_date(self):
        self.assertEqual(ev.parse_date("2026年3月27日"), date(2026, 3, 27))
        self.assertEqual(ev.parse_date("2026年3月", end=True), date(2026, 3, 31))
        self.assertEqual(ev.parse_date("2026年", end=True), date(2026, 12, 31))
        self.assertEqual(ev.parse_date("令和8年", end=True), date(2026, 12, 31))
        self.assertEqual(ev.parse_date("令和8年3月27日"), date(2026, 3, 27))
        self.assertEqual(ev.parse_date("2026년 3월 27일"), date(2026, 3, 27))
        self.assertEqual(ev.parse_date("民國115年5月"), date(2026, 5, 1))
        self.assertIsNone(ev.parse_date("115年5月"))       # parse_date 里纪年要带前缀
        self.assertIsNone(ev.parse_date("2026年2月30日"))
        self.assertEqual(ev.parse_date("2025-08", end=True), date(2025, 8, 31))   # 原有写法不变
        self.assertEqual(ev.parse_date("Sep 4, 2025"), date(2025, 9, 4))

    def test_era_years(self):
        self.assertEqual(ev.era_years("115年5月出生數為6832人"), {2026})
        self.assertEqual(ev.era_years("令和8年"), {2026})
        self.assertEqual(ev.era_years("令和元年"), {2019})
        self.assertEqual(ev.era_years("平成30年"), {2018})
        self.assertEqual(ev.era_years("民国114年、民國 113 年"), {2025, 2024})
        self.assertEqual(ev.era_years("１１５年"), {2026})
        for t in ("8年ぶり", "2115年", "1,115年", "115.5年", "2026年", "200年", "099年"):
            self.assertEqual(ev.era_years(t), set(), t)


class TestCjkLeakForms(unittest.TestCase):
    def test_exact_forms_only(self):
        f = ev.leak_forms(356920)
        for x in ("35万6920", "35萬6920", "35만6920", "35万6,920", "35萬6,920", "35만6,920"):
            self.assertIn(x, f)
        for x in ("36万", "35.7万", "35万7000", "35.69万"):
            self.assertNotIn(x, f)
        self.assertIn("2만4,275", ev.leak_forms(24275))
        self.assertIn("718万", ev.leak_forms(7_180_000))
        self.assertIn("1億2345万6789", ev.leak_forms(123_456_789))
        self.assertTrue(all(x.isascii() for x in ev.leak_forms(9999)))
        self.assertTrue(all(x.isascii() for x in ev.leak_forms(4.25)))
        # 原有的英文写法一个不少：非 ASCII 的写法正好是新加的中日韩写法
        for v in (356920, 24275, 7_180_000, 856_467):
            self.assertEqual({x for x in ev.leak_forms(v) if not x.isascii()}, ev._cjk_exact_forms(v))
        self.assertIn("356,920", f)
        self.assertIn("0.36 million", f)

    def test_scan(self):
        pats = ev.leak_patterns([356920, 24275])
        for t in ("転入者数は35万6920人", "35萬6,920人", "출생아 수는 2만4275명", "２万4,275人"):
            self.assertTrue(ev.leak_scan(t, pats), t)
        for t in ("135万6920", "35万69201", "35万6920.5", "約36万人", "2万4276"):
            self.assertFalse(ev.leak_scan(t, pats), t)


if __name__ == "__main__":
    unittest.main()
