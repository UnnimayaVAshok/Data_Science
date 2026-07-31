# GCD

"""
factors of 28 = 1,2,4,7,14,28
factors of 20 = 1,2,4,5,10,20
largest factor = 4

"""
num_1 = 20
num_2 = 28

for i in range(1,min(num_1,num_2)):

    if num_1 % i == 0 and num_2 % i == 0:

        gcd = i

print(gcd)