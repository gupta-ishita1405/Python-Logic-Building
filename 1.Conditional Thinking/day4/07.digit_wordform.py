#Take a single digit (0–9) and print its word form (“Zero” to “Nine”). 
digit=int(input("enter a day number:"))
match  digit:
    case 1:
        print("one")
    case 2:
        print("Two ")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("nine")
    case _:
        print("invalid ")


