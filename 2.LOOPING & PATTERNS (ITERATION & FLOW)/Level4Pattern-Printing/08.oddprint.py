#Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=11
for i in range(1,n):
    if(i%2!=0):
        for j in range(1,i+1):
            print("*",end="")
        print()