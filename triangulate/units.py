"""显式的小单位表 + 单位串解析器。所有单位换算都在这里由代码完成，不交给模型。

单位串语法（宽松）：因子之间用 * 或 / 连接，因子可带 **n 指数；空格当乘号；支持 per、^、square/cubic 等写法。
维度只追踪 m、kg、s、USD、byte 五个基；温度、电流、角度、分贝等不在表里。
- strict=True（用于数据集答案的目标单位）：表外的词一律报错，只放行少量计数名词（person/people/sheet）。
- strict=False（用于模型给的单位）：表外的词当作「计数名词」（people、trucks、cups），无量纲、系数 1，并记录下来。
"""
import math
import re
from fractions import Fraction
from typing import NamedTuple

BASES = ("m", "kg", "s", "USD", "byte")


def _d(**kw):
    return tuple(sorted((k, Fraction(v)) for k, v in kw.items() if v))


DIMLESS = ()
L, M, T, USD, BYTE = _d(m=1), _d(kg=1), _d(s=1), _d(USD=1), _d(byte=1)
YEAR = 365.25 * 86400  # 与 pint 一致：儒略年

# name -> (系数：1 该单位 = 多少 SI 基单位, 维度)
UNITS = {
    # 无量纲与倍数词
    "": (1.0, DIMLESS), "1": (1.0, DIMLESS), "count": (1.0, DIMLESS), "number": (1.0, DIMLESS),
    "dimensionless": (1.0, DIMLESS), "unitless": (1.0, DIMLESS), "fraction": (1.0, DIMLESS),
    "ratio": (1.0, DIMLESS), "share": (1.0, DIMLESS), "times": (1.0, DIMLESS),
    "%": (0.01, DIMLESS), "percent": (0.01, DIMLESS), "pct": (0.01, DIMLESS), "ppm": (1e-6, DIMLESS),
    "dozen": (12.0, DIMLESS), "hundred": (1e2, DIMLESS), "thousand": (1e3, DIMLESS),
    "million": (1e6, DIMLESS), "billion": (1e9, DIMLESS), "trillion": (1e12, DIMLESS),
    # 长度
    "m": (1.0, L), "meter": (1.0, L), "metre": (1.0, L),
    "in": (0.0254, L), "inch": (0.0254, L), "inches": (0.0254, L),
    "ft": (0.3048, L), "foot": (0.3048, L), "feet": (0.3048, L),
    "yd": (0.9144, L), "yard": (0.9144, L),
    "mi": (1609.344, L), "mile": (1609.344, L),
    "ly": (9.4607304725808e15, L), "au": (1.495978707e11, L), "AU": (1.495978707e11, L),
    # 质量
    "g": (1e-3, M), "gram": (1e-3, M), "kg": (1.0, M),
    "t": (1e3, M), "tonne": (1e3, M),
    "ton": (907.18474, M),  # 与 pint 一致：short ton；公吨请写 tonne / t / metric ton
    "lb": (0.45359237, M), "lbs": (0.45359237, M), "pound": (0.45359237, M),
    "oz": (0.028349523125, M), "ounce": (0.028349523125, M),
    # 时间
    "s": (1.0, T), "sec": (1.0, T), "second": (1.0, T),
    "min": (60.0, T), "minute": (60.0, T),
    "h": (3600.0, T), "hr": (3600.0, T), "hour": (3600.0, T),
    "d": (86400.0, T), "day": (86400.0, T), "week": (7 * 86400.0, T), "wk": (7 * 86400.0, T),
    "month": (YEAR / 12, T), "yr": (YEAR, T), "year": (YEAR, T),
    "decade": (10 * YEAR, T), "century": (100 * YEAR, T),
    # 面积 / 体积
    "acre": (4046.8564224, _d(m=2)), "ha": (1e4, _d(m=2)), "hectare": (1e4, _d(m=2)),
    "L": (1e-3, _d(m=3)), "l": (1e-3, _d(m=3)), "liter": (1e-3, _d(m=3)), "litre": (1e-3, _d(m=3)),
    "gal": (3.785411784e-3, _d(m=3)), "gallon": (3.785411784e-3, _d(m=3)),
    "pint": (4.73176473e-4, _d(m=3)), "quart": (9.46352946e-4, _d(m=3)),
    "barrel": (0.158987294928, _d(m=3)), "bbl": (0.158987294928, _d(m=3)),
    # v2.13c：油气行业的写法，SPE 惯例 M = 千、MM = 百万（4 个字符以上的名字查表时也按小写查：Mboe -> mboe、MMcf -> mmcf）。
    # boe 是计数名词（系数 1）：没有这几项时 mboe/d 会被当成另一个计数名词、按 1 换成 boe/d（差 1000 倍、不报错，BUGS S75）。
    # mb/d（IEA 用作百万桶/日）有歧义，不收
    "boe": (1.0, DIMLESS), "BOE": (1.0, DIMLESS), "mboe": (1e3, DIMLESS), "kboe": (1e3, DIMLESS), "mmboe": (1e6, DIMLESS),
    "mbbl": (1e3 * 0.158987294928, _d(m=3)), "kbbl": (1e3 * 0.158987294928, _d(m=3)),
    "mmbbl": (1e6 * 0.158987294928, _d(m=3)), "bpd": (0.158987294928 / 86400, _d(m=3, s=-1)),
    "cf": (0.028316846592, _d(m=3)), "scf": (0.028316846592, _d(m=3)),
    "Mcf": (1e3 * 0.028316846592, _d(m=3)), "mcf": (1e3 * 0.028316846592, _d(m=3)), "mscf": (1e3 * 0.028316846592, _d(m=3)),
    "mmcf": (1e6 * 0.028316846592, _d(m=3)), "mmscf": (1e6 * 0.028316846592, _d(m=3)),
    "Bcf": (1e9 * 0.028316846592, _d(m=3)), "bcf": (1e9 * 0.028316846592, _d(m=3)),
    "Tcf": (1e12 * 0.028316846592, _d(m=3)), "tcf": (1e12 * 0.028316846592, _d(m=3)),
    "bcm": (1e9, _d(m=3)), "BCM": (1e9, _d(m=3)), "mmbtu": (1.05505585262e9, _d(kg=1, m=2, s=-2)),
    # v2.13e（审查发现）：4 个字符以下的名字查表时不按小写查，大写 / 首字母大写的写法要单列（否则 MCF/d 还是计数名词、按 1 换成 boe/d）；
    # 补上 bpd 系列、ccf（= 100 cf）、cfs（立方英尺/秒，不是 cf 的复数）
    "CF": (0.028316846592, _d(m=3)), "SCF": (0.028316846592, _d(m=3)), "MCF": (1e3 * 0.028316846592, _d(m=3)),
    "BCF": (1e9 * 0.028316846592, _d(m=3)), "TCF": (1e12 * 0.028316846592, _d(m=3)), "Bcm": (1e9, _d(m=3)),
    "BBL": (0.158987294928, _d(m=3)), "Bbl": (0.158987294928, _d(m=3)), "BPD": (0.158987294928 / 86400, _d(m=3, s=-1)),
    "mbpd": (1e3 * 0.158987294928 / 86400, _d(m=3, s=-1)), "kbpd": (1e3 * 0.158987294928 / 86400, _d(m=3, s=-1)),
    "mmbpd": (1e6 * 0.158987294928 / 86400, _d(m=3, s=-1)),
    "ccf": (100 * 0.028316846592, _d(m=3)), "Ccf": (100 * 0.028316846592, _d(m=3)), "CCF": (100 * 0.028316846592, _d(m=3)),
    "cfs": (0.028316846592, _d(m=3, s=-1)), "CFS": (0.028316846592, _d(m=3, s=-1)),
    # v2.13f（第二轮审查）：吨油当量（41.868 GJ）；Mtoe / mtoe / MTOE 都是百万吨（4 个字符以上按小写查到 mtoe）
    "toe": (41.868e9, _d(kg=1, m=2, s=-2)), "TOE": (41.868e9, _d(kg=1, m=2, s=-2)),
    "ktoe": (1e3 * 41.868e9, _d(kg=1, m=2, s=-2)), "mtoe": (1e6 * 41.868e9, _d(kg=1, m=2, s=-2)),
    # v2.13g（第三轮审查）：EIA / Energy Star 的 kBtu、TBtu，十亿吨油当量 Gtoe，十亿桶 Bbbl、十亿标准立方英尺 Bscf，千 cfs
    "kbtu": (1e3 * 1055.05585262, _d(kg=1, m=2, s=-2)), "tbtu": (1e12 * 1055.05585262, _d(kg=1, m=2, s=-2)),
    "gtoe": (1e9 * 41.868e9, _d(kg=1, m=2, s=-2)), "bbbl": (1e9 * 0.158987294928, _d(m=3)),
    "bscf": (1e9 * 0.028316846592, _d(m=3)), "kcfs": (1e3 * 0.028316846592, _d(m=3, s=-1)),
    # v2.13g（第三轮审查）：这几个以前是计数名词（系数 1），换成 % 或 1 时静默差 100 到 10^9 倍；MM boe/d 的 MM = 百万（油气 / 金融写法）
    "PCT": (0.01, DIMLESS), "Pct": (0.01, DIMLESS), "pp": (0.01, DIMLESS), "bp": (1e-4, DIMLESS), "ppb": (1e-9, DIMLESS),
    "PPM": (1e-6, DIMLESS), "PPB": (1e-9, DIMLESS), "MM": (1e6, DIMLESS),
    "kmph": (1000 / 3600, _d(m=1, s=-1)), "dwt": (1e3, M), "DWT": (1e3, M),   # 载重吨按公吨计
    # 能量 / 功率 / 力 / 压强 / 频率
    "J": (1.0, _d(kg=1, m=2, s=-2)), "joule": (1.0, _d(kg=1, m=2, s=-2)),
    "Wh": (3600.0, _d(kg=1, m=2, s=-2)),
    "cal": (4.184, _d(kg=1, m=2, s=-2)), "calorie": (4.184, _d(kg=1, m=2, s=-2)),
    "kcal": (4184.0, _d(kg=1, m=2, s=-2)), "Cal": (4184.0, _d(kg=1, m=2, s=-2)),
    "BTU": (1055.05585262, _d(kg=1, m=2, s=-2)), "Btu": (1055.05585262, _d(kg=1, m=2, s=-2)),
    "W": (1.0, _d(kg=1, m=2, s=-3)), "watt": (1.0, _d(kg=1, m=2, s=-3)),
    "hp": (745.69987158227022, _d(kg=1, m=2, s=-3)), "horsepower": (745.69987158227022, _d(kg=1, m=2, s=-3)),
    "N": (1.0, _d(kg=1, m=1, s=-2)), "newton": (1.0, _d(kg=1, m=1, s=-2)),
    "Pa": (1.0, _d(kg=1, m=-1, s=-2)), "pascal": (1.0, _d(kg=1, m=-1, s=-2)),
    "atm": (101325.0, _d(kg=1, m=-1, s=-2)), "bar": (1e5, _d(kg=1, m=-1, s=-2)),
    "psi": (6894.757293168, _d(kg=1, m=-1, s=-2)),
    "Hz": (1.0, _d(s=-1)), "hertz": (1.0, _d(s=-1)),
    # 速度简写
    "mph": (1609.344 / 3600, _d(m=1, s=-1)), "kph": (1000 / 3600, _d(m=1, s=-1)),
    "knot": (1852 / 3600, _d(m=1, s=-1)),
    # 数据（十进制前缀，与 pint 一致）
    "B": (1.0, BYTE), "byte": (1.0, BYTE), "bit": (0.125, BYTE), "b": (0.125, BYTE),
    # 货币
    "USD": (1.0, USD), "usd": (1.0, USD), "dollar": (1.0, USD), "cent": (0.01, USD),
    # 金融里常见的写法
    "mt": (1e3, M), "MT": (1e3, M), "bn": (1e9, DIMLESS), "mn": (1e6, DIMLESS), "mln": (1e6, DIMLESS),
    "century": (100 * YEAR, T), "centuries": (100 * YEAR, T),
}

