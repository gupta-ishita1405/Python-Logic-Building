#Print first n terms of a geometric Progression.
m= int(input("enter a number"))
first=int(input("enter a first number"))
ratio=int(input("enter a ratio number"))

for i in range(1,m+1):
    print(first* ratio **(i-1))