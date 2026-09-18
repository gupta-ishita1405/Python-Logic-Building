#Take 24-hour time (hours and minutes) and print whether it is AM or PM. 
hour=int(input("enter hour in 24 hour format :-"))
minutes=int(input("enter minutes: "))
if(minutes<=60 and hour<24):
    if(hour<12): print(hour,":",minutes,"AM")
    else: print(hour,":",minutes,"PM")
else:
    print("wrong time")