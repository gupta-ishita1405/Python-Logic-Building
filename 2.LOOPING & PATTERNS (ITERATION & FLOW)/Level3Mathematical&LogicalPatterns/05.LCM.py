#Find LCM of two numbers using loops
n1=int(input ("enter a number n1:-"))
n2=int(input ("enter a number n2:-"))
sum =1
m= n1
n=n2
while(n1!=n2):
    if(n1>n2):
        n1=n1-n2
    elif(n2>n1):
        n2=n2-n1
hcf=n1
lcm=m*n // hcf
    
print(lcm)
        