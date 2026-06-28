days = int(input("Enter the number of days : "))

years = days // 365

#print(f"Years : {years}")

months = (days % 365) // 30

#print(f"Months : {months}")

remaining_days = (days % 365) % 30

#print(f"Remaining days in a month : {remaining_days}")

print(f"{years} years , {months} months and {remaining_days} days")