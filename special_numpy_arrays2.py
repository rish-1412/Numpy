# Array with range of elements
import numpy as np
a= np.arange(5)
print(a)  # [0 1 2 3 4]

b= np.arange(1,4)
print(b)  # [1 2 3]

# Array with diagonal elements filled with 1's
a_diag= np.eye(4) # creates a 4x4 identity matrix
print(a_diag)

b_diag= np.eye(2,3) # creates a 2x3 matrix with diagonal elements as 1's
print(b_diag)

# Create an array with values that are spaced linearly in a specified interval  # linspace
a_space= np.linspace(0, 20, num=5) # starts with 0 then intervals are taken as (20-0)/4 = 5
print(a_space)

b_space= np.linspace(1,29,num=8) # starts with 1 then intervals are taken as (29-1)/7 = 4
print(b_space)