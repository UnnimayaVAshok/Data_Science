"""
Spy number 

sum of digits equal to product of digits

number = 123

sum = 6

product = 6

"""
"""
number = int(input("Enter the number: "))

sum = 0

product = 1

for i in str(number):

    sum += int(i)

    product *= int(i)

print("Spy number" if sum == product else "Not a spy number")

"""

number = int(input("Enter the number: "))

sum = 0

product = 1

while(number > 0):

    digit = number % 10

    sum += digit

    product *= digit

    number //= 10

print("Spy number" if sum == product else "Not a spy number")
