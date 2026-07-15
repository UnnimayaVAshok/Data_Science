numbers = [2,22,3,4,6,5,7,9,8]

for i in numbers.copy():

    if i % 2 == 0:

        numbers.remove(i)

print(numbers)