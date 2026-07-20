# find the largest digit in a number

number = int(input("Enter the number: "))

largest = 0

while(number > 0):

    digit = number % 10

    if largest < digit:

        largest = digit

    number //= 10

print(largest)