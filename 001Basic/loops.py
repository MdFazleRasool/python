#for Loop

#range(start,end,step)

# a = range(0,20,1)
# for i in a :
#     print(i)

# for i in range(0,28,2) :
#     print(i)

# for i in range(17):
#     print(i)

# for i in range(16,1,-1):
#     print(i)

# for i in range(-1,-16,-1):
#     print(i)

#table
# for i in range(5,51,5):
#     print(i)

#loop for strings

# a = "Md Fazle Rasool"
# for i in range(len(a)):
#     print(a[i])

# for char in a : 
#     print(char)

# a = range(0,20,1)
# for i in a :
#     if i == 15 :
#         continue
#     elif i == 17 :
#         break
#     print(i)
    
# a = range(0,15,1)
# for i in a :
#     if i == 15 :
#         print('break statement executed ')
#         break
#     print(i)

#else : print("break statement is not executed")


"""
✅ Rule

In Python, statements with the same indentation level belong to the same block.

Since else lines up with for, Python pairs them.

🧠 Bonus Tip

Python actually allows:

if ... else

for ... else

while ... else

try ... else

So else is not exclusive to if.

In Python, else can belong to:

if
for
while
try

and the else will only run if the break statement is not executed
"""


# a = range(0,20,1)
# for i in a :
#     if i == 15 :
#         print('break statement executed ')
#         break
#     print(i)

# else : print("break statement is not executed")


# n = int(input("Enter a no "))
# for i in range(n):
#     print("hello")
# n = int(input("Enter a no "))
# for i in range(1,n+1,1):
#     print(i)

# for i in range(n,0,-1):
#     print(i)

# n = int(input("Enter a no to print its table "))
# for i in range(n,n*10+1,n):
#     print(i)

# n = int(input("Enter a no to print its table "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("Enter a no to print its sum upto the no  "))
# sum=0
# for i in range(0,n+1,1):
#     sum+=i
#     print(sum)
# print(f"your sum is {sum}")

# n = int(input("Enter a no to print its factorial  "))
# num=1
# for i in range(1,n+1,1):
#     num*=i
# print(num)

n = int(input("Enter a no to print its sum of even no and odd no  "))
even =0 
odd =0
for i in range(0,n+1,1):
    if i % 2 == 0 :
        even+=i
    else :
        odd+=i
print(f"sum even no = {even} and sum of odd no = {odd}")



