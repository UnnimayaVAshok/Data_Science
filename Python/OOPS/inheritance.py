"""
Inheritance
===========================

It is the technique or advantage that a child class / derived class
aquires the properties (methods) of another class (Parent class / base class)
which enables code reusability and relationships

Types of inheritance
================================

single level inheritance
multiple inheritance
multilevel inheritance
hybrid inheritance


"""


class Parent(object):

    def car(self):

        print("Maruti 800")

    def bike(self):

        print("Royal enfield")

class Child(Parent): # inheriting the parent class

    pass

obj1 = Child()
obj1.car()
obj1.bike() # calling method from parent calss due to inheritance