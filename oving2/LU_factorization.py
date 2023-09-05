import numpy as np

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
 
A = np.array([ 1.0,  2,-1,0,3,1,2,-1,1 ])
A=A.reshape((3,3))
try:
   L,U = LUfactorize(A)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")

print(L)
print(U)
