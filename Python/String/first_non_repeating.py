# wap to get first two non repeating character from the text

text = "programming"
count = 0

for i in text:

    if text.count(i) == 1:
        count += 1
        print(i)

    if count == 2:
        break