''' Ranf function: It is used to do random sampling in numpy. It returns an array of specified shape
fills it with random floats in the half open interval [0.0, 1.0) i.e. values greater than or equal to 
0 but less than 1 '''

import numpy as np
a= np.random.ranf(5)
print(a)

''' Randint function: Generates random values between two given numbers.
Used in this format= np.random.randint(min, max, total_number_of_values_to_be_generated) '''

b= np.random.randint(5,20,10) # 10 values to be generated between 5 and 20
print(b)