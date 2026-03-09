# Array values from user in Python:
from array import *
arr=array('i',[])
n=int(input("Enter the length of the array:"))

for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print(arr)

# Searching the element:
# getting index of the element:
vals=int(input("Enter the value for search:"))
k=0
for e in arr:
    if e==vals:
        print(k)
        break
    k+=1

# or we can use a function to find the inex of a searching element in the array:

# print(arr.index(vals))

