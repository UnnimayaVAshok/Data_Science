# find occurnce of a given character without count()

text = input("Enter the text: ")

char = input("Enter the character to count: ")

frequency = 0

for i in text:

    if i == char:

        frequency += 1

print(frequency)