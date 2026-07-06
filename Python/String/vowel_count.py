# count how many times each vowel appears

text = input("Enter the text: ")
text = text.lower()
vowels = "aeiou"
count = 0
new = ""

for i in text:
    
    if i in vowels:

        if i not in new:

            count = text.count(i)
            print(i,count)
            new += i