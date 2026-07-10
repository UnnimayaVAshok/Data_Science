# given an integer n,return True if n is within 10 of either 100 or 200

def within_10(n):

    return True if (n >= 90 and n <= 110) or (n >= 190 and n <= 210) else False

print(within_10(200))
