#WAP to print all even number from 1 to N where you have to take N as input from the user
n=int(input("enter the number: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)