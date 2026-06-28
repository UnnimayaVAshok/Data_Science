number = int(input("Enter the number: "))

if number % 2 == 0:

    if number >= 2 and number <= 5:

        print("Not weird")

    elif number >= 6 and number <= 20:

        print("Weird")

    elif number > 20:

        print("Not weird")

    else:

        print("get out")

else:
    
    print("Weird")
    