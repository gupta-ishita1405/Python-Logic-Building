n=int(input("enter 3 digit number:"))
h=n//100
t=(n//10)%10
o=n%10
if(h!=o and h!=t and t!=o):
    print("all digits are distinct")
else:
    print("all digits are not distinct")