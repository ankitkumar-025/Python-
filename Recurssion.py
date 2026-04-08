# Recurrsion
# Using Recursion print "Ankit" 4 times

# Head Recurrsion:First doing job i.e..Printing("Ankit") then Calling the function func()
# count=0
# def func():
#     global count
#     if (count==4):
#         return
#     print("Ankit")
#     count+=1
#     func()
# func()  

# Tail Recurrsion:First calling the function func(),then doing job i.e,Printing("Ankit")
count=0
def func():
    global count
    if count==4:
        return
    count+=1 
    func()
    print("Ankit")
func()

# Note: Here Time complexity=O(N) also it is O(N+1) approx-O(N)
# AND Space Complexity =O(N)

