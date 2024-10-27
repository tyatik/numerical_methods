import numpy as np
import sympy as sp
import scipy.integrate as intimport matplotlib.pyplot as plt
x0, x1, x2, x3, x4 = 0.531, 0.533, 0.535, 0.537, 0.539
y0, y1, y2, y3, y4 = 3.39625, 3.41193, 3.42768, 3.44350, 3.45919
h = 0.002
n = 5
def f(x):    
    A = y0 * (((x - x1) * (x - x2) * (x - x3)*(x-x4)) / ((x0 - x1) * (x0 - x2) * (x0-x3)*(x-x4)))
    B = y1 * (((x - x0) * (x - x2) * (x-x3)*(x-x4)) / ((x1 - x0) * (x1 - x2) * (x1-x3)*(x-x4)))
    C = y2 * (((x - x0) * (x - x1)*(x-x3)*(x-x4)) / ((x2 - x0) * (x2 - x1) * (x2-x3)*(x-x4)))
    D = y3 * (((x-x0)*(x-x1)*(x-x2)*(x-x4))/((x3-x0)*(x3-x1)*(x3-x2)*(x-x4)))
    E = y4 * (((x-x0)*(x-x1)*(x-x2)*(x-x3))/((x3-x0)*(x3-x1)*(x3-x2)*(x-x3)))
    return A + B + C + D + E

def newtonkotes():    
    A = 7*h*y0/90
    B = 16*h*y1/45
    C = 2*h*y2/15
    D = 16*h*y3/45
    E = 7*h*y4/90
    return A + B + C + D + E

def rectangle():    
    A = h*y0/n
    B = h*y1/n    
    C = h*y2/n
    D = h*y3/n
    E = h*y4/n
    return A + B + C + D + E

def trapezoid():    # A = h*(y0+y1)/(2*n)
    # B = h*(y1+y2)/(2*n)    # C = h*(y2+y3)/(2*n)
    # D = h*(y3+y4)/(2*n)    result = (h/(2*4))*(y0+2*(y1+y2+y3)+y4)
    return result

def simpsons():    
    A = y0 * 2
    B = y1 * 4    
    C = y2 * 2
    D = y3 * 4   
    E = y4 * 2
    return (A + B + C + D + E)*(h/(3*n))

print("Newton-Kotes: ", newtonkotes())
print("Rectangle: ", rectangle())
print("Trapezoid: ", trapezoid())
print("Simpsons: ", simpsons())