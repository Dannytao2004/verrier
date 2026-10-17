"""agent/qty.py（v2.7 U0）：单位解析、公式单位推导、换算系数。
披萨题（ask_3e7f14f7）的三条路线用字面值重建，不读 results/。
样本换算一律走模块 docstring 的做法：输入先乘 base_factor 换到基本单位，结果除以目标单位的 base_factor（U2 照这个做）。"""
import math
import unittest
from unittest import mock

from triangulate.agent import assumptions as A
from triangulate.agent import compute as C
from triangulate.agent import methods as M
from triangulate.agent import qty as Q
from triangulate.expr import Formula


def unit(text):
    u, err = Q.parse_unit(text)
    if err:
        raise AssertionError(err)
    return u


def base(text):
    f, err = Q.base_factor(text)
    if err:
        raise AssertionError(err)
    return f


def to_target(value_in_base, formula_u, target):
    """公式结果（基本单位）-> 目标单位：先用 convert_factor 查能不能换，再除以目标单位的 base_factor。"""
    _, err = Q.convert_factor(formula_u, target)
    if err:
        raise AssertionError(err)
    return value_in_base / base(target)


class TestParse(unittest.TestCase):
    def assertSameUnit(self, a, b):
        f, err = Q.convert_factor(a, b)
        self.assertEqual(err, "")
        self.assertAlmostEqual(f, 1.0, places=12)
        self.assertEqual(Q.text(unit(a)), Q.text(unit(b)))

    def assertParseError(self, t, want):
        u, err = Q.parse_unit(t)
        self.assertIsNone(u, t)
        self.assertTrue(err.startswith(f"unit {t!r}: "), err)
        self.assertIn(want, err)

    def test_basic_units(self):
        self.assertEqual(Q.text(unit("kg/day")), "kilogram / day")
        self.assertEqual(Q.text(unit("t/day")), "metric_ton / day")
        self.assertEqual(Q.text(unit("USD/year")), "USD / year")
        self.assertEqual(Q.text(unit("kg")), "kilogram")

    def test_per_phrases(self):
        self.assertSameUnit("kg per day", "kg/day")
        self.assertEqual(Q.text(unit("USD per pizza")), "USD / pizza")
        self.assertSameUnit("slices per person per day", "slice/person/day")
        self.assertSameUnit("slices per eater-day", "slice/(eater*day)")
        self.assertSameUnit("kg per person / day", "kg/person/day")
        self.assertSameUnit("kg per capita per year", "kg/person/year")
        self.assertEqual(Q.text(unit("per day")), "1 / day")
        u = unit("births per 1,000 people")
        self.assertAlmostEqual(u.magnitude, 0.001)
        self.assertEqual(Q.text(u), "0.001 birth / person")
        self.assertSameUnit("births per 1,000 people", "birth/(1000 person)")

    def test_hyphen_compound_after_slash_is_one_denominator(self):
        self.assertSameUnit("slices/eater-day", "slices per eater-day")
        self.assertEqual(Q.text(unit("slices/eater-day")), "slice / day / eater")
        self.assertSameUnit("kg/person-day", "kg/(person*day)")
        self.assertEqual(Q.text(unit("person-day")), "day * person")
        # 指数只作用在自己那一项上，不作用到整串
        self.assertSameUnit("kg-m^2", "kg*m^2")
        self.assertSameUnit("person-km^2", "person*km^2")
        self.assertSameUnit("kg-m squared", "kg*m^2")
        self.assertSameUnit("square km-person", "km^2*person")
        self.assertSameUnit("kg/person-km^2", "kg/(person*km^2)")
        self.assertSameUnit("kg-m^-2", "kg/m^2")

    def test_percent_family(self):
        for t in ("percent", "%", "pct", "per cent", "percentage"):
            with self.subTest(t=t):
                self.assertEqual(Q.text(unit(t)), "percent")
                self.assertEqual(Q.base_factor(t), (0.01, ""))
        for t in ("percentage point", "percentage points", "pp"):
            with self.subTest(t=t):
                self.assertEqual(Q.text(unit(t)), "percentage_point")
                self.assertEqual(Q.base_factor(t), (0.01, ""))
        for t in ("bp", "bps", "basis point", "basis points"):
            with self.subTest(t=t):
                self.assertEqual(Q.text(unit(t)), "basis_point")
                self.assertAlmostEqual(Q.base_factor(t)[0], 1e-4)
        self.assertAlmostEqual(Q.convert_factor("bp", "percent")[0], 0.01)
        self.assertAlmostEqual(Q.convert_factor("percent", "1")[0], 0.01)

    def test_dimensionless_words(self):
        for t in ("1", "dimensionless", "share", "ratio", "fraction", "proportion", "factor", "multiplier", "shares"):
            with self.subTest(t=t):
                u = unit(t)
                self.assertTrue(u.dimensionless)
                self.assertEqual(Q.base_factor(u), (1.0, ""))

    def test_currencies_are_separate_dimensions(self):
        for c in Q.CURRENCIES:
            self.assertEqual(Q.text(unit(f"{c}/year")), f"{c} / year")
        f, err = Q.convert_factor("USD/year", "EUR/year")
        self.assertIsNone(f)
        self.assertEqual(err, "USD / year cannot be converted to EUR / year")
        self.assertEqual(Q.text(unit("usd/year")), "USD / year")

    def test_plural_normalisation(self):
        for t in ("people", "persons", "person", "capita", "Persons"):
            self.assertEqual(Q.text(unit(t)), "person", t)
        cases = {"children": "child", "women": "woman", "batteries": "battery", "visits": "visit", "pizzas": "pizza",
                 "slices": "slice", "Visitors": "visitor", "glass": "glass", "bus": "bus", "births": "birth",
                 "boxes": "box", "classes": "class", "matches": "match", "dishes": "dish"}
        for t, want in cases.items():
            self.assertEqual(Q.text(unit(t)), want, t)
        self.assertSameUnit("visitors/day", "visitor/day")

    def test_case_and_acronym_plurals_are_consistent(self):
        self.assertSameUnit("Inches", "inches")                     # 先按小写查 pint，再单数化（不是名词 inche）
        self.assertEqual(Q.text(unit("Inches")), "inch")
        self.assertSameUnit("Centuries", "century")
        self.assertSameUnit("Liters", "liter")
        self.assertSameUnit("Siemens", "siemens")                   # 单数化会得到 siemen；只有按小写查 pint 才对
        for plural, single in (("GPUs", "GPU"), ("SKUs", "SKU"), ("EVs", "EV"), ("USDs", "USD")):
            with self.subTest(t=plural):
                self.assertSameUnit(plural, single)
        self.assertEqual(Q.text(unit("GPUs")), "gpu")
        for t in ("PC", "PCs", "ATM", "ATMs"):                     # 小写后 pint 认识（parsec、atm）：和单数一样报错
            with self.subTest(t=t):
                self.assertParseError(t, f"{t!r} is ambiguous in capitals")

    def test_interpretation_does_not_depend_on_order(self):
        # 第一次解析会自动定义名词；之后再遇到同一个词，解释不能变（全大写的缩写曾因此报 'ambiguous in capitals'）
        for t in ("TEU", "TEU", "people", "PEOPLE", "PEOPLE", "GDP per capita", "GDP per capita"):
            with self.subTest(t=t):
                self.assertNotEqual(unit(t), None)
        self.assertEqual(Q.text(unit("TEU")), "teu")
        self.assertEqual(Q.text(unit("PEOPLE")), "person")
        self.assertEqual(Q.text(unit("GDP per capita")), "gdp / person")
        self.assertEqual(Q.formula_unit("a * b", {"a": "TEU/year", "b": "USD/TEU"})[1], "")
        self.assertEqual(Q.text(Q.formula_unit("a * b", {"a": "TEU/year", "b": "USD/TEU"})[0]), "USD / year")

    def test_count_nouns_are_their_own_dimension(self):
        self.assertEqual(Q.base_factor("pizza"), (1.0, ""))
        f, err = Q.convert_factor("slice/eater/day", "slice/person/day")
        self.assertIsNone(f)
        self.assertEqual(err, "slice / day / eater cannot be converted to slice / day / person")
        self.assertEqual(unit("eater").dimensionality, unit("eaters").dimensionality)

    def test_words_pint_would_misread(self):
        self.assertEqual(Q.text(unit("units")), "unit")           # pint: micro-nit
        self.assertEqual(Q.text(unit("app")), "app")              # pint: atto-point
        self.assertEqual(Q.text(unit("pct")), "percent")          # pint: pico-carat
        self.assertEqual(Q.text(unit("kilos")), "kilogram")       # pint: kilosecond
        self.assertEqual(Q.text(unit("fat")), "fat")              # pint: femto-technical-atmosphere（非公制前缀不认）
        self.assertEqual(Q.convert_factor("USD/quarter", "USD/year"), (4.0, ""))   # pint: quarter = 28 lb
        self.assertEqual(Q.convert_factor("percent per annum", "percent/year"), (1.0, ""))
        self.assertAlmostEqual(Q.convert_factor("USD/decade", "USD/year")[0], 0.1)   # pint: decade 是对数单位
        self.assertAlmostEqual(Q.convert_factor("decades", "year")[0], 10.0)

    def test_same_dimension_misreads_are_errors(self):
        # pint 能读、量纲也对，但系数和常见用法不同：报错并给写法，不悄悄算错
        cases = {"mt/year": "pint reads 'mt' as a milli-tonne (1 kg)", "MT": "write 't' for metric tons",
                 "Mt": "'Mt' is ambiguous", "calories/day": "food calories are kilocalories; write 'kcal'",
                 "Calories": "write 'kcal'", "cal": "write 'kcal'", "calories per serving": "write 'kcal'",
                 "bbl/day": "for oil write 'oil_barrel' (42 gallons)", "barrels": "31.5-gallon barrel"}
        for t, want in cases.items():
            with self.subTest(t=t):
                self.assertParseError(t, want)
        self.assertAlmostEqual(Q.convert_factor("oil barrels/day", "m^3/day")[0], 0.158987, places=6)
        self.assertAlmostEqual(Q.convert_factor("kcal/day", "kJ/day")[0], 4.184)
        self.assertAlmostEqual(Q.convert_factor("megatonne", "t")[0], 1e6)

    def test_dimensionless_words_with_a_factor_are_errors(self):
        # pint 读成无量纲、系数不是 1 的词（角度、常数）：和 1 / share 混用时量纲不报错、系数却错，所以一律报错
        cases = {"degrees": "pint reads it as degree (a dimensionless factor 0.01745)",
                 "grades": "pint reads it as grade (a dimensionless factor 0.01571)",
                 "revolutions": "pint reads it as turn (a dimensionless factor 6.283)", "circle": "pint reads it as turn",
                 "cycle": "pint reads it as turn", "turns": "pint reads it as turn",
                 "per mil": "'mil' is ambiguous: pint reads it as mil (a dimensionless factor 9.817e-05)",
                 "mass": "pint reads it as milliarcsecond", "g e": "pint reads it as electron_g_factor", "pi": "pint reads it as pi",
                 "Degrees": "pint reads it as degree", "students per grade": "'grade' is ambiguous"}
        for t, want in cases.items():
            with self.subTest(t=t):
                self.assertParseError(t, want)
                self.assertTrue(Q.parse_unit(t)[1].endswith("; write another word"))
        self.assertEqual(Q.formula_unit("a * b", {"a": "student/grade", "b": "1"}),
                         (None, "input a: unit 'student/grade': 'grade' is ambiguous: pint reads it as grade "
                                "(a dimensionless factor 0.01571); write another word"))
        # 百分数一族、bit / byte 一族照 pint 的意思用；系数是 1 的 radian 不受影响
        for t, f in (("ppm", 1e-6), ("permille", 1e-3), ("bit", 1.0), ("byte", 8.0), ("kB", 8000.0), ("GB", 8e9), ("radian", 1.0)):
            with self.subTest(t=t):
                self.assertAlmostEqual(base(t), f)
        # base_factor 和 convert_factor 一样拒绝不是正数的系数（直接给 Quantity，绕过解析）
        self.assertEqual(Q.base_factor(Q.UREG.Quantity(1, "electron_g_factor")),
                         (None, "cannot convert electron_g_factor to base units (factor -2.00231930436092)"))

    def test_exponent_guard(self):
        # 链式幂和巨大指数会让 pint 算到挂死（幂塔），解析前就报错；常规的平方、立方、开方照旧
        for t in ("kg**2**3**4**5", "kg**999999999", "kg**inf", "kg^1e308", "m**7"):
            with self.subTest(t=t):
                self.assertParseError(t, "exponents must be numbers between -6 and 6")
        for t, want in (("m**2", "meter ** 2"), ("km^2", "kilometer ** 2"), ("s^-1", "1 / second"), ("kg**0.5", "kilogram ** 0.5")):
            with self.subTest(t=t):
                self.assertEqual(str(unit(t).units), want)

    def test_numbers_only_as_rate_base(self):
        for t in ("2015 USD/year", "1,000 tonnes", "0.5 kg", "1e6 USD", "100 g", "kg * 1000"):
            with self.subTest(t=t):
                self.assertParseError(t, "would multiply the unit; the value is already scaled")
        self.assertParseError("per 1.000 people", "number 1.000 is ambiguous ('.' may be a thousands separator); write 1000 or 1")
        self.assertAlmostEqual(unit("per 0.001 kg").magnitude, 1000.0)          # 0 开头的数不会有千位分隔符
        for t in ("USD/1000 people", "birth/1000 person", "kcal/100 g", "USD/1000 person-day", "USD/1 person",
                  "USD/1000-person", "USD/1-person", "birth/1000-person"):
            with self.subTest(t=t):
                self.assertParseError(t, "right after '/' divides only itself, so the unit after it would multiply; "
                                         "put the base and its unit in parentheses or use 'per'")
        self.assertSameUnit("USD/(1000 person)", "USD per 1000 people")
        self.assertAlmostEqual(unit("kg/1000/day").magnitude, 0.001)
        self.assertAlmostEqual(unit("kcal per 100 g").magnitude, 0.01)
        self.assertAlmostEqual(Q.convert_factor("USD per 1,000 kg", "USD/t")[0], 1.0)
        self.assertAlmostEqual(unit("birth/(1000 person)").magnitude, 0.001)
        self.assertAlmostEqual(unit("1/1000").magnitude, 0.001)
        for t in ("1", "1/day", "1 kg", "m^2", "s^-1", "kg**0.5"):
            with self.subTest(t=t):
                self.assertEqual(unit(t).magnitude, 1.0)

    def test_metric_prefixes_and_multiword_names(self):
        self.assertEqual(Q.base_factor("km"), (1000.0, ""))
        self.assertAlmostEqual(Q.base_factor("mg")[0], 1e-6)
        self.assertEqual(Q.text(unit("kWh")), "kilowatt_hour")
        for t in ("metric ton", "metric tons", "Metric Tons", "metric-ton", "tonnes", "t"):
            self.assertEqual(Q.text(unit(t)), "metric_ton", t)
        self.assertSameUnit("people per square kilometer", "person/km^2")
        self.assertSameUnit("km squared", "km**2")
        self.assertEqual(Q.text(unit("s^-1")), "1 / second")

    def test_errors_are_returned_not_raised(self):
        cases = {
            "kg or lbs": "'or' gives alternatives; pin exactly one unit",
            "pizza mass per day (kg or lbs), with secondary slice/serving count per day": "'or' gives alternatives",
            "% of population": "'of' is not a unit word",
            "recreation visits": "two units side by side",
            "kg/(person day)": "two units side by side",
            "billion USD": "'billion' is a scale word",
            "kg per": "nothing after 'per'",
            "m2": "write exponents with ^",
            "件": "write units in English",
            "KG/day": "'KG' is ambiguous in capitals",
            "tons": "'tons' is ambiguous: pint reads it as a 2000 lb short ton",
            "points": "'points' is ambiguous: pint reads it as a printer's point",
            "shot": "'shot' is ambiguous",
            "degC": "non-multiplicative unit (offset or logarithmic, e.g. degC, dB) is not supported",
            "dB": "non-multiplicative unit",
            "USD/dB": "non-multiplicative unit",
            "per 1e400 people": "scale must be a positive number",
            "year-on-year": "'on' is not a unit word",
            "kg $": "character '$' is not allowed",
            "(kg/day": "unbalanced parentheses",
            "()": "empty parentheses",
            "kg//day": "'/' must follow a unit",
            "/day": "'/' must follow a unit",
        }
        for t, want in cases.items():
            with self.subTest(t=t):
                self.assertParseError(t, want)
        for t in ("", "  ", None, 5):
            self.assertEqual(Q.parse_unit(t), (None, "unit is empty"))


