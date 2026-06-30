"""
harshad number is a positive whole number
it is divisible by sum of its digits

"""

number = int(input("Enter the number: "))

sum = 0

for i in str(number):

# Converting number to  a string so we can look at each digit
# loops over each character in number

    sum += int(i)

# converting string digit into integer for arithmetic operation

print("Harshad" if number % sum == 0 else "Not harshad")

"""
number = int(input("Enter the number: "))

temp = number

sum = 0

while(number > 0):

    digit = number % 10

    sum += digit

    number //= 10

print("Harshad" if temp % sum == 0 else "Not harshad")

"""