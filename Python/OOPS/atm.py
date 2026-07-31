"""
create a class ATM

describe the methods
====================

method_1 should accept the name,balance
method_2 for deposit the amount
method_3 for amount withdrawal
method_4 for display the name,current balance

"""

class ATM():

    bank_name = "sbi"        # Attribute
    location = "kochi"

    def get_details(self,name,balance):

        self.name = name
        self.balance = balance
        print(f"The user {name} has beed added successfully to {self.bank_name}")

    def deposit(self,amount):

        self.balance += amount

        print(f"{amount} deposited successfully.Available balance is {self.balance}")

    def withdrawal(self,amount):

        if amount > self.balance:

            print("Insufficient balance")

        else:

            self.balance -= amount
            print(f"withdrawal successfull.Available balance is {self.balance}")

    def display(self):

        print(f"Hi {self.name}, you have a balance of {self.balance}")

obj1 = ATM()
obj1.get_details("Arun",5000)
obj1.deposit(5000)
obj1.withdrawal(20000)
obj1.display()
print(obj1.bank_name)