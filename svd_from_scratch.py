import numpy as n
import numpy.linalg as alg

A = n.array([[1,2],[3,4],[5,6]])
print (A)
U,s,V = alg.svd(A)
print(U,)
print(s,)
print(V,)
Sigma = n.zeros((A.shape[0],A.shape[1]))
print (Sigma)
Sigma[:A.shape[1],:A.shape[1]] = n.diag(s)
print (Sigma)
B = U.dot(Sigma.dot(V))
print (B)
