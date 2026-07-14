def sum_digits(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total
print(sum_digits(4567))