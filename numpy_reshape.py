'''
reshape() function is used to change the dimension of an array.
We can use it as:
(variable).reshape(no._of_rows, no._of_elements_in_each_row)
'''
import numpy as np
a= np.array([1,2,3,4,5,6,7,8,9])
print(a)
print(a.ndim)
b= a.reshape(3,3)
print(b)
print(b.ndim) # Converted as a 2 dimensional array

c= np.array([1,2,3,4,5,6,7,8])
d= c.reshape(2,2,2)
print(d)
print(d.ndim) # Converted as a 3 dimensional array

one= d.reshape(-1)
print(one)
print(one.ndim) # Converted as a 1 dimensional array