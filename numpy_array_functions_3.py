import numpy as np

'''Insert function: It inserts value into an array at a specified index
    syntax: np.insert(variable_of_array, index_value_where_value_to_be _inserted, value_to_be_inserted)'''

# For 1D array
a= np.array([1,2,3,4,5,6])
print(np.insert(a, 3, 100))
# Can also insert value at more indices
print(np.insert(a, (0,4), 99))
# Can also insert more values
print(np.insert(a, 2, (45,50,33)))

# For 2D array (need to define axis also)
b= np.array([[1,2,3], [4,5,6]])
print(np.insert(b, 1, 23, axis=0))
print(np.insert(b, 1, 23, axis=1))

# ** Limitation of insert function ** : It cannot insert float values into array.

'''Append function: Can insert values into array and also float values can be inserted using append.'''
c= np.array([[23,44,56],[78,100,81]])
print(np.append(c, [[10.8,99.99,50.5]], axis=0))

'''Delete function: deletes certain value from array.
    syntax: np.delete(variable_of_array, index_of_value_to_be_deleted)'''
d= np.array([1,2,3,4,5,6])
print(np.delete(d, (2,4))) # 3 and 5 will be deleted from array d.