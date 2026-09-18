#Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits
n=int(input("enter a number:-  "))

a=thousand=n//1000
b=hundred=(n//100)%10
c=tens=(n//10)%10
d=ones=n%10

sum=a+b+c+d
product=a*b*c*d
if(sum>product) :
    print("sum of its digits is greater than")
else:
    print("product is greater or equal")