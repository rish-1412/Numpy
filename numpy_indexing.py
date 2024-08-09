'''
For a 1D array: Indexing is same as in list. [2 3 4 5] has indices 0,1,2,3

For a 2D array: Let us consider a 2D array like [[1 2 3] [4 5 6]].
Here for outer brackets we have different indexing and different for inside.
[1 2 3] has 0 index and [4 5 6] has 1 index
also for inside indexing is like 1=> 0, 2=> 1, 3=>2    4=> 0, 5=> 1, 6=> 2

For a 3D array: Let us consider a 3D array like [[[1 2 3]] [[4 5 6]]].
[[1 2 3]] has 0 index then [[4 5 6]] has 1 index
[1 2 3] has 0 index and [4 5 6] has 1 index
also for inside indexing is like 1=> 0, 2=> 1, 3=>2    4=> 0, 5=> 1, 6=> 2
'''
import numpy as np
a= np.array([1,2,4])
print(a[0]) # Output is 1
print(a[-2]) # Output is 2

b= np.array([[1,2],[3,4]])
print(b[0,1]) # Output is 2 since we are finding it in outer index 0 and inside index 1
print(b[1,0]) # Output is 3 since we are finding it in outer index 1 and inside index 0

c= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c)
print(c.ndim)
print(c.shape)
print(c[0,1,1]) # Output is 5
print(c[1,1,0]) # Output is 10
print(c[0,0,0]) # Output is 1
print(c[1,1,1]) # Output is 11