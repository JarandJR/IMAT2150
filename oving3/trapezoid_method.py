import numpy as np

def trapes(f, y_init, h, t_slutt):
   t = np.arange(0,t_slutt + h, h)
   y = np.zeros_like(t)
   y[0] = y_init
   for i in range(1,t.size):
      s1 = f(t[i-1], y[i-1])
      s2 = f(t[i-1]+h, y[i-1]+h*s1)
      y[i] = y[i-1] + (1/2)*h*(s1 + s2)
   return t, y

f = lambda t,y: (t**2)*y
y_exact = lambda t: np.exp((t**3)/3)
t, y = trapes(f, 1, 0.25, 1.0)
error = np.abs(y - y_exact(t))

headers = ["t", "trapes", "error"]
print(f"{headers[0]:<8}{headers[1]:<8} {headers[2]:<8}")
for i in range(t.size):
   print(f"{t[i]:<8.2f}{y[i]:<8.3f}{error[i]:<8.3f}")