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


def _in_fresh_process(steps):
    """新进程里按顺序跑 qty.convert_factor：steps = [(src, dst), ...]，返回每一步的倍数（换不了是 None）。"""
    code = ("import sys, json; sys.path.insert(0, {root!r}); from triangulate.agent import qty as Q; "
            "print(json.dumps([Q.convert_factor(a, b)[0] for a, b in {steps!r}]))")
    r = subprocess.run([sys.executable, "-c", code.format(root=str(ROOT), steps=steps)], capture_output=True, text=True,
                       timeout=120)
    if r.returncode:
        raise AssertionError(r.stderr)
    import json
    return json.loads(r.stdout)


class TestQtyReviewFindings(unittest.TestCase):
    """v2.13e：v2.13c 审查发现的问题（同一进程里先解析的写法会改掉后面的读法）。"""

    def test_case_variants_do_not_break_pint_units(self):
        # v2.13c 回归：Kg 的单数 kg 被重定义成计数名词，之后整个进程的 kg 都换不了 t
        got = _in_fresh_process([("Kg", "g"), ("kg/day", "t/day"), ("USD/kg", "USD/t"), ("KM", "m"), ("km", "m"),
                                 ("Megatonnes/year", "Mt/year"), ("megatonne", "t"), ("Kcal", "J"), ("kcal", "J")])
        self.assertEqual(got, [1000.0, 0.001, 1000.0, 1000.0, 1000.0, 1.0, 1e6, 4184.0, 4184.0])

    def test_no_prefix_on_case_aliases(self):
        # MBoe 之后的 MMBoe 不是 mega-MBoe；Bbl 之后的 MBbl 不是 mega-Bbl
        self.assertEqual(_in_fresh_process([("MBoe", "boe"), ("MMBoe", "boe"), ("Boe", "boe"), ("Bbl/d", "bbl/d"),
                                            ("MBbl/d", "bbl/d"), ("MMBbl", "bbl"), ("Bbls", "bbl"), ("MBbls", "bbl")]),
                         [1e3, 1e6, 1.0, 1.0, 1e3, 1e6, 1.0, 1e3])

    def test_more_industry_spellings(self):
        got = _in_fresh_process([("MBPD", "bbl/d"), ("mbpd", "bbl/d"), ("Mbpd", "bbl/d"), ("MMbpd", "bbl/d"), ("mscf", "cf"),
                                 ("Mmcf", "cf"), ("Mmbbl", "bbl"), ("Mmboe", "boe"), ("ccf", "cf"), ("USD/ccf", "USD/Mcf"),
                                 ("cfs", "ft**3/s"), ("cfs", "m**3"), ("kcf", "cf")])
        for g, want in zip(got, [1e3, 1e3, 1e3, 1e6, 1e3, 1e6, 1e6, 1e6, 100.0, 10.0, 1.0, None, None]):
            self.assertTrue(g == want if want is None else abs(g / want - 1) < 1e-9, (got, want))

    def test_order_inside_one_string(self):
        # 同一串里先定义的 all 不能让后面的 calls 读成 centi-all
        self.assertEqual(_in_fresh_process([("all/calls", "1"), ("air*pairs", "air**2")]), [None, None])


