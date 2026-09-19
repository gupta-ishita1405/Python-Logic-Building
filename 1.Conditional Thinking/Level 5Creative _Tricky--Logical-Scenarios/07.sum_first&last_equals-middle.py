#Take a 3-digit number and check if the sum of the first and last digit equals the middle digit. 
n=int(input("enter three digit no.:-"))
hundred=n//100
ones=n%10
tens=(n//10)%10
if(hundred+ones==tens):
    print("equal")
else:
    print("unqual")