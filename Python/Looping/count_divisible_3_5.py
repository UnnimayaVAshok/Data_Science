# wap to count the numbers divisible by 3 and 5

n = int(input("Enter the number: "))

i = 1

count = 0

while(i <= n):

    if i % 3 == 0 and i % 5 == 0:

        count += 1

    i += 1

print(count)