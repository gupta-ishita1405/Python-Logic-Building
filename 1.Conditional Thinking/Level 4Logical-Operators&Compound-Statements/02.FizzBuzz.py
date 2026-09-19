#Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both.
n=int(input("enter no to find FizzBuzz:"))
if(n%3==0 and n%5==0):
    print("FizzBuzzz")
elif(n%5==0):
    print("Buzzz")
elif(n%3==0 ):
    print("FiZZ")