'''
Iteration can be done using for loop and for each dimension we need to use the loop corresponding times
to fully iterate it.
for e.g. 1D array=> 1 time for loop
for e.g. 2D array=> 2 times for loop
for e.g. 3D array=> 3 times for loop
'''
import numpy as np
# Iteration in 1D array
a= np.array([1,2,3,4,5,6,7,8,9])
for i in a:
    print(i)


# Iteration in 2D array
b= np.array([[1,2,3,4],[5,6,7,8],[8,9,10,11]])
for j in b:
    print(j) # this will only iterate the inner rows and won't fully iterate array if once used.
for k in b:
    for l in k:
        print(l) # this will fully iterate the array b.


# Iteration in 3D array
c= np.array([[[3,4],[5,6]],[[1,2],[9,10]],[[7,8],[11,12]]])
for m in c:
    print(m) # iterate once
for n in c:
    for o in n:
        print(o) # iterates twice
for p in c:
    for q in p:
        for s in q:
            print(s) # iterates fully the array c.