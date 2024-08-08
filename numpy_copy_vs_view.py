'''
For difference between copy and view, refer to the related image in the same folder.
Basic difference is that, any changes made to the existing data won't be reflected in the copied data 
    as it is an independent data but it would reflected in the viewed data.
'''
import numpy as np
original_data= np.array([1,2,3,4,5,6])

copied_data= original_data.copy()
print(copied_data)

# *** Changes are made now:
original_data[3]= 10 # We are replacing the 3rd index i.e. 4 with 10.

viewed_data= original_data.view()
print(viewed_data)
