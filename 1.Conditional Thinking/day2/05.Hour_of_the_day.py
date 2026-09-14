hour=int(input("enter hour in 24 hour format :-"))
if(hour>=4 and hour<=12):
    print("good morning")
elif(hour>12 and hour<=16):
    print("good afternoon")
elif(hour>16 and hour<=19):
    print("good evening")
elif(hour>19 and hour<=23):
    print("good night") 