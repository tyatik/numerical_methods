import matplotlib.pyplot as plt
import numpy as np

a = [0, 1, 1, 2, 1, 2]
b = [-1, 3, -2, -1, 1, 0]
c = [10, -10, -10, -10, -10, -10]
F = [10, 4, -10, 1, -10, 2]
al = [0, 0, 0, 0, 0, 0]
bt = [0, 0, 0, 0, 0, 0]
al[5] = a[5]/c[5]
bt[5] = F[5]/c[5]
x = [0, 0, 0, 0, 0, 0]
for i in range(4, -1, -1):
    al[i] = a[i]/(c[i] - b[i]*al[i+1])
    bt[i] = (F[i] + b[i]*bt[i+1])/(c[i] - b[i]*al[i+1])
x[0] = bt[0]
for i in range(1, 6):
    x[i] = al[i]*x[i-1]+bt[i]
print(x)