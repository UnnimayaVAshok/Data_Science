# 4)Write a Python program that takes a positive integer as input and performs the following tasks:**



# 	Reverse the digits of the number.**

# 	If the reversed number is greater than 500, print "Reversed Number is Greater than 500".**

# 	If the reversed number ends with 0, print "Reversed Number Ends with 0".**

# 	If none of these conditions are met, print "Reversed Number does not meet any condition".**

number = int(input("Enter a positive number: "))
reversed = 0
while number > 0:

    digit = number % 10
    reversed = reversed * 10 + digit
    number //= 10
#print(reversed)
if reversed > 500:

    print("Reversed Number is Greater than 500")

elif str(reversed).endswith("0"):

    print("Reversed Number Ends with 0")

else:

    print("Reversed Number does not meet any condition")