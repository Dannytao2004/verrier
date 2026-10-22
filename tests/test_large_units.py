"""v2.11a：大数单位（英文到 quintillion、lakh / crore / milliard、缩写、confirm-only 记号、中日韩千万亿 / 천억 / 亿亿、复合写法）。
倍数只有 evidence.py 里的几张表，各处的正则从表里派生。夹具的 quote 是已存运行的缓存页原句（results/agent/ask_02c360ec、
ask_81334846、fc_mx_exports_2026_09、fc_kr_births_2026_07 的点和丢点）。纯函数测试，不联网、不调模型、不读 data/ 和 results/。"""
import unittest
from datetime import date

from triangulate.agent import evidence as ev
from triangulate.agent.pipeline import verify_point

# 缓存页原句（ask_02c360ec / ask_81334846 的 v1、v2 运行里，这些点被丢过：unknown scale word 'quadrillion' 或 scale word not supported）
EV_Q = ("Exponential View estimates the total tokens processed across all providers at 40 quadrillion tokens per quarter, "
        "i.e., around 5 billion tokens per second, four times Google's traffic.")                       # epoch.ai compute crunch
PYMNTS = "By comparison Google said recently it was processing 1.3 quadrillion tokens per month on all of its services"
MENLO = "Enterprise LLM spend more than doubled in just six months, rising from $3.5B in November 2024 to $8.4B by mid-2025"
GEMINI = "With agentic processing, a 1-hour lecture that would use ~1.08M tokens in static mode might use ~108K tokens"
OPENROUTER = "OpenRouter's State of AI report looks at 100T tokens worth of production data"              # epoch.ai
TUNGUZ = '"We processed over 100t tokens this quarter, up 5x year over year, including a record 50t tokens last month alone."'
A16Z = "OpenRouter now serves over 5+ million developers and routes traffic across 300+ models"
HUXIU = "一项研究将典型推理任务设定为输入10k、输出1.5k tokens,据此估算"
SGNL = "| End-2026 effective capacity (~8Q/day) | 160,000/day | 229,000/day | 286,000/day |"           # ask_81334846
META_DC = "supported by 153 MW of IT power at a capital cost of $5.8 B. In Q1 2027, we project it to rise to 407k H100e"
GREEN = "2026年1-2月全国绿电交易电量484亿千瓦时,同比增长7.6%,国家级智算枢纽绿电占比超80%。"            # ask_02c360ec 68c8d7acfcf41ccd
MX = "los ingresos alcanzaron los 84 millones 176 mil 999 dólares"                                   # fc_mx_exports p81（保留点）
KR = "지난해 인천시 출생아 수는 1만5천242명으로, 1년 전인 2023년보다 11.6% 증가해 전국에서 가장 높은 상승률을 기록했다."  # fc_kr_births p42


def vp(quote, vw, sw="", unit="tokens", page=None, **kw):
    raw = {"name": "x", "value_as_written": vw, "scale_word": sw, "unit": unit, "period_start": "2025-01-01",
           "period_end": "2025-12-31", "quote": quote, **kw}
    return verify_point(raw, ev.norm("2025 " + (page or quote)), date(2026, 10, 22), None, False)


def err(vw, sw=""):
    with unittest.TestCase().assertRaises(ValueError) as cm:
        ev.parse_value(vw, sw)
    return str(cm.exception)


