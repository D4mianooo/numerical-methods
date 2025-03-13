import tkinter
from re import sub
from tkinter.messagebox import showinfo
from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import ndarray
from tkinter import ttk
from tkinter import *

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

def draw_gui():
    root = Tk()
    frm = ttk.Frame(root)
    frm.grid()
    funcs = [polymonial, trigonometric, exponential, composite]
    function = [("f1", 1),("f2", 2),("f3", 3),("f4", 4),("f5", 5),("f6", 6)]
    
    v = IntVar()
    def draw():
        window = Tk()
        
        domain = np.linspace(-5, 5)
        fig = Figure(figsize = (6, 5), dpi = 100)
        ax = fig.add_subplot()
        ax.grid()
        ax.set_ylim(-10, 10)
        ax.margins(0.05)
        ax.plot(domain, funcs[v.get() - 1](domain), zorder=1)
        canvas = FigureCanvasTkAgg(fig,master = window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas,
                                       window)
        toolbar.update()
        canvas.get_tk_widget().pack()

    for formula, idx in function:
        ttk.Radiobutton(root, text=formula, variable=v, value=idx, command=draw).grid(column=1, row=idx, sticky="N")
        

    # 
    # 
    # 
    # ttk.Button(frm, text="Narysuj", command=draw).grid(column=6, row=0)
    # ttk.Button(frm, text="Szukaj", command=root.destroy).grid(column=0, row=2)
    # ttk.Entry(frm).grid(column = 1, row = 3)
    # ttk.Entry(frm).grid(column = 2, row = 3)
    # ttk.Label(frm, text="Zakres").grid(column=0, row= 3)
    # ttk.Label(frm, text="Zakres").grid(column=0, row= 3)
    # ttk.Radiobutton(frm, text="Epsilon").grid(column=0, row=4)
    # ttk.Radiobutton(frm, text="Iteracje").grid(column=1, row=4)

    # cb.bind("<<ComboboxSelected>>", draw)
    root.mainloop()


if __name__ == '__main__':
    draw_gui()
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
    

