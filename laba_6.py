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

def min_changes(A, b, x, eps):
    r = 0
    err = float('inf')
    n = len(b)
    k = 0
    errors = []
    B = np.eye(n)
    r = A @ x - b
    w = np.linalg.solve(B, r)
    while err > eps:
        x_prev = x.copy()
        Aw = A @ w
        B_inv_Aw = np.linalg.solve(B, Aw)
        t = (Aw @ w) / (B_inv_Aw @ Aw)
        x = x - t * w
        r = A @ x - b
        
        w = w - t * B_inv_Aw
        err = error_calc(x_prev, x)
        errors.append(err)

        k += 1
    return x, errors, k    

def connected_gradients(A, b, x, eps):
    r = 0
    err = float('inf')
    n = len(b)
    k = 0
    errors = []
    B = np.eye(n)

    x_prev = x.copy()
    r_prev = A @ x - b
    w_prev = np.linalg.solve(B, r_prev)
    tau_prev = (r_prev @ r_prev) / ((A @ w_prev) @ w_prev)

    x = x - tau_prev * w_prev
    r = A @ x - b

    while err > eps:
        w = np.linalg.solve(B, r)  
        denom_tau = (A @ w)
        denom_alpha = (r_prev @ r_prev)

        if np.linalg.norm(denom_tau) > 1e-10:
            tau = (r @ r) / denom_tau
        else:
            tau = 0 

        if np.linalg.norm(denom_alpha) > 1e-10:
            alpha = (r @ r) / denom_alpha
        else:
            alpha = 0 
        x_next = alpha * x + (1 - alpha) * x_prev - tau * w
        
        x_prev, x = x, x_next
        r_prev, r = r, A @ x - b
        w_prev = w
        
        err = error_calc(x_prev, x)
        errors.append(err)
        
        k += 1
    
    return x, errors, k

def simple_iteration(A, b, x, eps):
    err = float('inf')
    k = 0
    errors = []

    while err > eps:
        r = A @ x - b
        t = (r @ r) / ((A @ r) @ r)
        s = x - t * r

        err = error_calc(s, x)
        errors.append(err)

        x = s
        k += 1

    return x, errors, k


A = np.array([[30, -4, 3, 8, 4], 
              [-4, 35, -4, -8, 5], 
              [-5, 2,41, -1, 8], 
              [-4, -7, -2, 47, 3], 
              [1, 9, -7, -9, 37]]) 
 
b = np.array([41, 24, 45, 37, 31]) 
x_initial = np.zeros(len(b)) 
 
eps = 0.00001  

mc_result, mc_errors, n_c = min_changes(A, b, x_initial, eps)
ng_result, ng_errors, n_ng = connected_gradients(A, b, x_initial, eps)
si_result, si_errors, n_si = simple_iteration(A, b, x_initial, eps)
 
# print("\nMIN CHANGES'S METHOD") 
# for i in range (len(b)): 
#     print(f"x{i} = {mc_result[i]}") 
 
# print(n_c) 

# print("\nMIN GRADIENTS' METHOD") 
# for i in range (len(b)): 
#     print(f"x{i} = {ng_result[i]}") 
 
# print(n_ng)

print("\nSIMPLE ITERATION METHOD") 
for i in range (len(b)): 
    print(f"x{i} = {si_result[i]}") 
 
print(n_si) 
 
# plt.figure(figsize=(10, 10)) 
# plt.plot(mc_errors, label='Min Changes Errors') 
# plt.yscale('log')
# plt.xlabel('Iterations') 
# plt.ylabel('Error') 
# plt.title('Error Convergence in Min Change Method') 
# plt.legend() 
# plt.grid(True) 
# plt.show()

# plt.figure(figsize=(10, 10)) 
# plt.plot(ng_errors, label='Connected Gradients Errors') 
# plt.yscale('log')
# plt.xlabel('Iterations') 
# plt.ylabel('Error') 
# plt.title('Error Convergence in Connected Gradients Method') 
# plt.legend() 
# plt.grid(True) 
# plt.show()

plt.figure(figsize=(10, 10)) 
plt.plot(si_errors, label='Simple Iteration Errors') 
plt.yscale('log')
plt.xlabel('Iterations') 
plt.ylabel('Error') 
plt.title('Error Convergence in Simple Iteration Method') 
plt.legend() 
plt.grid(True) 
plt.show() 