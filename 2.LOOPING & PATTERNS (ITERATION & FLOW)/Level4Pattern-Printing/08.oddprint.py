#Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=11
for i in range(1,n):
    for j in range(1,2*i):
        print("*",end="")
    print()