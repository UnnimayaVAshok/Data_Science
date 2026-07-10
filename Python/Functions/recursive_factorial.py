# when we call the factorial(5) it didn't get the immediate answers

# it has to wind up a stack of function calls until it hits the base case

def factorial(n):

    if n == 0 or n == 1:

        return 1
    
    else:

        return n * factorial(n-1)
    
print(factorial(5))