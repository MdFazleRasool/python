#class
class Factory:
    a=12 # attribute

    def hello(self) : # method
        print("Method inside a factory classs")

    print(" Hello How are you ")

# print(":- Using class :- ")
# print(Factory().a)
# Factory().hello()

#Object


# print(":- Using Object of the class :- ")

# obj = Factory()
# print(obj.a)
# obj.hello()

# print(":- Using 2nd  Object of the class :- ")

# obj2 = Factory()
# print(obj2.a)
# obj2.hello()


#Constructor

class Car:

    def __init__(self,name,color):
        #print(self)
        self.name = name
        self.color = color

    def show(self) : # method
        print(f"Your Object Details are Car Brand {self.name} and its color is :- {self.color}")

obj1 = Car("BMW","Light Blue")

obj2 = Car("AUDI","Dark Blue")

# obj2.show()


# Types of Attributes and methods
class Animal:
    name = "lion" # class attribute
    def __init__(self,type):
        #print(self)
        self.type = type #instance attribute
        

    def show(self) : # instance method
        print(f"Your Object Details are Animal name  {self.name} and its type is :- {self.type}")

    @classmethod
    def classMethod(cls):
        print("Class method called")

    @staticmethod
    def staticMethod():
        print("Static method called")


obj = Animal("carnivores")

obj.show()
obj.classMethod()
obj.staticMethod()