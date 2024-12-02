import numpy as np

A = np.array([[37.0, 1.0, -1.0, -10.0, 6.0],
	          [1.0, 38.0, 3.0, 1.0, -9.0],
              [-1.0, 3.0, 33.0, 0.0, 3.0],
			  [-10.0, 1.0, 0.0, 49.0, -8.0],
              [6.0, -9.0, 3.0, -8.0, 32.0]])
			  
# b = np.array([33.0, 34.0, 38.0, 32.0, 24.0]) не юзается

def method_scalar_mult(A, num_iterations=1000):
    n = A.shape[1]
    x = np.ones(n)
    
    x = x / np.linalg.norm(x)
    
    for i in range(num_iterations):
        x_new = np.dot(A, x)
        
        lambda_max = np.dot(x_new.T, x) / np.dot(x.T, x)
        
        x = x_new / np.linalg.norm(x_new)
        
    return lambda_max

max_eigen_value = method_scalar_mult(A, 10)
print(f"максимальное собственное число: {max_eigen_value}")

eigen_values, eigen_vecotrs = np.linalg.eig(A)
print(f"собственные значения np.linalg.eig: {eigen_values}")
print(f"максимальное собственное число np.linalg.eig: {max(eigen_values)}")
