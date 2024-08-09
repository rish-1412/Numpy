# We can check and also convert the array data types usong "dtype" function.
import numpy as np

# To check the datatype
a= np.array([1,2,3,4])
print("Datatype: ", a.dtype)

b= np.array(["a", "b", "c", "d"])
print("Datatype: ", b.dtype)

# To convert the datatype
c= np.array([1,2,3,4], dtype= np.float32)
print("Datatype: ", c.dtype)

d= np.array([1,2,3,4], dtype= "f")  # 'f' represents float32
print("Datatype: ", d.dtype)
print(d)

# To convert in other ways
e= np.array([1.0, 2.0, 3.0, 4.0])
x= np.int_(e)  # int_ is used to convert into integer data type.
print(e)
print(e.dtype)
print(x)
print(x.dtype)
