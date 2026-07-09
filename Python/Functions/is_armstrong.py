def is_armstrong(num):
    result = 0
    temp = num
    length = len(str(num))

    while(num > 0):

        digit = num % 10
        result += digit ** length
        num //= 10
    print("Armstrong" if temp == result else "Not armstrong")

is_armstrong(153)