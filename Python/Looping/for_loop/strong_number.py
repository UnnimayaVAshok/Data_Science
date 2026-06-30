"""
sum of factorials of digit equals to the number, eg 145

"""
number = int(input("Enter the number: "))

sum =0

for num in str(number):

    fact = 1

    for i in range(1,int(num)+1):

        fact *= i

    sum += fact

print("Strong number" if sum == number else "Not strong number")