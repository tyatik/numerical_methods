import numpy as np

# A = np.array([[5.0, -2.0, 3.0, 4.0, -5.0],
#               [3.0, 6.0, 7.0, -6.0, -7.0],
#               [8.0, 3.0, -9.0, -10.0, 8.0],
#               [4.0, -5.0, 6.0, 7.0, -6.0],
#               [3.0, 5.0, -7.0, -8.0, -9.0]])

# b = np.array([16.0, -14.0, -13.0, 28.0, -133.0])

A = np.array([[3.0, 11.0, -4.0, 7.0, -6.0],
              [4.0, 12.0, -3.0, -6.0, -5.0],
              [5.0, -10.0, 4.0, -7.0, 4.0],
              [6.0, -9.0, -5.0, 8.0, -7.0],
              [7.0, 8.0, -6.0, -9.0, -10.0]])

b = np.array([51.0, 38.0, -13.0, -12.0, 13.0])

# x = [5, 4, 1, 2, 3]

eps = 0.00001
def LU(A):    
    n = 5
    L = np.zeros((5, 5))
    U = np.zeros((5, 5))
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
    y = np.zeros(n)
    for i in range(n):
        sumLy = 0
        for j in range(i):
            sumLy += L[i][j] * y[j]
            y[i] = b[i] - sumLy
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sumUx = 0
        for j in range(i + 1, n):
            sumUx += U[i][j] * x[j]
            # if U[i][i]  != 0:
            #     x[i] = (y[i] - sumUx) / U[i][i]
            x[i] = (y[i] - sumUx) / U[i][i]
    return x
	
L, U = LU(A)

# print(L, U)
result = LUrazl(L, U, b)
print(result)
