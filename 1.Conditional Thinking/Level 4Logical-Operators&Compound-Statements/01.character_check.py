#Take a character and check if it is a letter, a digit, or neither. 

chara=input("enter character")
if ("A"<=chara<="Z" or "a" <=chara<="z"): print("is letter")
elif ("0"<=chara <="9"):print("is digit")
else: print("neither")
