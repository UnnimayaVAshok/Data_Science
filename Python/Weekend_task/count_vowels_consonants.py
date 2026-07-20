# count vowels and consonants in a string

text = input("Enter the text: ")

vowels = "AEIOUaeiou"

count_vowels = 0

count_consonants = 0

for i in text:

    if i in vowels:

        count_vowels += 1

    else:

        count_consonants += 1

print(f"{count_vowels} vowela and {count_consonants} consonants")