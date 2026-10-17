"""单位和量纲（v2.7 U0，设计见 UNITS_PLAN.md「单位注册表」）：agent 用的单位注册表，基于 pint 0.26.1。
本阶段只有这个模块和它的测试，还没有接入任何流程（U1 规划钉死单位、U2 formula_mc 量纲检查才接）。不用也不改基线的 units.py。

注册表（模块级的一个 pint UnitRegistry，UREG；重定义直接报错：pint 默认只记一条 warning，新定义会悄悄覆盖 pint 原有的单位）：
- pint 已有的单位照 pint 的意思：kg、g、t（= metric_ton = tonne）、lb、day、week、month（= year / 12）、year（= 365.25 day）、percent……
  带前缀的拆法只接受公制单位（km、mg、kWh、MWh）；units -> micro-nit、app -> atto-point 这类偶然拆法不认。
- 货币 CURRENCIES 各是独立的基本维度，互相不换算（汇率是证据，不是常数），混用就是量纲不符；代码大小写都认（usd -> USD）。
- 计数名词：pint 不认识的英文单词（person、slice、pizza、visit、birth、passenger、vehicle、eater……）第一次出现时自动定义成
  各自的基本维度。先归一复数和不规则形式：people / persons / capita -> person，children -> child，men -> man，women -> woman，
  -ies -> -y，-sses / -xes / -ches / -shes 去掉 es（classes -> class、boxes -> box），其余词尾的 s 去掉（ss、us、is 结尾的不去：
  glass、bus、basis）；全大写缩写的复数先去掉小写 s（GPUs -> GPU）。带大写字母的词先按原样、再按小写查 pint，最后才单数化
  （Inches -> inch）。名词写得前后不一致（eater 对 person）就是量纲不符。
  一个词怎么解释只看 pint 自带的单位，不看之前自动定义过哪些名词，所以结果不随解析顺序变化（TEU 解析几次都是名词 teu）。
  pint 只能靠前缀或复数拆出来的计数名词（NOUNS：unit = micro-nit、bus = bu + s、app = atto-point）也当计数名词；
  pint 的读法和常见用法不同的词（AMBIGUOUS：ton 是短吨、mt 是毫吨、calorie / cal 是小卡、barrel / bbl 是 31.5 加仑、
  point、bar、bag、shot、chain）报错并提示写法。
  pint 读成「无量纲、系数不是 1」的词一律报错（degree、grade、turn / cycle / revolution / circle、mil、mas、pi、alpha、g_e……：
  量纲和 1、share 相同，系数却是 0.01745、6.283 这类，混用时会悄悄算错）；DIMLESS_OK 除外（percent、percentage_point、basis_point、
  ppm、permille，以及 bit / byte 一族，带公制前缀的也算）。
- 百分数：percent、%、pct、percentage、per cent = 0.01；percentage point / pp = 0.01，basis point / bp / bps = 0.0001。
- 无量纲：1、dimensionless、share、ratio、fraction、proportion、factor、multiplier。
- 时间：quarter = 3 个月（pint 自带的 quarter 是 28 磅），decade = 10 年（pint 自带的 decade 是对数单位），annum = year。
  kilo / kilos = kilogram（pint 会读成 kilosecond）。

写法：
- per 把后面一段整个放进分母：'slices per person per day' = slice / person / day；'births per 1,000 people' = birth / (1000 person)。
  / * ^ ** 和括号照算术（'/' 之后只除紧跟的一项，同 pint）。
- 连字符连起来的一串单词是一个整体的乘积（person-day），在 '/' 之后也整体做分母：'slices/eater-day' = 'slices per eater-day'
  = slice / (eater * day)。square / sq / cubic X、X squared / cubed 是平方 / 立方。连字符串里每一项的指数只作用在这一项上
  （'kg-m^2' = kg * m^2，'square km-person' = km^2 * person）。pint 的多词单位名可以用空格写（metric ton、oil barrel）。
- 单位里的数字只能做比率的基数，紧跟在 per 或 '/' 之后（'per 1,000 people'、'kcal per 100 g'、'birth/(1000 person)'），倍数记在 unit 的
  magnitude 里，由代码换算；另外允许指数（m^2、s^-1）和单独的 1（'1'、'1/day'）。其他位置的数字报错（'2015 USD'、'1,000 tonnes'：
  证据的值已经按倍数乘过）；'1.000' 这种写法（1–9 开头、1–3 位、点、3 位）报错（可能是欧洲写法的 1000）。
  紧跟 '/' 的基数后面如果还有不在括号里的单位，报错（'USD/1000 people'：'/' 只除 1000，people 会乘上去；写 'USD/(1000 person)' 或 per）。
- 报错（返回错误文字，不抛异常）：or / and / vs 连起来的候选；of / in / at / a 这类虚词（'% of population'）；
  thousand / million 这类倍数词（值已经按倍数词乘过）；两个单词并排（'recreation visits'）；全大写又和 pint 的写法撞车（KG）；
  AMBIGUOUS 里的词；无量纲、系数不是 1 的词（degree）；摄氏 / 华氏、dB 这类非乘性单位（带偏移或对数）；空括号；非英文单词；
  无法解析的写法。

公开函数（都不抛异常；error 为 "" 表示成功，否则是一句给裁判修正轮看的英文）：
- parse_unit(text) -> (unit, error)：unit 是 pint Quantity，magnitude 是单位里的倍数（一般 1.0；'birth/(1000 person)' 是 0.001）。
- formula_unit(formula, units) -> (unit, error)：formula 是公式文字或 expr.Formula，units 是 {输入名: 单位文字或 unit}。
  沿 expr.py 的语法树推导结果的单位（只读 Formula.root，不改 expr.py）：乘除、常数次幂、sqrt 照 pint；
  加减和 min / max / mean 的各项只要求量纲相同（kg 和 t 算相同、percent 和 1 算相同），结果取第一项的单位。
- convert_factor(src, dst) -> (factor, error)：src 的 1 个单位等于多少个 dst（kg/year -> t/day 是 1 / 365250）；
  量纲不同报 'X cannot be converted to Y'。
- base_factor(unit) -> (factor, error)：换到 pint 基本单位的系数（g -> kilogram 0.001，day -> second 86400，percent 0.01）；
  系数不是有限的正数时报错（同 convert_factor）。
- text(unit) -> str：给人看的写法（'kilogram * pizza / year'；倍数不是 1 时前面带倍数，如 '0.001 birth / person'）。

样本换算的做法（U2 一律这样做）：每个输入的样本先乘 base_factor(输入的单位) 换到基本单位，再代入公式；公式的结果就在基本单位里，
用 convert_factor(formula_unit 的结果, 目标单位) 检查能不能换（不能换就是给修正轮的错误），再除以 base_factor(目标单位) 得到目标单位的值。
不要把原始样本代入公式后直接乘 convert_factor：这只对纯乘除、乘方的公式成立；有加减或 min / max / mean 时会悄悄算错
（'a * (1 - s)'，s 是 11 percent，原始值代入算成 1 - 11；kg + t 算成 kg + kg）。
"""
import ast
import math
import re
import threading

