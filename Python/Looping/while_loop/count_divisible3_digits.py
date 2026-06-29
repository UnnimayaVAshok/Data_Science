num = int(input("Enter the number: "))

count = 0

while(num != 0):

    digit = num % 10

    if digit % 3 == 0:

        count += 1

    num //= 10

print(count)
