#Print Stars and Spaces Alternating (Stars and Blank Spaces)
n=5
for i in range(1,n):
    for j in range(1,n-i):
        print("b",end="")
    for k in range(1,2*i):
        if(k%2==0):
            print("*",end="")
        else:
            print("b",end="")
    print()
