'''
It is to be noted that the number of data contained in an array should be according to the 
dimension of the array. For e.g. in a two dimension array we can only fit two lists and similarly
in a three dimension array we can fit three lists.
'''
import numpy as np
a= np.array([[1,2,3,4], [1,2,3,4]])
print(a) # if 3 lists are typed then it will show error.
print(a.ndim)

b= np.array([[[1,2,3,4], [1,2,3,4], [1,2,3,4]]])
print(b)
print(b.ndim)