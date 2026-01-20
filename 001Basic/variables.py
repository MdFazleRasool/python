"""

You can not use numbers at variable start
You can not use spaces in variables.
 You should not use special characters in variables.
"""

#Naming Conventions

examDate = '12-09-25' # camel case
ExamDate = '12-09-25'  # Pascal case
exam_date = '12-09-25'  # snake case

#DataTypes

#int
a=-34

#float
b=56.4
c=12/4 # why this always be false
print(type (a))
print(type (b))
print(type (c))

#complex
complex_data_type = 30j # to make a variable of complex data type add j
print(type (complex_data_type))

#String
s='abc' # signle quote declaration
t="abc" # double quote declaration
print(s+" " + t)


#boolean
b=True
print(type(b))
t = False
print(type(t))

print(ord('a')) # ord() ->   char -> unicode
print(chr(97))  # ch() -> unicode -> char 


#String 
"""
Indexing in String starts from 

# left to right =  0 -> (length-1)

# right to left  =  -1 -> -(length)
"""
s="MFRasool"
print("positive indexing"+s[0])
print("negative indexing"+s[-8])

#String Slicing
print(s[1::1]) #[start,end,step] #end takes n -> n-1


#Types Conversion

# int-> String

a=12;
a=str(a);
print(type(a))

# String-> int

b='12';
b=int(b);

print(type(b))

#boolean 

# falsy values and truthy values


# 1 .) Formatted_String And 2.) Raw_String

print()


# Input Function
# s = int(input("hello what is your age "))
# print(s)


## Arithematic operator
print("Arithematic Operators ")

a=5
b=32
print("Addition :- ",a+b)
print("Subtraction :- ",a-b)
print("Multiplication :- ",a*b)
print("Division :- ",b/a)
print("floor :- ",b//a)
print("Modulus :- ",b%a)


#Assignment Operators
print("Assignment Operators ")

a=20 

a=a+20

#compound Assignment Operations

a+=20
print(a)
a+=20
print(a)
a*=20
print(a)
a/=20
print(a)
a//=20
print(a)
a**=20
print(a)


#comparison opeartors 

print("comparison opeartors :--   "," > , < , <= ,>=  , == , != ")

a=12
b=12

print(a==b)
print(a!=b)

#when we compare string it compares ascii value

print(ord("a"))
print(ord("A"))

print('A" > "a" :- ',"A" > "a")
print('ABDC" > "ABCD" :- ',"ABDC" > "ABCD") # comparing each char one by on e



#Logical Operators
print("Logical opeartors :--   "," and , or , not ")

print(123 > 100 and 34 == 34)
print(123 < 100 or 34 == 34)
print(not 34 == 34)

print((456==456)!= (235 == 236))
print(True and bool(0))