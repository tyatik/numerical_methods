import numpy as np

A = np.array([[-5.0, 4.0, -3.0, 6.0, 10.0],
	          [4.0, 5.0, 2.0, -7.0, -9.0],
              [3.0, -4.0, -6.0, 5.0, -8.0],
			  [2.0, 3.0, -7.0, -6.0, 5.0],
              [1.0, -4.0, 8.0, -9.0, 3.0]])
			  
b = np.array([28.0, 13.0, -37.0, -12.0, -4.0])
eps = 0.00001
def LU(A):    
    n = A.shape[0]
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
            x[i] = (y[i] - sumUx) / U[i][i]
    return x

def A_1(A, b):
    n = len(b)
    L, U = LU(A)
    Aobr = np.zeros((n, n))

    for i in range(n):
        b = np.zeros(n)
        for j in range(n):
            if i==j:
                b[j]  = 1
            else:
                b[j] = 0
                x = LUrazl(L, U, b)
        for j in range(n):
            Aobr[j][i] = x[j]
    return Aobr

A1=np.linalg.inv(A)
L, U = LU(A)
A_obr = A_1(A, b)
result = LUrazl(L, U, b)
print(result)
print(f'A_1: \n{A1}\n Обратная матрица через ЛУ:\n{A_obr} ')

B = np.array([[2.0, -1.0, 3.0],
              [1.0, 3.0, -1.0],
              [5.0, 2.0, 1.0]])

f = np.array([-4.0, 2.0, 5.0])
L1, U1 = LU(B)
result1 = LUrazl(L1, U1, f)
print(result1)