#Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
amount=int(input("entr amount value"))
if(amount%2000 ==0 and amount%500 ==0 and amount%100==0):
    print("evenly")
else:
    print("unevenly")