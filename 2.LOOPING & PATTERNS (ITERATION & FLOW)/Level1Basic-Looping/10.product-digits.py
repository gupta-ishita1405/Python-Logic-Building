#Print the product of digits of a given number. 
n=int(input("enter a no.:-"))
sum=1
while(n>0):
    v=n%10
    sum= sum*v
    n=n//10

print(" no.:",sum)
