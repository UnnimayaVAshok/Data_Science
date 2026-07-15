# wap to get armstrong numbers in a list

numbers = [153,123,370,456,407,500]

for i in numbers:

    total = 0
    length = len(str(i))
    for j in str(i):
        total += int(j)**length

    if total == i:
         print(i)