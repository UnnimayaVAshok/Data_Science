# define  a function which accepts the list and return the two numbers sum which equal to the target

numbers = [3,4,5,1,2]

target = 7
result = []
def sum_two_numbers(elements):

    for i in elements:

        for j in range(i+1,len(elements) + 1):

            if i + j == target:

                result.append([i,j])

    print(result)

sum_two_numbers(numbers)
