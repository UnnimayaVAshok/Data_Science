# wap to find the sum of cubes from 1 to n

n = int(input("Enter the number: "))

i = 1

sum = 0

while(i <= n):

    sum += i**3

    i += 1

print(sum)