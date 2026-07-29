# craete a class Character and menthods

# method1 accepts a string and return each character with its count

# methods accepts the string and return the string with unique characetrs(remove duplicate)

class Character():

    def frequency(self,text):
        self.text = text
        print({i:text.count(i) for i in text})

    def unique(self):

        print(set(self.text))

obj1 = Character()
obj1.frequency("Hello")
obj1.unique()