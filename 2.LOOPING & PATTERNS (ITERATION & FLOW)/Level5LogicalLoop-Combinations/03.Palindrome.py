#Print all numbers that are palindromes between 1–500. 
count=0
for i in range(1,501):
    m=i
    sum=0
    while(i>0):
        r=i%10
        sum=sum*10+r
        i=i//10
    if(sum==m):
        count+=1
        print("palindrome",m)
print(count)
