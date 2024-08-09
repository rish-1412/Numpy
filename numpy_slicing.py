'''
For slicing we just need to use the format: (variable_of_array)[start:stop] 
    in stop point we need to put the index as (stop_value+1)
For slicing with skip values we need to use format: (variable_of_array)[start:stop:skip/step]
'''
import numpy as np

# For 1D array
a= np.array([9,8,7,6,5,4,3,2,1,0])
print(a)
print("7 to 4: ", a[2:6])
print("6 to end: ", a[3:])
print("start to 4: ", a[:6])
print("with skip of 2 places from 8 to 2: ", a[1:8:2])
print("with skip of 2 places from start to end: ", a[::2])
print("with skip of 3 places from start to end: ", a[::3])


# For 2D array
b= np.array([[100,90,80,70,60],[50,40,30,20,10]])
print(b)
print("90 to 70: ", b[0,1:4])
print("40 to end: ", b[1,1:])
print("start to 70: ", b[0,:4])
print("with skip of 2 places from 100 to 70: ", b[0,:4:2])
print("with skip of 2 places from start to end: ", b[1,::2])
print("with skip of 3 places from start to end: ", b[0,::3])