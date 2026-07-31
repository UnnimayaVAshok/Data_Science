"""
# least commom multiple

lcm = (num_1 * num_2) // GCD

lcm of 4 and 5 is 20, lcm of 3 and 6 is 6,lcm of 12 and 8 is 24

multiples of 4 = 4,8,12,16,20,24...
multiples of 5 = 5,10,15,20,25..

"""

num_1 = 12
num_2 = 8
"""
for i in range(1,(num_1 * num_2) + 1):

    for j in range(1,(num_1 * num_2) + 1):

        if num_1 * i == num_2 * j:

            print(num_1 * i)

            exit()
"""
"""
for i in range(1,(num_1*num_2)+1):

    if i % num_1 == 0 and i % num_2 == 0:

        print(i)

        break
"""

for i in range(2,num_1*num_2):
    m = min(num_1,num_2) * i
    if m % max(num_1,num_2) == 0:
        print(m)
        break
