"""
A prime number is a whole number greater than 1
only divided by 1 and thet umber itself

"""
"""
n = int(input("Enter the number: "))

for i in range(2,n):

    if n % i == 0:

        print("Not prime")

        break

else:

    print(f"{n} is prime")

"""

n = int(input("Enter the number: "))

while(n <= 1):

    n = int(input("Enter a number greater than one: "))

for i in range(2,n):

    if n % i == 0:

        print(f"{n} is not a prime number")

        break

else:

    print(f"{n} is a prime number")