"""L1（v2.8a）：parse_date 里 ISO 和中日韩整串写法仍用原来的正则，其他写法交给 dateparser。改前能读出日期的写法结果不变；
改前不认的几种常见英文写法现在能读；没写年份、相对现在的写法（yesterday、时间戳）和改前一样读不出。不联网、不读 results/。"""
import unittest
from datetime import date

from triangulate.agent import evidence as ev


class TestParseDateViaDateparser(unittest.TestCase):
    def test_old_forms_unchanged(self):
        # 期望值是 v2.7e 的 parse_date 对同一个串算出来的（L1.md 第 3 节）
        cases = {("August 2025", False): date(2025, 8, 1), ("August 2025", True): date(2025, 8, 31),
                 ("Sept. 5, 2025", False): date(2025, 9, 5), ("2026 年 3 月 27 日", False): date(2026, 3, 27),
                 ("令和 8 年 3 月", True): date(2026, 3, 31), ("2026년 10월 1일", False): date(2026, 10, 1),
                 ("２０２６年９月", True): date(2026, 9, 30), ("2026년", True): date(2026, 12, 31),
                 ("2026年09月", False): date(2026, 9, 1), ("2026年09月", True): date(2026, 9, 30),
                 ("2026년 08월", True): date(2026, 8, 31), ("令和8年03月", False): date(2026, 3, 1)}
        for (s, end), d in cases.items():
            self.assertEqual(ev.parse_date(s, end=end), d, s)
        self.assertEqual(ev.text_dates("令和 8 年 3 月 27 日、2026 年 3 月 27 日"), [date(2026, 3, 27)] * 2)

    def test_forms_old_code_missed(self):
        self.assertEqual(ev.parse_date("5 August 2025"), date(2025, 8, 5))
        self.assertEqual(ev.parse_date("August 5th, 2025"), date(2025, 8, 5))
        self.assertEqual(ev.parse_date("August 5, 2025 23:30"), date(2025, 8, 5))
        self.assertEqual(ev.parse_date("year 2025", end=True), date(2025, 12, 31))   # 只写年份：取年末，不取当月

    def test_still_none(self):
        for s in ("March 5", "March", "yesterday", "3 months ago", "1700000000", "Q3 2025", "115年5月", "2026年2月30日"):
            self.assertIsNone(ev.parse_date(s), s)
            self.assertIsNone(ev.parse_date(s, end=True), s)


if __name__ == "__main__":
    unittest.main()
