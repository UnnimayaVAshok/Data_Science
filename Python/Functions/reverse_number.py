# define a function to reverse a number enter y user

def reverse_number(num_1):
    reversed = 0
    while(num_1 > 0):
         
         digit = num_1 % 10
         reversed = reversed *10 + digit
         num_1 //= 10
    
    print(reversed)

reverse_number(123)