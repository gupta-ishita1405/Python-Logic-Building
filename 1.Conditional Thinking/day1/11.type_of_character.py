n=input("Enter a character: ")  
if (n>="A" and n<="Z"):
    print(n,"is an uppercase letter.")  
elif (n>="a" and n<="z"):
    print(n,"is a lowercase letter.")   
elif (n>="0" and n<="9")    :
    print(n,"is a digit.")  
else:
    print(n,"is a special character.")