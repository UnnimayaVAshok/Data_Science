text = input("Enter the text: ")
char = input("Enter the charater: ")

for i in text:

    if i == char:

        print(text.index(i))
        break