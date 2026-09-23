#Print the squares of numbers from 1 to n. 
n=10
for i in range (1,n+1):
    for j in range(1,i+1):
        if(i==j):
            sum=i*j
            print(sum)