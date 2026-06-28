num = int(input("Enter the number: "))

product = 1

while(num != 0):

    digit = num % 10

    if digit % 2 != 0:

        product *= digit

    num //= 10

print(product)
