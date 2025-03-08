import math
import numpy as np

def polymonial(x : float | np.ndarray) -> float:
    return x*(x*x - 1) + 1

def trigonometric(x : float | np.ndarray) -> float:
    return math.cos(x - 2)

def exponential(x : float | np.ndarray) -> float:
    return pow(0.5, x) - x

def composite(x : float | np.ndarray) -> float:
    return exponential(polymonial(x))
