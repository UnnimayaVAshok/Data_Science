num = int(input("Enter the number: "))

sum = 0

while(num != 0):

    digit = num % 10

    if digit % 2 == 0:

        sum += digit

    num //= 10

print(sum)
