text = input("Enter the text: ")

text.lower()

count = 0

vowels = "aeiou"

for i in text:

    if i in vowels:

        count += 1
    
print(count)