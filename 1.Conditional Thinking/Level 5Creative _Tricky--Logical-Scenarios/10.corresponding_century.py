# Take a year and print the corresponding century (e.g., “19th century”, “20th century”) 
century=int(input("enter year:-  "))
century=century+100
a=thousand=century//1000
b=hundred=(century//100)%10

print("year is corresponding",century)
print ("century",a,b)