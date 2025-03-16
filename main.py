from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


from algorithms import bisection, newton
from derivates import polymonial_derivate, composite2_derivate, composite3_derivate, exponential_derivate, \
    composite_derivate, trigonometric_derivate
from functions import polymonial, trigonometric, exponential, composite, composite2, composite3
from utils import prompt, get_values_array, label_axis, draw_axis

funcs = [polymonial, trigonometric, exponential, composite, composite2, composite3]
funcs_derivates = [polymonial_derivate, trigonometric_derivate, exponential_derivate, composite_derivate, composite2_derivate, composite3_derivate]
samples = 300



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
 
        func : Callable[[float | ndarray], float] = funcs[choice]
        func_derivate : Callable[[float | ndarray], float] = funcs_derivates[choice]
        
        domain = np.linspace(-10, 10, samples)
        plt.plot(domain, get_values_array(domain, func))
        plt.show()
    
    
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
        
        domain = np.linspace(input_range[0], input_range[1], samples)
        plt.plot(domain, get_values_array(domain, func))
        
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
                x_zero_b, iterations_b = bisection(input_range, func, eps, True)
                x_zero_n, iterations_n = newton(input_range, func, func_derivate, eps, True)
                precision_b = func(x_zero_b)
                precision_n = func(x_zero_n)
                
                plt.scatter(x_zero_b, precision_b, linewidth=2, marker="1", s=100, c="red", zorder=1, label="Bisekcja")
                plt.scatter(x_zero_n, precision_n, linewidth=2, marker="2", s=100, c="blue", zorder=2, label="Stycznych/Newtona")
                
                print(f"Kryterium: Epsilon({eps})")
                print(f"Miejsce zerowe (Bisekcja): {x_zero_b}, Iteracje: {iterations_b}, Dokładność: {abs(precision_b)}")
                print(f"Miejsce zerowe (Newton): {x_zero_n}, Iteracje: {iterations_n}, Dokładność: {abs(precision_n)}")
            case 1:
                iterations = int(input("Iteracje: "))
                x_zero_b, iterations_b = bisection(input_range, func, iterations, False)
                x_zero_n, iterations_b = newton(input_range, func, func_derivate , iterations, False)
                precision_b = func(x_zero_b)
                precision_n = func(x_zero_n)

                plt.scatter(x_zero_b, precision_b, linewidth=2, marker="1", s=100, c="red", zorder=1, label="Bisekcja")
                plt.scatter(x_zero_n, precision_n, linewidth=2, marker="2", s=100, c="blue", zorder=2,label="Stycznych/Newtona")
          
                print(f"Kryterium: Iterations({iterations})")
                print(f"Miejsce zerowe (Bisekcja): {x_zero_b}, Iteracje: {iterations}, Dokładność: {abs(precision_b)}")
                print(f"Miejsce zerowe (Newton): {x_zero_n}, Iteracje: {iterations}, Dokładność: {abs(precision_n)}")
            
        plt.legend()
        plt.show()
    

