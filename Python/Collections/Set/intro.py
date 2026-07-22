items = set() # in empty string

items = {1,True,"hello","python","hello"}
print(items)

nums = [1,2,3,4,5]

print(set(nums))

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

set_1.union(set_2) # {1,2,3,4,5,6,7,8}

# combine all he elements from the given set and return in anew set

set_1.intersection(set_2) # {4,5}

# return the common elements from the given set

set_1.difference(set_2) #{1,2,3}

# return the element in a new set which is present in set_1 but not present in set_2

set_1 = {1,2,3,4,5}
set_2 = {3,4,5}

print(set_1.issubset(set_2)) # False
print(set_1.issuperset(set_2)) # True

"""
a subset is a smaller set whose elements are all contained within a larger set

a superset is a larger set which contain all elements of a smaller set
"""