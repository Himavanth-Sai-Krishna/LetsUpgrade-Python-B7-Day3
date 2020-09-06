#Day 3 - Assignment 2

print("The Prime Numbers from 1 to 200 are:")

for i in range(2,201):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
