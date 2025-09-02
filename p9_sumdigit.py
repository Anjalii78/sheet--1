n = int(input("Enter a no. : "))
sum = 0
while(n > 0) : 
    r =  n % 10
    sum +=r
    n = n//10
print("Sum of Digits : ",sum)
# take an integer N as input.your task is to calculate and print the sum of the digits of the given number N
