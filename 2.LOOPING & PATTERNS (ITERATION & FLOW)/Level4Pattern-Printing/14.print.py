#
n=9
num=1
for i in range(0,n+1):
    for j in range(1,i):
        print(num,end=" ")
        num=num+1
        if(num==10):
            num=0
    print()