import pint

from ..expr import Formula, FormulaError, _const

UREG = pint.UnitRegistry(on_redefinition="raise")
CURRENCIES = ("USD", "EUR", "GBP", "JPY", "CNY", "KRW", "TWD", "CAD", "AUD", "CHF", "HKD", "INR")
for _c in CURRENCIES:
    UREG.define(f"{_c} = [currency_{_c}]")
UREG.define("percentage_point = 0.01")
UREG.define("basis_point = 1e-4")
UREG.define("quarter_year = 3 * month")
UREG.define("decade_year = 10 * year")

ALIASES = {"pct": "percent", "percentage": "percent", "pp": "percentage_point", "bp": "basis_point",
           "quarter": "quarter_year", "decade": "decade_year", "annum": "year", "kilo": "kilogram"}
DIMLESS = {"dimensionless", "share", "ratio", "fraction", "proportion", "factor", "multiplier"}
IRREGULAR = {"people": "person", "persons": "person", "capita": "person", "children": "child", "men": "man", "women": "woman"}
NOUNS = {"unit", "bus", "app"}
_CAL = "pint reads it as a small calorie (4.184 J), but food calories are kilocalories; write 'kcal'"
_BBL = "pint reads it as a 31.5-gallon barrel; for oil write 'oil_barrel' (42 gallons)"
AMBIGUOUS = {"ton": "pint reads it as a 2000 lb short ton; write 't' for metric tons or 'short_ton'",
             "mt": "pint reads 'mt' as a milli-tonne (1 kg) and 'Mt' as a megatonne; write 't' for metric tons or 'megatonne'",
             "calorie": _CAL, "cal": _CAL, "barrel": _BBL, "bbl": _BBL,
             "point": "pint reads it as a printer's point (a length); write 'percentage_point' or 'basis_point', or another word",
             "bar": "pint reads it as a unit of pressure; write another word",
             "bag": "pint reads it as a unit of mass; write another word",
             "shot": "pint reads it as a unit of volume; write another word (e.g. 'dose')",
             "chain": "pint reads it as a unit of length; write another word"}
