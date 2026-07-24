# raise
#============

# used to create an exception manually if it doesnt meet any condition

# using raise we can throw custom exceptions during the runtime

# Used when we want to stop the execution because a condition is invalid

# we can raise ValueError,IndexError,....

age = int(input("Enter your age: "))

if age < 18:

    raise Exception("Invalid age")

print("Thank you")

# assert >>> AssertError
#=============================

# used to check a condition is True.If the condition is false Python automatically raises a AsserError

# used for debugging and unit testing to catch program mistakes

# assert Condition , "Error message"

age = int(input("Enter the age: "))

assert age > 18 ,"Invalid Age"

print("Thank you")