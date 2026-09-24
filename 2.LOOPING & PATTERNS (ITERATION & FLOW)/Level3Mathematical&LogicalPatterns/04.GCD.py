#Find HCF (GCD) of two numbers using loops.
n1=int(input ("enter a number n1:-"))
n2=int(input ("enter a number n2:-"))
while(n1!=n2):
    if(n1>n2):
        n1=n1-n2
    elif(n2>n1):
        n2=n2-n1
    print(n1,n2)
        
