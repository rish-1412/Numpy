import numpy as np

'''Where function (used to search from array)'''
a= np.array([2,4,6,8,1,3,5,7,9,2,3,4,1,7,5,8,6,9,0,2,4])
b= np.where(a==2) # returns index where a is 2
print(b)
c= np.where((a%2)==0) # returns index where whenever any value is divided by 2, remainder is 0
print(c)
d= np.where((a+1)== 5) # returns index where value is 4.
print(d)

'''Searchsorted function: It performs a binary search in the array and returns the index where the
    specified value would be inserted to maintain the search order.'''
e= np.array([1,2,3,4,7,8,9])
f= np.searchsorted(e,(5,6))
print(f)
print(np.searchsorted(e,[10,11,12,13]))
# We can also define a side to the function, by default it goes left to right

'''Sort function: We can sort numeric/ alphabetic arrays in ascending order.'''
a1= np.array([12,27,30,9,3,6,1,99,78,64,15,10,23])
b1= np.sort(a1)
print(b1)
c1= np.array(["d","a","c","x","i","h","e"])
print(np.sort(c1))

'''Filter function: Getting some elements out of an existing array and creating a new array out of them.'''
d1= np.array([10,20,30,40,50])
e1= [True,False,False,False,True]
f1= d1[e1]
print(f1)
print(type(f1))