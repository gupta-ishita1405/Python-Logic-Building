#Print a Centered Pyramid of Stars
n=10
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end ="")
    print()                   
        
