import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

def error_func(x, x_new):
    err = abs(x - x_new)
    return err

def my_funс_1(x):
    res = 2 * math.log(x) - x / 2 + 1
    return res

def my_funс_2(x):
    res = 2 - x - math.log(x)
    return res

def fi_1(x):
    return math.exp((x - 2) / 4)

def fi_2(x):
    return 2 - math.log(x)

def simple_iteration(func, x, n_iterations = 1000):
    for i in range(n_iterations):
        x_new = func(x)
        if error_func(x, x_new) < eps:
            return x, i + 1
        x = x_new

def programm(func):
    if func == 1:
        res, iteration = simple_iteration(fi_1, x0)
        x_values = np.linspace(0.1, 3, 200)
        my_func_values = [my_funс_1(x) for x in x_values]  
        fi_values = [fi_1(x) for x in x_values]  
        print(f"корень: {res}\nитерация: {iteration}")
        show(x_values, my_func_values, fi_values)
    elif func == 2:
        res, iteration = simple_iteration(fi_2, x0)
        x_values = np.linspace(0.01, 3, 500)
        my_func_values = [my_funс_2(x) for x in x_values]  
        fi_values = [fi_2(x) for x in x_values]  
        print(f"корень: {res}\nитерация: {iteration}")
        show(x_values, my_func_values, fi_values)
    else:
        print("ERROR!!!")
    

def show(x_values, my_func_values, fi_values):
    plt.figure(figsize=(10, 6))

    plt.plot(x_values, my_func_values, label=r'my_func(x)', color='blue')
    plt.plot(x_values, fi_values, label=r'fi(x)', color='red', linestyle='--')

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    plt.title('simple iteration method')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    eps = 1e-8
    x0 = 1.5 #выбрана чуть больше 1

    what_func = int(input("выберите функцию. 1 или 2:   "))
    programm(what_func)