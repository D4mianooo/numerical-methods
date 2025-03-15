from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


from algorithms import bisection, newton, bisection_i, newton_i
from derivates import polymonial_derivate, composite2_derivate, composite3_derivate, exponential_derivate, \
    composite_derivate, trigonometric_derivate
from functions import polymonial, trigonometric, exponential, composite, composite2, composite3

funcs = [polymonial, trigonometric, exponential, composite, composite2, composite3]
funcs_derivates = [polymonial_derivate, trigonometric_derivate, exponential_derivate, composite_derivate, composite2_derivate, composite3_derivate]

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
    while True:
        input_range : list = [1, 0]
        
        print("0. f(x) = x\xB3 - x\xB2 - 3x + 1")
        print("1. g(x) = cos(x - 2)")
        print("2. h(x) = 3\u02E3 - 0.5\u02E3 + 2")
        print("3. k(x) = (h\u2218f)(x)")
        print("4. j(x) = (g\u2218f)(x)")
        print("5. c(x) = (f\u2218h)(x)")
        print("6. Wyjście")
    
        choice = prompt()
        
        if choice == 6:
            exit(0)
            
        plt.grid()
        plt.axis('equal')
        plt.ylim(-15, 15)
        label_axis()
        draw_axis()
        
        domain = np.linspace(-5, 5)
        plt.plot(domain, funcs[choice](domain))
        plt.show()
    
        func : Callable[[float | ndarray], float] = funcs[choice]
        func_derivate : Callable[[float | ndarray], float] = funcs_derivates[choice]
    
        print("[a, b]")
    
        while input_range[0] >= input_range[1]:
            a_input = input("a: ")
            b_input = input("b: ")
            input_range[0] = float(a_input)
            input_range[1] = float(b_input)
    
        if func(input_range[0])*func(input_range[1]) > 0:
            print("Brak przeciwnych znaków na krańcach badanego przedziału")
            break

        print("Kryterium")
        print("0 - Dokładność")
        print("1 - Liczba iteracji")
    
    
        plt.grid()
        plt.axis('equal')
        label_axis()
        draw_axis()
        
        domain = np.linspace(input_range[0], input_range[1])
        plt.plot(domain, func(domain), zorder=1)
        
        choice2 = prompt()
        x_zero_b = 0
        x_zero_n = 0
        iterations_b = 0
        iterations_n = 0
        
        match choice2:
            case 0:
                eps = 2
                while eps > 1 or eps <= 0:
                    eps = float(input("Epsilon: "))
                x_zero_b, iterations_b = bisection(input_range, func, eps)
                x_zero_n, iterations_n = newton(input_range, func, func_derivate, eps)
                precision_b = func(x_zero_b)
                precision_n = func(x_zero_n)
                
                plt.scatter(x_zero_b, precision_b, edgecolors="black", linewidth=1, s=60, c="red", zorder=1, alpha=0.7)
                plt.scatter(x_zero_n, precision_n, edgecolors="black", linewidth=1, s=60, c="blue", zorder=2, alpha=0.3)
                
                print(f"Kryterium: Epsilon({eps})")
                print(f"Miejsce zerowe (Bisekcja): {x_zero_b}, Iteracje: {iterations_b}, Dokładność: {abs(precision_b)}")
                print(f"Miejsce zerowe (Newton): {x_zero_n}, Iteracje: {iterations_n}, Dokładność: {abs(precision_n)}")
            case 1:
                iterations = int(input("Iteracje: "))
                x_zero_b = bisection_i(input_range, polymonial, iterations)
                x_zero_n = newton_i(input_range, func, func_derivate , iterations)
                precision_b = func(x_zero_b)
                precision_n = func(x_zero_n)

                plt.scatter(x_zero_b, precision_b, edgecolors="black", linewidth=1, s=60, c="red", zorder=1, alpha=0.7)
                plt.scatter(x_zero_n, precision_n, edgecolors="black", linewidth=1, s=60, c="blue", zorder=2, alpha=0.3)
          
                print(f"Kryterium: Iterations({iterations})")
                print(f"Miejsce zerowe (Bisekcja): {x_zero_b}, Iteracje: {iterations}, Dokładność: {abs(precision_b)}")
                print(f"Miejsce zerowe (Newton): {x_zero_n}, Iteracje: {iterations}, Dokładność: {abs(precision_n)}")
            
         
        plt.show()
    

