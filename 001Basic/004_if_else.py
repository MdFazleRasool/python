# a = int(input("Enter the First no :- "))
# b = int(input("Enter the second no :- "))
# if a > b : 
#     print(f"{a} is the larger than no {b}")
# else : 
#     print(b," , b is the largest no")

# c = input("Enter your gender as (M or F) ")
# if c == 'M' or 'm' :
#     print(f"Good Morning sir")
# elif c== 'F' or 'f':
#     print("Good morning mam")
# else : 
#     print(f"wrong input")


# num = int(input("Enter a number to check it odd or even "))
# if num% 2 == 0 :
#     print("even no")
# else :
#     print("Odd no")

# print("Valid voter check program")
# name = input("Enter your name ")
# age = int(input("Enter your age "))
# if(age >= 18):
#     print(f"Hello {name} you are a valid voter")
# else :
#     print(f"{name} you are not a valid voter ")


#leap year

# leap = int(input("Enter a year to check it is a leap year or not :- "))
# if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0 and leap % 100 == 0) :
#     print("Leap year")
# else : 
#     print("Not a leap year")


temp = int(input("Enter temperature in *C "))
if temp < 0 : 
    print("Freezing Cold")
elif temp >= 0 and temp < 10 : 
    print("Very Cold");
elif temp >= 10 and temp < 20 : 
    print("cold") 
elif temp >= 20 and temp < 30 : 
    print("pleasant") 
elif temp >= 30 and temp < 40 : 
    print("Hot") 
else : 
    print("Very Hot")