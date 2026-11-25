"""v2.17a（BUGS S24）：数字写法按页面定。德、荷、意、西、葡等语言的页面用「.」分千位、「,」作小数点，只在判成欧式的页面上
换读法；英式页面（以及识别不了语言的页面）读法不变。存档重放见 probes/replay_s24_v217a.py。"""
import builtins
import unittest
from datetime import date
from unittest import mock

from triangulate.agent import evidence as ev
from triangulate.agent import pipeline as P

KBA = ("Im August 2026 wurden insgesamt 212.563 neue Autos in den Verkehr gebracht. Das ist ein Plus von 3,2 Prozent "
       "gegenüber dem Vorjahresmonat, teilte das Kraftfahrt-Bundesamt am 3.9.2026 in Flensburg mit.")
INE = ("El número de viajeros del transporte urbano alcanzó 371,6 millones en agosto, un 4,1% más que el mismo mes "
       "del año anterior, según el Instituto Nacional de Estadística.")
INEGI = ("La población ocupada fue de 59,358,271 personas en el tercer trimestre, con una tasa de desocupación de 2.7%, "
         "informó el instituto nacional de estadística.")
DE_EN_TABLE = ("Die Zahl der Neuzulassungen lag im September bei 1,234,567 Fahrzeugen und 212.563 Elektroautos laut der "
               "Statistik des Bundesamtes.")
DE_DOT_DECIMAL = ("Der effektive Zinssatz für neue Hypotheken lag im August bei 4.60% und im Juli bei 4.45%, "
                  "berichtete die Bank.")
HEATHROW = "Heathrow handled 7,348,000 passengers in September 2025, up 2.7% on the year, the airport said."


def fmt(text, url="https://example.org/x"):
    return ev.page_number_format(ev.norm(text), url)[0]


class TestPageFormat(unittest.TestCase):
    def test_language_and_page_evidence(self):
        self.assertEqual(ev.page_number_format(ev.norm(KBA), "https://www.kba.de/x"), ("eu", "de"))
        self.assertEqual(fmt(INE, "https://www.ine.es/x"), "eu")
        self.assertEqual(fmt(INEGI, "https://www.inegi.org.mx/x"), "en")   # 墨西哥写 1,234.5
        self.assertEqual(fmt(DE_EN_TABLE), "mixed")                        # 德语页面里又有 1,234,567
        self.assertEqual(fmt(DE_DOT_DECIMAL), "mixed")                     # 4.60%：点后两位只能是小数点
        self.assertEqual(fmt(HEATHROW), "en")
        self.assertEqual(fmt("2026年7月の出生数は62,494人で、前年同月比0.3%増加した。"), "en")
        self.assertEqual(fmt(""), "en")

    def test_dates_are_not_english_evidence(self):
        self.assertEqual(fmt("Am 24.11.2026 und am 1.10. meldete das Amt 212.563 Neuzulassungen in ganz Deutschland."), "eu")

    def test_without_the_language_library_nothing_changes(self):
        real = builtins.__import__

        def no_langid(name, *a, **k):
            if name == "py3langid":
                raise ImportError(name)
            return real(name, *a, **k)
        with mock.patch.object(builtins, "__import__", no_langid):
            self.assertEqual(ev.page_number_format(ev.norm(KBA), ""), ("en", ""))


class TestReadings(unittest.TestCase):
    def ok(self, vw, f, want, pct=False):
        self.assertEqual(ev.parse_value(vw, "", f), (want, pct), (vw, f))

    def bad(self, vw, f, why):
        with self.assertRaises(ValueError) as cm:
            ev.parse_value(vw, "", f)
        self.assertIn(why, str(cm.exception), (vw, f))

    def test_european_page(self):
        for vw, v in [("212.563", 212563.0), ("235.528 Einheiten", 235528.0), ("2.994.415", 2994415.0), ("1.234,5", 1234.5),
                      ("3,2 Prozent", 3.2), ("-66.981", -66981.0)]:
            self.ok(vw, "eu", v)
        self.ok("4,1%", "eu", 4.1, True)
        self.bad("3.5", "eu", "must group thousands")               # 欧式页面上的点只能是千分位
        self.bad("1. Januar 2026", "eu", "must group thousands")    # 日期不是数
        self.bad("220,000", "eu", "could also be an English thousands separator")

    def test_mixed_page_reads_only_what_is_unambiguous(self):
        self.bad("212.563", "mixed", "ambiguous separators")
        for vw, v in [("2.994.415", 2994415.0), ("1.234,5", 1234.5), ("0,24", 0.24), ("1,234", 1234.0), ("3.5", 3.5)]:
            self.ok(vw, "mixed", v)

    def test_english_page_unchanged(self):
        self.ok("212.563", "en", 212.563)
        self.ok("1,234,567", "en", 1234567.0)
        self.bad("2.994.415", "en", "ambiguous separators")
        self.assertEqual(ev.parse_value("212.563", ""), ev.parse_value("212.563", "", "en"))   # 默认就是英式

    def test_reading_path_on_a_european_page(self):
        self.assertEqual(ev.read_reading({"low": 1200, "high": 1500}, "1.200-1.500", "", "eu")[1:3], (1200.0, 1500.0))
        with self.assertRaises(ValueError):   # 抽取员按小数读的区间：和代码读的数对不上
            ev.read_reading({"low": 1.2, "high": 1.5}, "1.200-1.500", "", "eu")
        self.assertEqual(ev.read_reading({"number": -0.1}, "minus 0,1", "", "eu")[0], -0.1)
        self.assertEqual(ev.read_reading({"number": 84176999}, "84 millones 176 mil 999", "", "eu")[0], 84176999.0)


class TestVerifyPoint(unittest.TestCase):
    def raw(self, vw, quote, period=("2026-08-01", "2026-08-31")):
        return {"name": "count", "value_as_written": vw, "scale_word": "", "unit": "count", "period_start": period[0],
                "period_end": period[1], "quote": quote}

    def test_german_page_point_reads_thousands_and_records_the_format(self):
        p, why = P.verify_point(self.raw("212.563", "Im August 2026 wurden insgesamt 212.563 neue Autos in den Verkehr gebracht"),
                                ev.norm(KBA), date(2026, 9, 10), None, None, url="https://www.kba.de/x")
        self.assertEqual(why, "")
        self.assertEqual(p["value"], 212563.0)
        self.assertEqual(p["number_format"], {"format": "eu", "lang": "de"})

    def test_english_page_point_is_unchanged(self):
        p, why = P.verify_point(self.raw("7,348,000", "Heathrow handled 7,348,000 passengers in September 2025",
                                         ("2025-09-01", "2025-09-30")),
                                ev.norm(HEATHROW), date(2026, 9, 10), None, None, url="https://heathrow.com/x")
        self.assertEqual((why, p["value"]), ("", 7348000.0))
        self.assertNotIn("number_format", p)


if __name__ == "__main__":
    unittest.main()
