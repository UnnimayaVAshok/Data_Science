"""
Polymorphism
===================

The ability of different classes to respond to the same method call in their  own unique way

same method name but different implementation(functionality)

"""

class A():

    def method_1(self,a,b):

        print(a + b)

class B():

    def method_1(self,a,b,c):

        print(a*b*c)

"""
Method overloading, python doesnt support
=======================

a programming feature where a class has multiple methods with the same name but different parameters

"""
class A():

    def method_1(self,a,b,c):

        print(a,b,c)

    def method_1(self,name,age):

        print(name,age)

"""
Method overriding
==========================

feature that lets a child class provide its own specific version of a method already defined in its parent class

"""
class A():

    def method_1(self):

        print("Hello")

class B(A):

    def method_1(self):

        print("Hello world")

obj = B()
print(obj.method_1())

"""
OOPs

class and object

Explain python is an object oriented language

Advantages(inheritance,polymorphism,abstraction,encapsulation)

method overloading,method overriding

"""