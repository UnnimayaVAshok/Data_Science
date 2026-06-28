#even or odd

number = int(input("Enter the number: "))

"""
if number % 2 == 0:

    print(f"{number} is even")

else:

    print(f"{number} is odd")

"""

# Ternary operator

print(f"{number} is even" if number % 2 == 0 else f"{number} is odd")