water_level = int(input("Enter water level in percentage: "))

if water_level == 0:

    print("Reservoir empty")

elif water_level >= 1 and water_level <= 25:

    print("Critical level")

elif water_level >= 26 and water_level <= 50:

    print("Low level")

elif water_level >= 51 and water_level <= 75:

    print("Normal level")

elif water_level >= 76 and water_level <= 100:

    print("Full capacity")

elif water_level > 100:

    print("Flood alert")

else:

    print("Invalid input")