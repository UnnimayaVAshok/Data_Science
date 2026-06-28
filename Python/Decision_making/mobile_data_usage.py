gb = float(input("Enter the data used in GB: "))

if gb == 0:

    print("No usage")

elif gb >= 1 and gb <= 2:

    print("Normal usage")

elif gb >= 3 and gb <= 5:

    print("High usage")

elif gb >= 6 and gb <= 8:

    print("Warning")

elif gb > 8:

    print("Limit exceeded")

else:

    print("Invalid input")