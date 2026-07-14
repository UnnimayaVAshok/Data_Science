text = "Education"

text = text.lower()

vowels = "aeiou"
count_vowels = 0
count_consonants = 0

for i in text:
    if i in vowels:
        count_vowels += 1
    else:
        count_consonants += 1

print(f"V = {count_vowels}, C = {count_consonants}")