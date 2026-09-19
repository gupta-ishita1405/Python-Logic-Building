#Take three numbers and check if they are in arithmetic progression. 
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a-b==b-c:
    print("arithmetic progression")
else:
    print("not")