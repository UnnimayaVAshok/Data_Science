numbers = [123,999,456,87]
maximum = 0
for i in numbers:
    total = 0
    
    for j in str(i):

        total += int(j)

    if total > maximum:

        maximum = total

        number = i

print(number)

        