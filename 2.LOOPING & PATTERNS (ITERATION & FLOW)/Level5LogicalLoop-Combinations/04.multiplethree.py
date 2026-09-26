#Print numbers between 1–100 whose digits add up to a multiple of 3. 
count=0
for i in range (1,101):
    sum=0
    n=i
    while(n>0):
        r=n%10
        sum=sum+r
        n=n//10
    if(sum%3==0):
        count+=1
        print(i)
print(count)
        