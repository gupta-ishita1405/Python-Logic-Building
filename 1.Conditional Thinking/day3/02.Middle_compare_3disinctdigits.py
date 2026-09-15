n=int (input("enter 3 digit number:"))
h=n//100
t=(n//10)%10
o=n%10
if(h!=t and h!=o and t!=0):
    print("all digits are  distinct")
    if(t>h and t>o):
        print("t is largest")
    elif(t<h and t<o):
        print("t is smallest")
    else:
        print("neither")
else:
    print("not distinct")
