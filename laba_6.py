import numpy as np 
import matplotlib.pyplot as plt 
 
np.set_printoptions(precision=6, suppress=True) 
 
def error_calc(x, xn): 
    errors = np.abs(xn - x) 
    return np.max(errors) 
 
def min_discrepancie(A, b, x, eps):
    r = 0
    err = float('inf')
    n = len(b)
    k = 0
    errors = np.array([])
    while err > eps:
        xn = x[k].copy() 
        x = np.vstack([x, np.zeros(n)])
        for i in range(n):
            r = A * x[k] - b
            t = np.dot((A * r).transpose(), r) / (np.linalg.norm(A * r)**2)
            x[k + 1][i] = x[k][i] - t * r

        x[k] = x[k] - float(t) * r
        k += 1
        err = error_calc(x[k + 1], xn)
        errors.append(err)
    return x[-1], errors, k

     
A = np.array([[30, -4, 3, 8, 4], 
              [-4, 35, -4, -8, 5], 
              [-5, 2,41, -1, 8], 
              [-4, -7, -2, 47, 3], 
              [1, 9, -7, -9, 37]]) 
 
b = np.array([41, 24, 45, 37, 31]) 
x_initial = np.zeros((1, len(b))) 
 
eps = 0.00001  

md_result, md_errors, n_s = min_discrepancie(A, b, x_initial, eps) 
 
print("\nMIN DISCREPANCIE'S METHOD") 
for i in range (len(b)): 
    print(f"x{i} = {md_result[i]}") 
 
print(n_s) 
 
plt.figure(figsize=(10, 10)) 
plt.plot(md_errors, label='Min Discrepancie Errors') 
 
plt.xlabel('Iterations') 
plt.ylabel('Error') 
plt.title('Error Convergence in Min Discrepancie Method') 
plt.legend() 
plt.grid(True) 
plt.show() 