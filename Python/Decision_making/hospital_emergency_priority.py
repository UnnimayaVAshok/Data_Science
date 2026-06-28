priority = int(input("Enter the priority: "))

if priority == 0:

    print("No treatment required")

elif priority >= 1 and priority <= 3:

    print("Normal checkup")

elif priority >= 4 and priority <= 6:

    print("Priority consultation")

elif priority == 7 or priority == 8:

    print("Emergency ward")

elif priority == 9 or priority == 10:

    print("ICU admission")

else:

    print("Invalid input")

