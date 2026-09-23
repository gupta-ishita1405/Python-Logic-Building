#Print the sum of all even numbers up to n.
n=int(input("entr a number to find its even sum:- "))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    print(i)
print("sum of even no.:",sum)