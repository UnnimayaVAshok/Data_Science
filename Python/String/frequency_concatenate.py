text = "programming"

new = ""

for i in text:

    if i not in new:

        new += i + str(text.count(i))

print(new)