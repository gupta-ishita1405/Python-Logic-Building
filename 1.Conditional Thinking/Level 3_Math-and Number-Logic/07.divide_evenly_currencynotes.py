#Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
x=int(input("enter amount:"))
if(x%100==0):
    print("evenly divided")
else:
    print("not evenly divided")