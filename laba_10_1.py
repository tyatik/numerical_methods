#метод правой прогонки

import numpy as np

A = np.array([[5.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              [1.0, 5.0, 1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 5.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 5.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0, 5.0, 1.0],
              [0.0, 0.0, 0.0, 0.0, 1.0, 5.0]])

f = np.array([6.0, 7.0, 7.0, 7.0, 7.0, 6.0])
n = len(f)

def diag_defining():
    a = [0]
    b = [1]
    for i in range(1, n):
        a.append(A[i][i-1])  # поддиагональ
        if i < n - 1:
            b.append(A[i][i+1])
    b.append(0)  # наддиагональ
    return np.array(a), np.array(b)

def right_progonka(a, b, c, f):
    alfa = np.zeros(n)
    beta = np.zeros(n)
    
    alfa[0] = b[0] / (-c[0])
    beta[0] = -f[0] / (-c[0])
    
    for i in range(1, n):
        denominator = (-c[i]) - alfa[i-1] * a[i-1]
        alfa[i] = b[i] / denominator
        beta[i] = (-f[i] + beta[i-1] * a[i-1]) / denominator

    x = np.zeros(n)
    x[n-1] = beta[n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = alfa[i] * x[i+1] + beta[i]

    return x

a, b = diag_defining()

c = np.diag(A)

x = right_progonka(a, b, c, f)

# print(a, b)
print(x)