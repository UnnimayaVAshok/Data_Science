# wap to get first  repeating character from the string

text = "programming"

for i in text:

    if text.count(i) > 1:

        print(i)

        break