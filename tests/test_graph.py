import unittest

from triangulate.engine import evaluate_structured
from triangulate.expr import Formula
from triangulate.graph import INPUT_STATUSES, sensitivity


def _inp(name, lo, hi, unit="", ptype="assumption"):
    prov = {"type": "assumption", "rationale": "test"} if ptype == "assumption" else {"type": "sourced", "source": "X"}
    return {"name": name, "description": name, "value": (lo * hi) ** 0.5, "low": lo, "high": hi, "unit": unit, "provenance": prov}


class TestSensitivity(unittest.TestCase):
    def test_product_and_constant(self):
        s = sensitivity({"a": (1.0, 100.0), "b": (3.0, 3.0)}, {"p1": Formula("a * b")}, 1.0)
        self.assertAlmostEqual(s["a"]["final"], 2.0)
        self.assertAlmostEqual(s["b"]["final"], 0.0)

    def test_denominator_is_negative(self):
        s = sensitivity({"a": (5.0, 5.0), "b": (2.0, 20.0)}, {"p1": Formula("a / b")}, 1.0)
        self.assertAlmostEqual(s["b"]["final"], -1.0)
        self.assertAlmostEqual(s["b"]["path_max"], 1.0)

    def test_median_aggregation_can_mask_an_input(self):
        # p3 远高于另两条路径；x 只进 p3，移动 x 不改变中位路径 -> final 为 0，但 path_max 不为 0
        s = sensitivity({"a": (10.0, 10.0), "b": (12.0, 12.0), "x": (1000.0, 10000.0)},
                        {"p1": Formula("a"), "p2": Formula("b"), "p3": Formula("x")}, 1.0)
        self.assertAlmostEqual(s["x"]["final"], 0.0)
        self.assertAlmostEqual(s["x"]["path_max"], 1.0)

    def test_unused_input(self):
        s = sensitivity({"a": (1.0, 2.0), "z": (1.0, 2.0)}, {"p1": Formula("a")}, 1.0)
        self.assertIsNone(s["z"]["final"])


class TestGraphFromEngine(unittest.TestCase):
    def setUp(self):
        self.spec = {
            "target": {"definition": "distance", "unit": "km"},
            "inputs": [_inp("speed", 50, 100, "km/h"), _inp("hours", 2, 2, "h"), _inp("steps", 1e4, 3e4, "", "sourced"),
                       _inp("step_len", 0.6, 0.8, "m"), _inp("mass", 1, 2, "kg")],
            "paths": [{"id": "p1", "method": "top_down", "formula": "speed * hours", "output_unit": "km"},
                      {"id": "p2", "method": "bottom_up", "formula": "steps * step_len", "output_unit": "m"},
                      {"id": "p3", "method": "proxy", "formula": "mass * ghost", "output_unit": "km"}],
        }

    def test_nodes_edges_status_and_dependents(self):
        st = evaluate_structured(self.spec, "km", "t1", n=500)
        g = st["graph"]
        ids = {n["id"]: n for n in g["nodes"]}
        self.assertIn("target", ids)
        self.assertEqual(ids["path:p1"]["status"], "valid")
        self.assertEqual(ids["path:p3"]["status"], "invalid")         # 引用未定义的 ghost
        self.assertEqual(ids["input:ghost"]["status"], "missing")
        self.assertEqual(ids["input:steps"]["status"], "sourced_unverified")
        self.assertEqual(ids["input:speed"]["status"], "assumption")
        self.assertEqual(ids["input:mass"]["n_dependents"], 1)
        for n in g["nodes"]:
            if n["kind"] == "input":
                self.assertIn(n["status"], INPUT_STATUSES)
        kinds = {(e["source"], e["target"]): e["kind"] for e in g["edges"]}
        self.assertEqual(kinds[("input:speed", "path:p1")], "used_by")
        self.assertEqual(kinds[("path:p1", "target")], "aggregated_into")
        self.assertTrue(any("ghost" in e for e in st["errors"]))
        # 单位：p2 给的是 m，代码换算成 km；两条有效路径中位数约 141.4 km 与 12.0 km，取几何平均
        self.assertEqual(st["result"]["n_valid_paths"], 2)
        self.assertAlmostEqual(st["result"]["central"], (141.4 * 12.0) ** 0.5, delta=1.5)

    def test_dimension_mismatch_invalidates_path(self):
        self.spec["paths"][2] = {"id": "p3", "method": "proxy", "formula": "mass * speed", "output_unit": "km"}
        st = evaluate_structured(self.spec, "km", "t2", n=200)
        p3 = next(p for p in st["paths"] if p["id"] == "p3")
        self.assertEqual(p3["status"], "invalid")
        self.assertTrue(any("dimension mismatch" in m for m in p3["issues"]))

    def test_deterministic(self):
        a = evaluate_structured(self.spec, "km", "t3", n=300)["result"]
        b = evaluate_structured(self.spec, "km", "t3", n=300)["result"]
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
