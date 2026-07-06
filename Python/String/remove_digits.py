text = input("Enter the string: ")
new = "" 

for i in text:
    if i.isalpha() == True:
        new += i

print(new)