# define a function to check and return the armstrong numbers from 100 to 1000

def is_armstrong(n):
    
    length = len(str(n))
    total = 0

    for i in str(n):

        total += int(i) ** length

    if n == total:

        return n 

for i in range(100,1001):

    result = is_armstrong(i)

    if result != None:

        print(result) 