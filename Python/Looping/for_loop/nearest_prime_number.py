n = int(input("Enter the number: "))

while(n <= 1):

    n = int(input("Enter the number greater than 1: "))

for i in range(n+1,n**2):

    for j in range(2,i):

        if i % j == 0:

            break

    else:

        print(i)

        break