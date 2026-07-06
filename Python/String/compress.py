# compress from aaabbc to a3b2c1

text = input("Enter the string: ")
count = 0
new = ""

for i in text:
    if i not in new:
        new += i
        new += str(text.count(i))
print(new)