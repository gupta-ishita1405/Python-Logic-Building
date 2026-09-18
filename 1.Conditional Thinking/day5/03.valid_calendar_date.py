#Take day and month and check if it forms a valid calendar date (ignoring leap years).
date=int(input("enter date ;- "))
month=int(input("enter month ;- "))
if (month ==2):
    if(month>=1 and month<=28):
        print("valid")
    else:
         print("Invalid")
elif(month ==4 or month==6 or month==9  or month==11):
    if(month>=1 and month<=30):
        print("valid")
    else:
         print("Invalid")
elif(month ==1 or month==3 or month==5  or month==7 or month ==8 or month==10 or month==12  ):
    if(month>=1 and month<=30):
        print("valid")
    else:
         print("Invalid")
else:
    print("Invalid")
