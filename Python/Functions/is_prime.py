# define a function to check the given number is prime or not

def is_prime(num_1):
    # num_1 = 7
    if num_1 > 1:

        for i in range(2,num_1):

            if num_1 % i == 0:
                print("Not prime")
                break
        else:

            print("Prime")

    else:
        print("Invalid input")

is_prime(7)