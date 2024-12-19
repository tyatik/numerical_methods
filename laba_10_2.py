#метод левой прогонки

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

def left_progonka(a, b, c, f):
    alfa = np.zeros(n)
    beta = np.zeros(n)
    
    alfa[n - 1] = b[n - 1] / (-c[n - 1])
    beta[n - 1] = -f[n - 1] / (-c[n - 1])
    
    for i in range(n - 2, -1, -1):
        alfa[i] = a[i]/(-c[i] - b[i]*alfa[i+1])
        beta[i] = (-f[i] + b[i]* beta[i+1])/(-c[i] - b[i]*alfa[i+1])

    x = np.zeros(n)
    x[0] = beta[0]
    
    for i in range(1, n):
        x[i] = alfa[i]*x[i-1]+beta[i]

    return x

a, b = diag_defining()

c = np.diag(A)

x = left_progonka(a, b, c, f)

# print(a, b)
# for i in range(6):
#     print(x[i])

print(x)