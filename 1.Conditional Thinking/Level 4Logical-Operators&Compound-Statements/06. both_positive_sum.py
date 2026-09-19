#Take two numbers and check if both are positive and their sum is less than 100. 
a=int(input("enter a number "))
b=int(input("enter a number "))
if(a>0 and b>0):
    c=a+b
    print("sum ",c)
else:
    print("negative")