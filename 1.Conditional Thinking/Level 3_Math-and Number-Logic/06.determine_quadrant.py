#Take coordinates (x, y) and determine which quadrant the point lies in.
x=int (input("enter x-axis :"))
y=int (input("enter y-axis:"))
if(x==0 and y==0):
    print("(0,0) is the center of all")
elif(x>0 and y>0):
    print("(",x,",",y,")","is the first I quadrant")
elif(x<0 and y>0):
    print("(",x,",",y,")","is the secound II quadrant")
elif(x<0 and y<0):
    print("(",x,",",y,")","is the third III quadrant")
else:
    print("(",x,",",y,")","is the fourth IV quadrant")