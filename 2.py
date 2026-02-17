# /USing function to convert celsius to farhenheit
# Formula- c= 5 * (f-32)/9
def temp(f):
    # f=int(input("Enter temp:"))
  
   
    return 5*(f-32)/9
  
    
f=int(input("Enter temp:"))
print(f"The temp in farenherit is {round(temp(f),2)}°C")



