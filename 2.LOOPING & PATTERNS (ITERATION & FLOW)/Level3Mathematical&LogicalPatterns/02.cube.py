# Print cubes of numbers from 1 to n.
n= int ( input ("enter a number"))
sum=1
for i in range(1,n+1):
    for j in range (1,i+1):
        for k in range (1,j+1):
            sum= i * j * k
    print(sum)
            


