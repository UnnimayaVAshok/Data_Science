# exception handling
#======================
# Exception is the error occuring during the run time(program is running)

# while getting an exception python stop the execution abruptlt and getting a traceback

# By exception handling
#======================

# program starts >>> exception occurs >>> Exception can be handled >>> program continuess

# wap to get division of 2 numbers

num_1 = int(input("Enter the number: "))

num_2 = int(input("Enter the number: "))

try:

    result = num_1 / num_2
    print(result)

    # try block is used to keep the risky code(where exception may occur during run time)

except:

    print("Division by zero not possible")

    # Except block runs only if any exception occurs in try block

print("end")