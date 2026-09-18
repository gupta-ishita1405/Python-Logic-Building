#Take a password string and check basic rules (length ≥ 8 and contains at least one digit).
password=str(input("enter password:-"))
if(len(password)>=8 and any(map(str.isdigit, password))):
    print("valid")
else:
    print("invalid")