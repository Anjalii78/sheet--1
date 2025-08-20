#WAP to find the sum of all natural numbers from 1 to N where you have to take N as input from user
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of natural_number:",sum)