class TestEnglishWords(unittest.TestCase):
    def test_quadrillion_and_quintillion(self):
        for vw, sw, v in [("1.3 quadrillion", "", 1.3e15), ("1.3 quadrillion", "quadrillion", 1.3e15),
                          ("1.3", "quadrillion", 1.3e15), ("1.3 Quadrillions", "", 1.3e15), ("over 3.2 quadrillion", "", 3.2e15),
                          ("2.5 quintillion bytes", "", 2.5e18), ("1.3 quintillion", "", 1.3e18)]:
            self.assertEqual(ev.parse_value(vw, sw), (v, False), (vw, sw))
        self.assertIn("scale conflict", err("40 quadrillion", "trillion"))   # 以前静默得 4e13

    def test_indian_and_british_words(self):
        for vw, v in [("5 lakh", 5e5), ("2.5 lakhs", 2.5e5), ("3 crore", 3e7), ("Rs 2.5 lakh crore", 2.5e12),
                      ("3 thousand crore", 3e10), ("2 milliard", 2e9), ("4 milliards", 4e9)]:
            self.assertEqual(ev.parse_value(vw, ""), (v, False), vw)

    def test_stacked_words(self):
        self.assertEqual(ev.parse_value("3 hundred million", ""), (3e8, False))         # 以前 300
        self.assertEqual(ev.parse_value("3 hundred million", "million"), (3e8, False))  # scale_word 填末词不算冲突
        self.assertEqual(ev.parse_value("4.5 thousand million", ""), (4.5e9, False))
        self.assertEqual(ev.parse_value("4.5 thousand million", "billion"), (4.5e9, False))
        self.assertEqual(ev.parse_value("3 hundred thousand", ""), (3e5, False))
        self.assertEqual(ev.parse_value("5", "ten thousand"), (5e4, False))             # smoke_tdr 丢过一次 unknown
        self.assertEqual(ev.parse_value("5", "Ten-Thousand"), (5e4, False))
        self.assertEqual(ev.parse_value("3 hundred", ""), (300.0, False))               # 照旧
        self.assertIn("scale conflict", err("4.5 thousand million", "thousand"))
        for vw in ("3 million billion", "3 thousand thousand", "3万 million", "3千 million"):
            self.assertIn("two multipliers in a row", err(vw), vw)

    def test_plus_and_hyphen(self):
        self.assertEqual(ev.parse_value("$1.2-billion", ""), (1.2e9, False))
        self.assertEqual(ev.parse_value("5+ million", ""), (5e6, False))
        self.assertEqual(ev.parse_value("a 3-million-person city", ""), (3e6, False))

    def test_reading_path_keeps_the_last_word_rule(self):
        """叠加词只在紧跟数字时整体算：two hundred thousand 配 thousand、number 200 照旧是 2e5（v2.11 审查改的规则）。"""
        q = "Sales reached two hundred thousand pies"
        p, why = vp(q, "two hundred thousand", "thousand", "pies", number=200)
        self.assertEqual((why, p["value"], p["value_check"]), ("", 2e5, "pending"))
        p, why = vp(q, "two hundred thousand", "", "pies", number=200)
        self.assertEqual((why, p["value"]), ("", 2e5))
        p, why = vp(q, "two hundred thousand", "hundred thousand", "pies", number=2)
        self.assertEqual((why, p["value"]), ("", 2e5))
        self.assertEqual(ev.split_multiplier("one hundred million", ""), ("one hundred", 1e6))
        self.assertEqual(ev.split_multiplier("3 hundred million", ""), ("3", 1e8))
        self.assertEqual(ev.split_multiplier("3 hundred million", "million"), ("3 hundred", 1e6))
        self.assertEqual(ev.split_multiplier("four thousand two hundred", ""), ("four thousand two hundred", 1.0))

    def test_saved_quadrillion_points_are_kept(self):
        p, why = vp(EV_Q, "40", "", "quadrillion tokens per quarter")
        self.assertEqual(why, "")
        self.assertEqual((p["value"], p["unit"], p["scale_word"], p["scale_basis"], p["unit_as_written"]),
                         (4e16, "tokens per quarter", "quadrillion", "quote", "quadrillion tokens per quarter"))
        p, why = vp(EV_Q, "40 quadrillion", "quadrillion", "tokens per quarter")
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 4e16, "quote"))
        p, why = vp(PYMNTS, "1.3", "quadrillion", "tokens per month")
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 1.3e15, "quote"))
        p, why = vp(PYMNTS, "1.3 quadrillion", "", "tokens per month")
        self.assertEqual((why, p["value"]), ("", 1.3e15))


class TestScaleTokenErrors(unittest.TestCase):
    def test_recognised_but_unsupported_words_drop(self):
        for vw, msg in [("2 septillion", "unsupported scale word 'septillion'"), ("5 zillion", "unsupported scale word"),
                        ("1 millionth", "ordinal or fraction 'millionth'"), ("2 hundredths", "ordinal or fraction"),
                        ("2,994 Millionen", "not English or CJK"), ("3 Milliarden", "not English or CJK"),
                        ("3,007 Mio", "not English or CJK"), ("2 Mio.", "not English or CJK"), ("60.6 mil millones", "not English or CJK"),
                        ("4 mil", "not English or CJK"), ("3 millones de dólares", "not English or CJK"), ("2垓", "'垓'")]:
            self.assertIn(msg, err(vw), vw)

    def test_look_alikes_are_not_scale_words(self):
        for vw, v in [("3 billionaires", 3.0), ("$3 billionaire", 3.0), ("97.3 quads", 97.3), ("24,500 t", 24500.0),
                      ("4.8 m", 4.8), ("5mm", 5.0), ("12 miles", 12.0)]:
            self.assertEqual(ev.parse_value(vw, ""), (v, False), vw)
        self.assertIn("more than one number", err("3Q 2026"))   # 照旧

    def test_reading_path_raises_too(self):
        with self.assertRaises(ValueError):
            ev.read_reading({"number": 2}, "two septillion", "")
        with self.assertRaises(ValueError):
            ev.split_multiplier("3.5 millones de dólares", "")
        with self.assertRaises(ValueError):
            ev.split_multiplier("3万 million", "")

    def test_spanish_compound_on_the_reading_path_is_unchanged(self):
        """fc_mx_exports 的 15 个西语复合写法点（84 millones 176 mil 999 dólares）：最后一个倍数词后面还有数，照旧交给读数。"""
        for vw in ("84 millones 176 mil 999 dólares", "23 mil 504 unidades adicionales", "277 mil 369"):
            self.assertEqual(ev.split_multiplier(vw, ""), (vw, 1.0), vw)
        p, why = vp(MX, "84 millones 176 mil 999 dólares", "", "USD", number=84176999)
        self.assertEqual((why, p["value"], p["value_check"]), ("", 84176999.0, "pending"))


