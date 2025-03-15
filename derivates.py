import numpy as np

from functions import polymonial, exponential

def polymonial_derivate(x : float | np.ndarray) -> float:
    return x * (3 * x - 2) - 3

def trigonometric_derivate(x : float | np.ndarray) -> float:
    return -np.sin(x - 2)

def exponential_derivate(x : float | np.ndarray):
    return (np.pow(3, x) * np.log(3)) - (np.pow(0.5, x) * np.log(0.5))

def composite_derivate(x : float | np.ndarray) -> float:
    return exponential_derivate(polymonial(x)) * polymonial_derivate(x)

def composite2_derivate(x : float | np.ndarray) -> float:
    return trigonometric_derivate(polymonial(x)) * polymonial_derivate(x)

def composite3_derivate(x : float | np.ndarray) -> float:
    return polymonial_derivate(exponential(x)) * exponential_derivate(x)