class TestFormulaUnit(unittest.TestCase):
    M1 = {"a": "percent", "b": "slice/person/day", "c": "g/slice", "d": "person", "e": "ratio"}
    M2 = {"a": "USD/year", "b": "share", "c": "USD/pizza", "d": "kg/pizza"}

    def test_pizza_m1_incidence_route(self):
        # (11 percent) * (2.5 slice/person/day) * (77 g/slice) * (2.7e6 person) * 1.15，各项先换到基本单位
        fu, err = Q.formula_unit("a * b * c * d * e", self.M1)
        self.assertEqual(err, "")
        self.assertEqual(Q.text(fu), "gram * percent / day")
        v = dict(zip("abcde", (11, 2.5, 77, 2.7e6, 1.15)))
        b = math.prod(v[k] * base(self.M1[k]) for k in "abcde")
        self.assertAlmostEqual(to_target(b, fu, "t/day"), 65.748375, places=6)

    def test_pizza_m2_revenue_route_per_year_to_per_day(self):
        fu, err = Q.formula_unit("a * b / c * d", self.M2)
        self.assertEqual((Q.text(fu), err), ("kilogram / year", ""))
        self.assertAlmostEqual(Q.convert_factor(fu, "t/day")[0] * 1000 * 365.25, 1.0, places=12)
        v = {"a": 50.1e9, "b": 0.008, "c": 18, "d": 1.0}
        b = v["a"] * base(self.M2["a"]) * v["b"] * base(self.M2["b"]) / (v["c"] * base(self.M2["c"])) * v["d"] * base(self.M2["d"])
        self.assertAlmostEqual(to_target(b, fu, "t/day"), 60.963, places=3)

    def test_sums_need_base_units(self):
        # 'a * (1 - s)'：s 是 11 percent。换到基本单位再代入是 100 * 0.89 kg/day；原始值代入再乘系数会算成 100 * (1 - 11)
        fu, err = Q.formula_unit("a * (1 - s)", {"a": "kg/day", "s": "percent"})
        self.assertEqual((Q.text(fu), err), ("kilogram / day", ""))
        b = 100 * base("kg/day") * (1 - 11 * base("percent"))
        self.assertAlmostEqual(to_target(b, fu, "t/day"), 0.089)
        wrong = 100 * (1 - 11) * Q.convert_factor(fu, "t/day")[0]
        self.assertAlmostEqual(wrong, -1.0)
        # kg + t：量纲相同可以加，结果取第一项的单位；只有换到基本单位才是 1.001 t/day
        fu, err = Q.formula_unit("a + b", {"a": "kg/day", "b": "t/day"})
        self.assertEqual((Q.text(fu), err), ("kilogram / day", ""))
        self.assertAlmostEqual(to_target(1.0 * base("kg/day") + 1.0 * base("t/day"), fu, "t/day"), 1.001)

    def test_missing_per_pizza_gives_readable_error(self):
        fu, err = Q.formula_unit("a * b / c * d", {**self.M2, "d": "kg"})
        self.assertEqual(Q.text(fu), "kilogram * pizza / year")
        self.assertEqual(Q.convert_factor(fu, "t/day"), (None, "kilogram * pizza / year cannot be converted to metric_ton / day"))

    def test_currency_mismatch(self):
        fu, err = Q.formula_unit("a * b / c * d", {**self.M2, "a": "EUR/year"})
        self.assertEqual(err, "")
        k, err = Q.convert_factor(fu, "t/day")
        self.assertIsNone(k)
        self.assertEqual(err, "EUR * kilogram / USD / year cannot be converted to metric_ton / day")

    def test_noun_mismatch_eater_vs_person(self):
        # 原运行的写法：a3 'slices per eater-day'，a1 'people'
        fu, err = Q.formula_unit("a * b * c * d * e", {**self.M1, "b": "slices per eater-day", "d": "people"})
        self.assertEqual(err, "")
        k, err = Q.convert_factor(fu, "t/day")
        self.assertIsNone(k)
        self.assertEqual(err, "gram * percent * person / day / eater cannot be converted to metric_ton / day")

    def test_addition_needs_the_same_dimension(self):
        self.assertEqual(Q.formula_unit("a + b", {"a": "kg/day", "b": "person/day"}),
                         (None, "adding/subtracting kilogram / day and person / day"))
        self.assertEqual(Q.formula_unit("a - b", {"a": "USD/year", "b": "EUR/year"}),
                         (None, "adding/subtracting USD / year and EUR / year"))
        self.assertEqual(Q.formula_unit("min(a, b)", {"a": "kg/day", "b": "person/day"}),
                         (None, "min() of mixed units: kilogram / day and person / day"))
        self.assertEqual(Q.formula_unit("a + 1", {"a": "kg"}), (None, "adding/subtracting kilogram and dimensionless"))

    def test_powers_functions_and_constants(self):
        fu, _ = Q.formula_unit("sqrt(a) * b ** 2", {"a": "km^2", "b": "s"})
        self.assertEqual(Q.text(fu), "kilometer * second ** 2")
        self.assertEqual(Q.text(Q.formula_unit("a ** -1", {"a": "day"})[0]), "1 / day")
        self.assertEqual(Q.text(Q.formula_unit("mean(a, b, c)", {"a": "kg", "b": "t", "c": "lb"})[0]), "kilogram")
        self.assertEqual(Q.text(Q.formula_unit("a / k", {"a": "USD/year", "k": "day/year"})[0]), "USD / day")
        fu, err = Q.formula_unit(Formula("a * b"), {"a": "person", "b": "kg/person/day"})
        self.assertEqual((Q.text(fu), err), ("kilogram / day", ""))

    def test_input_and_formula_errors(self):
        self.assertEqual(Q.formula_unit("a * b", {"a": "kg"}), (None, "input b: no unit"))
        self.assertEqual(Q.formula_unit("a * b", {"a": "kg", "b": "kg or lbs"}),
                         (None, "input b: unit 'kg or lbs': 'or' gives alternatives; pin exactly one unit"))
        u, err = Q.formula_unit("2 * a", {"a": "kg"})
        self.assertIsNone(u)
        self.assertTrue(err.startswith("formula: numeric constant 2 not allowed"), err)
        self.assertEqual(Q.formula_unit(None, {}), (None, "formula: formula must be a non-empty string"))


