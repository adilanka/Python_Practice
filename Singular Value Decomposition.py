import numpy as np
from numpy.linalg import eig

a = np.array([[2, 2, 4], 
              [1, 3, 5],
              [2, 3, 4]])
s,v=eig(a)
print('E-value:', s)
print('E-vector', v)

# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
# SVD
U, s, VT = svd(a)
print(U)
print("\n")
#Singular
print(s)
#Transpose
print("\n")
print(VT)