class TestQtySecondReview(unittest.TestCase):
    """v2.13f：第二轮审查和存档语料扫描查出的误读：都改成报错或读成名词，不再静默乘一个假倍数。"""

    def test_uppercase_acronyms_are_not_prefixed_units(self):
        # API 的小写 api = atto-π、CPI = centi-π、KPI = kilo-π、US = 微秒、MCal = milli-calorie
        got = _in_fresh_process([("API tokens per minute", "tokens per minute"), ("index (CPI)", "index"), ("KPI", "percent"),
                                 ("US dollars per hour", "dollars"), ("MCal", "kcal"), ("api", "1"), ("cpi", "1")])
        self.assertEqual(got, [None] * 7)

    def test_toe_family(self):
        got = _in_fresh_process([("mtoe", "Mtoe"), ("MTOE", "Mtoe"), ("mtoe/year", "TWh/year"), ("ktoe", "toe")])
        self.assertEqual(got[:2], [1.0, 1.0])
        self.assertAlmostEqual(got[2], 11.63, places=9)
        self.assertAlmostEqual(got[3], 1000.0, places=9)

    def test_common_words_are_not_prefix_plus_obscure_unit(self):
        # unit = micro-nit、pct = pico-carat、as = atto-second、TV = tera-volt、KB = kilo-barn、exams = exa-m、kilos = kilo-s
        self.assertEqual(_in_fresh_process([("housing units", "housing unit"), ("pct", "percent"), ("units (as recorded)", "unit"),
                                            ("TV", "V"), ("KB", "kB"), ("exams", "m"), ("kilos", "s")]),
                         [1.0, 1.0, None, None, None, None, None])

    def test_legit_prefixes_untouched(self):
        got = _in_fresh_process([("kWh", "J"), ("MW", "W"), ("GB", "MB"), ("mL", "L"), ("ms", "s"), ("kV", "V"), ("MHz", "Hz"),
                                 ("Mt", "t"), ("kPa", "Pa"), ("kilometers", "m"), ("exabytes", "B"), ("Gigabytes", "GB")])
        for g, want in zip(got, [3.6e6, 1e6, 1e3, 1e-3, 1e-3, 1e3, 1e6, 1e6, 1e3, 1e3, 1e18, 1.0]):
            self.assertAlmostEqual(g / want, 1.0, places=9)

    def test_acronym_plurals_either_order(self):
        self.assertEqual(_in_fresh_process([("VM", "VM"), ("VMs", "VM")]), [1.0, 1.0])
        self.assertEqual(_in_fresh_process([("VMs", "VMs"), ("VM", "VM"), ("VMs", "VM")]), [1.0, 1.0, 1.0])

    def test_unit_is_a_count_not_luminance(self):
        # v2.13e 以前 unit / units 被 pint 读成 micro-nit（亮度），两边都是 units 时换算还是 1，所以要直接看量纲
        for w in ("units", "housing units", "USD per unit"):
            self.assertNotIn("[luminosity]", str(Q.parse_unit(w)[0].dimensionality), w)

    def test_offset_unit_variants_do_not_raise(self):
        for w in ("Kfahrenheit", "KDECADE", "Cdecade"):
            q, err = Q.parse_unit(w)   # 公开函数不抛异常
            self.assertTrue(q is not None or err)


class TestThirdReview(unittest.TestCase):
    """v2.13g：第三轮审查查出的静默错倍数（多数 v2.13c 之前就有）和 v2.13f 拆掉的 dt。"""

    def test_qty_silent_factors_fixed(self):
        got = _in_fresh_process([("USD/mt", "USD/t"), ("MT", "t"), ("Mt", "t"), ("Cal/day", "kcal/day"), ("Calorie", "kcal"),
                                 ("cal", "J"), ("kmph", "km/h"), ("dwt", "t"), ("DWT", "t"), ("dt/ha", "t/ha"), ("mcgs", "ug"),
                                 ("Bbbl", "bbl"), ("Bscf", "Mcf"), ("kcfs", "cfs"), ("TBtu", "Btu")])
        for g, want in zip(got, [1.0, 1.0, 1e6, 1.0, 1.0, 4.184, 1.0, 1.0, 1.0, 0.1, 1.0, 1e9, 1e6, 1e3, 1e12]):
            self.assertAlmostEqual(g / want, 1.0, places=9)
        self.assertAlmostEqual(Q.convert_factor("pennyweight", "g")[0], 1.55517384, places=6)   # pint 的 dwt 按名字还能用
        self.assertEqual(_in_fresh_process([("DT", "kg"), ("NT", "t"), ("US dollars", "dollar")]), [None, None, None])

    def test_units_silent_factors_fixed(self):
        for src, dst, f in (("MM boe/d", "boe/d", 1e6), ("PCT", "%", 1.0), ("Pct", "%", 1.0), ("pp", "%", 1.0), ("bp", "%", 0.01),
                            ("ppb", "1", 1e-9), ("PPM", "ppm", 1.0), ("kBtu", "Btu", 1e3), ("TBtu", "Btu", 1e12), ("Gtoe", "toe", 1e9),
                            ("Bbbl", "bbl", 1e9), ("Bscf", "Mcf", 1e6), ("kcfs", "cfs", 1e3), ("kmph", "kph", 1.0), ("dwt", "t", 1.0),
                            ("Boe./d", "boe/d", 1.0)):
            with self.subTest(src=src):
                self.assertAlmostEqual(U.convert(1.0, U.parse_unit(src), U.parse_unit(dst)) / f, 1.0, places=9)
        for src in ("bps", "MMscfe/d", "MMBO/d", "MMb/d"):   # 有歧义 / 认不出的油气写法：报错
            with self.subTest(src=src), self.assertRaises(U.UnitError):
                U.parse_unit(src)


