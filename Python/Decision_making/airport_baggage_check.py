weight = float(input("Enter the weight of luggage in kg: "))

if weight == 0:

    print("No luggage")

elif weight >= 1 and weight <= 15:

    print("Allowed")

elif weight >= 16 and weight <= 25:

    print("Extra charge")

elif weight >= 26 and weight <= 40:

    print("Heavy baggage")

elif weight > 40:

    print("Not Allowed")

else:

    print("Invalid input")