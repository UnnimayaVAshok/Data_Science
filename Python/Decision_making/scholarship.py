mark = int(input("Enter the mark: "))

income = int(input("Enter the income: "))

if mark >= 80:

    if income <= 200000:

        print("Eligible for full scholarship")

    else:

        print("Eligible for partial scholarship")

elif mark >= 60 and mark <= 79:

    if income <= 100000:

        print("Eligible for partial scholarship")

    else:

        print("No scholarship")

elif mark < 60:

    print("No scholarship")

else:

    print("Invalid input")