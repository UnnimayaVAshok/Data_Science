char_1 = ["a","b","c"]

char_2 = ["p","q","r","s","t","u"]

# o/p = "apbqcrs"

new = ""

for i in range(0,len(char_1)):

    new += char_1[i]
    new += char_2[i]

for i in char_2[len(char_1):]:

    new += i

print(new)
