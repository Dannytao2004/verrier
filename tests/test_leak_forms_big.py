"""v2.12c（S31）：泄漏哨兵的写法表加十亿 / 万亿级写法（billion / trillion / bn / B / tn、亿 / 億 / 억 的取整和小数、万亿 / 兆 / 조、
조 / 억 / 만 的分段写法和韩文「N천M」）。1 亿以下的英文写法表不变。不联网、不调模型。"""
import math
import unittest

from triangulate import forecast
from triangulate.agent import evidence as ev

BY_ID = {q["id"]: q for q in forecast.QUESTIONS}


def hit(text, values, answer=None):
    return bool(ev.leak_scan(text, ev.leak_patterns(values, answer=answer)))


def reg(qid):
    """题库登记的 (leak_values, answer_value)：run.prepare 交给哨兵的就是这两样。"""
    return BY_ID[qid]["leak_values"], BY_ID[qid]["answer_value"]


class TestHeadlineForms(unittest.TestCase):
    def test_test3_headlines(self):
        """复查报告点名的写法：$768.6 billion、37247亿元、$7.9 billion；用题库登记的 leak_values 扫。"""
        us, cn, nz = (reg(i) for i in ("fc_us_retail_2026_06", "fc_cn_retail_2026_04", "fc_nz_exports_2026_03"))
        for t in ("were $768.6 billion, up 0.2 percent", "sales hit $768.6B in June", "US$768.55bn", "768.553 billion dollars"):
            self.assertTrue(hit(t, *us), t)
        for t in ("4月份，社会消费品零售总额37247亿元", "社会消费品零售总额3.72万亿元", "reached 3,724.7 billion yuan",
                  "3.7247 trillion yuan", "37,247億元", "3.7万亿元"):
            self.assertTrue(hit(t, *cn), t)
        for t in ("to $7.9 billion in March 2026", "exports of NZ$7.94bn", "$7,944 million"):
            self.assertTrue(hit(t, *nz), t)

    def test_neighbours_do_not_hit(self):
        """去年同月和前一个月的标题写法不命中（as_of 之前的页面：2025 年 6 月 $720.1 billion、5 月 $763.7 billion、
        2025 年 4 月 37174亿元 / 3,717.4 billion yuan、2025 年 3 月 $7.6 billion）。"""
        us, cn, nz = (reg(i) for i in ("fc_us_retail_2026_06", "fc_cn_retail_2026_04", "fc_nz_exports_2026_03"))
        for t in ("were $720.1 billion", "were $763.7 billion", "$768.5 billion", "$768.65 billion"):
            self.assertFalse(hit(t, *us), t)
        for t in ("4月份，社会消费品零售总额37174亿元", "reached 3,717.4 billion yuan", "41616亿元"):
            self.assertFalse(hit(t, *cn), t)
        for t in ("to $7.6 billion", "$7.95 billion", "7.9 Bq of caesium", "17.9 billion", "7.9 billion7"):
            self.assertFalse(hit(t, *nz), t)

    def test_two_figure_forms_only_for_the_answer(self):
        """v2.12d（审查）：两位有效数字的一位小数（x.x billion / trillion / 万亿 / 亿）只给目标真值登记。新西兰题其他 7 个登记值
        的这种写法撞上 as_of 前的官方页原句（2026-02-20 发布页「imports ... to $6.7 billion」、2025-11-21「exports ... to
        $6.5 billion」、2025-12-19「$7.2 billion」），以前整页作废。三位有效数字的写法照旧给每个登记值。"""
        vals, ans = reg("fc_nz_exports_2026_03")
        for t in ("goods imports rose by $126 million (1.9 percent), to $6.7 billion",
                  "Goods exports rose by $879 million (16 percent), to $6.5 billion, in October 2025",
                  "goods imports rose by $301 million (4.4 percent), to $7.2 billion", "$8.6 billion", "$8.9 billion"):
            self.assertFalse(hit(t, vals, ans), t)
        for t in ("imports were $7.25 billion", "NZ$8.62bn", "$6.656 billion", "to $7.9 billion"):
            self.assertTrue(hit(t, vals, ans), t)
        self.assertFalse(hit("to $7.9 billion", vals))            # 一组值、没说哪个是真值：两位有效数字的都不登记
        self.assertTrue(hit("to $7.9 billion", 7943894499))       # 一个值就是真值
        self.assertFalse(hit("3.7 trillion", 3724700000000, 1))   # 指明了别的真值
        self.assertTrue(hit("3.7 trillion", 3724700000000))
        self.assertTrue(hit("3.7亿", 370000000) and not hit("3.7亿", [370000000, 5], 5))
        self.assertTrue(hit("24.2조원", [24211800000000, 1], 1))  # 1e13 以上一位小数已是三位有效数字

    def test_korean_compound_forms(self):
        """S31 原文：fc_kr_online 登记值 24211800000000 的「24조 2천118억」「24조 2,118억」以前没登记。"""
        kr = BY_ID["fc_kr_online_2026_08"]["leak_values"]
        for t in ("거래액은 24조 2,118억원으로", "24조2118억원", "24조 2천118억원", "24조2천118억 원", "24.2조원", "242,118억원",
                  "24兆2118億円", "24.21万亿韩元"):
            self.assertTrue(hit(t, kr), t)
        for t in ("22조 4,802억원", "24조 2,119억원", "124조 2,118억원"):
            self.assertFalse(hit(t, kr), t)
        self.assertTrue(hit("출생아 수는 2만4천275명", 24275))
        self.assertTrue(hit("2만 4,275명", 24275))
        self.assertFalse(hit("2만4천276명", 24275))

    def test_abbreviation_guard(self):
        pats = ev.leak_patterns(7943894499)
        for f in ("7.9B", "7.9 B", "7.94bn", "7.944 bn"):
            p = next(p for p in pats if p.pattern.startswith(r"(?<![\d.,])" + f.replace(".", r"\.").replace(" ", r"\ ")))
            self.assertTrue(p.pattern.endswith("(?![A-Za-z])"), f)
        self.assertFalse(hit("7.9 Bq", 7943894499))
        self.assertTrue(hit("7.9 B.", 7943894499))
        p = next(p for p in ev.leak_patterns(3724700000000) if r"3\.72\ trillion" in p.pattern)
        self.assertFalse(p.pattern.endswith("(?![A-Za-z])"))   # 单词写法同 million：后面不加限制


