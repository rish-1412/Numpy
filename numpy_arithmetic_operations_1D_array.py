# For different arithmetic operations used in numpy, refer to the image saved in the same folder.

import numpy as np

# Addition
a= np.array([1,2,3,4])
b= a + 5
print(b)  # Output = [6 7 8 9]
print(np.add(a,5)) # Output same as in print(b)

c= np.array([4,5,6,7])
print(np.add(a,c))  # a and c will be added and output = [5 7 9 11]
# can also use 'print(a + c)'

# Subtraction
print(a - 2)
print(np.subtract(a,c))

# Multiplication
print(c * 3)
print(np.multiply(a,c))

# Division
print(c/a)
print(np.divide(c,a))

# Modulus (%) = Gives remainder when something is divided by something
d= np.array([10,20,30,40])
e= np.array([3,6,9,12])
print(np.mod(d,e))

# Exponent/Power
print(d ** 2)
print(np.power(d,2))
print(np.power(a,c))

# Reciprocal
print(np.reciprocal(a))