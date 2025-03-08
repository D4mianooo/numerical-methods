from re import sub
from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

from algorithms import bisection, newton
from derivates import polymonial_derivate
from functions import polymonial, trigonometric, exponential, composite

def prompt() -> int:
    c = -1
    while c < 0:
        choice_input = input()
        if choice_input.isnumeric():
            c = int(choice_input)
    return c

if __name__ == '__main__':
    input_range : list = [1, 0]
    funcs = [polymonial, trigonometric, exponential, composite]
    funcs_derivates = [polymonial_derivate, trigonometric, exponential, composite]
    
    print("0. f(x) = 3x^2 + x + 5")
    print("1. g(x) = cos(x - 2)")
    print("2. h(x) = 0,5^x - x")
    print("3. k(x) = h(f(x))")
    print("4 - wyjście")

    choice = prompt()

    print("[a, b]")

    while input_range[0] >= input_range[1]:
        a_input = input("a: ")
        b_input = input("b: ")
        while not sub('-', '', a_input).isnumeric():
            a_input = input("a: ")
        while not sub('-', '', b_input).isnumeric():
            b_input = input("b: ")
        input_range[0] = int(a_input)
        input_range[1] = int(b_input)

    print("Kryterium")
    print("0 - Dokładność")
    print("1 - Liczba iteracji")

    func : Callable[[float | ndarray], float] = funcs[choice]
    func_derivate : Callable[[float | ndarray], float] = funcs_derivates[choice]
    
    domain = np.linspace(input_range[0], input_range[1])
    plt.plot(domain, func(domain))
    
    choice2 = prompt()

    match choice2:
        case 0:
            eps = float(input("Epsilon: "))
            xb_0 = bisection(input_range, func, eps)
            xn_0 = newton(input_range, func, func_derivate, eps)
            plt.scatter(xb_0, func(xb_0))
            plt.scatter(xn_0, func(xn_0))
        # case 1:
            # iterations = input("Iteracje: ")
            # bisection(input_range, polymonial, iterations)
            # newton(input_range, polymonial, , iterations)
    plt.show()
    

