# wap to create lists in python using a single expression.

# [new_item for item in iterable]

# new_item is the transformed value

# item comes from the iterable

numbers = [1,2,3,4,5]

result = [i ** 2 for i in numbers]

print(result)

print([i for i in numbers if i % 2 == 0])

"""
new = []

for i in numbers:

    new.append(i**2)

print(new)

"""

