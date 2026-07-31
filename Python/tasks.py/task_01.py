# 1)Write a Python program that asks the user to input three numbers. Based on the input, perform the following tasks:**

# If the sum of the three numbers is greater than 100, print their product.**

# If the sum is between 50 and 100 (inclusive), print their average.**

# If the sum is less than 50, check if any of the numbers is divisible by 5. If true, print the smallest number among them.**

#  If none of the numbers is divisible by 5, print the largest number.**

num_1 = int(input("Enter the number: "))
num_2 = int(input("Enter the number: "))
num_3 = int(input("Enter the number: "))
total = num_1 + num_2 + num_3
if total > 100:

    print(num_1 * num_2 * num_3)

elif total <= 100 and total >= 50:

    print(total/3)

elif total < 50:

    if num_1 % 5 == 0 or num_2 % 5 == 0 or num_3 % 5 == 0:

        print(min(num_1,num_2,num_3))

    else:

        print(max(num_1,num_2,num_3))



