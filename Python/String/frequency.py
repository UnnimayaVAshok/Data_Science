# wap to get frequency of the string

text = "programming"

# p, 1

# r, 2

text = "programming"

new = ""

for i in text:

    if i not in new:

        print(i,text.count(i))

        new += i