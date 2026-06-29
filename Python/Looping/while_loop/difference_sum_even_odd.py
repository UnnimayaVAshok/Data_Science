n = int(input("Enter the number: "))

i = 1

sum_odd = 0

sum_even = 0

while(i <= n):

    if i % 2 == 0:

        sum_even += i

    else:

        sum_odd += i

    i += 1

print(sum_even - sum_odd)
