import numpy as np

def trapes(f, y_init, start, stop, h):
    n = int((stop - start) / h) + 1
    t = np.linspace(start, stop, n)
    y = np.zeros((n, len(y_init)))
    y[0, :] = y_init

    for i in range(1, n):
        t_prev, y_prev = t[i-1], y[i-1, :]
        k1 = f(t_prev, y_prev)
        k2 = f(t[i], y_prev + h * k1)
        y[i, :] = y_prev + 0.5 * h * (k1 + k2)

    return t, y

def f(t, y):
    return np.array([y[0] + y[1], -y[0] + y[1]])

def exact_solution(t):
    return np.array([np.exp(t) * np.cos(t), -np.exp(t) * np.sin(t)])

y_init = np.array([1, 0])
t, y = trapes(f, y_init, 0, 1, 0.25)

exact = exact_solution(t).T
error = np.abs(y - exact)

print("t      y[0]          y[1]    error[0]      error[1]")
for i in range(t.size):
    print(f"{t[i]:.2f}   {y[i, 0]:.6f}   {y[i, 1]:.6f}   {error[i, 0]:.6f}   {error[i, 1]:.6f}")
