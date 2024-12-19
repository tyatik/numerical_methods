import numpy as np

# np.random.seed(1)
A = np.array([[5.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              [1.0, 5.0, 1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 5.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 5.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0, 5.0, 1.0],
              [0.0, 0.0, 0.0, 0.0, 1.0, 5.0]])

f = np.array([6.0, 7.0, 7.0, 7.0, 7.0, 6.0])
n = len(f)
# m = n // 2
m = np.random.randint(2, n-2)

a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)
for i in range(n):
    c[i] = A[i, i]
    if i > 0:
        a[i] = A[i, i-1]
    if i < n-1:
        b[i] = A[i, i+1]

def left_progonka(a, b, c, f, m):
    alpha = np.zeros(n)
    beta = np.zeros(n)
    alpha[0] = -b[0] / c[0]
    beta[0] = f[0] / c[0]
    for i in range(1, n):
        denominator = c[i] + a[i] * alpha[i - 1]
        alpha[i] = -b[i] / denominator
        beta[i] = (f[i] - a[i] * beta[i - 1]) / denominator
    return alpha, beta

def right_progonka(a, b, c, f, m, n):
    xi = np.zeros(n - m + 1)
    eta = np.zeros(n - m + 1)
    xi[0] = -a[n-1] / c[n-1]
    eta[0] = f[n-1] / c[n-1]
    for i in range(1, n - m):
        denominator = c[i] + b[i] * xi[i - 1]
        xi[i] = -a[i] / denominator
        eta[i] = (f[i] - b[i] * eta[i - 1]) / denominator
    return xi, eta

def m_value(alpha, beta, xi, eta, m):
    denominator = 1 - xi[-1] * alpha[-1]
    ym = (eta[-1] + xi[-1] * beta[-1]) / denominator
    return ym

def backward(alpha, beta, xi, eta, ym, m, n):
    y = np.zeros(n)
    y[m] = ym
    
    for i in range(m - 1, -1, -1):
        y[i] = alpha[i] * y[i + 1] + beta[i]
    
    for i in range(1, n - m):
        y[n - 1 - i] = xi[i - 1] * y[n - i] + eta[i - 1]
    y[n - 1] = beta[n - 1]
    return y

alpha, beta = left_progonka(a, b, c, f, m)
xi, eta = right_progonka(a, b, c, f, m, n)
ym = m_value(alpha, beta, xi, eta, m)
y = backward(alpha, beta, xi, eta, ym, m, n)

print(m)
print("Решение системы методом встречной прогонки:")
print(y)

print(a, b)