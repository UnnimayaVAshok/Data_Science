total = 0

for i in range(1,6):

    n = int(input("Enter the number: "))

    number_include = input("Do you need to include this number...(y/n)")

    if number_include == "y":

        total += n

print(total)