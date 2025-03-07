import functions as fn
import derivates as dn
import algorithms as al
import numpy as np
import matplotlib.pyplot as plt

from functions import polymonial

if __name__ == '__main__':
    # input_range = [-2, 2]
    # print(al.newton(input_range, fn.polymonial, dn.polymonial_derivate, 5))
    # zero = bisection(input_range, polymonial, 1e-10)
    # t = np.linspace(input_range[0], input_range[1])
    #
    # plt.plot(t, polymonial(t))
    # plt.grid(color='black', linestyle='-', linewidth=1)
    # plt.scatter(zero, polymonial(zero))
    # plt.show()

    choice : int = -1
    input_range : list = [1, 0]
    # parameter : str = ""

    print("0. f(x) = 3x^2 + x + 5")
    print("1. f(x) = cos(x)")
    print("3 - wyjście")

    while choice < 0:
        choice_input = input()
        if choice_input.isnumeric():
            choice = int(choice_input)

    print("[a, b]")

    while input_range[0] >= input_range[1]:
        a_input = input("a: ")
        b_input = input("b: ")
        while not a_input.isnumeric():
            a_input = input("a: ")
        while not b_input.isnumeric():
            b_input = input("b: ")
        input_range[0] = int(a_input)
        input_range[1] = int(b_input)

    match choice:
        case 0:
            xes = np.linspace(input_range[0], input_range[1])
            plt.plot(xes, polymonial(xes))

    plt.show()
    #
    # print("Kryterium")
    # print("a - Dokładność")
    # print("b - Liczba iteracji")
    #
    # parameter_input : str = ""
    # while parameter_input != 'a' or parameter_input != 'b':
    #     parameter = parameter_input

