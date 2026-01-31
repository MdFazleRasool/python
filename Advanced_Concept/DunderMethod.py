class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Modifying Object address and my name is {self.name}"
    def __add__(self,other):
        return f"sum of ages are {self.age + other.age }"

obj = Animal("dog",4)
print(obj)

obj2 = Animal("cat",2)
print(obj+obj2)