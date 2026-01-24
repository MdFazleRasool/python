def hello():
    print("Hello functionction called")

def sum(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

sum(2,3) # positional argument

def person(name,age):
    print(f"your name {name} and your age is {age}")


person(age = 22 , name = 'mfrasool') #keyword argument


def person1(name,age= 24):
    print(f"your name {name} and your age is {age}")


person1( name = 'mfrasool') #default argument persent

def palindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev+=st[i]
    if(st == rev):
        print("Palinddrome")
    else:
        print("not a palindrome")

palindrome("racecar")

def hello():
    return "Hello how are u "

hello()
print(hello())
a=hello()
print(a)