class TestAbbreviations(unittest.TestCase):
    def test_glued_and_spaced(self):
        for vw, v in [("4.8m", 4.8e6), ("$5bn", 5e9), ("4.8MM", 4.8e6), ("$5MM", 5e6), ("$1.2trn", 1.2e12), ("EUR 5 bln", 5e9),
                      ("$5 bn", 5e9), ("5 mln", 5e6), ("2.44 mn", 2.44e6), ("$1.2 tn", 1.2e12), ("~1.08M", 1.08e6),
                      ("$5.8 B", 5.8e9), ("$55.23 M", 55.23e6), ("$10 K", 1e4)]:
            self.assertAlmostEqual(ev.parse_value(vw, "")[0], v, delta=v * 1e-12, msg=vw)
        self.assertEqual(ev.parse_value("5.8 B", ""), (5.8, False))   # 空格隔开的 B 前面没有货币符号：照旧按面值（BUGS）

    def test_confirm_only_tokens(self):
        self.assertIn("ambiguous 'T'", err("100T"))
        self.assertIn("ambiguous 'Q'", err("8Q"))
        self.assertEqual(ev.parse_value("100T", "trillion"), (1e14, False))
        self.assertEqual(ev.parse_value("100T", "T"), (1e14, False))        # scale_word 填 T：转小写之前看
        self.assertEqual(ev.parse_value("1.6T", "trillion"), (1.6e12, False))
        self.assertEqual(ev.parse_value("8Q", "quadrillion"), (8e15, False))
        self.assertEqual(ev.parse_value("8Q", "Q"), (8e15, False))
        self.assertEqual(ev.parse_value("100t", "trillion"), (1e14, False))
        self.assertEqual(ev.parse_value("3.5t", ""), (3.5, False))           # 小写 t、scale_word 为空：吨
        self.assertEqual(ev.parse_value("3.5t", "million"), (3.5e6, False))  # 和以前一样按 scale_word
        self.assertIn("scale conflict", err("100T", "billion"))
        self.assertIn("unknown scale word", err("3", "t"))                   # scale_word 小写 t 不认
        self.assertEqual(ev.parse_value("3", "MM"), (3e6, False))
        self.assertIn("unknown scale word", err("3", "mm"))
        with self.assertRaises(ValueError):
            ev.split_multiplier("100T", "")
        self.assertEqual(ev.split_multiplier("100T", "trillion"), ("100", 1e12))
        self.assertEqual(ev.split_multiplier("100t", ""), ("100t", 1.0))

    def test_unconfirmed_token_drops_the_point_on_both_paths(self):
        p, why = vp(OPENROUTER, "100T", "", number=100)
        self.assertIsNone(p)
        self.assertIn("ambiguous 'T'", why)
        p, why = vp(OPENROUTER, "100T", "trillion")
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 1e14, "quote"))


class TestScaleSupportedByFactor(unittest.TestCase):
    """缩写配全词以前被丢（已存运行约 141 个）：scale_supported 按倍数比。"""

    def test_run_data_pairs(self):
        for sw, q, vw in [("billion", MENLO, "$3.5B"), ("billion", MENLO, "$8.4B"), ("million", GEMINI, "~1.08M"),
                          ("thousand", GEMINI, "~108K"), ("trillion", OPENROUTER, "100T"), ("trillion", OPENROUTER, "100"),
                          ("trillion", TUNGUZ, "100t"), ("trillion", TUNGUZ, "50t"), ("thousand", HUXIU, "10k"),
                          ("thousand", HUXIU, "1.5k"), ("million", A16Z, "5+ million"), ("quadrillion", SGNL, "8"),
                          ("billion", META_DC, "$5.8 B"), ("billion", META_DC, "5.8"), ("milliard", MENLO, "$3.5B"),
                          ("ten thousand", "3409万", "3409万"), ("T", OPENROUTER, "100")]:
            self.assertEqual(ev.scale_supported(sw, ev.norm(q), "", vw), "quote", (sw, vw))

    def test_still_not_supported(self):
        self.assertEqual(ev.scale_supported("million", "4.8 m", "", "4.8"), "")        # 米
        self.assertEqual(ev.scale_supported("m", "4.8 m", "", "4.8"), "quote")          # 缩写本身的写法照旧
        self.assertEqual(ev.scale_supported("billion", "5.8 B", "", "5.8"), "")        # 没有货币符号
        self.assertEqual(ev.scale_supported("m", "| 4.8 |", "(in millions)", "4.8"), "")   # 表头只认单词
        self.assertEqual(ev.scale_supported("million", "| 4.8 |", "(in millions)", "4.8"), "page_header")
        self.assertEqual(ev.scale_supported("crore", "| 4.8 |", "(in crores)", "4.8"), "page_header")
        self.assertEqual(ev.scale_supported("trillion", ev.norm(OPENROUTER), "", "10"), "")
        self.assertEqual(ev.scale_supported("billion", ev.norm(MENLO), "", "$3.5"), "quote")
        self.assertEqual(ev.scale_supported("million", ev.norm(MENLO), "", "$3.5B"), "")   # 倍数不一样

    def test_trust_change_is_pinned(self):
        """scale_word 填了 trillion 时，quote 里紧跟数字的 t 也算依据（3.5t gvw 会读成 3.5e12，代码解析的数不交模型核对）。"""
        self.assertEqual(ev.scale_supported("trillion", "3.5t gvw", "", "3.5"), "quote")
        self.assertEqual(ev.scale_supported("", "3.5t gvw", "", "3.5t"), "none_needed")

    def test_verify_point_keeps_the_run_data_points(self):
        p, why = vp(MENLO, "$3.5B", "billion", "USD")
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 3.5e9, "quote"))
        p, why = vp(A16Z, "5+ million", "million", "developers")
        self.assertEqual((why, p["value"]), ("", 5e6))
        p, why = vp(TUNGUZ, "100t", "trillion")
        self.assertEqual((why, p["value"]), ("", 1e14))
        p, why = vp(SGNL, "8", "quadrillion", "tokens/day")
        self.assertEqual((why, p["value"]), ("", 8e15))
        p, why = vp(HUXIU, "10k", "thousand")
        self.assertEqual((why, p["value"]), ("", 1e4))


