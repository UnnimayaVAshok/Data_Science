# wap to get the missing numbers fron the sequence of numbers in the list

numbers = [1,4,2,3,6,8,9]

for i in range(min(numbers),max(numbers) + 1):

    if i not in numbers:

        print(i)