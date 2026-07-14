def factors(number):
    for i in range(1,number + 1):
        if number % int(i) == 0:
            print(i,end = " ")
factors(24)