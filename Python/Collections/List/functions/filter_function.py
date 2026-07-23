# filter()

# keeps only items for which the condition is True

# Syntax

# filter(function,iterable)

numbers = [1,2,3,4,5,6,7,8]

print(list(filter(lambda a:a % 2 == 0,numbers)))

# using filter function get the numbers divisible by 3 from 1 to 20

print(list(filter(lambda a:a % 3 == 0,range(1,21))))