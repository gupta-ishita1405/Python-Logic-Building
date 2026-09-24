#Check if a number is a strong number.
n=int(input("enter a number:-"))
m=n
count=0

while(n>0):
    v=n%10
    sum=1
    for i in range (1,v+1):
        sum=sum * i
    count=count +sum
    n=n//10
if(m==count):
    print("Strong Number")
else:
    print("not")


