from re import sub
from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

from algorithms import bisection, newton, bisection_i, newton_i
from derivates import polymonial_derivate
from functions import polymonial, trigonometric, exponential, composite

def prompt() -> int:
    c = -1
    while c < 0:
        choice_input = input()
        if choice_input.isnumeric():
            c = int(choice_input)
    return c


def draw_axis():
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")


def label_axis():
    plt.xlabel("x")
    plt.ylabel("y")


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
    
    plt.grid()
    plt.axis('equal')
    plt.ylim(-15, 15)
    label_axis()
    draw_axis()
    
    dupa = np.linspace(-5, 5)
    plt.plot(dupa, funcs[choice](dupa))
    plt.show()

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

    plt.grid()
    label_axis()
    draw_axis()
    
    plt.plot(dupa, func(dupa), zorder=1)
    
    choice2 = prompt()

    match choice2:
        case 0:
            eps = 2
            while eps > 1 or eps <= 0:
                eps = float(input("Epsilon: "))
            x_zero_b = bisection(input_range, func, eps)
            x_zero_n = newton(input_range, func, func_derivate, eps)
            plt.scatter(x_zero_b, func(x_zero_b), edgecolors="black", linewidth=2, s=100, c="red", zorder=2)
            plt.scatter(x_zero_n, func(x_zero_n), edgecolors="black", linewidth=2, s=100, c="blue", zorder=2)
        case 1:
            iterations = int(input("Iteracje: "))
            x_zero_b = bisection_i(input_range, polymonial, iterations)
            x_zero_n = newton_i(input_range, func, func_derivate , iterations)
            plt.scatter(x_zero_b, func(x_zero_b))
            plt.scatter(x_zero_n, func(x_zero_n))
    
    plt.show()
    

