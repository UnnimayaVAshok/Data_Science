# wap to get the unique characters from the string joined together

text = "programming"

new = ""

for i in text:

    if text.count(i) == 1:

        new += i

print(new)