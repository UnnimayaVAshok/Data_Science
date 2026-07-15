numbers = [1234,999,5678,2468]

for i in numbers:
    sum_even = 0
    sum_odd = 0
    for j in str(i):

        if int(j) % 2 == 0:

            sum_even += int(j)

        else:

            sum_odd += int(j)
    print(sum_even,sum_odd)
            
