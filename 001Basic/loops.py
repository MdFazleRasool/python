import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example
#print(isPrime(29))  # True
#print(isPrime(100)) # False


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

# n = int(input("Enter a no to print its sum of even no and odd no  "))
# even =0 
# odd =0
# for i in range(0,n+1,1):
#     if i % 2 == 0 :
#         even+=i
#     else :
#         odd+=i
# print(f"sum even no = {even} and sum of odd no = {odd}")

##factorial
# n = int(input("Enter a no to print its factorial :- "))
# for i in range(1,n+1):
#     if(n%i == 0):
#         print(i)

#perfect no  :-  sum of factors is equal to the number
# n = int(input("Enter a no to check it is a perfevt no or not :- "))
# sum=0
# for i in range(1,n):
#     if(n%i == 0):
#         sum+=i
# if sum == n :
#     print(f"{n} is a perfect no")
# else :
#     print(f"{n} is not a perfect no")


#prime no 

# n = int(input("Enter a no to check prime or not:- "))
# sum=0
# for i in range(2,n):
#     if(n%i == 0):
#         print(f"{n} is not a prime no")
#         break
# else :
#     print(f"{n} is a Prime no")

#optimised prime no 

# n = int(input("Enter a no to check prime or not:- "))
# sum=0
# for i in range(2,int(math.sqrt(n))+1):
#     if(n%i == 0):
#         print(f"{n} is not a prime no")
#         break
# else :
#     print(f"{n} is a Prime no")


#String

#reverse
a="mfrasool"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)

#Palindrome

a="racecar"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]

if(b==a):
    print("palindrome")
else:
    print("Not a palindrome")


#count
#method 1 
str = "P@#yn29at^&i0ve"
num=char=symbol=0
for i in range(len(str)):
    ascii = ord(str[i])
    if(ascii>47 and ascii <58):
        num+=1
    elif (ascii<= 90 and ascii >= 65) or (ascii<= 122 and ascii >= 97):
        char+=1
    else :
        symbol+=1
print(f"char = {char} , number = {num} , symbol = {symbol}")

num=char=symbol=0
for i in str :
    if i.isdigit():
        num+=1
    elif i.isalpha():
        char+=1
    else :
        symbol+=1
print(f"char = {char} , number = {num} , symbol = {symbol}")
