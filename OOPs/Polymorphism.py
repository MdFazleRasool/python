# method Overriding
class Animal :
    def show(self):
        print(f"Animal class show func")
class Human(Animal):
    # method Overriding
    def show(self):
        print(f"Human class show func")


human = Human()
human.show()


#Duck Typing
class Animal :
    def show(self):
        print(f"Animal class show func")
class Human:
    def show(self):
        print(f"Human class show func")

obj1=Animal()
obj2 = Human()

obj1.show()
obj2.show()