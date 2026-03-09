n=int(input())
num=n
count=0
while num>0:
    count+=1
    num=num//10
print(count)     

# Alternate way
#from math import *
# return int(log(10)(num)+1)