#Count the number of digits in a given number. 
n=int (input("enter a number"))
count=0
while(n>0):
    count=count+1
    n=n//10

print(count)