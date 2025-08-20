N = int(input("Enter a number: "))
count = 0
num = abs(N)   

if num == 0:   
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Count of digits:", count)

# take an integer N as input and print the count of that number