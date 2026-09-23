
#Check if a number is a perfect number.
n=int(input("enter a number:-"))
m=n
sum=0
for i in range (1,n):
    if (n%i ==0):
        sum=sum+i 
print(sum)
if(sum==m):
    print("Perfect Number")
else:
    print("Not Perfect Number")