class TestCjkLarge(unittest.TestCase):
    def test_new_table_entries(self):
        for vw, sw, v in [("1.3千万亿", "", 1.3e15), ("1.3千萬億", "", 1.3e15), ("12百万亿", "", 1.2e15), ("1.5十万亿", "", 1.5e13),
                          ("3亿亿", "", 3e16), ("3億億", "", 3e16), ("3천억", "", 3e11), ("3천조", "", 3e15), ("3백조", "", 3e14),
                          ("3십억", "", 3e9), ("3", "천억 원", 3e11), ("1.3", "千万亿", 1.3e15), ("5", "십조", 5e13)]:
            self.assertEqual(ev.parse_value(vw, sw), (v, False), (vw, sw))
        self.assertEqual(ev.split_multiplier("1.3千万亿", ""), ("1.3", 1e15))   # 以前 ('1.3亿', 1e7)
        self.assertEqual(ev.parse_value("3", "만 조합원"), (3e4, False))   # 单位里的韩文词以 조 打头不算倍数字（照旧）

    def test_composite_segments(self):
        for vw, v in [("1조 2천억", 1.2e12), ("27억6천만", 2.76e9), ("1億3千万", 1.3e8), ("3万亿5千亿", 3.5e12),
                      ("3천억 5천만", 300_050_000_000), ("1조 2천억 5000만", 1_200_050_000_000), ("2만4천275", 24_275),
                      ("13만4천433명", 134_433), ("3천만5천", 30_005_000), ("1천72만", 10_720_000)]:
            self.assertEqual(ev.parse_value(vw, ""), (float(v), False), vw)

    def test_still_rejected(self):
        for vw, sw, msg in [("61万1千", "", "CJK numerals"), ("1억2천", "", "CJK numerals"), ("1억2천500", "", "more than one number"),
                            ("2천5백만", "", "more than one number"),
                            ("1千兆", "", "two scale characters"), ("10万兆", "", "two scale characters"),
                            ("1.3千万万", "", "two scale characters"), ("1.3万亿亿", "", "two scale characters"),
                            ("3万亿15千亿", "", "each part must be smaller"), ("5", "亿万", "unknown scale word"),
                            ("3409万", "万万", "unknown scale word"), ("5", "千万亿亿", "unknown scale word"),
                            ("3京", "", "ambiguous '京'"), ("1경 원", "", "ambiguous '경'"), ("500兆瓦", "", "ambiguous '兆'")]:
            with self.assertRaises(ValueError, msg=vw) as cm:
                ev.parse_value(vw, sw)
            self.assertIn(msg, str(cm.exception), vw)
        with self.assertRaises(ValueError):
            ev.split_multiplier("5千亿亿", "")   # 以前 ('5亿', 1e11)

    def test_words_that_are_not_scales(self):
        self.assertEqual(ev.parse_value("3경기", ""), (3.0, False))
        self.assertEqual(ev.parse_value("제10조", ""), (10.0, False))      # 法条编号，以前 1e13
        self.assertEqual(ev.split_multiplier("제10조", ""), ("제10조", 1.0))
        self.assertEqual(ev.parse_value("3조", ""), (3e12, False))
        self.assertEqual(ev.parse_value("100兆宽带", ""), (1e14, False))   # R17 遗留，照旧
        p, why = vp("45,926 16,306 경기 59,771", "16,306", unit="people")
        self.assertEqual((why, p["value"]), ("", 16306.0))

    def test_confirm_only_kyo_and_gyeong(self):
        p, why = vp("営業利益1京円", "1", "京円", "JPY")
        self.assertEqual((why, p["value"], p["scale_basis"]), ("", 1e16, "quote"))
        p, why = vp("총액 1경 원", "1", "경", "KRW")
        self.assertEqual((why, p["value"]), ("", 1e16))
        self.assertEqual(ev.parse_value("1京円", "京円"), (1e16, False))
        self.assertIn("unknown scale word", err("3", "경기"))

    def test_kilo_si_unit_after_a_scale(self):
        """「千 + SI 基本单位字」是单位：万亿千瓦时、484亿千瓦时（以前两条路都丢）。"""
        self.assertEqual(ev.parse_value("9.8", "万亿千瓦时"), (9.8e12, False))
        self.assertEqual(ev.parse_value("9.8万亿千瓦时", ""), (9.8e12, False))
        self.assertEqual(ev.parse_value("2", "亿千瓦"), (2e8, False))
        self.assertIn("unknown scale word", err("5", "万千"))   # 千 后面不是 SI 单位：照旧
        p, why = vp(GREEN, "484", "亿千瓦时", "千瓦时")
        self.assertEqual((why, p["value"], p["unit"], p["scale_basis"]), ("", 4.84e10, "千瓦时", "quote"))
        p, why = vp(GREEN, "484亿", "", "千瓦时")
        self.assertEqual((why, p["value"], p["unit"]), ("", 4.84e10, "千瓦时"))
        self.assertEqual(ev.cjk_fragment(ev.norm(GREEN), "484", "亿千瓦时"), "")
        self.assertEqual(ev.split_multiplier("484亿千瓦时", ""), ("484千瓦时", 1e8))

    def test_verify_point(self):
        q = "谷歌每月处理1.3千万亿个token"
        p, why = vp(q, "1.3", "千万亿")
        self.assertEqual((why, p["value"]), ("", 1.3e15))
        p, why = vp(q, "1.3", "千万")
        self.assertEqual((p, why), (None, "scale word '千万' not supported by quote or table header"))
        p, why = vp(q, "1.3千万")   # 只抄了一截（后面还有亿）：find_value 的边界先挡住
        self.assertEqual((p, why), (None, "value_as_written not in quote as a whole number"))
        p, why = vp("올해 매출은 3천억 원", "3천억", unit="KRW")
        self.assertEqual((why, p["value"]), ("", 3e11))
        p, why = vp("올해 매출은 3천억 원", "3", "천억", "KRW")
        self.assertEqual((why, p["value"]), ("", 3e11))
        p, why = vp("1조 2천억 원", "2천억", unit="KRW")
        self.assertEqual((p, why), (None, "number: value_as_written is only part of a larger CJK number in the quote"))
        p, why = vp("1조 2천억 원", "1조 2천억", unit="KRW")
        self.assertEqual((why, p["value"]), ("", 1.2e12))

    def test_saved_korean_point_is_now_parsed_by_code(self):
        """fc_kr_births think 的 p42（1만5천242명）：以前走抽取员读数（pending），现在代码解析，数不变。"""
        p, why = vp(KR, "1만5천242명", "", "live births", number=15242)
        self.assertEqual((why, p["value"]), ("", 15242.0))
        self.assertNotIn("value_check", p)
        self.assertEqual(ev.cjk_fragment(ev.norm("출생아 2만4천275명"), "2만4", ""),
                         "value_as_written is only part of a larger CJK number in the quote")   # 只抄一截照旧丢


