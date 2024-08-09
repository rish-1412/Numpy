# For different arithmetic operations used in numpy, refer to the image saved in the same folder.
# It is to be noted that we are using 2D arrays here.
# To use the arithmetic functions in 2D arrays, we denote them by using axis.
# axis= 0: column, axis= 1: row

import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8]])  # created a 2D array
print(np.sum(a,axis=0)) # sum along column i.e. 1+5, 2+6, 3+7, 4+8
print(np.sum(a,axis=1)) # sum along row i.e. 1+2+3+4, 5+6+7+8

print(np.min(a,axis=0))
print(np.min(a,axis=1))

print(np.max(a,axis=0))
print(np.max(a,axis=1))

# Can perform similarly for other functions also.