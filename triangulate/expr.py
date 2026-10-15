"""白名单表达式求值器：只接受 + - * / **、括号、min/max/mean/sqrt、输入名和极少数常量。

用 ast.parse 解析成语法树，再逐节点检查类型；不调用 eval/exec，不允许属性访问、下标、其他函数。
同一棵树支持三种求值：标量求值、向量求值（Monte Carlo 样本列表）、量纲推导。
"""
import ast
import math
import re
from fractions import Fraction

from .units import DIMLESS, dims_mul, dims_pow, dims_str

MAX_LEN = 400
MAX_NODES = 200
MAX_EXP = 4
FUNCS = {"min", "max", "sqrt", "mean"}
NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


class FormulaError(ValueError):
    pass


class DimError(ValueError):
    pass


def _const(node):
    """返回常量节点（含一元负号）的数值，否则 None。"""
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = _const(node.operand)
        if v is not None:
            return -v if isinstance(node.op, ast.USub) else v
    return None


class Formula:
    def __init__(self, text: str):
        if not isinstance(text, str) or not text.strip():
            raise FormulaError("formula must be a non-empty string")
        if len(text) > MAX_LEN:
            raise FormulaError(f"formula longer than {MAX_LEN} characters")
        self.text = text.strip()
        src = self.text.replace("^", "**")
        try:
            tree = ast.parse(src, mode="eval")
        except SyntaxError as e:
            raise FormulaError(f"syntax error: {e.msg}") from None
        self.names = set()
        self._count = 0
        self.root = self._check(tree.body, exponent=False)

    def _check(self, node, exponent: bool):
        self._count += 1
        if self._count > MAX_NODES:
            raise FormulaError(f"formula has more than {MAX_NODES} nodes")
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
            self._check(node.left, exponent=False)
            if isinstance(node.op, ast.Pow):
                e = _const(node.right)
                if e is None:
                    raise FormulaError("exponent must be a plain number")
                if abs(e) > MAX_EXP:
                    raise FormulaError(f"exponent {e} outside [-{MAX_EXP}, {MAX_EXP}]")
                self._count += 1
            else:
                self._check(node.right, exponent=False)
            return node
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            self._check(node.operand, exponent=exponent)
            return node
        if isinstance(node, ast.Name):
            if node.id in FUNCS:
                raise FormulaError(f"{node.id!r} is a function name, not an input")
            if not NAME_RE.match(node.id):
                raise FormulaError(f"bad name {node.id!r}")
            self.names.add(node.id)
            return node
        if isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise FormulaError(f"constant {node.value!r} not allowed")
            if float(node.value) != 1.0:
                raise FormulaError(f"numeric constant {node.value!r} not allowed (only 1 and exponents); make it a named input")
            return node
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in FUNCS:
                raise FormulaError("only min(), max(), mean(), sqrt() may be called")
            if node.keywords or not node.args:
                raise FormulaError(f"bad call to {node.func.id}()")
            if node.func.id == "sqrt" and len(node.args) != 1:
                raise FormulaError("sqrt() takes one argument")
            for a in node.args:
                self._check(a, exponent=False)
            return node
        raise FormulaError(f"{type(node).__name__} not allowed in formula")

    # ---------- 标量 ----------
    def eval(self, env: dict) -> float:
        return _scalar(self.root, env)

    # ---------- 向量 ----------
    def eval_vec(self, env: dict, n: int) -> list:
        out = _vec(self.root, env, n)
        return out if isinstance(out, list) else [out] * n

    # ---------- 量纲 ----------
    def dims(self, dims_env: dict):
        return _dims(self.root, dims_env)


def _div(a, b):
    if b == 0:
        return math.copysign(math.inf, a) if a != 0 else math.nan
    return a / b


def _pow(a, e):
    try:
        return math.pow(a, e)
    except (OverflowError, ValueError):
        return math.nan if a < 0 else math.inf


