def remove_vowels(text):
    new = ""
    vowels = "AEIOUaeiou"
    for i in text:
        if i not in vowels:
            new += i

    print(new)

remove_vowels("Education")