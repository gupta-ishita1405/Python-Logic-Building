#Print sum of first n terms of Fibonacci series. 

n=int(input("enter a number:- "))
a=0
b=1
sum =0
for i in range(1,n+1):
    sum=sum+a
    next = a+b
    a=b
    b=next
print(b)