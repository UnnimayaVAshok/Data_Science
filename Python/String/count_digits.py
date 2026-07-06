text = input("Enter a string: ")
count = 0

for i in text:

    if i.isalpha() == False:

        count += 1

print(count)