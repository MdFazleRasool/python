from abc import ABC , abstractmethod
class Animal(ABC):

    @abstractmethod
    def Sound(self):
        pass
class Dog(Animal):
    def type(self):
        print("carnivores")
    def Sound(self):
        print("Bark")

dog = Dog()

dog.type()