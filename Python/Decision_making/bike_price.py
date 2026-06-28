bike_price = int(input("Enter the price of bike: "))

if bike_price > 200000:

    tax = bike_price * 0.12

elif bike_price >= 100000 and bike_price <= 200000:

    tax = bike_price * 0.10

else:

    tax = bike_price * 0.07

print(f"Total price of bike is {bike_price + tax}") 