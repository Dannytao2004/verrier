"""v2.13c：油气行业的单位写法（SPE 惯例 M = 千、MM = 百万）和「SI 前缀不接在自动定义的名词上」。
两套单位库都测：agent 用的 triangulate/agent/qty.py（pint），基线臂用的 triangulate/units.py。
起因：留出测试 4 Equinor 题，agent 一路用 mboe/d，打分时换不到 boe/d；先解析过 boe 时 mboe 又会被 pint 读成 milli-boe（BUGS S75）。"""
import subprocess
import sys
import unittest
from pathlib import Path

from triangulate import units as U
from triangulate.agent import qty as Q

ROOT = Path(__file__).resolve().parents[1]

# (写法, 目标, 1 个写法 = 多少个目标)：两套库都要对
SAME_IN_BOTH = [("mboe/d", "boe/d", 1e3), ("Mboe/d", "boe/d", 1e3), ("kboe/d", "boe/d", 1e3), ("MMboe/d", "boe/d", 1e6),
                ("mmboe", "boe", 1e6), ("Mbbl/d", "bbl/d", 1e3), ("MMbbl", "bbl", 1e6), ("bpd", "bbl/d", 1.0),
                ("MMcf/d", "Mcf/d", 1e3), ("Bcf", "m**3", 28316846.592), ("bcm", "Bcf", 35.31466672148859),
                ("MMBtu", "Btu", 1e6), ("bbl", "gallon", 42.0)]


class TestQtyOilGas(unittest.TestCase):
    def test_industry_multipliers(self):
        for src, dst, f in SAME_IN_BOTH:
            with self.subTest(src=src, dst=dst):
                got, err = Q.convert_factor(src, dst)
                self.assertEqual(err, "")
                self.assertAlmostEqual(got / f, 1.0, places=9)

    def test_barrel_is_the_oil_barrel(self):
        # pint 自带的 barrel 是 31.5 加仑的美制液体桶
        for name in ("barrel", "bbl", "barrels", "oil_barrel"):
            self.assertAlmostEqual(Q.convert_factor(name, "gallon")[0], 42.0, places=9)

    def test_ambiguous_ones_stay_errors(self):
        # mb/d：IEA 用作百万桶/日，SPE 惯例是千桶/日。不猜，换不了就交给修正轮
        self.assertIsNone(Q.convert_factor("mb/d", "bbl/d")[0])
        self.assertIsNone(Q.convert_factor("thousand boe/d", "boe/d")[0])   # 倍数词不进单位（规划 / 抽取的约定）

    def test_display_uses_the_names(self):
        self.assertEqual(f"{Q.parse_unit('mboe/d')[0].units:~}", "mboe / d")
        self.assertEqual(f"{Q.parse_unit('MMcf/d')[0].units:~}", "MMcf / d")


class TestQtyPrefixOnAutoNoun(unittest.TestCase):
    def test_prefixed_auto_noun_is_its_own_noun(self):
        Q.parse_unit("grommetq")   # 自动定义 grommetq
        q, err = Q.parse_unit("mgrommetqs")
        self.assertEqual(err, "")
        self.assertNotIn("milli", str(q.units))
        self.assertIsNone(Q.convert_factor("mgrommetq", "grommetq")[0])   # 不再静默 x 0.001

    def test_same_result_in_either_order(self):
        """新进程里两种顺序（先 all 再 calls / 先 calls 再 all）：calls 都是自己的名词，不是 centi-all。"""
        code = ("import sys; sys.path.insert(0, {root!r}); from triangulate.agent import qty as Q\n"
                "for w in {order!r}: Q.parse_unit(w)\n"
                "print(Q.parse_unit('calls')[0].units, Q.convert_factor('calls', 'all')[0])")
        outs = []
        for order in (["all", "calls"], ["calls", "all"]):
            r = subprocess.run([sys.executable, "-c", code.format(root=str(ROOT), order=order)], capture_output=True,
                               text=True, timeout=120)
            self.assertEqual(r.returncode, 0, r.stderr)
            outs.append(r.stdout.strip())
        self.assertEqual(outs, ["call None", "call None"])

    def test_pint_units_keep_their_prefixes(self):
        self.assertEqual(Q.convert_factor("km", "m")[0], 1000.0)
        self.assertEqual(Q.convert_factor("kWh", "J")[0], 3.6e6)
        self.assertAlmostEqual(Q.convert_factor("mg/day", "g/day")[0], 1e-3)


class TestUnitsOilGas(unittest.TestCase):
    def test_industry_multipliers(self):
        for src, dst, f in SAME_IN_BOTH:
            with self.subTest(src=src, dst=dst):
                self.assertAlmostEqual(U.convert(1.0, U.parse_unit(src), U.parse_unit(dst)) / f, 1.0, places=9)

    def test_spelled_out_boe(self):
        self.assertAlmostEqual(U.convert(1.0, U.parse_unit("barrels of oil equivalent per day"), U.parse_unit("boe/d")), 1.0)

    def test_gas_is_not_a_count(self):
        # 以前 MMcf 是计数名词，MMcf/d 会按 1 换成 boe/d
        with self.assertRaises(U.UnitMismatch):
            U.convert(1.0, U.parse_unit("MMcf/d"), U.parse_unit("boe/d"))


if __name__ == "__main__":
    unittest.main()
