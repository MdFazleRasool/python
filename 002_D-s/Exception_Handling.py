
a= int(input("Enter a number to divide a number :-  "))
#print(10/a) # this line may cause an error(E_H) if a -> 0

#Wxception Handling

try:
    print(10/a)
except Exception as err:
    print(f"Sorry you cannot divide by zero {err} error")
else:
    print("No exception Occurred")
finally:
    print("I will run in every case")

print("ok i have done a 10/a division")



age = int(input("Tell your age to enter in my club :-  "))

try:
    if age < 14 or age > 21 :
        raise ValueError("Your age must be between 14 and 21")
    else :
        print("Welcome to My Club")

except Exception as err :
    print(f" An error occured  {err}")

print("The Club will Start soon !! Stay Tuned !!")