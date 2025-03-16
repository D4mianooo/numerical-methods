import numpy as np


def horner(x : float | np.ndarray, factors : list):
    y = factors[0]
    for i in range(1, len(factors)):
        y = y * x + factors[i]
    return y