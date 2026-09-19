#Take time (hours and minutes) and print the smaller angle between the hour and minute hands. 
hours=int(input("enter hours"))
minutes=int(input("enter minutes"))
hourAngle = (hours % 12) * 30 + minutes * 0.5
minuteAngle = minutes * 6
angle = abs(hourAngle - minuteAngle)
if angle > 180:
    angle = 360 - angle
print(angle)