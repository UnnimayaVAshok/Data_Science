text = "PyThon"

new = ""

for i in text:

    if i.isupper():

        new += i.lower()

    else:

        new += i.upper()

print(new)
