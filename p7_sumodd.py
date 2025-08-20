
A = int(input("Enter a number: "))
odd_sum = 0
for i in range(1, A+1):
    if i % 2 != 0:
        odd_sum += i
print("Sum of odd numbers:", odd_sum)

#take an integer A as input.you have to print the sum of all odd number in the range[1,A]