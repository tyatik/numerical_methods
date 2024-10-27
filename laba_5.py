import numpy as np 
import matplotlib.pyplot as plt 
 
np.set_printoptions(precision=6, suppress=True) 
 
def error_calc(x, xn): 
    errors = np.abs(xn - x) 
    return np.max(errors) 
 
def l2_norm(x, xn): 
    return  
 
def jacobi(A, b, x, eps): 
    n = len(b) 
    flag = 1 
    errors = [] 
    iters = 0 
    iterations = 0 
    for i in range(0, n): 
        if A[i][i] == 0: 
            print("ERROR!!!") 
            flag = 0 
     
    if flag == 1: 
        err = float('inf') 
        k = 0 
         
        while err > eps: 
            xn = x[k].copy() 
            x = np.vstack([x, np.zeros(n)])  
            for i in range(0, n): 
                x[k + 1][i] = b[i] 
                for j in range(0, n): 
                    if j != i: 
                        x[k + 1][i] -= A[i][j] * x[k][j] 
                 
                x[k + 1][i] /= A[i][i] 
                 
            err = error_calc(x[k + 1], xn) 
            errors.append(np.log(err)) 
            k += 1 
            iters += 1 
            # xn = x[k].copy() 
 
    return x[-1], errors, iters 
     
def seidel(A, b, x, eps):
    n = len(b) 
    flag = 1 
    errors = [] 
    for i in range(0, n): 
        if A[i][i] == 0: 
            print("ERROR!!!") 
            flag = 0 
     
    if flag == 1: 
        err = float('inf') 
        k = 0 
         
        while err > eps: 
            xn = x[k].copy() 
            x = np.vstack([x, np.zeros(n)])  
            for i in range(0, n): 
                x[k + 1][i] = b[i] 
                for j in range(0, n): 
                    if j != i and i < j: 
                        x[k + 1][i] -= A[i][j] * x[k][j]
                    elif j != i and i > j:
                        x[k + 1][i] -= A[i][j] * x[k + 1][j]
                 
                x[k + 1][i] /= A[i][i] 
                 
            err = error_calc(x[k + 1], xn) 
            errors.append(np.log(err)) 
            k += 1 
            # xn = x[k].copy() 
 
    return x[-1], errors, k 

     
A = np.array([[30, -4, 3, 8, 4], 
              [-4, 35, -4, -8, 5], 
              [-5, 2,41, -1, 8], 
              [-4, -7, -2, 47, 3], 
              [1, 9, -7, -9, 37]]) 
 
b = np.array([41, 24, 45, 37, 31]) 
x_initial = np.zeros((1, len(b))) 
 
eps = 0.00001  
 
jacobi_result, jacobi_errors, n_j = jacobi(A, b, x_initial, eps) 
seidel_result, seidel_errors, n_s = seidel(A, b, x_initial, eps) 
 
print("\nJACOBI'S METHOD") 
for i in range (len(b)): 
    print(f"x{i} = {jacobi_result[i]}") 
 
print("\nSEIDEL'S METHOD") 
for i in range (len(b)): 
    print(f"x{i} = {seidel_result[i]}") 
 
print(n_j) 
print(n_s) 
 
plt.figure(figsize=(10, 10)) 
plt.plot(jacobi_errors, label='Jacobi Errors') 
plt.plot(seidel_errors, label='Seidel Errors') 
 
plt.xlabel('Iterations') 
plt.ylabel('Error') 
plt.title('Error Convergence in Jacobi and Seidel Methods') 
plt.legend() 
plt.grid(True) 
plt.show() 
     
# print(jacobi_errors) 
# print(seidel_errors)