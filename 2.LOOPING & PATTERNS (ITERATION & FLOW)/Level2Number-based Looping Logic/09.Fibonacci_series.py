#Print Fibonacci series up to n terms.
n= int(input("enter a number"))
a=0
b=1
for i in range (1,n+1):
    print(a)
    next = a + b
    a = b
    b = next
    


    