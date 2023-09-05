import numpy as np

def fix_point_solve(f, x0, tol):
    iter_count = 0 
    max_iter = 1000
    while True:
        x1 = f(x0)  
        if np.abs(x1 - x0) < tol or iter_count > max_iter:  
            return x1
        x0 = x1
        iter_count += 1
    raise Exception("Fixed-point iteration did not converge")

f1 = lambda x: (2*x + 2)**(1/3)
f2 = lambda x: np.log(7 - x)
f3 = lambda x: np.log(4 - np.sin(x))

funcs = [f1, f2, f3]
max_error = 1e-8
solved = []

for f in funcs:
    x_solved = fix_point_solve(f=f, x0=0, tol=max_error)
    solved.append(x_solved)

print(f"Solution to f1 x = {solved[0]:.8f}")
print(f"Solution to f2 x = {solved[1]:.8f}")
print(f"Solution to f3 x = {solved[2]:.8f}")
