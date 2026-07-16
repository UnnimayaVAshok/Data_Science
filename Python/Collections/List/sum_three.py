# define  a function which accepts the list and return the two numbers sum which equal to the target

numbers = [1,2,3,4,5,6,7]

target = 9

def sum_three_numbers(elements):

    for i in elements:

        for j in range(i+1, len(elements)+1):

            for k in range(j+1,len(elements)+1):

                if i + j + k == target:

                    print(i,j,k)

sum_three_numbers(numbers)