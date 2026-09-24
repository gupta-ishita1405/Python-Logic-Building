#Print first n terms of an arithmetic progression (a,d).
m= int(input("enter a number"))
first=int(input("enter a first number"))
differnce=int(input("enter a difference number"))

for i in range(1,m+1):
    print(first+ i *differnce)