# check whether a number is palindrome or not

number = int(input("Enter a number: "))

def is_palindrome(number):
    
    temp = number

    reversed = 0

    while(number > 0):

        digit = number % 10

        reversed = reversed * 10 + digit

        number //= 10

    if temp == reversed:

        return "Palindrome"
    
    else:

        return "Not Palindrome"
    
print(is_palindrome(number))