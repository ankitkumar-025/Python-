# Pattern Printing Using Functions and Recurrsion
# n=int(input())
# for i in range(1,n+1):
#     print("*" *n)
#     n-=1
  
def pattern(n):
    if n==0:
        return 
    print("*" *n)
    pattern(n-1) #reccursion follow ...

pattern(5)    

n=int(input("enter a number: "))
print(pattern(n))
    
