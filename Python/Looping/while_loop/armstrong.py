num = 152

temp = num

length = len(str(num))

sum =0

while(num > 0):

    digit = num % 10

    sum += digit ** length

    num //= 10

print("Armstrong" if temp == sum else "Not armstrong")


