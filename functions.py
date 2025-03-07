import math

def polymonial(x : float) -> float:
    return x*(x*x - 1) + 1

def trigonometric(x : float) -> float:
    return math.cos(x - 2)

def exponential(x : float) -> float:
    return pow(0.5, x) - x

def composite(x : float) -> float:
    return exponential(polymonial(x))
