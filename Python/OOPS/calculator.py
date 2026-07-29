# create a class Calculator and add methods of
# return sum of two numbers
# return the product of two numbers

class Calculator():

    def addition(self,num_1,num_2):

        return num_1 + num_2

    def product(self,num_1,num_2):

        return num_1*num_2

obj1 = Calculator()

print(obj1.addition(3,4))
print(obj1.product(2,3))