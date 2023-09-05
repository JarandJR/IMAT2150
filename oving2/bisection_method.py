import numpy as np

def bisection_solve(f, a,b, tol):
   while (b - a)/2 > tol:
      c = (a + b)/2 
      f_c = f(c)

      if f_c == 0:
         break
      if f(a) * f_c < 0:
         b = c
      else:
         a = c

   return c

f = lambda x: x**3 - 9
max_error = 10**-6
a = 1
b = 3
x_solved = bisection_solve(f,a,b, max_error)
print(x_solved)
