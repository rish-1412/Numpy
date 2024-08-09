import numpy as np

'''Transpose function: ixj converted into jxi'''
a= np.matrix([[1,2,3],[4,5,6]])
print(np.transpose(a))
# Or
print(a.T)

'''Swapaxes function: similar to transpose, just need to mention axes also.'''
b= np.matrix([[1,2],[3,4]])
print(np.swapaxes(b,0,1))

'''Inverse function: A^-1'''
c= np.matrix([[3,4],[1,2]])
print(np.linalg.inv(c))

'''Power function'''
d= np.matrix([[1,2],[3,4]])
print(np.linalg.matrix_power(d, 2)) # matrix multiplied by itself
print(np.linalg.matrix_power(d, 0)) # returns an identity matrix
print(np.linalg.matrix_power(d, -1)) # returns inverse*power of matrix

'''Determinant function (note: only possible in square matrix)'''
e= np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(np.linalg.det(e)) # Output= 0
f= np.matrix([[1,2],[3,4]])
print(np.linalg.det(f)) # Output= -2