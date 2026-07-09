# define a function to get the total number of vowels in the string enter by user

def count_vowels(text):

    vowels = "aeiou"

    text = text.lower()

    count = 0

    for i in text:

        if i in vowels:

            count += 1

    print(count)

count_vowels("hello")