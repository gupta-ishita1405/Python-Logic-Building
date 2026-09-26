#Print all numbers whose sum of digits is even (1–100). 
for i in range (1,101):
    n=i
    sum=0
    while(n>0):
        v=i%10
        sum=sum+v
        n=n//10
    if(sum%2==0):
        print("sum even",i)
    