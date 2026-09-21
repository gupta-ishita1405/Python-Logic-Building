#Print the sum of all odd numbers up to n.
n=int(input("enter a no.:-"))
sum=0
for i in range(1,n,2):
    sum=sum+i
    print(i)
print("sum of odd no.:",sum)