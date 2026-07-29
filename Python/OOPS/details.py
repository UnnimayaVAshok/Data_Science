# create  a class Details which should have methods

# method_1 accept name and age and return registered successfully

# method_2 should print the name and details

class Details():

    def register(self,name:str,age:int):

        self.name = name
        self.age = age
        return "Registered successfully"

    def display(self):

        return self.name,self.age

obj1 = Details()
print(obj1.register("Arun",22))
print(obj1.display())
    