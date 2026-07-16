# i > largest > second largest

# largest > i >second largest

# secondlargst > i > largset 

numbers = [1,8,5,6,2,9]

largest = numbers[0]
sec_largest = numbers[1]

if numbers[0] < numbers[1]:

    largest = numbers[1]

    sec_largest = numbers[0]

else:
    largest = numbers[0]

    sec_largest = numbers[1]

for i in numbers:

    if i > largest and i > sec_largest:

        sec_largest = largest
        largest = i

    elif i > sec_largest and i < largest:

        sec_largest = i

print(largest,sec_largest)
