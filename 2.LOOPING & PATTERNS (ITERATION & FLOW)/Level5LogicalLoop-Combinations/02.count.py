#Count how many numbers between 1–500 are divisible by 7 but not by 5.

n=500

for i in range (1,n+1):
    count=0
    if(i%7==0 and i%5!=0):
        count=count+1
print(count)
    