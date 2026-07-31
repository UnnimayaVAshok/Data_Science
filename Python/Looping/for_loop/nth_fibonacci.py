"""
0,1,1,2,3..........

each number is the sum of 2 numbers before it,starting with 1 and 1

"""

a = 0
b = 1
print(a,b,end=" ")
for i in range(10):

    result = a + b
    print(result,end=" ")
    a = b
    b = result