class TestUnitMultipliers(unittest.TestCase):
    def test_new_factors_in_units(self):
        self.assertEqual([f for _, f in ev.unit_multipliers("quadrillion tokens")], [1e15])
        self.assertEqual([f for _, f in ev.unit_multipliers("천억 원")], [1e11])
        self.assertEqual([f for _, f in ev.unit_multipliers("INR crore")], [1e7])
        self.assertEqual([f for _, f in ev.unit_multipliers("thousand million USD")], [1e9])
        self.assertEqual([f for _, f in ev.unit_multipliers("천만 원")], [1e7])   # 以前只认出里面的 만（1e4）
        for u in ("千克", "兆瓦", "조합원", "kg", "TN residents", "trn", "per thousand", "hundred people"):
            self.assertEqual(ev.unit_multipliers(u), [], u)

    def test_unit_multiplier_pairing(self):
        p, why = vp("올해 매출은 3천억 원", "3", "천억", "천억 원")   # 代码乘过 천억：unit 里同一个倍数去掉
        self.assertEqual((why, p["value"], p["unit"], p["unit_as_written"]), ("", 3e11, "원", "천억 원"))
        p, why = vp("올해 매출은 3억 원", "3", "억", "천억 원")
        self.assertIn("unit: unit '천억 원' names a different multiplier", why)
        # 倍数只写在 unit 里：1e11 没有挪到数上用的写法（v2.8r 起就没有，SCALE_FOR_FACTOR），不挪（数和单位照旧成对；
        # 就算有写法，_pair_unit 也只试一个，见 BUGS S29）
        p, why = vp("올해 매출은 3천억 원", "3", "", "천억 원")
        self.assertEqual((why, p["value"], p["unit"], p["scale_word"]), ("", 3.0, "천억 원", ""))

    def test_scale_for_factor(self):
        old = {1e3: "thousand", 1e4: "万", 1e5: "十万", 1e6: "million", 1e7: "千万", 1e8: "亿", 1e9: "billion", 1e12: "trillion"}
        self.assertEqual({f: w for f, w in ev.SCALE_FOR_FACTOR.items() if f in old}, old)   # v2.8r 的写法不变
        produced = {f for w in [*ev._UNIT_CJK, *ev._UNIT_WORDS, *ev.EN_STACKED] for _, f in ev.unit_multipliers(w)}
        # 单位里认得出的倍数都有挪到数上的写法；1e10 / 1e11（百亿、千亿）例外：v2.8r 起认得出、没有写法，照旧不挪
        self.assertLessEqual(produced - {1e10, 1e11}, set(ev.SCALE_FOR_FACTOR))
        self.assertFalse({1e10, 1e11} & set(ev.SCALE_FOR_FACTOR))
        p, why = vp("公司营收3.5千亿元", "3.5", "", "千亿元")
        self.assertEqual((why, p["value"], p["unit"], p["scale_basis"]), ("", 3.5, "千亿元", "none_needed"))


