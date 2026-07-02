# print difference btw consecutive prime numbers from 2 to n

n = int(input("Enter the number: "))

count = 0

for i in range(2,n+1):

    difference = 0

    for j in range(2,i):

        if i % j == 0:

            break

    else:

        count += 1

        if count == 2:

            difference = i - k

            print(f"Difference between {i} and {k} is {difference}")

            count = 0

        k = i

    


