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
import logging
import re
import threading

import pint

CURRENCIES = ("USD", "EUR", "GBP", "JPY", "CNY", "KRW", "TWD", "CAD", "AUD", "CHF", "HKD", "INR")
IRREGULAR = {"people": "person", "persons": "person", "children": "child", "men": "man", "women": "woman"}

# v2.13c / e：SI 前缀不接在这些名字上：油气单位（mboe 不是 milli-boe、Mmcf 不是 mega-mcf）、自动定义的计数名词和它们的
# 大小写 / 复数别名（先定义了 all，calls 也不读成 centi-all；MBoe 之后的 MMBoe 不是 mega-MBoe）。pint 自带单位的前缀不受影响（km、kWh）
NO_PREFIX = set()
# v2.13f（存档语料扫描）：pint 自带单位里，接上 SI 前缀只会凑出普通单词的误读、本项目用不到前缀的（unit = micro-nit、pct = pico-carat、
# KB 的小写 kb = kilo-barn、uk = micro-k_B、api = atto-π、rpt = ronto-pint、feu = femto-entropy_unit……）：整个不准加前缀
PINT_NO_PREFIX = {"nit", "barn", "pi", "carat", "parsec", "boltzmann_constant", "technical_atmosphere", "standard_atmosphere", "pint",
                  "molar", "elementary_charge", "point", "dram", "peck", "cup", "entropy_unit", "are"}
# 前缀本身常用、只有这几种组合是误读的：as（(as recorded)）= atto-second、kilos = kilo-second、pm = pico-meter、fl = femto-liter、
# dt / nt = deci- / nano-tonne、EV / TV = exa- / tera-volt
BAD_PREFIX = {("atto", "second"), ("kilo", "second"), ("pico", "meter"), ("femto", "liter"), ("deci", "metric_ton"),
              ("nano", "metric_ton"), ("exa", "volt"), ("tera", "volt")}


class _Registry(pint.UnitRegistry):
    """v2.13e（审查发现）：pint 挑读法时，把「SI 前缀 + NO_PREFIX 里的名字」这种候选拿掉。这样一个词怎么读不再取决于之前解析过
    什么（v2.13c 在 pint 外面先扫一遍再补定义，漏了 pint 自己的取舍：名字等于「完整前缀名 + 另一个单位」时，pint 丢掉不带前缀的
    读法，exaflops 读成 exa + flops、millions 读成 milli + ons）。拿掉以后没有读法的词照旧交给 _define_noun。"""

    def _dedup_candidates(self, candidates):
        return pint.UnitRegistry._dedup_candidates([c for c in candidates
                                                     if not (c[0] and (c[1] in NO_PREFIX or (c[0], c[1]) in BAD_PREFIX))])

    def parse_unit_name(self, unit_name, case_sensitive=None):
        """v2.13f：拼全的前缀名后面只剩一两个字母（单位的符号）的读法也拿掉：exams = exa + m + s（艾米）、kilos = kilo + s（千秒）。
        真要用长前缀名时，单位也写全名（kilometers、megawatts）。"""
        return tuple(c for c in super().parse_unit_name(unit_name, case_sensitive)
                     if not (c[0] and len(c[0]) > 2 and unit_name.lower().startswith(c[0])
                             and len(unit_name[len(c[0]):].rstrip("s")) <= 2))


UREG = _Registry()
for _c in CURRENCIES:
    UREG.define(f"{_c} = [currency_{_c}]")
UREG.define("percentage_point = 0.01 = pp")
UREG.define("basis_point = 0.0001 = bp")
# v2.13a（用户 10-26：「月」和「月份」这种应该是同一个东西，别区分开）：pint 不认的时间写法补成别名，
# 否则会被当成新的计数名词（visit/mo 换不到 visit/month，方法被误拦）
for _alias in ("mo = month", "mth = month", "wk = week", "annum = year"):
    UREG.define(_alias)
# v2.13c（用户 10-27：单位库更新一下）：油气行业的写法，按 SPE 惯例 M = 千、MM = 百万（Equinor 报告的 mboe/d = 千桶油当量/日）。
# 不定义时 mboe 会被当成新的计数名词、换不到 boe；boe 先定义过时又被 pint 读成 milli-boe（差 10^6，BUGS S75）。
# pint 自带的 barrel / bbl 是 31.5 加仑的美制液体桶，石油的桶是 42 加仑（oil_barrel）：这里改成油桶。
# 有歧义的不另定义：mb/d（IEA 用作百万桶/日，SPE 惯例读成千桶/日）、mcm；MBtu 照 pint 读成 10^6 Btu（IEA 的用法）。
# v2.13e（审查发现）：补上 mscf、ccf（= 100 cf，美国燃气账单的写法）、mbpd / MMbpd、cfs（立方英尺/秒，不是 cf 的复数）。
_pint_log = logging.getLogger("pint.util")
_level = _pint_log.level
_pint_log.setLevel(logging.ERROR)   # 重定义 barrel 时 pint 会打一条 Redefining 警告
try:
    UREG.define("barrel = oil_barrel = bbl")
finally:
    _pint_log.setLevel(_level)
