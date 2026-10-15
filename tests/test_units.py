import unittest

from triangulate.arms import check_naive
from triangulate.data import parse_answer
from triangulate.units import UnitError, UnitMismatch, convert, parse_unit


class TestUnits(unittest.TestCase):
    def test_conversions(self):
        self.assertAlmostEqual(convert(1, parse_unit("mile"), parse_unit("km")), 1.609344)
        self.assertAlmostEqual(convert(2, parse_unit("kWh"), parse_unit("J")), 7.2e6)
        self.assertAlmostEqual(convert(1, parse_unit("ft**2"), parse_unit("cm ** 2")), 929.0304)
        self.assertAlmostEqual(convert(50, parse_unit("%"), parse_unit("")), 0.5)
        self.assertAlmostEqual(convert(3, parse_unit("metric tons"), parse_unit("kg")), 3000)
        self.assertAlmostEqual(convert(1, parse_unit("ton"), parse_unit("pounds")), 2000)

    def test_count_nouns_are_dimensionless(self):
        u = parse_unit("trucks/year")
        self.assertEqual(u.count_nouns, ("trucks",))
        self.assertAlmostEqual(convert(10, u, parse_unit("1/day")), 10 / 365.25)

    def test_mismatch_and_errors(self):
        with self.assertRaises(UnitMismatch):
            convert(1, parse_unit("kg"), parse_unit("m"))
        for bad in ["degree C", "M", "kelvin", "kg/(m"]:
            with self.subTest(bad=bad), self.assertRaises(UnitError):
                parse_unit(bad)
        with self.assertRaises(UnitError):
            parse_unit("trucks", strict=True)

    def test_parse_answer(self):
        self.assertEqual(parse_answer("3.20E+13")[:2], (3.2e13, ""))
        self.assertEqual(parse_answer("1800 L")[:2], (1800.0, "L"))
        self.assertEqual(parse_answer("$75120")[:2], (75120.0, "USD"))
        self.assertIsNone(parse_answer("0.5 degree C")[0])
        self.assertIsNone(parse_answer("0")[0])

    def test_check_naive(self):
        self.assertEqual(check_naive({"estimate": 2, "unit": "km"}, "m")[:2], ("ok", 2000.0))
        self.assertEqual(check_naive({"estimate": 2, "unit": "kg"}, "m")[0], "unit_unreconciled")
        self.assertEqual(check_naive({"estimate": "lots", "unit": ""}, "")[0], "invalid_output")
        self.assertEqual(check_naive({"estimate": 5e9, "unit": "people"}, "")[:2], ("ok", 5e9))


if __name__ == "__main__":
    unittest.main()
