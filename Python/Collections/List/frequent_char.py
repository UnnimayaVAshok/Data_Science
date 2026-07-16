words = ["apple","banana","grapes"]
frequent_chars = []
for i in words:
    count = 0
    for j in i:

        if i.count(j) > count:

            count = i.count(j)
            char = j
    if count > 1:

        frequent_chars.append(char)
        
print(frequent_chars)