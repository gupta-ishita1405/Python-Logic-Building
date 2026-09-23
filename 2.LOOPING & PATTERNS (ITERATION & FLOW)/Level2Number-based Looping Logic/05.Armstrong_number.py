#  check if a number is an Armstrong number.
n=int (input("entre a number: "))
m=n
v=0
sum=0
while(n>0):
    v=n % 10
    sum=sum + v*v*v
    n= n // 10
if (m==sum):
    print("Armstrong number")
else:
    print("not")