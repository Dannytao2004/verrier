"""结构化基线的重试反馈（BUGS.md G1、N38、N39、N41）和展示集冻结的 engine（showcase_engine.py）。离线，不调模型。

数字规则不变：量纲规则、常数规则、mc.aggregate 都没改，改的只是发回模型的报错文字和「MC 之后才判无效」的路径也进 errors。
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from triangulate import arms, showcase, showcase_engine
from triangulate.engine import _unit_numbers, evaluate_structured
from triangulate.report import _clean

ROOT = Path(__file__).resolve().parents[1]
SAVED = sorted((ROOT / "results" / "forecast" / "raw" / "structured").glob("*.json"))
FROZEN_AT = "f1ac7b0"   # showcase1 打分时的 engine.py


def _inp(name, lo, hi, unit="", value=None):
    return {"name": name, "description": name, "value": value if value is not None else (lo * hi) ** 0.5,
            "low": lo, "high": hi, "unit": unit, "provenance": {"type": "assumption", "rationale": "test"}}


def _spec(inputs, *formulas):
    return {"target": {"definition": "t", "unit": ""}, "inputs": inputs,
            "paths": [{"id": f"p{k + 1}", "method": m, "formula": f, "output_unit": "visits"}
                      for k, (m, f) in enumerate(zip(("top_down", "bottom_up", "proxy"), formulas))]}


# NHS 9 月急诊（fc_nhs_ae_2026_09 第 1 次尝试的 p1）的简化版：人口 × 每人每年次数 × 9 月份额 = 每年的量，目标是 9 月总数
NHS = [_inp("england_population", 5.75e7, 5.75e7, "people"),
       _inp("annual_attendances_per_person", 0.42, 0.5, "attendances/person/year"),
       _inp("september_share_of_annual", 0.08, 0.087),
       _inp("days_per_year", 365, 365, "days/year")]


def _path_errors(st, pid):
    return [e for e in st["errors"] if e.startswith(f"path {pid}:")]


class TestDimensionMessage(unittest.TestCase):
    """(a) 量纲不符的报错用白话说清楚公式给的是什么、目标要的是什么，括号里留 SI 写法。"""

    def test_rate_per_time_says_how_to_fix(self):
        st = evaluate_structured(_spec(NHS, "england_population * annual_attendances_per_person * september_share_of_annual",
                                       "england_population * annual_attendances_per_person * september_share_of_annual * days_per_year",
                                       "england_population * september_share_of_annual"), "", "t_a1", strict_target=False, n=200)
        (m1,), (m2,) = _path_errors(st, "p1"), _path_errors(st, "p2")
        self.assertTrue(m1.startswith("path p1: dimension mismatch: the formula gives count per time (s**-1), but the "
                                      "target needs a pure number, a count or a share (dimensionless)."), m1)
        self.assertIn("annual_attendances_per_person ('attendances/person/year')", m1)   # 时间单位从哪个输入来
        self.assertIn("period_length = 1 with unit 'year'", m1)
        self.assertIn("'days/year', has no time unit", m1)
        # NHS 第 2 次尝试乘的就是 days/year（无量纲）：还是同一个错，报错文字也一样
        self.assertEqual(m1.replace("path p1:", ""), m2.replace("path p2:", ""))
        self.assertEqual(st["result"]["n_valid_paths"], 1)

    def test_following_the_advice_makes_the_path_valid(self):
        inputs = NHS + [_inp("period_length", 1, 1, "year")]
        st = evaluate_structured(_spec(inputs, "england_population * annual_attendances_per_person * period_length * september_share_of_annual",
                                       "england_population * september_share_of_annual",
                                       "england_population * september_share_of_annual"), "", "t_a2", strict_target=False, n=200)
        self.assertEqual(st["errors"], [])
        p1 = st["paths"][0]
        self.assertAlmostEqual(p1["median"], 5.75e7 * (0.42 * 0.5) ** 0.5 * (0.08 * 0.087) ** 0.5, delta=2e4)

    def test_other_mismatch_plain_words_without_time_hint(self):
        spec = {"target": {"definition": "d", "unit": "km"},
                "inputs": [_inp("speed", 50, 100, "km/h"), _inp("hours", 2, 2, "h"), _inp("mass", 1, 2, "kg")],
                "paths": [{"id": "p1", "method": "top_down", "formula": "speed * hours"},
                          {"id": "p2", "method": "bottom_up", "formula": "mass * speed"},
                          {"id": "p3", "method": "proxy", "formula": "speed * hours * hours"}]}
        st = evaluate_structured(spec, "km", "t_a3", n=200)
        self.assertEqual(_path_errors(st, "p2"), ["path p2: dimension mismatch: the formula gives mass * length per time "
                                                  "(kg*m*s**-1), but the target needs length (m)"])
        self.assertEqual(_path_errors(st, "p3"), ["path p3: dimension mismatch: the formula gives length * time (m*s), "
                                                  "but the target needs length (m)"])


class TestConstantDoesNotHideOtherProblems(unittest.TestCase):
    """(b) 公式里有数字常数时，同一条路径的量纲错误、未定义输入照样报出来；路径仍然无效（常数规则不变）。"""

    def test_constant_and_dimension_mismatch_reported_together(self):
        # 日本迁移（fc_jp_movers_2026_08 第 1 次尝试的 p1）的写法
        inputs = [_inp("japan_population", 1.2e8, 1.26e8, "people"),
                  _inp("annual_movers_per_1000", 30, 50, "people per 1000 people per year"),
                  _inp("august_share_of_annual", 0.08, 0.12)]
        st = evaluate_structured(_spec(inputs, "japan_population * (annual_movers_per_1000 / 1000) * august_share_of_annual",
                                       "japan_population * august_share_of_annual", "japan_population * august_share_of_annual"),
                                 "", "t_b1", strict_target=False, n=200)
        e = _path_errors(st, "p1")
        self.assertEqual(len(e), 2)
        self.assertIn("numeric constant 1000 not allowed", e[0])
        self.assertIn("dimension mismatch: the formula gives count per time (s**-1)", e[1])
        p1 = st["paths"][0]
        self.assertEqual((p1["status"], p1["uses"]), ("invalid", ["annual_movers_per_1000", "august_share_of_annual",
                                                                  "japan_population"]))
        self.assertEqual(st["result"]["n_valid_paths"], 2)

    def test_constant_and_undefined_input(self):
        st = evaluate_structured(_spec([_inp("a", 1, 2)], "a * ghost * 1000", "a", "a"), "", "t_b2", strict_target=False, n=200)
        e = _path_errors(st, "p1")
        self.assertIn("path p1: uses undefined input 'ghost'", e)
        self.assertTrue(any("numeric constant 1000" in x for x in e))
        self.assertEqual(next(i for i in st["inputs"] if i["name"] == "ghost")["status"], "missing")

    def test_second_formula_error_after_a_constant(self):
        st = evaluate_structured(_spec([_inp("a", 1, 2)], "a * 1000 + a.b", "a", "a"), "", "t_b3", strict_target=False, n=200)
        e = _path_errors(st, "p1")
        self.assertEqual(len(e), 2)
        self.assertIn("numeric constant 1000", e[0])
        self.assertIn("Attribute not allowed", e[1])

    def test_constant_only_path_is_still_invalid(self):
        st = evaluate_structured(_spec([_inp("a", 1, 2)], "a * 2", "a", "a"), "", "t_b4", strict_target=False, n=200)
        self.assertEqual([p["status"] for p in st["paths"]], ["invalid", "valid", "valid"])
        self.assertEqual(_path_errors(st, "p1"), ["path p1: formula: numeric constant 2 not allowed (only 1 and exponents); "
                                                  "make it a named input"])


class TestPostMonteCarloInvalid(unittest.TestCase):
    """(c) 量纲对、但 MC 之后中位数不是正有限数的路径也进 errors，arms._run 因此会重试一次。"""

    BAD = _spec([_inp("a", 1, 2), _inp("b", 10, 20)], "a", "a * b", "a - b")

    def test_listed_in_errors(self):
        st = evaluate_structured(self.BAD, "", "t_c1", strict_target=False, n=200)
        self.assertEqual(st["paths"][2]["status"], "invalid")
        self.assertEqual(st["errors"], ["path p3: path median is not a positive finite number"])
        self.assertEqual(st["result"]["n_valid_paths"], 2)

    def test_triggers_a_retry(self):
        good = _spec([_inp("a", 1, 2), _inp("b", 10, 20)], "a", "a * b", "b - a")

        class FakeLLM:
            def __init__(self, replies):
                self.replies, self.seen = replies, []

            def json_call(self, msgs, **kw):
                self.seen.append(msgs)
                r = self.replies[kw["attempt"] - 1]
                return r, json.dumps(r), None

        llm = FakeLLM([self.BAD, good])
        rec = arms.run_structured(llm, {"id": "t_c2", "question": "q", "answer_unit": "", "strict": False})
        self.assertEqual(rec["final_attempt"], 2)
        self.assertEqual(rec["attempts"][0]["problems"], ["path p3: path median is not a positive finite number"])
        self.assertIn("path p3: path median is not a positive finite number", llm.seen[1][-1]["content"])
        self.assertEqual(rec["attempts"][1]["problems"], [])


class TestScaledUnitNote(unittest.TestCase):
    """(d) N38：单位串里的数字（per 1000 people）代码已经换算；有错的路径用到这种输入时，反馈里说明不要再除一次。"""

    TW = [_inp("taiwan_population", 2.34e7, 2.34e7, "people"),
          _inp("annual_birth_rate", 5.5, 5.5, "births per 1000 people per year"),
          _inp("period_length", 1, 1, "year"), _inp("september_share", 0.083, 0.083),
          _inp("annual_births", 1.1e5, 1.5e5, "births")]

    def test_unit_numbers(self):
        self.assertEqual(_unit_numbers("births per 1000 people per year"), ["1000"])
        self.assertEqual(_unit_numbers("people per 1000 people per month"), ["1000"])
        self.assertEqual(_unit_numbers("1e3 people"), ["1e3"])
        for u in ("per year", "m**2", "km^2", "m2", "births/person/year", "", None):
            self.assertEqual(_unit_numbers(u), [], u)

    def test_note_when_a_path_using_it_is_invalid(self):
        st = evaluate_structured(_spec(self.TW, "taiwan_population * annual_birth_rate * september_share",
                                       "annual_births * september_share", "annual_births * september_share"),
                                 "", "t_d1", strict_target=False, n=200)
        note = [e for e in st["errors"] if e.startswith("input 'annual_birth_rate':")]
        self.assertEqual(note, ["input 'annual_birth_rate': its unit 'births per 1000 people per year' contains the number "
                                "1000, which Python already applies when converting units, so a formula must not divide or "
                                "multiply by 1000 again (neither as a number nor as an input equal to 1000)"])
        self.assertEqual(st["inputs"][1]["status"], "assumption")   # 只是提醒：输入本身仍可用

    def test_no_note_and_no_error_when_paths_are_valid(self):
        st = evaluate_structured(_spec(self.TW, "taiwan_population * annual_birth_rate * period_length * september_share",
                                       "annual_births * september_share", "annual_births * september_share"),
                                 "", "t_d2", strict_target=False, n=200)
        self.assertEqual(st["errors"], [])
        # 单位里的 1/1000 已经乘过：2.34e7 × 5.5e-3 × 0.083 ≈ 10682，不需要公式再除 1000
        self.assertAlmostEqual(st["paths"][0]["median"], 2.34e7 * 5.5e-3 * 0.083, delta=1)


def _old_engine():
    """FROZEN_AT 的 engine.py（git show）作为临时模块载入；拿不到 git 历史时返回 None。"""
    try:
        src = subprocess.run(["git", "show", f"{FROZEN_AT}:triangulate/engine.py"], cwd=ROOT, capture_output=True,
                             check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    path = Path(tempfile.mkdtemp()) / "_engine_frozen_at.py"
    path.write_bytes(src)
    spec = importlib.util.spec_from_file_location("triangulate._engine_frozen_at", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _dump(st):
    return json.dumps(_clean(st), sort_keys=True, default=str)


class TestFrozenShowcaseEngine(unittest.TestCase):
    """展示集每次打分都重算结构化臂：必须继续用 showcase1 打分时的 engine。"""

    @classmethod
    def setUpClass(cls):
        cls.old = _old_engine()

    def test_showcase_uses_the_frozen_engine(self):
        self.assertIs(showcase.evaluate_structured, showcase_engine.evaluate_structured)

    def test_frozen_source_is_the_old_engine(self):
        if self.old is None:
            self.skipTest("git history not available")
        old = Path(self.old.__file__).read_bytes().replace(b"\r\n", b"\n").decode("utf-8")
        frozen = Path(showcase_engine.__file__).read_bytes().replace(b"\r\n", b"\n").decode("utf-8")
        head, body = frozen.split("\n", 2)[:2], frozen.split("\n", 2)[2]
        self.assertTrue(all(x.startswith("#") for x in head))
        self.assertEqual(body, old)

    def test_same_state_as_old_engine_on_saved_replies(self):
        if self.old is None:
            self.skipTest("git history not available")
        self.assertTrue(SAVED)
        for f in SAVED:
            raw = json.loads(f.read_text(encoding="utf-8"))
            for a in raw["attempts"]:
                args = (a["reply"], raw["target_unit"], raw["qid"])
                self.assertEqual(_dump(showcase_engine.evaluate_structured(*args, strict_target=False)),
                                 _dump(self.old.evaluate_structured(*args, strict_target=False)), (raw["qid"], a["attempt"]))

    def test_reproduces_committed_showcase_structured_arm(self):
        d = json.loads((ROOT / "results" / "showcase" / "summary.json").read_text(encoding="utf-8"))
        qs = {q["id"]: q for q in showcase.SHOWCASE}
        for row in d["rows"]:
            got = showcase._structured(qs[row["id"]])
            want = row["arms"]["structured"]
            self.assertEqual({k: got[k] for k in ("estimate", "p10", "p90", "n_valid_paths", "attempts", "errors")},
                             {k: want[k] for k in ("estimate", "p10", "p90", "n_valid_paths", "attempts", "errors")}, row["id"])


class TestFixKeepsNumbers(unittest.TestCase):
    """修改后的 engine 在保存的回复上：估计、区间、有效路径数、各路径状态和中位数都和冻结的 engine 一样。"""

    def test_saved_replies(self):
        for f in SAVED:
            raw = json.loads(f.read_text(encoding="utf-8"))
            for a in raw["attempts"]:
                args = (a["reply"], raw["target_unit"], raw["qid"])
                new = _clean(evaluate_structured(*args, strict_target=False))
                old = _clean(showcase_engine.evaluate_structured(*args, strict_target=False))
                self.assertEqual(new["result"], old["result"], (raw["qid"], a["attempt"]))
                self.assertEqual([(p["id"], p["status"], p.get("median"), p.get("p10"), p.get("p90")) for p in new["paths"]],
                                 [(p["id"], p["status"], p.get("median"), p.get("p10"), p.get("p90")) for p in old["paths"]])


if __name__ == "__main__":
    unittest.main()