# v2.13f（第二轮审查）：油气单位按小写查的表（键都按 SPE 惯例：mcf = 千、mmcf = 百万）；OIL_GAS_LIKE = 长得像油气单位、表里又没有的写法
# （kcf、Gboe、kBtu……）：报错，不当计数名词按 1 换算
OIL_GAS_CI = {k.lower(): v for k, v in UNITS.items()
              if re.fullmatch(r"(?i)(?:[kmbt]|mm)?(?:s?cf|cfs|boe|bbl|bpd|bcm|btu|toe)|ccf", k)}
OIL_GAS_LIKE = re.compile(r"(?i)(?:[kmgbt]|mm)?(?:s?cfe?|boe|bo|bbl|bbloe|bpd|btu|toe)s?|mmb")   # v2.13g：+ MMscfe、MMBO、MMb

# 有量纲、但不在本表维度里的单位：报错，不能当计数名词吞掉
UNSUPPORTED = {"degree", "degrees", "deg", "celsius", "fahrenheit", "kelvin", "rad", "radian", "radians", "sr",
               "db", "decibel", "decibels", "amp", "amps", "ampere", "amperes", "mol", "mole", "moles",
               "volt", "volts", "ah", "mah", "lux", "lumen", "lumens", "candela", "tesla", "gauss", "ohm", "ohms",
               "coulomb", "farad", "henry", "sievert", "gray", "becquerel", "curie", "rem", "dpi",
               # v2.13e：立方英尺当量（气换成油的折算各公司不同），不能当计数名词、按 1 换成 boe
               "cfe", "mcfe", "mmcfe", "bcfe", "tcfe",
               "bps"}   # v2.13g：bps 既可能是基点、也可能是比特 / 秒，不猜

