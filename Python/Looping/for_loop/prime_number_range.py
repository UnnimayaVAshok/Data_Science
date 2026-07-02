# Print prime numbers from 1000 to 100

for i in range(1000,99,-1):

    for j in range(2,i):

        if i % j == 0:

            break

    else:

        print(i)