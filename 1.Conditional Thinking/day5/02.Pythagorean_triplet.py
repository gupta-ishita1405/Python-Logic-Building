#Take three numbers and check if they can form a Pythagorean triplet. 
a=int(input("Enter the first Base: "))
b=int(input("Enter the second Height: "))
c=int(input("Enter the third Perpendicular: "))
if  (( (a * a) ==(b * b) + (c * c)) or( b * b == a * a + c * c )or (c * c == a * a + b * b )):
    print("Pythagorean triplet")
else:
    print("not")