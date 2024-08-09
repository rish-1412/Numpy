# We can use "ndmin" function to ultimately convert an array into any dimensional array. max= 32

import numpy as np
a= np.array([1,2,3,4], ndmin = 10)
print(a) # it will be printed as a 10 dimensional array
print(a.ndim)

b= np.array([1.23, 43.2, 78], ndmin = 32)
print(b)
print(b.ndim)