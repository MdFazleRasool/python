
class Factory :
    #a="MFRasool" public 
    __a = "MFRasool"
    def show(self):
        print(f"Animal class show func {self.__a}")
obj= Factory()
obj.show()
#obj.__a
## Access Modifiers
class Car(Factory):
    # method Overriding
    def show(self):
        #print("Called in base class",super().__a) private attributes don't get inherited
        print(f"Human class show func")
    
obj = Car()
obj.show()