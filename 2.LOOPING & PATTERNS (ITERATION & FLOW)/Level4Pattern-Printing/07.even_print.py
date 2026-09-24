#Print Stars in Even Numbers (2, 4, 6, 8, 10)
n=11
for i in range(1,n):
    if(i%2==0):
        for j in range(1,i+1):
            print("*",end="")
        print()