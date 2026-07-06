# print every second character from the string

# text = "python" output = "yhn"

text = "python"

new = ""

for i in text:

    if text.index(i) % 2 != 0:

        new += i

print(new)