DIMLESS_OK = {"percent", "percentage_point", "basis_point", "ppm", "permille", "bit", "byte"}   # 无量纲、系数不是 1，但照 pint 的意思用
ALTERNATIVES = {"or", "and", "vs", "versus"}
NOT_UNITS = {"a", "an", "the", "of", "in", "on", "at", "as", "to", "for", "by", "from", "with", "each", "every", "than"}
SCALE_WORDS = {"thousand", "million", "billion", "trillion"}
METRIC = {"meter", "gram", "second", "liter", "metric_ton", "watt", "watt_hour", "joule", "calorie", "byte", "bit", "hertz",
          "pascal", "volt", "ampere", "newton", "mole"}
POWER_BEFORE = {"square": 2, "sq": 2, "cubic": 3}
POWER_AFTER = {"squared": 2, "cubed": 3}
NON_MULTIPLICATIVE = "non-multiplicative unit (offset or logarithmic, e.g. degC, dB) is not supported"

_TOKEN = re.compile(r"(?P<num>\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)|(?P<word>[^\W\d]+)|(?P<op>\*\*|[*/()%^-])")
_LOCK = threading.RLock()     # 注册表是模块级的、会自动加名词：解析时加锁
_nouns = set()                # 已自动定义的计数名词


class _Bad(ValueError):
    pass


def _singular(w: str) -> str:
    if w in IRREGULAR:
        return IRREGULAR[w]
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 4 and w.endswith(("sses", "xes", "ches", "shes")):
        return w[:-2]
    if len(w) > 2 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def _pint_name(w: str) -> str:
    """pint 自带的单位（不算自动定义的名词）认识这个词时返回它的规范名（前缀 + 单位，如 kilogram）；带前缀的只接受公制单位。
    不认识返回 ""。"""
    try:
        cands = UREG.parse_unit_name(w)
    except Exception:
        return ""
    for prefix, name, _suffix in cands:
        if name in _nouns:
            continue
        if not prefix or name in METRIC:
            return prefix + name
    return ""


def _noun(s: str, w: str) -> str:
    if s in _nouns:
        return s
    if not re.fullmatch(r"[a-z]{2,40}", s):
        raise _Bad(f"{w!r} is not a known unit" + ("" if w.isascii() else "; write units in English"))
    UREG.define(f"{s} = [n_{s}]")
    _nouns.add(s)
    return s


def _word(word: str) -> tuple:
    """一个单词 -> ("per",) / ("pre", n) / ("post", n) / ("name", pint 名字)。"""
    w = word[:-1] if len(word) > 2 and word.endswith("s") and word[:-1].isupper() else word   # 缩写的复数：GPUs -> GPU
    lw = w.lower()
    if lw == "per":
        return ("per", None)
    if lw in POWER_BEFORE:
        return ("pre", POWER_BEFORE[lw])
    if lw in POWER_AFTER:
        return ("post", POWER_AFTER[lw])
    if lw in NOT_UNITS:
        raise _Bad(f"{word!r} is not a unit word; write only units (e.g. 'percent', not '% of population')")
    s = _singular(lw)
    amb = sorted({lw, s, lw[:-1] if lw.endswith("s") else lw} & AMBIGUOUS.keys())   # calories：pint 的单数是 calorie
    if amb:
        raise _Bad(f"{word!r} is ambiguous: {AMBIGUOUS[amb[0]]}")
    if s in SCALE_WORDS:
        raise _Bad(f"{word!r} is a scale word: the value is already scaled, so write the plain unit (e.g. 'USD/year'); "
                   "for a rate per thousand write the number (e.g. 'birth/(1000 person)')")
    if w.upper() in CURRENCIES:
        return ("name", w.upper())
    if s in DIMLESS:
        return ("name", "dimensionless")
    if s in ALIASES:
        return ("name", ALIASES[s])
    if s in NOUNS:
        return ("name", _noun(s, word))
    name = _pint_name(w)
    if not name:
        name = _pint_name(lw) or _pint_name(s)
        if w.isupper() and len(w) > 1 and name:
            raise _Bad(f"{word!r} is ambiguous in capitals; write it as pint does (e.g. 't', 'kg', 'MWh') or as a lowercase noun")
        if not name:
            return ("name", _noun(s, word))
    _dimless_factor(word, name)
    return ("name", name)


