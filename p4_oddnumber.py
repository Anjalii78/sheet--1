#WAP to print all odd nunber from 1 to N where you have to take N as input from user
n=int(input("enter the number:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)