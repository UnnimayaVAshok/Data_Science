# map()

# applies afunction to every item in iterable

# syntax

# map(function,iterable)

numbers = [1,2,3,4,5] # return squares in list

print(list(map(lambda a:a ** 2,numbers)))

numbers = [1,2,3,4,5] # ["odd","even","odd","even","odd"]

print(list(map(lambda a:"even" if a % 2 == 0 else "odd",numbers)))