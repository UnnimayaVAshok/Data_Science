#9) wap to print sum of even and odd indexed digits in a given number**

number = int(input("Enter the number: "))
even_sum = 0
odd_sum = 0
for i in range(len(str(number))):
    if i % 2 != 0:
        even_sum += int(str(number)[i])
    else:
        odd_sum += int(str(number)[i])

print(even_sum,odd_sum)