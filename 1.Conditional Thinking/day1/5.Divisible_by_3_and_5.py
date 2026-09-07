print("Divisible by 3 and 5 checker")
n=int(input("Enter a number: "))
if (n%3==0 and n%5==0):
    print(n,"is divisible by both 3 and 5")
elif (n%3==0):  
    print(n,"is divisible by 3")
else:
    print(n,"is not divisible by either 3 or 5")