"""
1
2
3
4
5

"""
for i in range(1,6):

    print(i)

"""
12345
"""
for i in range(1,6):

    print(i,end=" ")

"""
12345
12345
12345
12345
12345
"""
for i in range(1,6):

    for j in range(1,6):

        print(j,end=" ")

    print()

"""
*****
*****
*****
"""

for i in range(3):

    for j in range(5):

        print("*",end="")
    print()

"""
11111
22222
33333
44444
55555
"""
for i in range(1,6):

    for j in range(1,6):

        print(i,end="")

    print()

"""
55555
44444
33333
22222
11111

"""

for i in range(5,0,-1):

    for j in range(5):

        print(i,end="")

    print()

print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 

"""

for i in range(1,6):

    for j in range(i):
        print(j + 1,end = " ")

    print()

print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


1 1 1 1 1
2 2 2 2
3 3 3 
4 4
5

"""

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
number = 0
for i in range(1,6):
    for j in range(i):
        number += 1
        print(number,end= " ")
    print()