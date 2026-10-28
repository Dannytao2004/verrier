"""v2.14a：修正轮是修，不是删（用户 10-27：「现在我们的修复功能更像删除功能了」）。
被点名的范围由报错决定（graph._repair_scope），范围外的改动和没给理由的删除由代码退回（graph._lock_repair）。"""
import unittest

from triangulate.agent import graph as G


def fm(mid, formula, **kw):
    return {"id": mid, "method": "formula_mc", "params": {"formula": formula, "inputs": {}}, **kw}


class TestRepairScope(unittest.TestCase):
    def test_methods_named_by_errors_and_conflicts(self):
        ms, asum = G._repair_scope(["method m3 (formula_mc): input audit: p81: base is a single channel",
                                    "methods disagree: m1 gives 348,294 but m2 gives 58,000 (more than 3x apart); ...",
                                    "assumption a4 rejected: need 0 < low <= value <= high"], [])
        self.assertEqual(ms, {"m1", "m2", "m3"})
        self.assertEqual(asum, {"a4"})

    def test_assumption_citing_an_objected_point_is_named(self):
        # 10-27 sponsor 题：p81（Handshake）被输入核对否了，理由引用 p81 的 a2 也算被点名，可以改
        _, asum = G._repair_scope(["method m3 (formula_mc): input audit: p81: base is a single channel"],
                                  [{"id": "a2", "rationale": "anchored on Handshake 2.6% (p81)"}, {"id": "a1", "rationale": "Indeed p16"}])
        self.assertEqual(asum, {"a2"})


class TestLockRepair(unittest.TestCase):
    prev_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2"), fm("m3", "p3 * a3")]
    prev_a = [{"id": "a1", "value": 0.5, "low": 0.4, "high": 0.6, "unit": "1"},
              {"id": "a2", "value": 2, "low": 1, "high": 3, "unit": "1"},
              {"id": "a3", "value": 3, "low": 2, "high": 4, "unit": "1"}]

    def test_unnamed_method_change_and_removal_are_undone(self):
        new_m = [fm("m1", "p1 * a1 * 2"), fm("m3", "p4 * a3")]   # m1 没被点名却被改了，m2 没被点名却被删了
        m, a, log = G._lock_repair(self.prev_m, self.prev_a, new_m, self.prev_a, {"m3"}, set(), [])
        by = {x["id"]: x for x in m}
        self.assertEqual(by["m1"]["params"]["formula"], "p1 * a1")
        self.assertEqual(by["m2"]["params"]["formula"], "p2 * a2")
        self.assertEqual(by["m3"]["params"]["formula"], "p4 * a3")   # 被点名的 m3 可以改
        self.assertEqual({(x["id"], x["action"]) for x in log}, {("m1", "change undone"), ("m2", "put back")})

    def test_named_method_removed_needs_a_reason(self):
        new_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2")]
        m, _, log = G._lock_repair(self.prev_m, self.prev_a, new_m, self.prev_a, {"m3"}, set(), [])
        self.assertIn("m3", [x["id"] for x in m])
        self.assertEqual(log[0]["action"], "put back")
        m, _, log = G._lock_repair(self.prev_m, self.prev_a, new_m, self.prev_a, {"m3"}, set(),
                                   [{"id": "m3", "wrong_input": "p3", "evidence": "p3 counts employers, not postings"}])
        self.assertNotIn("m3", [x["id"] for x in m])
        self.assertEqual(log[0]["action"], "dropped")
        _, _, log = G._lock_repair(self.prev_m, self.prev_a, new_m, self.prev_a, {"m3"}, set(), [{"id": "m3", "wrong_input": "p3"}])
        self.assertEqual(log[0]["action"], "put back")   # 没写证据不算

    def test_assumptions_of_unnamed_methods_are_kept(self):
        new_a = [{**self.prev_a[0], "value": 0.9}, self.prev_a[1], {**self.prev_a[2], "value": 9},
                 {"id": "a9", "value": 1, "low": 1, "high": 2, "unit": "1"}]
        _, a, log = G._lock_repair(self.prev_m, self.prev_a, self.prev_m, new_a, {"m3"}, {"a3"}, [])
        by = {x["id"]: x for x in a}
        self.assertEqual(by["a1"]["value"], 0.5)   # m1 没被点名，它用的 a1 不准改
        self.assertEqual(by["a3"]["value"], 9)     # a3 被点名，可以改
        self.assertIn("a9", by)                    # 新假设照收
        self.assertEqual([(x["id"], x["action"]) for x in log], [("a1", "change undone")])

    def test_new_methods_are_accepted(self):
        new_m = self.prev_m + [fm("m4", "p5 * a1")]
        m, _, log = G._lock_repair(self.prev_m, self.prev_a, new_m, self.prev_a, {"m3"}, set(), [])
        self.assertEqual([x["id"] for x in m], ["m1", "m2", "m3", "m4"])
        self.assertEqual(log, [])


