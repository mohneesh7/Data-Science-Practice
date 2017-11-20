import numpy as n
from scipy import sparse

matrix = n.vstack([[1,2,3],[2,3,4],[5,6,7],[7,8,9]])
matrix1 = n.vstack([[1,2,3],[2,3,4],[5,6,7],[7,8,9]])
matrix2 = n.vstack([[0,2,0],[0,0,4],[5,0,0]])
matrix3 = n.vstack([[0,2,0,7],[0,0,4,6],[5,0,0,3]])
# mean of a matrix
print "mean :",n.mean(matrix)

# variance
print "variance :",n.var(matrix)

# standard deviation
print "standard deviation :",n.std(matrix)

# reshape an array
print "reshaped to (2,6) :\n",matrix.reshape(2,6)

print "\n"

#add and subtract matrices

print "add m amd m1 :\n",n.add(matrix,matrix1),"\n"
print "subtract m1 :\n",n.subtract(matrix,matrix1),"\n"

# Do element operations using vectorize operation/map() like function for numpy arrays.

multiply_10 = lambda i:i*10
vectorize_function = n.vectorize(multiply_10)
print "multiplied 10 to every element :\n",vectorize_function(matrix),"\n"

# create a sparse matrix
matrix_sparse = sparse.csr_matrix(matrix2)
print "Sparse Matrix :\n",matrix_sparse,"\n"

print "shape :",matrix.shape,"\nSize :",matrix.size,"\nDimensions :",matrix.ndim,"\n"

# finding max and min of the matrix
print  "max of matrix :",n.max(matrix),"\nmin of matrix :",n.min(matrix),"\nmax by columns :",n.max(matrix,axis=0), \
		"\nmax by rows :",n.max(matrix,axis=1),"\n"

# inverse of a matrix
print "Inverse of the matrix :\n",n.linalg.inv(matrix2),"\n"

#calculate dot product
print "Dot product :\n",n.dot(matrix,matrix3),"\n"

# calculate the determinant of the matrix
print "Determinant of the matrix :\n",n.linalg.det(matrix2),"\n"

# calculate the trace of the matrix
print "Calculate trace of matrix :\n",matrix.diagonal().sum(),"\n"

# find the rank of a matrix
print "Rank of the matrix :",n.linalg.matrix_rank(matrix),"\n"

#flatten a matrix
print "flattened matrix :\n",matrix.flatten(),"\n"

# transpose a matrix
print "Transpose of the matrix :\n",matrix.T,"\n"



