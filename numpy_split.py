'''
Split function can be used to split an array in the form:
np.array_split(variable_of_array, number_of_arrays_to_be_split_into)
'''

import numpy as np

# For 1D array
a= np.array([1,2,3,4,5,6,7,8,9,0])
b= np.array_split(a, 5)
print()
print(b)
print(type(b)) # it is a list

# If we want to print a single array then we can use indexing
print(b[0])
print(b[2])

# For 2D array
c= np.array([[1,2],[3,4],[5,6],[7,8]])
d= np.array_split(c,4)
print(d)
print(type(d))

# We can also split along any axis
print(np.array_split(c,4,axis=1))