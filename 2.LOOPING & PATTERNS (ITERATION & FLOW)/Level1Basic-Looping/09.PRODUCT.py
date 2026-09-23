#Print the factorial of a given number.
n=int(input("enter a no.:-"))
sum=1
for i in range(1,n+1):
    sum=sum*i
    print(i)
print("factorial 10no.:",sum)