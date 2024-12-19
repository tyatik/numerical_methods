import numpy as np

A = np.array([[3.0, 11.0, -4.0, 7.0, -6.0],
              [4.0, 12.0, -3.0, -6.0, -5.0],
              [5.0, -10.0, 4.0, -7.0, 4.0],
              [6.0, -9.0, -5.0, 8.0, -7.0],
              [7.0, 8.0, -6.0, -9.0, -10.0]])

b = np.array([51.0, 38.0, -13.0, -12.0, 13.0])

def LU(A):    
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            sumLU = 0
            for k in range(i):
                sumLU += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - sumLU
        for j in range(i + 1, n):
            sumLU = 0
            for k in range(i):
                sumLU += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - sumLU) / U[i][i]
    return L, U

def LUrazl(L, U, b):
    n = len(b)
    # Решение L * y = b (прямой ход)
    y = np.zeros(n)
    for i in range(n):
        sumLy = 0
        for j in range(i):
            sumLy += L[i][j] * y[j]
        y[i] = b[i] - sumLy

    # Решение U * x = y (обратный ход)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sumUx = 0
        for j in range(i + 1, n):
            sumUx += U[i][j] * x[j]
        x[i] = (y[i] - sumUx) / U[i][i]
    return x

# Разложение матрицы A на L и U
L, U = LU(A)

# Решение системы Ax = b
result = LUrazl(L, U, b)
print("Решение системы Ax = b:", result)