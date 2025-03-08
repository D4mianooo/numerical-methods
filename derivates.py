import math

import numpy as np

def polymonial_derivate(x : float | np.ndarray) -> float:
    return 3*x*x-1

def trigonometric_derivate(x : float | np.ndarray) -> float:
    return math.sin(x - 2)

def exponential_derivate(x : float | np.ndarray) -> float:
    return pow(-0.5, x) * math.log(2) - x

# def composite(x : float | np.ndarray) -> float:
    # return exponential(polymonial(x))