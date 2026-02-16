def gratestOfThreeNum(a,b,c):
    # a=int(input("Enter 1st number: "))
    # b=int(input("Enter 1st number: "))
    # c=int(input("Enter 1st number: "))
    if a>=b and a>=c:
        print("a is greatest")
        return a
    elif b>=a and b>=c:
        print("b is greatest")
        return b
    else:
        print("c is greatest")
        return  c  
         

gratestOfThreeNum(1,2,3)       

gratestOfThreeNum(5,3,2)         
    