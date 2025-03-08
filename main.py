from re import sub

import functions as fn
import derivates as dn
import algorithms as al
import numpy as np
import matplotlib.pyplot as plt

from functions import polymonial, trigonometric, exponential, composite

if __name__ == '__main__':
    choice : int = -1
    input_range : list = [1, 0]
    parameter : str = 'a'

    print("0. f(x) = 3x^2 + x + 5")
    print("1. g(x) = cos(x - 2)")
    print("2. h(x) = 0,5^x - x")
    print("3. k(x) = h(f(x))")
    print("4 - wyjście")

    while choice < 0:
        choice_input = input()
        if choice_input.isnumeric():
            choice = int(choice_input)

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
    print("a - Dokładność")
    print("b - Liczba iteracji")

    # while parameter != 'a' or parameter != 'b':
    #     parameter = input()

    domain = np.linspace(input_range[0], input_range[1])
    
    match choice:
        case 0:
            plt.plot(domain, polymonial(domain))
        case 1:
            plt.plot(domain, trigonometric(domain))
        case 2:
            plt.plot(domain, exponential(domain))
        case 3:
            plt.plot(domain, composite(domain))

    plt.show()
    

