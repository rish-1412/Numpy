'''
If we want to fully iterate a 2D/3D/nD array at once we can use the function nditer().
If we want to have the iterated values along with their corresponding index we can use
    the function ndenumerate().
'''
import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(a):
    print(i)

b= np.array([[[1,2,3,4,5]]])
for j in np.nditer(b,flags=['buffered'],op_dtypes="S"): # converts iterations into string
    print(j)

c= np.array([[[1,2,3,4],[5,6,7]],[[2,4,5],[2,3,4,5]]])
for k,d in np.ndenumerate(c):
    print(k,d)