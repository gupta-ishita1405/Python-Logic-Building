print("Type of Triangle Checker")
a=int(input("enter the first side of the triangle:- "))
b=int(input("enter the secound side of the triangle:-"))
c=int(input("enter the third side of the triangle:-"))
if (a+b>c and b+c>a and a+c>b):
    if(a==b and b==c):
        print("equilateral Triangle")
    elif(a==b or b==c or a==c):
        print("isosceles triangle")
    else:
        print("Scalene Triangle")    
else:
    print("The triangle is not valid")        