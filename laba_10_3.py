#метод встречной прогонки

import numpy as np
np.random.seed(1)

A = np.array([[5.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              [1.0, 5.0, 1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 5.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 5.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0, 5.0, 1.0],
              [0.0, 0.0, 0.0, 0.0, 1.0, 5.0]])

f = np.array([6.0, 7.0, 7.0, 7.0, 7.0, 6.0])
n = len(f)
m = np.random.randint(2, n - 1)

def diag_defining():
    a = [0]
    b = [1]
    for i in range(1, n):
        a.append(A[i][i-1])  # поддиагональ
        if i < n - 1:
            b.append(A[i][i+1])
    b.append(0)  # наддиагональ
    return np.array(a), np.array(b)

def confront_progonka(a, b, c, f):
    alfa = np.zeros(n)
    beta = np.zeros(n)
    
    alfa[0] = b[0] / (-c[0])
    beta[0] = -f[0] / (-c[0])

    x = np.zeros(n)
    nyo = np.zeros(n)
    psi = np.zeros(n)
    
    for i in range(1, n-1):
        denominator = (-c[i]) - alfa[i-1] * a[i-1]
        alfa[i] = b[i] / denominator
        beta[i] = (-f[i] + beta[i-1] * a[i-1]) / denominator

    for i in range(m-1, -1, -1):
        x[i] = alfa[i] * x[i+1] + beta[i]

    nyo[n - 1] = f[n - 1] / c[n - 1]
    psi[n - 1] = a[n - 1] / c[n - 1]

  
    # print(x[n - 1])

    for i in range(n - 2, m, -1):
        nyo[i] = (f[i] + b[i] * nyo[i + 1]) / (c[i] - b[i] * psi[1 + i])
        psi[i] = a[i] / (c[i] - b[i] * psi[i + 1])

    x[m - 1] = (nyo[m - 1] + psi[m - 1] * beta[m - 2]) / (1 - psi[m - 1] * alfa[m - 2])
    
    for i in range(m - 1, n - 1):
        x[i + 1] = psi[i + 1] * x[i] + nyo[i + 1]

    # for i in range(m+1, n):  # Правая часть
    #     x[i] = psi[i] * x[i-1] + nyo[i]

    return x

a, b = diag_defining()

c = np.diag(A)

x = confront_progonka(a, b, c, f)

# print(a, b)
print(m)
print(x)