class TestLockRepairReviewFindings(unittest.TestCase):
    """v2.14a 审查查出的 7 处（每条一个用例）。"""
    A = [{"id": f"a{i}", "value": i, "low": i / 2, "high": i * 2, "unit": "1"} for i in range(1, 10)]

    def test_put_back_method_brings_its_assumptions(self):
        prev_m = [fm("m1", "p1 * a1"), fm("m3", "p3 * a3")]
        m, a, log = G._lock_repair(prev_m, self.A[:3], [fm("m1", "p1 * a1")], self.A[:2], {"m3"}, set(), [])
        self.assertIn("m3", [x["id"] for x in m])
        self.assertIn("a3", [x["id"] for x in a])   # 以前只放回方法，a3 没回来，m3 必然跑不了

    def test_renumbering_is_not_a_deletion(self):
        prev_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2"), fm("m3", "p3 * a3"), fm("m4", "p4 * a4")]
        # m2（只覆盖一部分，代码判死）删了；旧 m3 原样挪成 m2；旧 m4 修好挪成 m3
        new_m = [fm("m1", "p1 * a1"), fm("m2", "p3 * a3"), fm("m3", "p4 * a4 * a9")]
        m, _, log = G._lock_repair(prev_m, self.A, new_m, self.A, {"m2", "m3", "m4"}, set(), [], deletable={"m2"})
        self.assertEqual([x["params"]["formula"] for x in m], ["p1 * a1", "p3 * a3", "p4 * a4 * a9"])   # 没有重复、没放回未修版本
        self.assertEqual([(x["id"], x["action"]) for x in log], [("m2", "dropped")])

    def test_renumbering_cannot_dodge_the_reason_rule(self):
        # 冲突点名 m1、m3；裁判不写理由删掉 m1，再把 m2 -> m1、m3 -> m2
        prev_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2"), fm("m3", "p3 * a3")]
        new_m = [fm("m1", "p2 * a2"), fm("m2", "p3 * a3")]
        m, _, log = G._lock_repair(prev_m, self.A, new_m, self.A, {"m1", "m3"}, set(), [])
        self.assertEqual(sorted(x["params"]["formula"] for x in m), ["p1 * a1", "p2 * a2", "p3 * a3"])
        self.assertEqual(len({x["id"] for x in m}), 3)   # 放回的 m1 撞了编号：换一个空闲的
        self.assertIn(("m1", "put back"), [(x["id"], x["action"]) for x in log])

    def test_all_far_apart_methods_are_named(self):
        out = {"methods": [{"id": "m1", "estimate": 1201.0, "inputs_detail": []}, {"id": "m2", "estimate": 100.0, "inputs_detail": []},
                           {"id": "m4", "estimate": 100.0, "inputs_detail": []}]}
        _, probs = G._problems(out, out, {"rejected": []}, {})
        self.assertEqual(G._repair_scope(probs, [])[0], {"m1", "m2", "m4"})   # 以前只点名最高和最低两条

    def test_reused_assumption_id_keeps_old_value_for_unnamed_method(self):
        prev_m = [fm("m3", "p3 * a6"), fm("m5", "p5 * a5")]
        prev_a = [self.A[4], {"id": "a6", "value": 1.2, "low": 1.1, "high": 1.3, "unit": "1"}]
        new_a = [self.A[4], {"id": "a6", "value": 8e16, "low": 6e16, "high": 1e17, "unit": "token"}]
        m, a, log = G._lock_repair(prev_m, prev_a, [fm("m3", "p3 * a6"), fm("m5", "p5 * a5 + a6")], new_a, {"m5"}, set(), [])
        by_a = {x["id"]: x for x in a}
        m3 = next(x for x in m if x["id"] == "m3")
        old = next(k for k, v in by_a.items() if v["value"] == 1.2)
        self.assertNotEqual(old, "a6")
        self.assertIn(old, m3["params"]["formula"])          # m3 换到旧值的新 id
        self.assertEqual(by_a["a6"]["value"], 8e16)          # m5 用新值
        self.assertTrue(any(x["action"].startswith("kept as") for x in log))

    def test_code_rejected_methods_may_be_dropped(self):
        prev_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2")]
        m, _, log = G._lock_repair(prev_m, self.A, [fm("m1", "p1 * a1")], self.A, {"m2"}, set(), [], deletable={"m2"})
        self.assertEqual([x["id"] for x in m], ["m1"])
        self.assertEqual(log[0]["action"], "dropped")

    def test_put_back_is_a_copy(self):
        prev_m = [fm("m1", "p1 * a1"), fm("m2", "p2 * a2")]
        m, _, _ = G._lock_repair(prev_m, self.A, [fm("m1", "p1 * a1")], self.A, set(), set(), [])
        next(x for x in m if x["id"] == "m2")["unit"] = "changed later"
        self.assertNotIn("unit", prev_m[1])   # 单位核对之后原地改方法，不能改到修正前的快照

    def test_shared_named_assumption_change_is_logged(self):
        prev_m = [fm("m1", "p1 * a1"), fm("m3", "p3 * a1")]
        new_a = [{**self.A[0], "value": 0.05}]
        _, a, log = G._lock_repair(prev_m, self.A[:1], prev_m, new_a, {"m1"}, {"a1"}, [])
        self.assertEqual(a[0]["value"], 0.05)
        self.assertEqual([(x["id"], x["action"]) for x in log], [("a1", "changed (shared)")])


class TestConflictMessage(unittest.TestCase):
    def test_conflict_lists_the_inputs_of_both_methods(self):
        out = {"methods": [{"id": "m1", "estimate": 348294.0, "inputs_detail": [{"id": "p103", "p10": 3.4e6, "p90": 5e6, "unit": "job posting"},
                                                                                {"id": "a2", "p10": 0.005, "p90": 0.06, "unit": "%"}]},
                           {"id": "m2", "estimate": 58000.0, "inputs_detail": [{"id": "p103", "p10": 3.4e6, "p90": 5e6, "unit": "job posting"},
                                                                               {"id": "a5", "p10": 0.001, "p90": 0.01, "unit": "%"}]}]}
        _, probs = G._problems({"methods": out["methods"]}, out, {"rejected": []}, {})
        msg = next(p for p in probs if p.startswith("methods disagree"))
        self.assertIn("Inputs of m1: p103 3,400,000..5,000,000 job posting; a2 0.5%..6%", msg)
        self.assertIn("Inputs of m2:", msg)
        self.assertEqual(G._repair_scope([msg], [])[0], {"m1", "m2"})


if __name__ == "__main__":
    unittest.main()
