#Body Mass Ratio

"""
Women: BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161

"""
weight = float(input("Enter the weight"))

height = float(input("Enter the height in cm"))


age = float(input("Enter the age"))

bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

print(bmr)