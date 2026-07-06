text = input("Enter the text: ")

for i in text:

    if text.index(i) % 2 == 0:

        print(i)