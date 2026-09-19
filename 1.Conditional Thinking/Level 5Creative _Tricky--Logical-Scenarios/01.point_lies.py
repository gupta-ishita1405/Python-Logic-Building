#Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin. 
x=int(input ("enter a number for x-axis:-"))
y=int(input ("enter a number for y-axis:-"))
if y==0:
    print("X-axis")
elif x==0 :
     print("Y-axis")
else:
    print("origin")

