#Take three numbers and print the median value (neither maximum nor minimum).
a=int(input("enter value "))
b=int(input("enter value "))
c=int(input("enter value "))
if(a==b==c):
    print ("equal")
elif(b>= a and b<=c) or (b>=c and b<=a):
    print ("b is median",b)
elif((a>= b and a<=c) or (a>=c and a<=b)):
    print("a is median",a)
else:
    print ("c is median",c)