n = int(input("Enter a no. n : "))
reverseNum = 0
myNum = n

while(n > 0) :
    last_digit = n % 10
    reverseNum = reverseNum * 10 + last_digit
    n = n//10
if(myNum  == reverseNum):
    print(myNum,"=",reverseNum,"This no. is a Palindrome")
else:
    print("no.",myNum,"is NOT a palindrome")
    
#You are given an integer A as input, and you need to determine whether it is a palindrome
#or not. A palindrome integer is one whose digits, when reversed, result in the same number.

 
