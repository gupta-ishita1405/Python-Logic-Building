#Take a weekday number (1–7) and determine if it is a weekday or weekend. 
n=int(input("enter to find weekday or weekend"))
days=["","Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if(n==6 or n==7):
    print("weekend")
else:
    print("weekday")