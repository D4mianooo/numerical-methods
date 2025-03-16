import numpy as np

from horner import horner

def polymonial(x : float | np.ndarray) -> float:
    return horner(x, [1, -1, -3, 1])
    # return x * (x * (x - 1) - 3) + 1

def trigonometric(x : float | np.ndarray) -> float:
    return np.cos(x - 2)

def exponential(x : float | np.ndarray):
    return np.pow(3, x) - np.pow(0.5, x) + 2

def composite(x : float | np.ndarray) -> float:
    return exponential(polymonial(x))

def composite2(x : float | np.ndarray) -> float:
    return trigonometric(polymonial(x))

def composite3(x : float | np.ndarray) -> float:
    return polymonial(exponential(x))