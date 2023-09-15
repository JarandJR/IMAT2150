import numpy as np

def euler(f, y_init, start, stop, h):
    n = int((stop - start) / h) + 1 
    t = np.linspace(start, stop, n)  
    y = np.zeros((n, len(y_init))) 
    y[0, :] = y_init
    
    for i in range(1, n):
        y[i, :] = y[i-1, :] + h * f(y[i-1, :])
        
    return t, y

def y_exact(t):
    return np.array([3 * np.exp(-t) + 2 * np.exp(4 * t), -2 * np.exp(-t) + 2 * np.exp(4 * t)])

f = lambda y: np.array([y[0] + 3*y[1], 2*y[0] + 2*y[1]])
y_init = np.array([5, 0])
t, y = euler(f, y_init, 0, 1, 0.25)

exact = y_exact(t).T
error = np.abs(y - exact)

print("t      y[0]          y[1]    error[0]      error[1]")
for i in range(t.size):
    print(f"{t[i]:.2f}   {y[i, 0]:.6f}   {y[i, 1]:.6f}   {error[i, 0]:.6f}   {error[i, 1]:.6f}")