# 披萨题的字面值（ask_3e7f14f7/web_20261017T072118Z 的数据点和假设；这里不读 results/）
PIZZA_POINTS = {
    "p84": {"id": "p84", "name": "Share of U.S. population consuming pizza on any given day (NHANES 2017-March 2020)",
            "value": 11.0, "unit": "% of population", "period_start": "2017-01-01", "period_end": "2020-03-31", "keep": True},
    "p18": {"id": "p18", "name": "Serving size of one pizza slice (mass per serving)", "value": 77.0, "unit": "grams per slice",
            "period_start": "", "period_end": "", "keep": True},
    "p64": {"id": "p64", "name": "U.S. pizza restaurant industry revenue (2024)", "value": 50100000000.0, "unit": "USD",
            "period_start": "2024-01-01", "period_end": "2024-12-31", "keep": True},
    "p60": {"id": "p60", "name": "US frozen pizza industry sales, 2024", "value": 7000000000.0, "unit": "USD",
            "period_start": "2024-01-01", "period_end": "2024-12-31", "keep": True},
}
PIZZA_ASSUMPTIONS = [
    ("a1", "Chicago city population, 2026", 2700000, 2550000, 2850000, "people"),
    ("a2", "Chicago-vs-US pizza consumption adjustment factor", 1.15, 0.9, 1.5, "ratio"),
    ("a3", "Average slices eaten per pizza-eating day per eater", 2.5, 1.5, 4.0, "slices per eater-day"),
    ("a4", "Chicago share of US pizza restaurant revenue", 0.008, 0.005, 0.012, "share"),
    ("a5", "Average price per whole restaurant pizza", 18, 12, 26, "USD per pizza"),
    ("a6", "Average mass per whole pizza", 1.0, 0.7, 1.4, "kg per pizza"),
    ("a7", "Share of US frozen pizza sales attributable to Chicago", 0.008, 0.005, 0.012, "share"),
    ("a8", "Average price per frozen pizza", 7, 4, 11, "USD per frozen pizza"),
]
PIZZA_TARGET = {"what": "Total pizza consumed per day by people in Chicago",
                "unit": "pizza mass per day (kg or lbs), with secondary slice/serving count per day",
                "period_start": "2026-01-01", "period_end": "2026-12-31", "outcome_type": "continuous"}
