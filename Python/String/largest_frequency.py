# get the character having largest frequency from the string

text = "programming"
largest = 0
element = ""

for i in text:

    if largest < text.count(i):
        
        largest = text.count(i)
         # element = i

# print(element)

for i in text:

    if i not in element:

        if text.count(i) == largest:

            print(i, text.count(i))

            element += i
