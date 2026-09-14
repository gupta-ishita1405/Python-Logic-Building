a=int(input("enter a number"))
b=int(input("enter a number"))
if(a%2==0 and b%2==0):
    print("both even")
elif(a%2!=0 and b%2!=0):
    print("both odd")
else:
    print("one even and one odd")