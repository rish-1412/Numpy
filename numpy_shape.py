import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.shape) # Output= (2,4) which means it is a 2x4 matrix.

b= np.array([1,2,3,4], ndmin=4) # creating a 4 dimensional array using ndmin=4
print(b)
print(b.shape) # Output= (1, 1, 1, 4) which means it has 3 blocks with only 1 row and 4 columns.