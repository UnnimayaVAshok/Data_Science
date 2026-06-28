mark = int(input("Enter the mark: "))

if mark >= 0 and mark <= 100:

    if mark > 90:

        print("You scored A grade")

    elif mark > 75 and mark <= 90:

        print("You scored B grade")

    elif mark >= 60 and mark <= 75:

        print("You scored C grade")

    else:

        print("You failed")

else:

    print("Get out")