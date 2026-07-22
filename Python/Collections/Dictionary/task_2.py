mobiles = {"Apple":{"model":"iphone 13","price":130000,"color":"black"},
           "Samsung":{"model":"Galaxy S21","price":95000,"color":"white"},
           "Google":{"model":"Pixel 6","price":40000,"color":"black"}
          }

# wap to print the model and price of each model in the dictionary

result = {}

for i in mobiles:

    value = mobiles.get(i)

    model = value.get("model")

    price = value.get("price")

    result[i] = [model,price]

print(result)

# wap to get the mobile model name which have price in btw 50k and 1 lakh

for i in mobiles:

    value = mobiles.get(i)

    model = value.get("model")

    price = value.get("price")

    if price > 50000 and price < 100000:

        print(model)


# wap to get the mobiles which have the price above 90k and color is black

for i in mobiles:

    value = mobiles.get(i)

    # model = value.get("model")

    price = value.get("price")

    color = value.get("color")

    if price > 90000 and color == "black":

        print(i)

