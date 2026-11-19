"""v2.15：三方审计 + GPT 评估之后的五处小修（2026-11-19）。
a 报错里的数字格式；b 裁判 JSON 少右花括号时定点补上，补不好再关思考重问；c 百分数假设写成小数时交回确认；
d 量级闸门（和不联网直接问的粗估比，差 2 倍以上定向修正一次）；e 抽取每页上限 15 -> 30。"""
import unittest

from triangulate.agent import graph as G


def _m(mid, est):
    return {"id": mid, "method": "formula_mc", "estimate": est}


class TestErrorNumberFormat(unittest.TestCase):
    """v2.15a：BCG 那次（11-12）0.069 被写成「0」，修正轮看不出是哪条路线小了几个数量级。"""

    def test_small_estimates_keep_their_digits(self):
        jr = {"methods": [_m("m1", 0.06934), _m("m2", 15043.2)]}
        out = {"methods": [_m("m1", 0.06934), _m("m2", 15043.2)]}
        _, probs = G._problems(jr, out, {"rejected": []}, {})
        text = "\n".join(probs)
        self.assertIn("m2 gives 15,043 but m1 gives 0.06934", text)
        self.assertNotIn("gives 0 ", text)

    def test_third_far_method_listed_with_digits(self):
        ms = [_m("m1", 0.06934), _m("m2", 15043.2), _m("m3", 101.4)]
        _, probs = G._problems({"methods": ms}, {"methods": ms}, {"rejected": []}, {})
        far = [p for p in probs if p.startswith("methods more than")]
        self.assertEqual(len(far), 1)
        self.assertIn("m1 (0.06934)", far[0])
        self.assertIn("m3 (101)", far[0])



if __name__ == "__main__":
    unittest.main()
