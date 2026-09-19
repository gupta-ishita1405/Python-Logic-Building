a=int (input(print("Enter the first side of triangle: ")))
b=int (input(print("Enter the second side of triangle: ")))
c=int (input(print("Enter the third side of triangle: ")))
if (a+b>c and a+c>b and b+c>a):
    print("The triangle is valid")  
else:
    print("The triangle is not valid")