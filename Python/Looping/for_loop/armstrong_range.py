# check and print armstrong number in a range from 1 to 1000

for i in range(1,1001):

    length = len(str(i))

    sum = 0

    for j in str(i):

        sum += int(j) ** length

    if sum == i:

        print(i)


