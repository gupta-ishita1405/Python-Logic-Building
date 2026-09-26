#
n=9
ch=64

for i in range(1,n+1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+1):
        ch=ch+1
        print(chr(ch),end=" ")

    print()