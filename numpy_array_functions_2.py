import numpy as np

'''Shuffle function: Used to shuffle data in array'''
a= np.array([1,2,3,4,5,6,7,8,9,0])
b= np.random.shuffle(a)
print(a)

'''Unique function: Removes duplicates in array and returns array with all unique values'''
c= np.array([1,2,3,4,5,2,3,4,6,7,8,5,6,9,1,2])
print(np.unique(c))
# With index values
print(np.unique(c, return_index= True))
# with index values and with count i.e. how many times particular value repeated
print(np.unique(c, return_index=True, return_counts=True))

'''Resize function: Resizes an array into particular shape'''
d= np.array([10,20,30,40,50,60])
print(np.resize(d,(2,3))) # 2 rows and 3 columns
print(np.resize(d,(3,2))) # 3 rows and 2 columns

'''Flatten function: It convertes a 2D/nD array back into 1D array.
        For flatten we have order of arrays like:
          'C' means to flatten in row-major(C-style) order. By default C-style is there.
          'F' means to flatten in column-major (Fortran-style) order.
          'A' means to flatten in column-major order if 'a' is Fortran *contiguous* in memory, row-major
            order otherwise.
          'K' means to flatten 'a' in the order the elements occur in memory.'''
e= np.array([[1,2,3],[4,5,6]])
print(e.flatten())
print(e.flatten(order="F"))

'''Ravel Function: same as Flatten function, just syntax is different.'''
f= np.ravel(e)
print(f)
print(np.ravel(e,order="F"))