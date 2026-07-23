# define a functionto add 2 numbers

"""
def add_numbers(a,b):

    result = a + b

    return result
print(add_numbers(2,3))

"""

add_num = lambda num_1,num_2:num_1 + num_2

print(add_num(2,3))

# A lambda function is a small anonymous function_often written in one line

# syntax

# lambda args:expression

# writa lambda return the square of a number

square = lambda num_1:num_1 ** 2

print(square(5))

# create a lambda that eturn "Pass" if mark are 40 or above, otherwise "Fail"

result = lambda mark:"Pass" if mark >= 40 else "Fail"

print(result(75))

# define a function to find numbers divisible by both 3 and 5 from the given list

nums = [10,15,20,30,45,50,60]

result = lambda nums:[i for i in nums if i % 3 == 0 and i % 5 == 0]

print(result(nums))

# define a function palindromes from a list of words

words = ["madam","python","level","code","radar"]

palindromes = lambda words:[i for i in words if i == i[::-1]]

print(palindromes(words))

# define a function to check the number is positive negative or zero

result = lambda num_1:"Positive" if num_1 > 0 else("Negative" if num_1 < 0 else "Zero")

print(result(0))