class TestOneTable(unittest.TestCase):
    """各处的正则都从倍数表派生：表里每个写法在每处都认。"""

    def test_every_english_word(self):
        for w, f in ev.EN_SCALES.items():
            for vw in (f"2 {w}", f"2 {w}s", f"2 {w.capitalize()}", f"2-{w}"):
                self.assertEqual(ev.parse_value(vw, ""), (2 * f, False), vw)
            self.assertEqual(ev.parse_value("2", w), (2 * f, False), w)
            self.assertEqual(ev.split_multiplier(f"two {w}", w), ("two", f), w)
            self.assertTrue(ev._HEADER.search(f"(in {w}s)"), w)
        for w, f in ev.EN_STACKED.items():
            self.assertEqual(ev.parse_value(f"2 {w}", ""), (2 * f, False), w)
            self.assertEqual(ev.parse_value("2", w), (2 * f, False), w)
            self.assertEqual([g for _, g in ev.unit_multipliers(f"{w} USD")], [f], w)

    def test_every_abbreviation_and_cjk_word(self):
        for a, f in ev.EN_ABBR.items():
            self.assertEqual(ev.parse_value(f"2{a}", ""), (2 * f, False), a)
            self.assertEqual(ev.parse_value("2", a.upper()), (2 * f, False), a)
            self.assertEqual(ev.split_multiplier(f"2{a}", ""), ("2", f), a)
        for w, f in {**ev.CJK_SCALES, **ev.CJK_WORD_SCALES}.items():
            self.assertEqual(ev.parse_value("2", w), (2 * f, False), w)
            self.assertEqual(ev.parse_value(f"2{w}", ""), (2 * f, False), w)


