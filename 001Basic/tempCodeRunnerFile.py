n = int(input("Enter a no to check it is a perfevt no or not :- "))
sum=0
for i in range(1,n):
    if(n%i == 0):
        sum+=i
if sum == n :
    print(f"{n} is a perfect no")
else :
    print(f"{n} is not a perfect no")