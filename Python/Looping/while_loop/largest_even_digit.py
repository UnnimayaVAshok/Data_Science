num = int(input("Enter the number: "))

largest = 0

while(num != 0):

    digit = num % 10

    if digit % 2 == 0 and digit > largest:

        largest = digit

    num //= 10

print(largest)
