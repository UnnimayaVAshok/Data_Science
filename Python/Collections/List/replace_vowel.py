strings = ["python","education","apple"]

vowels = "aeiouAEIOU"

for i in strings:
    word = ""
    for j in i:

        if j in vowels:

            word += "*"

        else:

            word += j

    strings[strings.index(i)] = word
    
print(strings)

    