OIL_GAS = ("boe = [boe] = _ = BOE = barrel_of_oil_equivalent = barrel_oil_equivalent",   # _ = 短写就用名字本身
           "mboe = 1e3 * boe = _ = Mboe = MBOE = kboe", "MMboe = 1e6 * boe = _ = mmboe = MMBOE",
           "mbbl = 1e3 * bbl = _ = Mbbl = MBBL = kbbl", "MMbbl = 1e6 * bbl = _ = mmbbl = MMBBL", "bpd = bbl / day = _ = BPD",
           "mbpd = 1e3 * bpd = _ = Mbpd = MBPD = kbpd = KBPD", "MMbpd = 1e6 * bpd = _ = mmbpd = MMBPD",
           "cf = foot ** 3 = _ = scf = CF", "cfs = cf / second = _ = CFS", "ccf = 100 * cf = _ = Ccf = CCF",
           "Mcf = 1e3 * cf = _ = mcf = MCF = Mscf = mscf", "MMcf = 1e6 * cf = _ = mmcf = MMCF = MMscf = mmscf",
           "Bcf = 1e9 * cf = _ = bcf = BCF", "Tcf = 1e12 * cf = _ = tcf = TCF", "bcm = 1e9 * meter ** 3 = _ = BCM",
           "MMBtu = 1e6 * Btu = _ = mmbtu = MMBTU = MMbtu",
           # v2.13f（第二轮审查）：小写 mtoe 被 pint 读成 milli-toe；能源统计里 mtoe / MTOE 都指百万吨油当量（Mtoe 照 pint 读成 mega）
           "mtoe = 1e6 * tonne_of_oil_equivalent = _ = MTOE")
for _d in OIL_GAS:
    UREG.define(_d)
# pi：pint 的常数 π，前缀接上去就把 API、CPI、KPI 读成 atto-π、centi-π、kilo-π（第二轮审查）
NO_PREFIX.update({d.split("=")[0].strip() for d in OIL_GAS} | {"barrel", "oil_barrel"} | PINT_NO_PREFIX)
UREG.define("pct = percent")   # v2.13f：基线的 units.py 也这样读；不定义时 pct 被读成 pico-carat
# 中文的时间单位换成英文再解析（只换时间词；中文名词照旧解析不了，交给报错）
CJK_TIME = (("个月", " month "), ("月份", " month "), ("月度", " month "), ("季度", " (3 month) "), ("年度", " year "),
            ("星期", " week "), ("月", " month "), ("年", " year "), ("周", " week "), ("天", " day "), ("日", " day "))
_LOCK = threading.Lock()   # 注册表是模块级的，会自动加名词；网页里几个运行可能同时解析


def _singular(w: str) -> str:
    if re.fullmatch(r"[A-Z]{2,}s", w):   # v2.13f：大写缩写的复数（VMs、IPs），不受下面长度 > 3 的限制
        return w[:-1].lower()
    lw = w.lower()
    if lw in IRREGULAR:
        return IRREGULAR[lw]
    if lw.endswith("ies") and len(lw) > 4:
        return lw[:-3] + "y"
    if lw.endswith("s") and not lw.endswith("ss") and len(lw) > 3:
        return lw[:-1]
    return lw


def _known(name: str) -> bool:
    """name 在 pint 里有读法。pint 对「前缀 + 偏移 / 对数单位」（Kfahrenheit 的小写 kfahrenheit）会抛异常：当成没有读法。"""
    try:
        return name in UREG
    except Exception:  # noqa: BLE001
        return False


def _alias_ok(word: str, base: str) -> bool:
    """v2.13f（第二轮审查）：word 的小写 base 在 pint 里有读法时，能不能把 word 当成它的别名。base 本身就是单位（Mile -> mile）可以；
    base 只能读成「前缀 + 单位」时，只有大小写没改前缀意思的才行：大写 K -> kilo（Kg、KM、Kcal；大写 K 不是前缀），或者前缀名拼全了
    （Megatonnes -> megatonne）。其余的（API -> atto-π、MTOE -> milli-toe、US -> 微秒、MCal -> milli-calorie）大小写一改，前缀就变了。"""
    try:
        c = UREG.parse_unit_name(base)
    except Exception:  # noqa: BLE001
        return False
    if not c or any(not p for p, _, _ in c):
        return bool(c)
    p = c[0][0]
    return base.startswith(p) or (word[:1] == "K" and p == "kilo")


def _define_noun(word: str) -> bool:
    """把 pint 不认识的英文单词定义成计数单位（复数归到单数）。不是纯字母单词就不定义（交给错误）。
    v2.13c / e：新名词和别名进 NO_PREFIX（之后不会被读成「前缀 + 它」）。已经是单位的名字不重定义（v2.13c 一度改成「名字本身是
    单位才算」，Kg 的单数 kg 只能读成 kilo + gram，被重定义成计数名词，之后整个进程的 kg 都换不了 t，审查发现）。"""
    if not re.fullmatch(r"[A-Za-z]+", word):
        return False
    base = _singular(word)
    if not _known(base):
        UREG.define(f"{base} = [{base}]")
        NO_PREFIX.add(base)
    elif not _alias_ok(word, base):   # base 只能读成「前缀 + 单位」，而大小写改了前缀的意思：word 自己做名词
        own = word[:-1] if re.fullmatch(r"[A-Z]{2,}s", word) else word   # 大写缩写的复数归到单数（RPTs -> RPT），和先见到 RPT 时一样
        if not _known(own):
            UREG.define(f"{own} = [{own}]")
            NO_PREFIX.add(own)
        if word != own and not _known(word):
            UREG.define(f"{word} = {own}")
            NO_PREFIX.add(word)
        return True
    if word != base and not _known(word):
        UREG.define(f"{word} = {base}")
        NO_PREFIX.add(word)
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