def _dimless_factor(word: str, name: str):
    """pint 读成「无量纲、系数不是 1」的单位（degree、turn、grade、mil、mas、pi、g_e……）报错：和 1、share、percent 混用时量纲不报错，
    系数却是错的。DIMLESS_OK（百分数一族、bit / byte 一族，带前缀的也算）照 pint 的意思用；非乘性单位（dB）留给 _parse 报。"""
    q = UREG.Quantity(1, name)
    if not q._is_multiplicative:
        return
    q = q.to_base_units()
    f = float(q.magnitude)
    if q.dimensionless and abs(f - 1) > 1e-12 and not any(n in DIMLESS_OK for _p, n, _s in UREG.parse_unit_name(name)):
        raise _Bad(f"{word!r} is ambiguous: pint reads it as {name} (a dimensionless factor {f:.4g}); write another word")


def _tokens(s: str) -> list:
    """[(kind, value)]；kind 是 num / word / op（'^' 记成 '**'）。"""
    out, pos = [], 0
    while pos < len(s):
        if s[pos].isspace():
            pos += 1
            continue
        m = _TOKEN.match(s, pos)
        if not m:
            raise _Bad(f"character {s[pos]!r} is not allowed")
        out.append((m.lastgroup, "**" if m.group() == "^" else m.group()))
        pos = m.end()
    return out


def _join(toks: list) -> list:
    """pint 的多词单位名（metric ton、percentage points）用空格或连字符写时并成一个词。"""
    out = []
    for t in toks:
        if t[0] == "word" and out and out[-1][0] == "word" and _pint_name(f"{out[-1][1]}_{t[1]}".lower()):
            out[-1] = ("word", f"{out[-1][1]}_{t[1]}".lower())
            continue
        if (t[0] == "word" and len(out) >= 2 and out[-1][1] == "-" and out[-2][0] == "word"
                and _pint_name(f"{out[-2][1]}_{t[1]}".lower())):
            out.pop()
            out[-1] = ("word", f"{out[-1][1]}_{t[1]}".lower())
            continue
        out.append(t)
    return out


def _term_end(items: list, j: int):
    """items[j] 开头是不是一项 [square / cubic] 单位 [^ 指数 | squared / cubed]：是就返回这一项之后的下标，不是返回 None。"""
    n = len(items)
    if j < n and items[j][0] == "pre":
        j += 1
    if not (j < n and items[j][0] == "name"):
        return None
    j += 1
    if j < n and items[j][0] == "post":
        return j + 1
    if j + 1 < n and items[j] == ("op", "**"):
        e = j + 2 if items[j + 1] == ("op", "-") else j + 1
        if e < n and items[e][0] == "num":
            return e + 1
    return j


def _hyphens(items: list) -> list:
    """连字符连起来的一串单位（eater-day）整个加上括号，'/' 之后也整体做分母（同 per）。
    每一项的指数只作用在这一项上：'kg-m^2' = (kg * m^2)，'square km-person' = (km^2 * person)。"""
    out, k = [], 0
    while k < len(items):
        j, terms = _term_end(items, k), 1
        while j is not None and j + 1 < len(items) and items[j] == ("op", "-") and _term_end(items, j + 1) is not None:
            j, terms = _term_end(items, j + 1), terms + 1
        if terms > 1:
            out += [("op", "(")] + items[k:j] + [("op", ")")]
            k = j
        else:
            out.append(items[k])
            k += 1
    return out


def _number(items: list, k: int, v: str):
    """单位里的数字（不是指数）：只能是单独的 1，或紧跟在 per / '/'（中间可以有括号）之后做比率的基数。
    紧跟 '/' 又不在括号里的基数后面不能再有单位（'USD/1000 people' 会读成 0.001 USD * person）。"""
    if re.fullmatch(r"[1-9]\d{0,2}\.\d{3}", v):
        raise _Bad(f"number {v} is ambiguous ('.' may be a thousands separator); write {v.replace('.', '')} or {float(v):g}")
    if items[k - 1:k] == [("op", "/")] and k + 1 < len(items) and (items[k + 1][0] in ("name", "pre") or items[k + 1] in (("op", "("), ("op", "-"))):
        raise _Bad(f"number {v} right after '/' divides only itself, so the unit after it would multiply; "
                   "put the base and its unit in parentheses or use 'per' (e.g. 'USD/(1000 person)', 'USD per 1000 people')")
    if float(v) == 1:
        return
    j = k - 1
    while j >= 0 and items[j] == ("op", "("):
        j -= 1
    if j < 0 or not (items[j][0] == "per" or items[j] == ("op", "/")):
        raise _Bad(f"number {v} would multiply the unit; the value is already scaled, so write the plain unit (e.g. 'USD/year'); "
                   "a number is allowed only as a rate base right after 'per' or '/' (e.g. 'birth/(1000 person)')")


