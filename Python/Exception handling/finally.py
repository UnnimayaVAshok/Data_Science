try:

    num1 = int(input("Enter the number: "))

    print(100 / num1)

except ZeroDivisionError:

    print("Division by zero not possible")

except ValueError:

    print("Enter proper numbers")

print("End")

# wap to get the index posiion from the user and display the element from the list

words = ["python","a","b","java","c"]

index = int(input("Enter the index: "))

try:

    print(words[index])

except IndexError:

    print("Enter a valid index position")

finally:

    print("Thank you")

    # this block runs always whether execution occurs or not