class TestTablesBelowOneHundredMillion(unittest.TestCase):
    def test_english_table_unchanged_below_1e8(self):
        """1 亿以下：英文写法里没有 billion / trillion / bn / B / tn，非 ASCII 的写法正好是 _cjk_exact_forms。"""
        for v in (1946, 24275, 356920, 856467, 2440000, 7268445, 31686803, 99_999_999, 4.25, 1042652.3):
            forms = ev.leak_forms(v)
            self.assertFalse([f for f in forms if f.isascii() and f.endswith(ev._ABBREV[2:] + ("billion", "trillion"))], v)
            if v == int(v) and v >= 10_000:
                self.assertEqual({f for f in forms if not f.isascii()}, ev._cjk_exact_forms(int(v)), v)

    def test_24275_pinned(self):
        self.assertEqual(ev.leak_forms(24275), sorted([
            "24,275", "24 275", "24.275", "24275", "24,300", "24,000", "24 thousand", "24k", "24 k", "24.3 thousand", "24.3k",
            "24.3 k", "24.27 thousand", "24.27k", "24.27 k", "2万4275", "2万4,275", "2萬4275", "2萬4,275", "2만4275", "2만4,275",
            "2만 4275", "2만 4,275", "2만4천275", "2만 4천275"]))


class TestNumbers(unittest.TestCase):
    def test_readings(self):
        nz, cn = reg("fc_nz_exports_2026_03"), reg("fc_cn_retail_2026_04")
        self.assertTrue(ev.leak_number_hit(7.9e9, *nz))       # seven point nine billion
        self.assertTrue(ev.leak_number_hit(7.944e9, *nz))
        self.assertFalse(ev.leak_number_hit(7.6e9, *nz))
        self.assertFalse(ev.leak_number_hit(7.2e9, *nz))      # 7,245,909,283 的两位有效数字（v2.12d：只给真值）
        self.assertTrue(ev.leak_number_hit(7.25e9, *nz))
        self.assertFalse(ev.leak_number_hit(7.9e9, nz[0]))    # 没说哪个是真值
        self.assertTrue(ev.leak_number_hit(3.72e12, *cn))      # 三点七二万亿
        self.assertTrue(ev.leak_number_hit(3.7e12, *cn))
        self.assertTrue(ev.leak_number_hit(37247e8, *cn))
        self.assertFalse(ev.leak_number_hit(3.71e12, *cn))
        for v in (24275, 356920, 7268445):   # 1 亿以下不变
            self.assertTrue(all(math.isfinite(x) for x in ev.leak_numbers(v)))
        self.assertEqual(ev.leak_numbers(356920), {356920.0, 356900.0, 357000.0, round(356.92, 1) * 1e3,
                                                   round(356.92, 2) * 1e3, round(0.35692, 3) * 1e6, round(0.35692, 2) * 1e6})

    def test_reading_point_voids_page(self):
        p = {"reading": True, "value": 7.9e9, "value_as_written": "seven point nine billion"}
        self.assertTrue(ev.leak_point_hit(p, *reg("fc_nz_exports_2026_03")))
        self.assertFalse(ev.leak_point_hit({**p, "value": 7.2e9}, *reg("fc_nz_exports_2026_03")))


if __name__ == "__main__":
    unittest.main()
