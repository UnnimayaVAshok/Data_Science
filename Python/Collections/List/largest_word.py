string = "Python is a programming language"

largest = 0

for i in string.split():
    if len(i) > largest:

        largest = len(i)
        element = i

print(largest,element)