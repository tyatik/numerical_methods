import numpy as np

A = np.array([[37.0, 1.0, -1.0, -10.0, 6.0],
	          [1.0, 38.0, 3.0, 1.0, -9.0],
              [-1.0, 3.0, 33.0, 0.0, 3.0],
			  [-10.0, 1.0, 0.0, 49.0, -8.0],
              [6.0, -9.0, 3.0, -8.0, 32.0]])
			  
b = np.array([33.0, 34.0, 38.0, 32.0, 24.0])
# b = np.array([53.0, 47.0, 49.0, 59.0, 42.0])
eps = 0.00001
def error_calc(x, xn):    
    errors = np.abs(xn - x)
    return np.max(errors)

def pm(A):    
    y = b
    x = y / np.linalg.norm(y)    
    for i in range(1000):
        y_k = np.dot(A, x)
        lyambda = np.dot(x, y_k)
        x = y_k / np.linalg.norm(y_k)
    return lyambda

pm_alg = pm(A)
sobstv_znach, sobsv_vect = np.linalg.eig(A)
print(f'Через PM-разложение: {pm_alg}\nПроверка через np.linalg.eig(A): {np.max(sobstv_znach)}')

def scalar(A):
    y = b
    x = y / np.linalg.norm(y)
    for i in range(1000):
        y_k = np.dot(A, x)
        S = np.dot(y_k, y_k)
        t = np.dot(y_k, x)
        lyambda = S/t
        x = y_k / np.linalg.norm(y_k)
        return lyambda
    
print(f'Через метод скалярного проивзедения: {scalar(A)}')