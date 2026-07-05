text = input("Enter the text: ")

text.lower()

vowels = "aeiou"

new = ""

for i in text:

    if i in vowels:

        new += i

print(new)