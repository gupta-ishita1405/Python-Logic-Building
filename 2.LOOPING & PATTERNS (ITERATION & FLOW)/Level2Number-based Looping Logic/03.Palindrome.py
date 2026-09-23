#Check if a number is a palindrome. 
n=int (input ("enter a number : "))
m=n
v=0
while(n>0):
    v= v *10 + n % 10
    n=n//10
if (m==v):
    print("palindrome")
else:
    print("not")