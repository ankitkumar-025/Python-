# Print x,N times
def func(x,N): #Here x=24 and N=4 times
    if N==0:
        return
    print(x)
    func(x,N-1)
func(6,4)

