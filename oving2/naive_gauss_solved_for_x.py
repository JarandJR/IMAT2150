import numpy as np

def naive_gauss(A,b):
   n,m = np.shape(A)
   S = np.zeros((n,n+1))
   S[:,0:n] = A
   S[:,-1] = b
   for j in range(n-1):
      for i in range(j+1,n):
         mult = S[i,j]/S[j,j]
         S[i,j]=0.0
         for k in range( j + 1, n):
            S[i,k] = S[i,k] - mult*S[j, k]
         S[i, -1] = S[i, -1] - mult*S[j, -1]
            
   x = S[:,-1]
   for i in range(n -1, -1, -1):
      for j in range(i + 1,n):
         x[i] = x[i] - S[i, j] * x[j]
      x[i] = x[i]/S[i,i]
   return x

A = np.array([[1.0, 2.0, -1.0],
              [0.0, 3.0, 1.0],
              [2.0, -1.0, 1.0]])
b = np.array([2,4,2]).T
x = naive_gauss(A,b)
print(x)