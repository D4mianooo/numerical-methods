from collections.abc import Callable
import numpy as np


def bisection(input_range : list, f : Callable[[float | np.ndarray], float], epsilon: float) -> [float, int]:
    a = input_range[0]
    b = input_range[1]
    x = (a + b) / 2
    iterations = 0
    
    if f(x) == 0:
        return x, iterations

    while abs(f(x)) > epsilon:
        if f(a) * f(x) < 0:
            b = x
        if f(x) * f(b) < 0:
            a = x
        x = (a + b) / 2
        iterations += 1
    return x, iterations

def bisection_i(input_range : list, f , iterations: int) -> float:
    a = input_range[0]
    b = input_range[1]
    x = (a + b) / 2

    if f(x) == 0:
        return x

    for i in range(iterations):
        if f(a) * f(x) < 0:
            b = x
        if f(x) * f(b) < 0:
            a = x
        x = (a + b) / 2
    return x

def newton(input_range : list, f : Callable[[float | np.ndarray], float], d : Callable[[float | np.ndarray], float], epsilon: float) -> [float, int]:
    x = input_range[0]
    iterations = 0
    if f(x) == 0:
        return x, iterations
    f_val = f(x)    
    while abs(f_val) > epsilon:
        d_val = d(x)
        x = x - (f_val/d_val)
        f_val = f(x)
        iterations += 1
    return x, iterations

def newton_i(input_range : list, f, d, iterations: int) -> float:
    x = input_range[0]
    if f(x) == 0:
        return x
    for i in range(iterations):
        x = x - (f(x)/d(x))
    return x
