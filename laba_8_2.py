import numpy as np

A = np.array([[1.0, 1.0, 1.0, 6.0],
	          [1.0, -1.0, 1.0, 2.0],
              [3.0, 2.0, 1.0, 10]])
			  
def method_gauss(A):
    tmp = 0
    
    n = len(A)
    x = np.zeros(n)
    for i in range (0, n):
        tmp = A[i][i]
        for j in range (n, i - 1, -1):
            A[i][j] /= tmp
        for j in range (i + 1, n):
            tmp = A[j][i]
            for k in range (n, i - 1, -1):
                A[j][k] -= A[i][k] * tmp
    
    x[n - 1] = A[n - 1][n]
    for i in range (n - 2, -1, -1):
        x[i] = A[i][n]
        for j in range (i + 1, n):
            x[i] -= A[i][j] * x[j]
    
    return x

print(method_gauss(A))