# reverse a number using while

number = int(input("Enter a number: "))

reversed = 0

while(number > 0):

    digit = number % 10

    reversed = reversed * 10 + digit

    number //= 10

print(reversed)