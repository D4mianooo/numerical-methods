from collections.abc import Callable
import numpy as np


def bisection(input_range : list, f : Callable[[float | np.ndarray], float], criteria : float | int, useEpsilonCriteria : bool) -> [float, int]:
    a = input_range[0]
    b = input_range[1]
    x = (a + b) / 2
    iterations = 0
    
    if f(x) == 0:
        return x, iterations
    
    if useEpsilonCriteria:
        while abs(f(x)) > criteria:
            if f(a) * f(x) < 0:
                b = x
            if f(x) * f(b) < 0:
                a = x
            x = (a + b) / 2
            iterations += 1
    else:
        iterations = criteria
        for i in range(iterations):
            if f(a) * f(x) < 0:
                b = x
            if f(x) * f(b) < 0:
                a = x
            x = (a + b) / 2
    return x, iterations

def newton(input_range : list, f : Callable[[float | np.ndarray], float], d : Callable[[float | np.ndarray], float], criteria : float | int, useEpsilonCriteria : bool) -> [float, int]:
    x = input_range[0]
    iterations = 0
    f_val = f(x)
    
    if f_val == 0:
        return x, iterations
    
    if useEpsilonCriteria:
        while abs(f_val) > criteria:
            d_val = d(x)
            x = x - (f_val/d_val)
            f_val = f(x)
            iterations += 1
    else:
        iterations = criteria
        for i in range(iterations):
            d_val = d(x)
            x = x - (f_val/d_val)
            f_val = f(x)
    return x, iterations

