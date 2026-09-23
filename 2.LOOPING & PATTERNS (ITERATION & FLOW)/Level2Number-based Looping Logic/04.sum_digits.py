#Find the sum of digits of a number.
n=int ( input ("enter a number:"))
v=0
count =0
while(n>0):
    v=n%10
    count = count + v
    n = n // 10
print (count)