class TestReviewFixes(unittest.TestCase):
    """v2.11a 审查退回的几条（quote 取自缓存页原句：fc_meta_capex、fc_googl_tokens 的 p97、fc_kr_births_2026_08、
    fc_kr_online_2026_08、fc_kr_births_2026_07、smoke_pizza、ask_02c360ec）。"""

    def test_kilo_si_only_right_after_a_scale_character(self):
        for vw in ("1万2千瓦", "2万5千米ドル", "61万1千米", "5亿3千瓦时"):
            self.assertIn("CJK numerals", err(vw), vw)   # 千 跟在数字后面：照旧报错（以前一度读成 10002 ...）
        self.assertEqual(ev.parse_value("484亿千瓦时", ""), (4.84e10, False))
        self.assertEqual(ev.parse_value("3万千瓦", ""), (3e4, False))
        q = ev.norm("该电站装机容量1万2千瓦")
        self.assertEqual(ev.cjk_fragment(q, "1万2", ""), "value_as_written is only part of a larger CJK number in the quote")
        p, why = vp("该电站装机容量1万2千瓦", "1万2", "", "千瓦")
        self.assertIsNone(p)

    def test_sign_before_the_currency_symbol(self):
        for vw, sw, v in [("-$1.2B", "billion", -1.2e9), ("negative US$5.9 billion", "", -5.9e9), ("minus €3bn", "", -3e9),
                          ("-$182.84 M", "", -182.84e6), ("(-$1.2B)", "", -1.2e9), ("(-1,234)", "", -1234.0),
                          ("negative 2.3%", "", -2.3)]:
            self.assertAlmostEqual(ev.parse_value(vw, sw)[0], v, delta=abs(v) * 1e-12, msg=vw)
        for vw, v in [("($1,234)", -1234.0), ("pre-tax $5bn", 5e9), ("US$-5.9", -5.9), ("$5bn", 5e9)]:
            self.assertEqual(ev.parse_value(vw, "")[0], v, vw)   # 照旧
        q = "Gross margin is seen at 80.16%, capex at $40.97bn and free cash flow at negative $9.14bn."
        p, why = vp(q, "negative $9.14bn", "billion", "USD")
        self.assertEqual((why, p["value"]), ("", -9.14e9))
        p, why = vp("free cash flow falling to negative US$5.9 billion in the quarter", "negative US$5.9 billion", "billion", "USD")
        self.assertEqual((why, p["value"]), ("", -5.9e9))   # fc_googl_tokens test2 的 p97 存的是 +5.9e9

    def test_vague_cjk_numerals_before_a_scale(self):
        """数千万、超千亿元、삼천만：千 / 천 前面不是阿拉伯数字，是数的一部分，照旧切出 万 / 亿 / 만（v2.10i 的结果）。"""
        for vw, out in [("数千万", ("数千", 1e4)), ("近千万", ("近千", 1e4)), ("超千亿元", ("超千元", 1e8)),
                        ("수천억 원", ("수천 원", 1e8)), ("삼천만 명", ("삼천 명", 1e4)), ("三千万人", ("三人", 1e7))]:
            self.assertEqual(ev.split_multiplier(vw, ""), out, vw)
        p, why = vp("超千亿元", "超千亿元", "亿", "CNY", number=1000)
        self.assertEqual((why, p["value"], p["value_check"]), ("", 1e11, "pending"))
        p, why = vp("Talkie/星野数千万美元量级年收入", "数千万", "", "USD", number=3000)
        self.assertEqual((why, p["value"]), ("", 3e7))
        for vw in ("3万 million", "3千 million", "3 million billion"):
            with self.assertRaises(ValueError, msg=vw):
                ev.split_multiplier(vw, "")

    def test_article_number_needs_a_word_boundary(self):
        self.assertEqual(ev.parse_value("결제 1조 원", ""), (1e12, False))
        self.assertEqual(ev.parse_value("실제 3조원", ""), (3e12, False))
        self.assertEqual(ev.split_multiplier("결제 1조 원", ""), ("결제 1 원", 1e12))
        self.assertEqual(ev.parse_value("법 제10조", ""), (10.0, False))
        p, why = vp("법 제10조에 따라", "10조", unit="articles")   # vw 没带「제」：quote 里看
        self.assertEqual((p, why), (None, "number: '제N조' in the quote is an article number, not a multiplier"))
        p, why = vp("결제 1조 원 규모", "1조", unit="KRW")
        self.assertEqual((why, p["value"]), ("", 1e12))

    def test_portuguese_czech_and_mexican_scale_words_drop(self):
        for vw in ("R$ 38 milhões", "R$ 12 bilhões", "1 milhão", "195 mld.", "848 mdd", "3 mmdd", "4 milioni", "2 miliardi",
                   "22 miliard", "3.01 milionë", "5 milionów", "3 miljoen", "5 miljarder", "4 millioner"):
            self.assertIn("not English or CJK", err(vw), vw)
        self.assertEqual(ev.parse_value("300 MDD patients", ""), (300.0, False))   # MDD（抑郁症）：大写不算
        p, why = vp("em pizzarias, que movimentaram mais de R$ 38 milhões", "R$ 38 milhões", "", "BRL")
        self.assertIsNone(p)   # 以前保留成 38 BRL
        self.assertEqual(ev.parse_value("3 mln", ""), (3e6, False))   # 波兰 / 捷克 mln 和英文同义

    def test_tail_segment_of_a_composite_is_a_fragment(self):
        for q, vw, unit in [("3천억 5천만 원", "5천만", "원"), ("총 3千亿5千万元", "5千万", "元"), ("총 3천억 5000만 원", "5000만", "원"),
                            ("지난 8월 온라인으로 물건을 구매한 총액이 22조 4천802억 원으로", "802억", "원"),
                            ("총 3千5百万元", "5百万", "元")]:
            p, why = vp(q, vw, unit=unit)
            self.assertEqual((p, why), (None, "number: value_as_written is only part of a larger CJK number in the quote"), vw)
        p, why = vp("3천억 5천만 원", "3천억 5천만", unit="원")
        self.assertEqual((why, p["value"]), ("", 300_050_000_000))
        p, why = vp("1億2345万人", "1億2345万", unit="人")   # 照旧
        self.assertEqual((why, p["value"]), ("", 123_450_000))

    def test_korean_cheon_inside_a_group(self):
        """韩文一组之内的 N천M：缓存页原句（22조 4천802억、42억8천400만、2만4천275명、2천421명）。"""
        for vw, v in [("22조 4천802억", 22_480_200_000_000), ("17조 8천489억", 17_848_900_000_000), ("42억8천400만", 4_284_000_000),
                      ("2만4천275명", 24_275), ("2만 4천275", 24_275), ("2천421명", 2_421), ("7천478", 7_478), ("1천72만", 10_720_000),
                      ("4천802억", 480_200_000_000), ("3만2천500", 32_500)]:
            self.assertEqual(ev.parse_value(vw, ""), (float(v), False), vw)
        for vw in ("1억2천500", "1억 2천500", "1조2천", "2천5백만", "45천802억"):
            with self.assertRaises(ValueError, msg=vw):
                ev.parse_value(vw, "")   # 억 / 조 后面的尾段（口语常省 만 / 억）、천 后面接 백、两位数 + 천：不猜
        self.assertIn("scale conflict", err("22조 4천802억", "억"))
        q = "옛 통계청인 국가데이터처는 지난 8월 온라인으로 물건을 구매한 총액이 22조 4천802억 원으로 1년 전보다 6.6% 늘었다고"
        p, why = vp(q, "22조 4천802억", "억", "KRW", number=224802)   # fc_kr_online 的已存点：照旧走读数
        self.assertEqual((why, p["value"], p["value_check"]), ("", 2.24802e13, "pending"))
        p, why = vp(q, "22조 4천802억", "", "KRW")
        self.assertEqual((why, p["value"]), ("", 2.24802e13))

    def test_currency_gated_and_indian_abbreviations(self):
        for vw, v in [("Rs 500 cr", 5e9), ("₹500 Cr", 5e9), ("INR 3 crore", 3e7), ("5 lacs", 5e5), ("2.5 lac", 2.5e5),
                      ("$5 bil", 5e9), ("$5bil", 5e9), ("$5mm", 5e6), ("$5 MM", 5e6), ("USD 5mm", 5e6)]:
            self.assertAlmostEqual(ev.parse_value(vw, "")[0], v, delta=v * 1e-12, msg=vw)
        for vw, v in [("5mm", 5.0), ("5 cr", 5.0), ("$500 Cr", 500.0), ("5 bil", 5.0), ("$5BB", 5.0), ("$3MMM", 3.0)]:
            self.assertEqual(ev.parse_value(vw, "")[0], v, vw)   # 没有（对应的）货币符号：毫米、贷方、汽车；BB、MMM 照旧按面值（S32）
        self.assertEqual(ev.scale_supported("million", "raised $5mm in seed", "", "$5mm"), "quote")
        self.assertEqual(ev.scale_supported("crore", "Rs 500 cr in FY26", "", "Rs 500 cr"), "quote")
        self.assertIn("unknown scale word", err("5", "mm"))   # 这些缩写不当 scale_word 认
        for vw in ("5 Cadillac", "two lilacs", "3 shellac"):   # lac 不能从别的词里切出来
            self.assertEqual(ev.split_multiplier(vw, ""), (vw, 1.0), vw)
        self.assertEqual(ev.split_multiplier("five lacs", ""), ("five", 1e5))

    def test_tables_drive_the_regexes(self):
        self.assertEqual(ev._SW_CASED, {"T": 1e12, "Q": 1e15, "MM": 1e6})
        for k in ev.CONFIRM:
            self.assertTrue(ev._CONFIRM_TOKEN.match(k), k)
        self.assertEqual({a: ev._UNIT_MULT_FACTOR[a] for a in ev._UNIT_ABBR}, {"mn": 1e6, "mln": 1e6, "bn": 1e9})
        self.assertEqual(ev._KR_BIG, "만억조")
        self.assertEqual((ev._KR_MAN, ev._KR_KILO), ("만", "천"))
        self.assertIn("unsupported scale character '垓'", err("2垓"))


