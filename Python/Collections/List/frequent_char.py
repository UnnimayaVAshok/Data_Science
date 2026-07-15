words = ["apple","banana","grapes"]

for i in words:
    count = 0
    for j in i:

        if i.count(j) > count:

            count = i.count(j)
            char = j
    print(char,count)