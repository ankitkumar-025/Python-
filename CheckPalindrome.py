n=int(input("Enter a number:"))
num=n
result=0
while num>0:
    largest_digit=num%10
    result=(result*10)+largest_digit
    num=num//10
if n==result:
    print("It is Palindrome")
else:
    print("Not Palindrom")    
    
   