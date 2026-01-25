

a=(1,2,3,4,5)
#a[0]=10 #tuple' object does not support item assignment
print(type(a))

print(a[0])

for i in a :
    print(a)

for i in range(len(a)):
    print(a[i])

#methods of tuple

index = a.index(5)
count = a.count(5)

print(f"index of 5 is :-  {index} and count of 5 is :-  {count}")

# unpacking in tuple

nums = (1, 2, 3, 4, 5)
a, b, *rest = nums
print(a)      # 1
print(b)      # 2
print(rest)   # [3, 4, 5]