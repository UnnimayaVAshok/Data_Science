mark = int(input("Ente the mark: "))

if mark == 100:

    print("Perfect score")

elif mark >= 75 and mark <= 99:

    print("Passed with distinction")

elif mark >= 50 and mark <= 74:

    print("Passed")

elif mark >= 35 and mark <= 49:

    print("Re-Appear")

elif mark < 35 and mark >= 0:

    print("Failed")

else:

    print("Invalid input")