def _expr(items: list) -> str:
    """把解析好的项拼成 pint 表达式：per 的分母加括号，数字后面的单位补乘号，连字符变乘号。"""
    out, opened, depth, pre, exp_last = [], [], 0, None, False   # exp_last：上一个数字是指数（m^2 后面不补乘号）

    def operand_end():
        return bool(out) and out[-1] not in ("*", "/", "**", "(", "-")

    def close(d):
        while opened and opened[-1] == d:
            if out[-1] == "(":
                raise _Bad("nothing after 'per'")
            out.append(")")
            opened.pop()

    for k, (kind, v) in enumerate(items):
        prev = items[k - 1] if k else (None, None)
        nxt = items[k + 1] if k + 1 < len(items) else (None, None)
        starts = kind in ("name", "num", "pre") or (kind, v) == ("op", "(")
        if starts and operand_end():
            if prev[0] == "num" and kind != "num" and not exp_last:
                out.append("*")
            elif kind == "num":
                raise _Bad(f"number {v} after a unit; write exponents with ^ (e.g. m^2)")
            else:
                raise _Bad("two units side by side; use one word per unit (e.g. 'visit'), '*' or '-' for a product "
                           "(person*day), 'per' or '/' for a ratio")
        if pre is not None and kind != "name":
            raise _Bad("'square' / 'cubic' must be followed by a unit")
        if kind == "per":
            close(depth)
            if not operand_end():
                out.append("1")
            out += ["/", "("]
            opened.append(depth)
        elif kind == "pre":
            pre = v
        elif kind == "post":
            if not operand_end():
                raise _Bad("'squared' / 'cubed' must follow a unit")
            out += ["**", str(v)]
        elif kind in ("name", "num"):
            exp_last = kind == "num" and (out[-1:] == ["**"] or out[-2:] == ["**", "-"])
            if kind == "num" and not exp_last:
                _number(items, k, v)
            out.append(v)
            if pre is not None:
                out += ["**", str(pre)]
                pre = None
        elif v == "-":
            if prev == ("op", "**"):
                out.append("-")
            elif prev[0] in ("name", "num") and nxt[0] in ("name", "pre"):
                out.append("*")
            else:
                raise _Bad("'-' is only allowed between words (person-day) or in an exponent (s^-1)")
        elif v == "(":
            out.append("(")
            depth += 1
        elif v == ")":
            close(depth)
            depth -= 1
            if depth < 0:
                raise _Bad("unbalanced parentheses")
            if out[-1] == "(":
                raise _Bad("empty parentheses")
            out.append(")")
        else:   # * / **
            if not operand_end():
                raise _Bad(f"'{v}' must follow a unit (for a rate write e.g. '1/day' or 'per day')")
            if v == "/":
                close(depth)
            out.append(v)
    if pre is not None:
        raise _Bad("'square' / 'cubic' must be followed by a unit")
    if depth:
        raise _Bad("unbalanced parentheses")
    close(0)
    return "".join(out)


def _parse(t: str):
    alt = sorted({w.lower() for w in re.findall(r"[^\W\d]+", t)} & ALTERNATIVES)
    if alt:
        raise _Bad(f"{alt[0]!r} gives alternatives; pin exactly one unit")
    s = re.sub(r"\bper\s+cent\b", "percent", t, flags=re.I)
    s = re.sub(r"(?<=\d),(?=\d{3}\b)", "", s)
    items = []
    for kind, v in _join(_tokens(s)):
        if kind == "word":
            items.append(_word(v))
        elif v == "%":
            items.append(("name", "percent"))
        else:
            items.append((kind, v))
    try:
        q = UREG.parse_expression(_expr(_hyphens(items)))
    except (pint.errors.OffsetUnitCalculusError, pint.errors.LogarithmicUnitCalculusError):
        raise _Bad(NON_MULTIPLICATIVE) from None
    q = q if isinstance(q, UREG.Quantity) else UREG.Quantity(q)
    if not q._is_multiplicative:
        raise _Bad(NON_MULTIPLICATIVE)
    m = float(q.magnitude)
    if not (math.isfinite(m) and m > 0):
        raise _Bad("scale must be a positive number")
    return UREG.Quantity(m, q.units)


