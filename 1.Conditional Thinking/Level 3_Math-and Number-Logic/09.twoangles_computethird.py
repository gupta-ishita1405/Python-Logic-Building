x=int (input("enter first angle"))
y=int (input("enter second angle"))
z=x+y
thirdangle=180-z
if x>0 and y>0 and thirdangle>0:print("the third angle is :",thirdangle)
else: print("not a triangle")