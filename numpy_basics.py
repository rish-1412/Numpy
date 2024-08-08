import numpy as np
x= np.array([1,2,3,4])
print(x)
print(type(x))

l= []

for i in range(1,5):
    int_1= int(input("enter: "))
    l.append(int_1)

print(np.array(l))