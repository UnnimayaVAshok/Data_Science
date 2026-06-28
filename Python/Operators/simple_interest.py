principle_amount = int(input("Enter the principle amount"))

tenure = int(input("Enter the number of years"))

rate_of_interest = float(input("Enter the rate of interest"))

simple_interest = (principle_amount * tenure * rate_of_interest) / 100

print(f"Simple interest is {simple_interest}")