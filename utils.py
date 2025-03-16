from typing import Callable

import numpy as np
from matplotlib import pyplot as plt


def prompt() -> int:
    c = -1
    while c < 0:
        choice_input = input("Wybór: ")
        if choice_input.isnumeric():
            c = int(choice_input)
    return c
def get_values_array(domain : np.ndarray, f : Callable[[float | np.ndarray], float]):
    samples = len(domain)
    results = [0 for n in range(samples)]
    for i in range(samples):
        results[i] = f(domain[i])
    return results

def draw_axis():
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")


def label_axis():
    plt.xlabel("x")
    plt.ylabel("y")