def parse_unit(text) -> tuple:
    """单位文字 -> (unit, error)。unit 是 pint Quantity（magnitude = 单位里的倍数）；失败时 unit 为 None。"""
    if not isinstance(text, str) or not text.strip():
        return None, "unit is empty"
    t = text.strip()
    with _LOCK:
        try:
            return _parse(t), ""
        except _Bad as e:
            return None, f"unit {t!r}: {e}"
        except Exception as e:   # pint 的语法 / 定义错误：变成错误文字，不抛到图里
            return None, f"unit {t!r}: cannot parse ({type(e).__name__}: {e})"[:300]


def _unit(u) -> tuple:
    if isinstance(u, UREG.Quantity):
        return u, ""
    return parse_unit(u)


def text(unit) -> str:
    """unit -> 给人看的写法；None -> ""。"""
    if unit is None:
        return ""
    with _LOCK:
        units, m = str(unit.units), float(unit.magnitude)
    return units if m == 1 else f"{m:g} {units}"


def _same(a, b, what: str):
    if a.dimensionality != b.dimensionality:
        raise _Bad(f"{what} {text(a)} and {text(b)}")


def _walk(node, env):
    if isinstance(node, ast.BinOp):
        a = _walk(node.left, env)
        if isinstance(node.op, ast.Pow):
            e = _const(node.right)
            return a ** (int(e) if e == int(e) else e)
        b = _walk(node.right, env)
        if isinstance(node.op, (ast.Add, ast.Sub)):
            _same(a, b, "adding/subtracting")
            return a
        return a * b if isinstance(node.op, ast.Mult) else a / b
    if isinstance(node, ast.UnaryOp):
        return _walk(node.operand, env)
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Constant):
        return UREG.Quantity(1.0)
    if isinstance(node, ast.Call):
        args = [_walk(x, env) for x in node.args]
        if node.func.id == "sqrt":
            return args[0] ** 0.5
        for b in args[1:]:
            _same(args[0], b, f"{node.func.id}() of mixed units:")
        return args[0]
    raise _Bad(f"cannot derive the unit of {type(node).__name__}")


def formula_unit(formula, units: dict) -> tuple:
    """公式 + {输入名: 单位} -> (公式结果的 unit, error)。加减 / min / max / mean 只查量纲：样本要先换到基本单位（见模块 docstring）。"""
    with _LOCK:
        try:
            f = formula if isinstance(formula, Formula) else Formula(formula)
        except FormulaError as e:
            return None, f"formula: {e}"
        env = {}
        for name in sorted(f.names):
            if name not in (units or {}):
                return None, f"input {name}: no unit"
            u, err = _unit(units[name])
            if err:
                return None, f"input {name}: {err}"
            env[name] = u
        try:
            return _walk(f.root, env), ""
        except _Bad as e:
            return None, str(e)
        except Exception as e:
            return None, f"formula units: {type(e).__name__}: {e}"[:300]


def convert_factor(src, dst) -> tuple:
    """(src 的 1 个单位等于多少个 dst, error)。src / dst 是单位文字或 unit。"""
    with _LOCK:
        a, err = _unit(src)
        if err:
            return None, err
        b, err = _unit(dst)
        if err:
            return None, err
        try:
            if a.dimensionality != b.dimensionality:
                return None, f"{text(a)} cannot be converted to {text(b)}"
            f = float(a.to(b.units).magnitude) / float(b.magnitude)
        except Exception as e:
            return None, f"cannot convert {text(a)} to {text(b)} ({type(e).__name__}: {e})"[:300]
    if not (math.isfinite(f) and f > 0):
        return None, f"cannot convert {text(a)} to {text(b)} (factor {f})"
    return f, ""


def base_factor(unit) -> tuple:
    """(unit 换到 pint 基本单位的系数, error)。"""
    with _LOCK:
        a, err = _unit(unit)
        if err:
            return None, err
        try:
            f = float(a.to_base_units().magnitude)
        except Exception as e:
            return None, f"cannot convert {text(a)} to base units ({type(e).__name__}: {e})"[:300]
    if not (math.isfinite(f) and f > 0):
        return None, f"cannot convert {text(a)} to base units (factor {f})"
    return f, ""
