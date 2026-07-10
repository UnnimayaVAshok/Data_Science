def is_perfect(n):

    result = 0

    for i in range(1,n):

        if n % i == 0:
            
            result += i

    return "Perfect" if n == result else "Not perfect"
    
print(is_perfect(6))