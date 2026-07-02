"""
An automorphic number is a number whose square ends in the same digits as the number itself

5 5**2 25
6 6**2 36
25 25**2 625
"""

number = int(input("Enter the number: "))

square = number ** 2

# length = len(str(number))

count = 0

for i in str(number):

    count += 1

print("Automorphic" if square % (10 ** count) == number else "Not automorphic")
