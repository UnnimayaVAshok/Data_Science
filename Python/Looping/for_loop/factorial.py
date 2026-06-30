# wap to get the factorial of a given number n = 5, fact = 1*2*3*4*5
 
n = int(input("Enter the number: "))

fact = 1

for i in range(1,n+1):

    fact *= i

print(fact)