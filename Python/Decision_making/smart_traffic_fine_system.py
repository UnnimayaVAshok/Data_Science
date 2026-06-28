speed = int(input("Enter the speed: "))

if speed >= 0 and speed <= 60:

    print("Safe driving")

elif speed >= 61 and speed <= 80:

    print("Warning")

elif speed >= 81 and speed <= 100:

    print("500 fine")

elif speed >= 101 and speed <= 120:

    print("2000 fine")

else:

    print("License suspension recommended")