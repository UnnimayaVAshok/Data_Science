words = ["apple","banana","cherry"]  # ["Apple","Banana","Cherry"]

print([i.capitalize() for i in words])

# From a list of strings, build a list of strings that starts with the letter "a"

words = ["arun","apple","python","ml","arab"]

print([i for i in words if i[0] == "a"])

# given a list of words, return a list of word lengths

words = ["hello","world"]

print([len(i) for i in words])

# create a new list containing only the squares pf numbers that are divisible by 3 from 1 to 20

print([i ** 2 for i in range(1,21) if i % 3 == 0])

"""
given a sentence , use liist comprehension to build  a list of words that have more than 4 letters

"""

text = "python is a programming language"

print([i for i in text.split() if len(i) > 4])

# Dictionary comprehension
#==================================

words = ["python","programming","language"]

print({i:len(i) for i in words})

name = "programming"

print({i:name.count(i) for i in name})
