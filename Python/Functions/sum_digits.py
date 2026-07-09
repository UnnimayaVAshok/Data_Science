# define a function to return the sum of digits of the number entered

def sum_digits(num):

    sum_digit = 0

    for i in str(num):

        sum_digit += int(i)

    print(sum_digit)

sum_digits(12345)