def _mul(a, b):
    try:
        return a * b
    except OverflowError:
        return math.inf


BIN = {ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b, ast.Mult: _mul, ast.Div: _div}


def _scalar(node, env):
    if isinstance(node, ast.BinOp):
        a = _scalar(node.left, env)
        if isinstance(node.op, ast.Pow):
            return _pow(a, _const(node.right))
        return BIN[type(node.op)](a, _scalar(node.right, env))
    if isinstance(node, ast.UnaryOp):
        v = _scalar(node.operand, env)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise FormulaError(f"undefined input {node.id!r}")
        return float(env[node.id])
    if isinstance(node, ast.Constant):
        return float(node.value)
    if isinstance(node, ast.Call):
        args = [_scalar(a, env) for a in node.args]
        if node.func.id == "sqrt":
            return math.sqrt(args[0]) if args[0] >= 0 else math.nan
        if node.func.id == "mean":
            return sum(args) / len(args)
        return (min if node.func.id == "min" else max)(args)
    raise FormulaError(f"cannot evaluate {type(node).__name__}")


def _vec(node, env, n):
    """返回 float 或长度 n 的 list；标量与列表自动广播。"""
    if isinstance(node, ast.BinOp):
        a = _vec(node.left, env, n)
        if isinstance(node.op, ast.Pow):
            e = _const(node.right)
            return [_pow(x, e) for x in a] if isinstance(a, list) else _pow(a, e)
        b = _vec(node.right, env, n)
        f = BIN[type(node.op)]
        if isinstance(a, list) and isinstance(b, list):
            return [f(x, y) for x, y in zip(a, b)]
        if isinstance(a, list):
            return [f(x, b) for x in a]
        if isinstance(b, list):
            return [f(a, y) for y in b]
        return f(a, b)
    if isinstance(node, ast.UnaryOp):
        v = _vec(node.operand, env, n)
        if isinstance(node.op, ast.UAdd):
            return v
        return [-x for x in v] if isinstance(v, list) else -v
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise FormulaError(f"undefined input {node.id!r}")
        return env[node.id]
    if isinstance(node, ast.Constant):
        return float(node.value)
    if isinstance(node, ast.Call):
        args = [_vec(a, env, n) for a in node.args]
        cols = [a if isinstance(a, list) else [a] * n for a in args]
        if node.func.id == "sqrt":
            return [math.sqrt(x) if x >= 0 else math.nan for x in cols[0]]
        if node.func.id == "mean":
            return [sum(row) / len(row) for row in zip(*cols)]
        g = min if node.func.id == "min" else max
        return [g(row) for row in zip(*cols)]
    raise FormulaError(f"cannot evaluate {type(node).__name__}")


def _dims(node, env):
    if isinstance(node, ast.BinOp):
        a = _dims(node.left, env)
        if isinstance(node.op, ast.Pow):
            return dims_pow(a, Fraction(_const(node.right)).limit_denominator(1000))
        b = _dims(node.right, env)
        if isinstance(node.op, (ast.Add, ast.Sub)):
            if a != b:
                raise DimError(f"adding/subtracting {dims_str(a)} and {dims_str(b)}")
            return a
        return dims_mul(a, b, 1 if isinstance(node.op, ast.Mult) else -1)
    if isinstance(node, ast.UnaryOp):
        return _dims(node.operand, env)
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise FormulaError(f"undefined input {node.id!r}")
        return env[node.id]
    if isinstance(node, ast.Constant):
        return DIMLESS
    if isinstance(node, ast.Call):
        ds = [_dims(a, env) for a in node.args]
        if node.func.id == "sqrt":
            return dims_pow(ds[0], Fraction(1, 2))
        if any(d != ds[0] for d in ds):
            raise DimError(f"{node.func.id}() of mixed dimensions")
        return ds[0]
    raise FormulaError(f"cannot evaluate {type(node).__name__}")