class TestUnitsOilGas(unittest.TestCase):
    def test_industry_multipliers(self):
        for src, dst, f in SAME_IN_BOTH:
            with self.subTest(src=src, dst=dst):
                self.assertAlmostEqual(U.convert(1.0, U.parse_unit(src), U.parse_unit(dst)) / f, 1.0, places=9)

    def test_spelled_out_boe(self):
        self.assertAlmostEqual(U.convert(1.0, U.parse_unit("barrels of oil equivalent per day"), U.parse_unit("boe/d")), 1.0)

    def test_gas_is_not_a_count(self):
        # 以前 MMcf 是计数名词，MMcf/d 会按 1 换成 boe/d；v2.13e：4 个字符以下的大写写法也一样
        # v2.13f（第二轮审查）：要带 /d：不带的写法和 boe/d 本来就量纲不同，查不查得到都会报错，测不出东西
        for src in ("MMcf/d", "MCF/d", "BCF/d", "TCF/d", "CF/d", "SCF/d", "Scf/d", "Cf/d", "MCf/d", "BCf/d", "TCf/d"):
            with self.subTest(src=src), self.assertRaises(U.UnitMismatch):
                U.convert(1.0, U.parse_unit(src), U.parse_unit("boe/d"))
        with self.assertRaises(U.UnitError):   # 立方英尺当量：气换油的折算各公司不同，不能按 1 换
            U.parse_unit("MMcfe/d")

    def test_unknown_oil_gas_spellings_are_errors(self):
        # v2.13f：长得像油气单位、表里没有的写法报错，不当计数名词按 1 换成 boe（v2.13g：kBtu 收进表里了，换成有歧义的 MBtu）
        for src in ("kcf/d", "Gboe/d", "MBtu", "MMcfe/d"):
            with self.subTest(src=src), self.assertRaises(U.UnitError):
                U.parse_unit(src)

    def test_toe(self):
        for src, f in (("toe", 41.868e9), ("Mtoe", 41.868e15), ("mtoe", 41.868e15), ("MTOE", 41.868e15), ("ktoe", 41.868e12)):
            with self.subTest(src=src):
                self.assertAlmostEqual(U.convert(1.0, U.parse_unit(src), U.parse_unit("J")) / f, 1.0, places=9)

    def test_short_uppercase_spellings(self):
        for src, dst, f in (("MCF", "cf", 1e3), ("BCF", "Mcf", 1e6), ("BPD", "bbl/d", 1.0), ("BBL", "gallon", 42.0),
                            ("Bcm", "m**3", 1e9), ("MBPD", "bbl/d", 1e3), ("MMBPD", "bbl/d", 1e6), ("Ccf", "cf", 100.0),
                            ("cfs", "ft**3/s", 1.0)):
            with self.subTest(src=src):
                self.assertAlmostEqual(U.convert(1.0, U.parse_unit(src), U.parse_unit(dst)) / f, 1.0, places=9)


if __name__ == "__main__":
    unittest.main()
