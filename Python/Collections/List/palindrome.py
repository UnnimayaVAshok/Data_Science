# wap to get armstrong and palindrome numbers in a list

numbers = [121,153,123,370,454,407,99]

armstrong = []

palindrome = []

for i in numbers:

    total = 0
    length = len(str(i))
    for j in str(i):
        total += int(j)**length

    if total == i:
         armstrong.append(i)

    else:
        temp = str(i)
        new = ""
        for j in str(i):
            new = str(i)[::-1]
        if new == temp:
            palindrome.append(i)

print(armstrong,palindrome)
