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