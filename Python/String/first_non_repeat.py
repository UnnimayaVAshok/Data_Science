# wap to get first  non repeating character from the text

text = input("Enter the string: ")

for i in text:

    if text.count(i) == 1:
        print(i)
        break