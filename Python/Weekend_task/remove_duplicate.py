# remove duplicate character in a string

text = input("Enter the text: ")

new = ""

for i in text:

    if i not in new:

        new += i

print(new)