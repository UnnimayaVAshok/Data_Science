"""
Abstraction
=========================

It is the method of hiding the unnecessary details and showing only the essential features to the user

ABC = Abstract base class

"""

from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def method_1(self):
        pass

class B(A):

    def method_1(self):

        print("Helloworld")

obj1 = B()
print(obj1.method_1())