# 可加 SI 前缀的符号与长名
PREFIX = {"k": 1e3, "M": 1e6, "G": 1e9, "T": 1e12, "P": 1e15, "c": 1e-2, "m": 1e-3, "u": 1e-6, "µ": 1e-6, "μ": 1e-6, "n": 1e-9}
PREFIXABLE = {"m", "g", "s", "L", "l", "W", "J", "Wh", "B", "b", "bit", "Hz", "N", "Pa", "t", "cal", "eV"} - {"eV"}
LONG_PREFIX = {"kilo": 1e3, "mega": 1e6, "giga": 1e9, "tera": 1e12, "peta": 1e15, "centi": 1e-2, "milli": 1e-3, "micro": 1e-6, "nano": 1e-9}
LONG_PREFIXABLE = {"meter", "metre", "gram", "liter", "litre", "second", "watt", "joule", "byte", "bit", "hertz", "newton", "pascal", "tonne", "calorie"}

# strict 模式下放行的计数名词（来自官方 units.txt：person = people，sheet）
TARGET_COUNT_NOUNS = {"person", "people", "persons", "sheet", "sheets"}

PHRASES = [
    (r"\bmetric\s+tonnes?\b|\bmetric\s+tons?\b", "tonne"),
    (r"\bshort\s+tons?\b", "ton"),
    (r"\blight[\s-]+years?\b", "ly"),
    (r"\bbarrels?\s+of\s+oil\s+equivalents?\b", "boe"),   # v2.13c
    (r"\bUS\s*\$|\$", " USD "),
    (r"\bper\b", "/"),
]
SQUARE = re.compile(r"\b(?:square|sq\.?)\s+([A-Za-z]+)", re.I)
CUBIC = re.compile(r"\b(?:cubic|cu\.?)\s+([A-Za-z]+)", re.I)
TOKEN = re.compile(r"\s*(\*\*|\*|/|\(|\)|[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|[A-Za-z%µμ$_][A-Za-z0-9%µμ_.]*)")


