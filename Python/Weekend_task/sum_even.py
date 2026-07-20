# find sum of even numbers between two given values

num_1 = int(input("Enter the first number: "))

num_2 = int(input("Enter the second number: "))

total = 0

for i in range(num_1,num_2 + 1):

    if i % 2 == 0:

        total += i

print(total)
