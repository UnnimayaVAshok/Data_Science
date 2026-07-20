# count how many digita are divisible by 3

number = int(input("Enter a number: "))

count = 0

while(number > 0):

    digit = number % 10

    if digit % 3 == 0:

        count += 1

    number //= 10

print(count)