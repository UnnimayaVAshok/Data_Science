# print every second character from the string

# text = "python" output = "yhn"

text = "pythontp"

new = ""

"""
for i in text:
                                    duplicate characters index doest get using this iteration
    if text.index(i) % 2 != 0:

        new += i

print(new)
"""
for i in range(len(text)):

    if i % 2 != 0:

        new += text[i]

print(new)
