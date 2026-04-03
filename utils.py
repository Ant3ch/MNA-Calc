import math

def _implicit_mult(expr):
    result = []
    i = 0
    while i < len(expr):
        c = expr[i]
        result.append(c)
        if i + 1 < len(expr):
            nxt = expr[i + 1]
            if c.isdigit() and (nxt.isalpha() or nxt == '('):
                result.append('*')
            elif c == ')' and (nxt.isalpha() or nxt.isdigit() or nxt == '('):
                result.append('*')
        i += 1
    return ''.join(result)

def _log10(x):
    return math.log(x) / math.log(10)

def _log2(x):
    return math.log(x) / math.log(2)

def _ceil(x):
    i = int(x)
    return i + 1 if x > i else i

def _floor(x):
    i = int(x)
    return i - 1 if x < i else i

SAFE_ENV = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "arcsin": math.asin, "arccos": math.acos, "arctan": math.atan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "ln": math.log, "log": _log10, "log2": _log2, "exp": math.exp,
    "sqrt": math.sqrt, "abs": abs, "ceil": _ceil, "floor": _floor,
    "pi": math.pi, "e": math.e,
    "pow": pow, "max": max, "min": min,
}


def parse_function(func_str):
    try:
        expr = func_str.replace("^", "**")
        expr = _implicit_mult(expr)
        def f(x):
            env = {"x": x}
            env.update(SAFE_ENV)
            return eval(expr, {"__builtins__": {}}, env)
        return f
    except SyntaxError:
        raise SyntaxError("Syntaxe invalide : '" + func_str + "'")


def parse_number(expr_str):
    try:
        return float(eval(expr_str.replace("^", "**"), {"__builtins__": {}}, SAFE_ENV))
    except Exception:
        raise ValueError("Expression invalide : '" + expr_str + "'")


def ask_for_number(prompt):
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError as e:
            print(str(e))


def ask_for_function(prompt):
    while True:
        try:
            return parse_function(input(prompt))
        except SyntaxError as e:
            print(str(e))


def ask_for_function_with_domain(subdivision=False):
    return {
        "a": ask_for_number("Borne a: "),
        "b": ask_for_number("Borne b: "),
        "n": int(ask_for_number("subdivision n: ")) if subdivision else None,
        "f": ask_for_function("f(x): "),
    }