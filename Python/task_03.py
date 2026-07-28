# wap that takes a list of integers and perform the following steps:

# rorate the list to right by 2 positions

# last 2 eleemnets move to the front

# then replace every even number with its half and every odd number with its double

# print modified list

numbers = [1,2,3,4,5,6,7,8]
new = []

for i in range(2):

    element = numbers.pop()
    numbers.insert(0,element)

print(numbers)
"""
for i in numbers:

    if i % 2 == 0:

        new.append(i//2)

    else:

        new.append(i*2)

print(new)
"""
for index in range(len(numbers)):


    if numbers[index] % 2 == 0:
    
            numbers[index] = numbers[index]//2
    
    else:
    
       numbers[index] = numbers[index]*2

print(numbers)

