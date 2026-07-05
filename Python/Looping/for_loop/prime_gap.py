# print difference btw consecutive prime numbers from 2 to n

n = int(input("Enter the number: "))

previous_number = 0


for i in range(2,n+1):

    for j in range(2,i):

        if i % j == 0:

            break

    else:

        if previous_number != 0:

            print(f"Difference between {i} and {previous_number} is {i - previous_number}")
    
        previous_number = i

    


