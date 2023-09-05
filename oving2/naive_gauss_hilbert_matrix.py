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

def create_hilbert_matrix(n):
    H = np.zeros((n,n))
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            H[i - 1,j - 1] = 1.0 / (i + j - 1)
    return H
   
ns = [2, 5, 10]
xs = []
for n in ns:
    H = create_hilbert_matrix(n)
    b = np.ones(n)
    x = naive_gauss(H, b)
    
    xs.append(x)
    backward_error = (np.max(np.abs(np.dot(H, x) - b)))
print(xs[0])
print(xs[1])
print(xs[2])