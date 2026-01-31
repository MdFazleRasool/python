
# normal function
# def addition(a,b):
#     print(a+b)

addition = lambda a,b : a+b
print(addition(12,13))


evenOrOdd = lambda a : "even" if a % 2 == 0 else "odd"

# map :-  used when you want to transform every item in a list

a=[1,2,3,4,5]
# result = map(lambda x: x*2 , a)
# print(list(result))

# def   double(x):
#     return x*2

# result = map(double,a)
# print(list(result))


# filter

def even(x):
    if x % 2 == 0 :
        return True
    else  :
        return False
    
a = [1,2,3,4,5,6,7,8]

result = filter(even, a)
print(list(result))
print(tuple(result))
print(list(result))


# filter and lambda expression
 
result = filter(lambda x: True if x % 2 == 0 else False , a)
print(list(result))