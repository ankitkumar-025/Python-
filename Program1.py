# Array is same as list  but it stores same types of data...
# import array as arr
# arr.array()

from array import *
vals=array('i',[2,3,4,5,64,-9]) #int-> i
print(vals.buffer_info()) #buffer_info() willl give u the size and the address.

print(vals.typecode)
vals.reverse()
print(vals)

for i in vals:# or range(len(vals)) ->print(vals[i])
    print(i)

#Create a new array:
newArr=array(vals.typecode,(a for a in vals))  

for i in vals:# or range(len(vals)) ->print(vals[i])
    print(i) 


# Using While loop:

# i=0
# while i<len(newArr):
#     print(newArr[i])
#     i+=1    
print(newArr) 

