# wap to count the numbers divisible by 2 and 7 from 1 to n

n = int(input("Enter the number: "))

i =1

count = 0

while(i <= n):

    if i % 2 == 0 and i % 7 == 0:

        count += 1

    i += 1

print(count)
        