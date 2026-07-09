# twin prime
last = 0
for i in range(1,100):

    for j in range(2,i):

        if i % j == 0:

            break
    else:

        if i - last == 2:

            print(last,i)

        last = i