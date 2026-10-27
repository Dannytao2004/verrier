"""单位：直接用 pint 的写法（kg/day、USD/year、birth/(1000 person)、percent），本模块只是一层薄封装。

v2.7c 起砍薄：不再解析自然语言写法（per、连字符、比率基数等，原来约 500 行），单位由规划和裁判按 pint 写法写，
解析不了就把错误交给修正轮。这里只补 pint 没有的两样：
- 货币（USD、EUR……）各自是一个独立的基本维度，互相不换算（汇率是证据，不是常数）；
- 计数名词（person、visitor、slice、pizza……）第一次出现时自动定义成各自的基本维度；复数按简单规则归到单数
  （people -> person，-ies -> -y，末尾的 s 去掉），这样 slice/person 和 slices/person 是同一个单位。
公开函数都不抛异常，返回 (结果, 错误)；错误为 "" 表示成功，否则是一句给修正轮看的英文。
- parse_unit(text) -> (pint.Quantity | None, error)：Quantity 的数值是单位里的倍数（'birth/(1000 person)' 是 0.001）。
- convert_factor(src, dst) -> (float | None, error)：src 单位的 1 等于多少 dst 单位（'kg/year' -> 't/day' 是 1/365250）。
"""
import re
import threading

import pint

CURRENCIES = ("USD", "EUR", "GBP", "JPY", "CNY", "KRW", "TWD", "CAD", "AUD", "CHF", "HKD", "INR")
IRREGULAR = {"people": "person", "persons": "person", "children": "child", "men": "man", "women": "woman"}

UREG = pint.UnitRegistry()
for _c in CURRENCIES:
    UREG.define(f"{_c} = [currency_{_c}]")
UREG.define("percentage_point = 0.01 = pp")
UREG.define("basis_point = 0.0001 = bp")
# v2.13a（用户 10-26：「月」和「月份」这种应该是同一个东西，别区分开）：pint 不认的时间写法补成别名，
# 否则会被当成新的计数名词（visit/mo 换不到 visit/month，方法被误拦）
for _alias in ("mo = month", "mth = month", "wk = week", "annum = year"):
    UREG.define(_alias)
# 中文的时间单位换成英文再解析（只换时间词；中文名词照旧解析不了，交给报错）
CJK_TIME = (("个月", " month "), ("月份", " month "), ("月度", " month "), ("季度", " (3 month) "), ("年度", " year "),
            ("星期", " week "), ("月", " month "), ("年", " year "), ("周", " week "), ("天", " day "), ("日", " day "))
_LOCK = threading.Lock()   # 注册表是模块级的，会自动加名词；网页里几个运行可能同时解析


def _singular(w: str) -> str:
    lw = w.lower()
    if lw in IRREGULAR:
        return IRREGULAR[lw]
    if lw.endswith("ies") and len(lw) > 4:
        return lw[:-3] + "y"
    if lw.endswith("s") and not lw.endswith("ss") and len(lw) > 3:
        return lw[:-1]
    return lw


def _define_noun(word: str) -> bool:
    """把 pint 不认识的英文单词定义成计数单位（复数归到单数）。不是纯字母单词就不定义（交给错误）。"""
    if not re.fullmatch(r"[A-Za-z]+", word):
        return False
    base = _singular(word)
    if base not in UREG:
        UREG.define(f"{base} = [{base}]")
    if word != base and word not in UREG:
        UREG.define(f"{word} = {base}")
    return True


def parse_unit(text) -> tuple:
    if not isinstance(text, str) or not text.strip():
        return None, "unit is empty"
    s = text.strip().replace("%", " percent ")
    for cjk, en in CJK_TIME:
        s = s.replace(cjk, en)
    s = re.sub(r"\bquarters?\b", "(3 month)", s)   # pint 的 quarter 是重量单位；单位里写的季度是 3 个月
    m = re.search(r"[,;]|\b(?:or|and|vs|versus)\b", s, re.I)   # 'kg or lbs'、'kg, lb'：给了几个候选，不是一个单位
    if m:
        return None, f"unit '{text}': {m.group(0).lower()!r} gives alternatives; pin exactly one unit"
    with _LOCK:
        for _ in range(10):   # 每轮最多补定义一个新名词
            try:
                q = UREG.parse_expression(s)
                break
            except pint.UndefinedUnitError as e:
                names = e.unit_names if isinstance(e.unit_names, (list, tuple)) else [e.unit_names]
                if not all(_define_noun(str(n)) for n in names):
                    return None, f"unit '{text}': unknown name(s) {', '.join(map(str, names))}; use pint notation such as 'kg/day' or 'USD/year'"
            except Exception as e:  # noqa: BLE001  pint 的语法错误类型很多，统一转成一句话
                return None, f"unit '{text}' cannot be parsed ({type(e).__name__}); use pint notation such as 'kg/day', 'USD/year' or 'birth/(1000 person)'"
        else:
            return None, f"unit '{text}' cannot be parsed"
    if not isinstance(q, pint.Quantity):   # 纯数字（'1000'）
        q = UREG.Quantity(q, "dimensionless")
    if not (q.magnitude > 0):
        return None, f"unit '{text}' has a non-positive factor"
    return q, ""


def convert_factor(src, dst) -> tuple:
    a, ea = parse_unit(src) if not isinstance(src, pint.Quantity) else (src, "")
    if ea:
        return None, ea
    b, eb = parse_unit(dst) if not isinstance(dst, pint.Quantity) else (dst, "")
    if eb:
        return None, eb
    try:
        f = float(a.to(b.units).magnitude / b.magnitude)
    except pint.DimensionalityError:
        return None, f"'{src}' ({a.units:~}) cannot be converted to '{dst}' ({b.units:~})"
    return f, ""
