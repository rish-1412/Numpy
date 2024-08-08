import numpy as np

'''Matrix vs Array: Both have some differences based on the arithmetical operations performed and 
    by their type.'''
a= np.array([[1,2,3,4,5,6]])
print(a)
print(type(a)) # <class 'numpy.ndarray'>

b= np.matrix([[1,2,3,4,5,6]])
print(b)
print(type(b)) # <class 'numpy.matrix'>

# Hence from above, we can see that their types are different.
# As studied in 11th, matrix multiplication is different whereas in array multiplication,
# corresponding values are multiplied and shown as result.
# In matrix multiplication, shapes should be in the form (p*q),(q*n) and they can be multiplied (np.dot())
# In array multiplication, shapes can be in any form (np.multiply())