class UnitError(ValueError):
    pass


class Unit(NamedTuple):
    factor: float          # 1 该单位 = factor 个 SI 基单位组合
    dims: tuple            # ((base, Fraction exp), ...) 排序后
    count_nouns: tuple = ()  # 被当作无量纲的表外名词


def dims_mul(a, b, k=1):
    out = dict(a)
    for base, e in b:
        out[base] = out.get(base, Fraction(0)) + e * k
    return tuple(sorted((x, e) for x, e in out.items() if e != 0))


def dims_pow(a, k):
    k = Fraction(k).limit_denominator(1000)
    return tuple(sorted((x, e * k) for x, e in a if e * k != 0))


def dims_str(d) -> str:
    if not d:
        return "dimensionless"
    return "*".join(f"{b}" if e == 1 else f"{b}**{e}" for b, e in d)


def _lookup(name: str):
    """返回 (factor, dims) 或 None。"""
    if name in UNITS:
        return UNITS[name]
    n = name.rstrip(".")
    if n.lower() == "bps":   # v2.13g：基点还是比特 / 秒，不猜（不走下面的复数规则读成 bp）；在 UNSUPPORTED 里报错
        return None
    if n.lower() in OIL_GAS_CI:   # v2.13f：油气写法不分大小写（Scf、MCf、BCf）；小写时 M = 千，和 SPE 惯例一致（v2.13g：去掉末尾的点再查）
        return OIL_GAS_CI[n.lower()]
    if n in UNITS:
        return UNITS[n]
    candidates = [n]
    if len(n) >= 4:
        candidates.append(n.lower())
    for c in list(candidates):
        if len(c) >= 4 and c.endswith("es") and c[:-2] in UNITS:
            return UNITS[c[:-2]]
        if len(c) >= 3 and c.endswith("s") and c[:-1] in UNITS and len(c[:-1]) >= 2:
            return UNITS[c[:-1]]
        if c in UNITS and c != n:
            return UNITS[c]
    # 短符号 + SI 前缀，如 km、kWh、GB、Mt
    if len(n) >= 2 and n[0] in PREFIX:
        rest = n[1:]
        if n[:1] == "m" and rest == "in":  # min 已在表里；防止 m+in
            return None
        if rest in PREFIXABLE and rest in UNITS:
            f, d = UNITS[rest]
            return f * PREFIX[n[0]], d
    # 长名 + 长前缀，如 kilometres、kilobyte
    low = n.lower()
    for p, pf in LONG_PREFIX.items():
        if low.startswith(p):
            rest = low[len(p):]
            for r in (rest, rest[:-1] if rest.endswith("s") else rest):
                if r in LONG_PREFIXABLE:
                    f, d = UNITS[r]
                    return f * pf, d
    return None


