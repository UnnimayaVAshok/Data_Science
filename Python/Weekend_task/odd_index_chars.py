# print characters at odd index positions

text = input("Enter the text: ")

chars = []

for i in range(len(text)):

    if i % 2 != 0:

        chars.append(text[i])

print(chars)