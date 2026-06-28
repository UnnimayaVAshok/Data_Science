number_1 = int(input("Enter a number : "))

number_2 = int(input("Enter another number : "))

print(f"Number_1 = {number_1} and Number_2 = {number_2}")

number_2 += number_1

number_1 = number_2 - number_1

number_2 -= number_1

print(f"After swaping....Number_1 = {number_1} and Number_2 = {number_2}")

# Another way

# number_1 , number_2 = number_2 , number_1

# using temporary variable

# temp = number_1

# number_1 = number_2

# number_2 = temp
