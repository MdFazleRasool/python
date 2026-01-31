class Dog:
    def type(self):
        print("carnivores")
    @property #decorator
    def Sound(self):
        print("Bark")

dog = Dog()
dog.type()
dog.Sound


# def decorate(func):
#     def wrapper():
#         print("I am decorator")
#         func()
#         print("I will print after the func")
#     return wrapper



#@decorate
# def hello():
#     print("Hello I am Fazal")

# hello()


def decorate(func):
    def wrapper(a,b):
        print("The Addition of the no is ")
        func(a,b)
        print("Thank for your Efforts !!")
    return wrapper



@decorate
def addition(a,b):
    print(f"{a+b}")

addition(12,5)


# *args and **kwargs

def sum(*args ):
    print(args)
    add=0
    for i in args:
        add += i
    print(add)
sum(10,1,2,3,4,5)

def func(**kwargs):
    #print(kwargs) 
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

func(name = "faz" , age = 23 ,  designation = "AI / ML")