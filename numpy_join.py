import numpy as np

# Using concatenate function

# For 1D array
a= np.array([1,2,3,4])
b= np.array([5,6,7,8])
c= np.concatenate((a,b))
print(c)

# For 2D array (we can join along either axis 1 or axis 0)
d= np.array([[1,2],[3,4]])
e= np.array([[5,6],[7,8]])
f= np.concatenate((d,e), axis=0)
print(f)
g= np.concatenate((d,e), axis=1)
print(g)


# Using Stack function (we need to define axis here whenever using stack function)

# For 1D array
a1= np.array([1,2,3,4,5])
b1= np.array([6,7,8,9,10])

c1= np.stack((a1,b1),axis=0) # it becomes a 2D array
print(c1)
d1= np.stack((a1,b1),axis=1) # # it becomes a 2D array
print(d1)

# If don't want to use axis along with stack function
e1= np.hstack((a1,b1)) # along row # becomes a 1D array
f1= np.vstack((a1,b1)) # along column # becomes a 2D array
g1= np.dstack((a1,b1)) # along height # becomes a 3D array
print(e1)
print(f1) 
print(g1)

# Stack function for 2D array
a2= np.array([[1,2,3],[4,5,6]])
b2= np.array([[7,8,9],[10,11,12]])
c2= np.stack((a2,b2),axis=0)
print(c2)

# Can similarly use hstack, vstack and dstack for 2D arrays