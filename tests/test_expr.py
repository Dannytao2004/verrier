import math
import unittest

from triangulate.expr import DimError, Formula, FormulaError
from triangulate.units import parse_unit


class TestFormulaParsing(unittest.TestCase):
    def test_arithmetic_and_names(self):
        f = Formula("a * b / c + d - e")
        self.assertEqual(f.names, {"a", "b", "c", "d", "e"})
        self.assertAlmostEqual(f.eval({"a": 2, "b": 3, "c": 4, "d": 1, "e": 0.5}), 2.0)

    def test_power_unary_and_caret(self):
        self.assertAlmostEqual(Formula("-(a - b)**2").eval({"a": 1, "b": 4}), -9.0)
        self.assertAlmostEqual(Formula("a ^ 2").eval({"a": 3}), 9.0)
        self.assertAlmostEqual(Formula("a ** -1").eval({"a": 4}), 0.25)
        self.assertAlmostEqual(Formula("a ** 0.5").eval({"a": 9}), 3.0)

    def test_functions_and_literal_one(self):
        self.assertAlmostEqual(Formula("min(a, b) + max(a, b)").eval({"a": 1, "b": 5}), 6.0)
        self.assertAlmostEqual(Formula("sqrt(a)").eval({"a": 16}), 4.0)
        self.assertAlmostEqual(Formula("a * (1 - s)").eval({"a": 10, "s": 0.25}), 7.5)

    def test_rejects_unsafe_or_disallowed(self):
        bad = ["__import__('os').system('x')", "a.b", "a[0]", "lambda: 1", "2 * a", "a ** b", "a ** 10",
               "open(a)", "a if b else c", "a and b", "a == b", "[a, b]", "'x'", "", "min", "a; b",
               "f(a)", "sqrt(a, b)", "max(a, key=b)", "a ** (1/3)", "True * a"]
        for text in bad:
            with self.subTest(text=text):
                with self.assertRaises(FormulaError):
                    Formula(text)

    def test_length_limit(self):
        with self.assertRaises(FormulaError):
            Formula(" + ".join(["a"] * 300))

    def test_undefined_input(self):
        with self.assertRaises(FormulaError):
            Formula("a * b").eval({"a": 1})

    def test_division_by_zero_does_not_raise(self):
        self.assertTrue(math.isinf(Formula("a / b").eval({"a": 1, "b": 0})))
        self.assertTrue(math.isnan(Formula("sqrt(a)").eval({"a": -1})))


class TestVectorEval(unittest.TestCase):
    def test_vector_matches_scalar(self):
        f = Formula("a * b / (c + 1) - min(a, c) + sqrt(b) ** 2")
        env = {"a": [1.0, 2.0, 3.0], "b": [4.0, 5.0, 6.0], "c": 2.0}
        vec = f.eval_vec(env, 3)
        for k in range(3):
            self.assertAlmostEqual(vec[k], f.eval({"a": env["a"][k], "b": env["b"][k], "c": 2.0}))

    def test_constant_formula_broadcasts(self):
        self.assertEqual(Formula("a * b").eval_vec({"a": 2.0, "b": 3.0}, 4), [6.0] * 4)


class TestDims(unittest.TestCase):
    def test_product_and_cancellation(self):
        d = {"rate": parse_unit("trucks/year").dims, "period": parse_unit("year").dims, "speed": parse_unit("km/h").dims}
        self.assertEqual(Formula("rate * period").dims(d), ())
        self.assertEqual(Formula("speed * period").dims(d), parse_unit("m").dims)

    def test_add_mismatch_raises(self):
        with self.assertRaises(DimError):
            Formula("a + b").dims({"a": parse_unit("kg").dims, "b": parse_unit("m").dims})

    def test_sqrt_and_power(self):
        area = parse_unit("m**2").dims
        self.assertEqual(Formula("sqrt(a)").dims({"a": area}), parse_unit("m").dims)
        self.assertEqual(Formula("a ** 0.5").dims({"a": area}), parse_unit("m").dims)


if __name__ == "__main__":
    unittest.main()
