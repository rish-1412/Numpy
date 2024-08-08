# For different arithmetic operations used in numpy, refer to the image saved in the same folder.

import numpy as np 
# Maximum and minimum
a= np.array([14,32,11,23,2,4,10,67,89,68,92])
print("max: ",np.max(a))

print("min: ",np.min(a))

# argmin and argmax gives the positional values of the min. and max. data
print(np.argmax(a)) # Output= 10
print(np.argmin(a)) # Output= 4

# Square root
b= np.array([1,4,9,16,25,36,49,64,81,100])
print(np.sqrt(b))

# Sine and cosine
c= np.array([0,30,45,60,90,120,180,270,360])
print(np.sin(c))
print(np.cos(c))

# Cumulative sum
d= np.array([1,2,3,4,5,6,7,8,9,10])
print(np.cumsum(d))