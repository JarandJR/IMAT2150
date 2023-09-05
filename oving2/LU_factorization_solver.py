import numpy as np

def LUfactorize(A):
   n, m = np.shape(A)
   L = np.eye(n)
   U = A.copy()
   for j in range(n):
      for i in range(j + 1, n):
         if U[j, j] == 0.0:
            raise np.linalg.LinAlgError("Zero pivot encountered")
         mult = U[i, j] / U[j, j]
         U[i, j:] = U[i, j:] - mult * U[j, j:]
         L[i, j] = mult
      for k in range(j + 1, n):
         U[k, j] = U[k, j] / U[j, j]
   return L, U

   
def LUsolve(L,U,b):
    c = np.zeros_like(b)
    n = len(c) 
    for i in range(n):
        c[i] = b[i]
        for j in range(i):
            c[i] = c[i] - L[i, j] * c[j]

    x = c.copy()
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] = x[i] - U[i, j] * x[j]
        x[i] = x[i] / U[i, i]

    return x

A = np.array([[3., 1., 2.], [6., 3., 4.], [3., 1., 5.]])
b = np.array([0., 1., 3.])
try:
   L,U = LUfactorize(A)
   x = LUsolve(L,U,b)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")

print(x)