A = int(input("Enter a number: "))
original = A
reverse = 0

while A > 0:
    digit = A % 10
    reverse = reverse * 10 + digit
    A //= 10

if original == reverse:
    print("Yes")   
else:
    print("No")    
    
#You are given an integer A as input, and you need to determine whether it is a palindrome
#or not. A palindrome integer is one whose digits, when reversed, result in the same number.
 