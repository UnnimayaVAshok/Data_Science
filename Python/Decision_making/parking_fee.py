parking_time = float(input("Enter parking time in hours: "))

if parking_time == 0:

    print("Invalid entry")

elif parking_time >= 1 and parking_time <= 2:

    print("Rs.20")

elif parking_time >= 3 and parking_time <= 5:

    print("Rs.50")

elif parking_time >= 6 and parking_time <= 10:

    print("Rs.100")

elif parking_time > 10:

    print("Rs.200")

else:

    print("Invalid input")