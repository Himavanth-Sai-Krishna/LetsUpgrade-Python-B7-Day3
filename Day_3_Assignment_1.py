#Day 3 - Assignment 1

x=int(input("Enter The Altitude:"))

if x<=1000:
    print("Safe To Land")
elif (x>1000) & (x<5000):
    print("Bring Down To 1000")
else:
    print("Turn Around")
