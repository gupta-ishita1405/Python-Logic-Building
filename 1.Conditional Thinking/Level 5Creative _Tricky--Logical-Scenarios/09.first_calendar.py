#Take two dates (day and month) and determine which one comes first in the calendar. 
a=int(input("Enter the month 1: "))
b=int(input("Enter the month 2: "))
date1=int(input("enter the month 1 date:- "))
date2=int(input("enter the month 2 date:- "))
if (a>b):
    print(a,"is the month will come first",date1)
else:
    print(b,"is the month will come first",date2)