#Recursion is a function where it calling itself..
# It is used to directly use a mathematical formula as function..
# Factorial(5)
# factorial(n)= n * factorial(n-1)
def fact(n):
    if (n==1 or n==0):  # fact(1)=1 and fact(0)=1
        return 1
    return n * fact(n-1)
  


n=int(input("Enter a number:"))
print(f"The factorial of the given nummber is : {fact(n)}")
# print(fact(n))