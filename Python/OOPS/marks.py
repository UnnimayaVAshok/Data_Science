"""
define a class Mark analyzer
method_1 accept the name and mark of 5 subjects
method_2 calculate the average
method_3 return the student name and average

"""
"""
The __init__() method is technically an object initializer, it functions as the constructor 
which is automatically invoked during object initialization

"""
class Mark_analyzer():

    def __init__(self,name,marks:list):
        self.name = name
        self.marks = marks
        print(f"Hi {name}")

    def average(self):

        average = sum(self.marks) / len(self.marks)
        self.average = average

    def display(self):

        print(self.name,self.average)

user_1 = Mark_analyzer("Arun",[20,40,50,60,70])

user_1.average()
user_1.display()
    