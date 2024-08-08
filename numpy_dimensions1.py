'''
The number of "[ ]" in an array is used to find out the dimension of an array.
For e.g. [1 2 3 4] is a one-dimensional array, [[1 2 3 4]] is a two dimensional array and 
[[[1 2 3 4]]] is a three dimensional array.

also we can check the dimensions of an array by the ndim function
'''
import numpy as np
l= np.array([1,2,3,4])
print(l)
print(l.ndim) # it is a one dimensional array

a= np.array([[1,3,4,6,7]])
print(a)
print(a.ndim) # it is a two dimensional array

b= np.array([[["hello world", 19, "Rishabh", 14, 12]]])
print(b)
print(b.ndim)