# find sum of odd digits of a number

number = int(input("Enter a number: "))

odd_sum = 0

while(number > 0):

    digit = number % 10

    if digit % 2 != 0:

        odd_sum += digit

    number //= 10

print(odd_sum)