n=int(input("Enter a Number:"))
num=n
no_of_digits=len(str(n))
total=0
while num>0:
    largest_digit=num%10
    total=total+(largest_digit**no_of_digits)
    num=num//10
    
if n==total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")        


