'''
Broadcasting is an error which comes when performing operations on arrays lacking same
dimensions.
For e.g. arrays like [1 2 3] and [1 2 3 4] when added together shows broadcasting error.
Requirements for not showing broadcasting error:
1) Same dimension
2) Atleast in array shapes like (1,3) and (2,3); one number should be same in shape to perform
   the operations. The resultant array would be in the shape (2,3).
3) Atleast any one in the corresponding elements of shapes should be equal. For e.g. (1,2) and (2,2).
'''
import numpy as np
a= np.array([1,2,3,4]) # it is a (1,4) array
b= np.array([[10,2,3,4],[4,5,6,7]]) # it is a (2,4) array 
c= a+b
print(a)
print(b)
print(c)
print(c.shape)
print(a.shape)
print(b.shape)

# Another example
d= np.array([[1],[2]]) # it is a (2,1) array
e= np.array([[3,4,5],[6,7,8]]) # it is a (2,3) array
f= d+e
print(d)
print(e)
print(f)
print(d.shape)
print(e.shape)
print(f.shape)