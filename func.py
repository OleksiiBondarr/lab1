import sympy
e = 0.00001


def f(x):
    return -x**4.+3.*x**3.-2.*x+4.


def df(c):
    x = sympy.Symbol('x')
    r = sympy.diff(f(x), x)
    return r.evalf(subs={x: c})

