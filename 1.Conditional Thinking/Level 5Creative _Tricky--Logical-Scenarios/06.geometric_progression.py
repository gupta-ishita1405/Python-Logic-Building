#Take three numbers and check if they are in geometric progression.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if (b * b == a * c):
    print(" geometric progression")
else:
    print("not")