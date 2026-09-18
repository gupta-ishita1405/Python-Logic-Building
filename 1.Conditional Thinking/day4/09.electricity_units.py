#Take electricity units consumed and calculate the bill as per slabs (using if-else). 
units=int (input("enter units"))
if(units<=100):
    units=units*5
    print(units)
elif(units<=200):
    units=(units*5)+(units-100)*7
    print(units)
else:
    units=(units*5) + (units*7) + ((units - 200)*9)
    print(units)
