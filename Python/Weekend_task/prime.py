# print all prime numbers between 1 and N

n = int(input("Enter the limit: "))

prime_numbers = []

for i in range(2,n):
    
    for j in range(2,i):

        if i % j == 0:

            break
        
    else:

        prime_numbers.append(i)

print(prime_numbers)