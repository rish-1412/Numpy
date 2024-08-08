# Rand function which generates random values between 0 and 1
import numpy as np
a= np.random.rand(4) # generates a 1D array with 4 random numbers between 0 and 1
print(a)

b= np.random.rand(3,4) # generates a 2D array (3x4) with random numbers between 0 and 1
print(b)

c= np.random.rand(1,2,3) # generates a 3D array with random numbers between 0 and 1
print(c)

# Randn function which generates random values close to 0 which could be positive or negative
d= np.random.randn(4) # generates a 1D array with values close to 0
print(d)

e= np.random.randn(3,4)
print(e)