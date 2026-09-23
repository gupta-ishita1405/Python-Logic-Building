#Print all numbers between a and b divisible by 7. 
a= int (input ("enter number from :- "))
b= int (input ("enter number too:- "))
for i in range(a,b+1):
    if(i%7==0):
        print(i)