def _normalise(s: str) -> str:
    s = s.strip()
    for pat, rep in PHRASES:
        s = re.sub(pat, rep, s, flags=re.I)
    s = SQUARE.sub(r"\1**2", s)
    s = CUBIC.sub(r"\1**3", s)
    s = re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", "*", s)  # passenger-km、kilowatt-hours
    s = s.replace("^", "**").replace("·", "*").replace("×", "*").replace("²", "**2").replace("³", "**3")
    s = re.sub(r"\s*(\*\*|\*|/)\s*", r"\1", s)
    s = re.sub(r"\s+", "*", s.strip())
    if s.startswith("/"):
        s = "1" + s  # "per year" -> "1/year"
    return s


def parse_unit(text, strict: bool = False) -> Unit:
    if text is None:
        text = ""
    if not isinstance(text, str):
        raise UnitError(f"unit must be a string, got {type(text).__name__}")
    s = _normalise(text)
    if s.lower() in ("", "1", "-", "none", "n/a", "dimensionless", "unitless", "count", "number"):
        return Unit(1.0, DIMLESS, ())
    pos, toks = 0, []
    while pos < len(s):
        m = TOKEN.match(s, pos)
        if not m or m.end() == pos:
            raise UnitError(f"cannot tokenise unit {text!r} at {s[pos:]!r}")
        toks.append(m.group(1))
        pos = m.end()
    state = {"i": 0, "nouns": []}

    def peek():
        return toks[state["i"]] if state["i"] < len(toks) else None

    def take():
        t = peek()
        state["i"] += 1
        return t

    def number(tok):
        try:
            return float(tok)
        except (TypeError, ValueError):
            return None

    def atom():
        tok = take()
        if tok is None:
            raise UnitError(f"unexpected end of unit {text!r}")
        if tok in ("*", "/", "**", ")"):
            raise UnitError(f"unexpected {tok!r} in unit {text!r}")
        if tok == "(":
            f, d = term()
            if take() != ")":
                raise UnitError(f"unbalanced parentheses in {text!r}")
        elif number(tok) is not None:
            f, d = number(tok), DIMLESS
        else:
            name = tok
            hit = _lookup(name)
            if hit is None:
                # 粘连指数，如 m2、km3
                m2 = re.fullmatch(r"([A-Za-z]+)([23])", name)
                if m2 and _lookup(m2.group(1)) is not None:
                    f0, d0 = _lookup(m2.group(1))
                    hit = (f0 ** int(m2.group(2)), dims_pow(d0, int(m2.group(2))))
            if hit is None:
                if name.rstrip(".").lower() in UNSUPPORTED:
                    raise UnitError(f"unsupported unit {name!r} in {text!r} (dimension not in table)")
                if OIL_GAS_LIKE.fullmatch(name.rstrip(".")):   # v2.13f
                    raise UnitError(f"unrecognised oil / gas unit {name!r} in {text!r}")
                if len(name.rstrip(".")) < 2:
                    raise UnitError(f"ambiguous one-letter unit {name!r} in {text!r}")
                if strict and name.lower() not in TARGET_COUNT_NOUNS:
                    raise UnitError(f"unknown unit {name!r} in {text!r}")
                state["nouns"].append(name)
                hit = (1.0, DIMLESS)
            f, d = hit
        if peek() == "**":
            take()
            e = number(take())
            if e is None or abs(e) > 6:
                raise UnitError(f"bad exponent in {text!r}")
            f, d = f ** e, dims_pow(d, e)
        return f, d

    def term():
        f, d = atom()
        while peek() in ("*", "/"):
            op = take()
            f2, d2 = atom()
            if op == "*":
                f, d = f * f2, dims_mul(d, d2)
            else:
                f, d = f / f2, dims_mul(d, d2, -1)
        return f, d

    f, d = term()
    if state["i"] != len(toks):
        raise UnitError(f"trailing tokens in unit {text!r}")
    if not (math.isfinite(f) and f > 0):
        raise UnitError(f"non-positive unit factor in {text!r}")
    return Unit(f, d, tuple(state["nouns"]))


class UnitMismatch(ValueError):
    pass


def convert(value: float, src: Unit, dst: Unit) -> float:
    if src.dims != dst.dims:
        raise UnitMismatch(f"{dims_str(src.dims)} vs {dims_str(dst.dims)}")
    return value * src.factor / dst.factor
