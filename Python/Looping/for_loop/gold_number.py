"""
A number is a gold number if:

it is divisible by 3

it is not divisible by 5

sum of digits is even

print all gold number from 1 to n

"""

n = int(input("Enter the range: "))

for i in range(1,n+1):

    sum = 0

    for j in str(i):

        sum += int(j)

    if sum % 2 == 0:

        if i % 3 == 0 and i % 5 != 0:

            print(i)