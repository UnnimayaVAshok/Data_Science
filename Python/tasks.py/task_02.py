# 2)Write a Python program that asks the user to input a positive integer. The program should calculate 
# the sum of the digits of the number using a while loop.**

#  Additionally, if the sum of the digits is an even number, print "Sum is Even"; otherwise, print "Sum is Odd."**


number = int(input("enter a positive number: "))
total = 0
while number > 0:

    digit = number % 10
    total += digit
    number //= 10

print("Sum is even" if total % 2 == 0 else "Sum is odd")