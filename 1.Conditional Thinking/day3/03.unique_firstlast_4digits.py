n=int(input("enter 4 digit number :"))
last=n%10
first=n//1000
if(first==last):
    print("first and last are equal")
else:
    print("unequal")