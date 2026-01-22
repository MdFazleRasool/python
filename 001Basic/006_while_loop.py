# a=int(input("Enter a number :- "))
# while a> 0:
#     print(a%10)
#     a//=10

#reverse
# rev=0
# b=int(input("Enter a number :- "))
# a=b
# while a> 0:
#     rem=(a%10)
#     rev=rev*10+rem
#     a//=10
# print(f"reversed no = {rev} and original  no = {b}")

# rev=0
# b=int(input("Enter a number :- "))
# a=b
# while a> 0:
#     rem=(a%10)
#     rev=rev*10+rem
#     a//=10
# if(rev==b):
#     print(f"{b} is a palindrome no")
# else : 
#     print(f"{b} is not a palindrome no")


import random

num = random.randint(1,100)
tries=0
while(tries<10):
    guess = int(input("Guess your number "))
    if(num == guess):
        tries+=1
        print(f"you successfully guessed the number {num} in {tries}th attempt")
        if tries> 5 :
            print("Try to be quick < 5 attempts")
        break
    elif(guess > num):
        tries+=1
        print(f"{guess}  is larger than the number try again!")
    elif(guess < num):
        tries+=1
        print(f"{guess}  is smaller than the number try again!")
    
else : 
    print("you have taken too many attempt try again !")
    