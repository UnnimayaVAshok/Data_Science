hours = int(input("Enter the number of hours : "))

minutes = int(input("Enter the number of minutes : "))

seconds = int(input("Enter the number of seconds : "))

total_seconds = seconds + (minutes * 60) + (hours * 60 * 60)

print(f"Total number of seconds : {total_seconds}")