imimport numpy as n
import numpy.linalg as alg

A = n.array([[1,2],[3,4],[5,6]])
print ("Original Matrix:: \n",A)
U,s,V = alg.svd(A)
print("U:: \n",U)
print("Sigma:: \n",s)
print("V:: \n",V)
Sigma = n.zeros((A.shape[0],A.shape[1]))
Sigma[:A.shape[1],:A.shape[1]] = n.diag(s)
print ("Sigma NxN:: \n",Sigma)
B = U.dot(Sigma.dot(V))
print ("Recomposing:: \n",B)
d = 1/s
D=n.zeros(A.shape)
D[:A.shape[1],:A.shape[1]]=n.diag(d)
Pinv = U.dot(D.dot(V))
print ("PsudoInverse:: \n",Pinv)
