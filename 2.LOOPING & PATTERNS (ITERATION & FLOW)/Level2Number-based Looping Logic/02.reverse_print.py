#Print the reverse of a given number. 
n=int(input("enter a number to reverse:- "))
v=0
while (n > 0) :
    v = v * 10 + n % 10
    n=n//10
print(v)
