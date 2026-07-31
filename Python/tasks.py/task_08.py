#7) wap to find the prime numbers below n where n is entered by user

n = int(input("Enter the limit: "))

for i in range(2,n+1):
    for j in range(2,i):

        if i % j == 0:
            break

    else:
        print(i)