# 按新规则给方法的每个输入写的单位（U2 起由裁判写在方法的 input 上）；p84 写 percent，11 由单位换成 0.11
PIZZA_UNITS = {"p84": "percent", "p18": "g/slice", "p64": "USD/year", "p60": "USD/year",
               "a1": "person", "a2": "ratio", "a3": "slice/person/day", "a4": "share", "a5": "USD/pizza", "a6": "kg/pizza",
               "a7": "share", "a8": "USD/pizza"}


def _mc(label, formula, inputs):
    return {"id": label, "method": "formula_mc", "params": {"formula": formula, "inputs": {k: {"id": v} for k, v in inputs.items()}}}


class TestPizzaFixtures(unittest.TestCase):
    """原运行的三条路线：点和假设先按 PIZZA_UNITS 换到基本单位，再交给 compute.run（现有代码，不认单位），
    MC 中位数在基本单位里，除以 t/day 的 base_factor = probes/out/_pizza_tonnes.py 的吨/天。"""

    @classmethod
    def setUpClass(cls):
        f = {k: base(u) for k, u in PIZZA_UNITS.items()}
        cls.points = {k: {**p, "value": p["value"] * f[k]} for k, p in PIZZA_POINTS.items()}
        raw = [{"id": i, "name": n, "value": v * f[i], "low": lo * f[i], "high": hi * f[i], "unit": u, "rationale": "fixture"}
               for i, n, v, lo, hi, u in PIZZA_ASSUMPTIONS]
        cls.av = A.validate(raw, PIZZA_TARGET)
        cls.methods = [_mc("m2", "a * b * c * d * e", {"a": "p84", "b": "a3", "c": "p18", "d": "a1", "e": "a2"}),
                       _mc("m3", "a * b / c * d", {"a": "p64", "b": "a4", "c": "a5", "d": "a6"}),
                       _mc("m4", "a * b / c * d", {"a": "p60", "b": "a7", "c": "a8", "d": "a6"})]
        cls.supply = _mc("supply", "(ra * rs / rp + fa * fs / fp) * w",
                         {"ra": "p64", "rs": "a4", "rp": "a5", "fa": "p60", "fs": "a7", "fp": "a8", "w": "a6"})

    def _tonnes(self, r, method):
        self.assertNotIn("error", r)
        units = {k: PIZZA_UNITS[v["id"]] for k, v in method["params"]["inputs"].items()}
        fu, err = Q.formula_unit(r["params"]["formula"], units)
        self.assertEqual(err, "")
        return {"id": r["id"], "estimate": to_target(r["estimate"], fu, "t/day"), "backtest": [],
                "mc": {"p10": to_target(r["mc"]["p10"], fu, "t/day"), "p90": to_target(r["mc"]["p90"], fu, "t/day")}}

    def test_all_assumptions_kept(self):
        self.assertEqual([a["id"] for a in self.av["kept"]], [f"a{i}" for i in range(1, 9)])
        self.assertEqual(self.av["rejected"], [])
        self.assertAlmostEqual(self.points["p84"]["value"], 0.11)   # 11 % 由单位换算除以 100

    def test_three_routes_in_tonnes_per_day(self):
        res = C.run(self.methods, self.points, PIZZA_TARGET, assumptions=self.av)
        rows = [self._tonnes(r, m) for r, m in zip(res["methods"], self.methods)]
        for row, want in zip(rows, (64.8, 59.9, 22.3)):
            self.assertAlmostEqual(row["estimate"], want, delta=0.05, msg=row["id"])

    def test_supply_route_and_combination(self):
        with mock.patch.object(A, "MAX_PER_METHOD", 5):   # 两个渠道合成一个公式用 5 个假设（U3 的 sum 方法才放宽）
            res = C.run([self.supply, self.methods[0]], self.points, PIZZA_TARGET, assumptions=self.av)
        supply = self._tonnes(res["methods"][0], self.supply)
        demand = self._tonnes(res["methods"][1], self.methods[0])
        self.assertAlmostEqual(supply["estimate"], 86.2, delta=0.05)
        self.assertAlmostEqual(demand["estimate"], 64.8, delta=0.05)
        c = M.combine([demand, supply])
        self.assertAlmostEqual(c["central"], 74.7, delta=0.05)
        self.assertTrue(math.isfinite(c["p10"]) and c["p10"] < c["central"] < c["p90"])


if __name__ == "__main__":
    unittest.main()
