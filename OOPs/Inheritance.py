
class Factory : #parent class / superClass
    a = 'I am a attribute mentioned inside Factory class'
    def hello(self):
        print("Method mentioned inside a factory class")

class Branch(Factory): # child Class / subclass
    pass

# fac = Factory()
# fac.hello()
# print(fac.a)



# branch = Branch()
# branch.hello()
# print(branch.a)



# constructor in inheritance

class Animal :
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")

class Human(Animal):
    pass


# animal = Animal("Lion")
# animal.show()

# human = Human("MF")
# human.show()

# Super keyword
# constructor in inheritance

class Animal :
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")

# single Inheritance
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"Hello your name is {self.name}  , age is {self.age}")


animal = Animal("Lion")
animal.show()

human = Human("MF",22)
human.show()


#Multiple Inheritance
class Animal:
    def __init__(self,name):
        pass
    name1 = "lion"

class Human :
    def __init__(self,name,age):
        pass
    name2 = " mf"

class Robots(Animal,Human):
    name3 = 'chitti'

obj = Robots("faz") # the constructor func will be inherited of the 1st class that has been inherited


#MultiLevel Inheritance
class Factory :
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class Bhopal(Factory) :
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color = color

class PuneFactory(Factory) :
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color)
        self.pockets=pockets


obj = PuneFactory()

#Hierarchical Inheritance