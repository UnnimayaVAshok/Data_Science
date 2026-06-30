# perfect number, sum of factors excluding the input = number

n = int(input("Enter the input: "))

sum = 0

for i in range(1,n//2 + 1):

    if n % i == 0:

        sum += i

print("Perfect number" if n == sum else "Not perfect number")