class TestLeakGuardForCjkParsedNumbers(unittest.TestCase):
    """v2.11a：2만4천275명 以前走读数、被按数值比过；现在代码能读，页面哨兵的写法表里没有。代码解析的中日韩写法按精确值比。"""

    def _page(self, raw, text, leak):
        from types import SimpleNamespace
        from triangulate.agent import pipeline as P

        class LLM:
            def ask(self, *a, **k):
                return {"points": [dict(raw)]}, None
        ctx = SimpleNamespace(leak_patterns=ev.leak_patterns(leak), leak_values=leak, as_of=date(2026, 9, 30), qid="t",
                              llm=LLM(), budget=None)
        page = {"url": "https://example.kr/news/2026-09-23", "status": "live_dated", "page_date": "2026-09-23"}
        out = {"pages": [], "points": [], "dropped_points": []}
        P._process_page(ctx, {"what": "x"}, {"id": "d1"}, 1, page, text, out, False)
        return page, out

    def test_korean_form_of_a_registered_value_voids_the_page(self):
        text = "국가데이터처가 23일 발표한 '7월 인구동향'에 따르면 지난 7월 출생아 수는 2만4천275명으로 작년 동월보다 증가했다."
        raw = {"name": "births", "value_as_written": "2만4천275명", "scale_word": "", "unit": "live births",
               "period_start": "2026-07-01", "period_end": "2026-07-31", "quote": "지난 7월 출생아 수는 2만4천275명으로"}
        page, out = self._page(raw, text, [24275, 170079])
        self.assertEqual(ev.leak_scan(text, ev.leak_patterns([24275, 170079])), [])   # 页面哨兵认不出这个写法
        self.assertEqual((out["points"], page["status_detail"]), ([], "excluded: leak sentinel hit (CJK number parsed by code)"))
        self.assertEqual(page["leak_hits"], ["2만4천275명 (read as 24275)"])
        page, out = self._page(raw, text, [24276])   # 不是登记值：照常
        self.assertEqual(len(out["points"]), 1)

    def test_rounded_cjk_and_english_forms_are_not_compared(self):
        self.assertFalse(ev.leak_point_hit({"value_as_written": "2.4만", "value": 24000.0}, [24275]))   # 四舍五入写法不比（C3）
        self.assertFalse(ev.leak_point_hit({"value_as_written": "3.2 million", "value": 3.2e6}, [3_200_000]))   # 英文写法：照旧只靠页面哨兵
        self.assertTrue(ev.leak_point_hit({"value_as_written": "2만4275", "value": 24275.0}, 24275))
        self.assertTrue(ev.leak_point_hit({"value_as_written": "two million", "value": 2e6, "reading": {"number": 2}}, 2_000_000))
        self.assertFalse(ev.leak_point_hit({"value_as_written": "2만4275", "value": 24275.0}, None))


if __name__ == "__main__":
    unittest.main()
