#[]

list = [1,2,3,4,5]

#mutable
list[0]=12

#heterogeneous

list[4]="mf"
# print(list)

# print(list[0:5])

#traversing

# for i in range(len(list)):
#     print(list[i])

# for i in list :
#     print(i)

l = [-1,2,3,-5,1,-2,4,-3,8,20,22,25]

# list methods

numbers = [5,3,2,5,6,7,9,4]

numbers.append(10) # Adds 10 to the end

numbers.insert(2,15) # Inset 15 at index 2

numbers.extend([20,25,30]) # Adds multiple elements at the end

numbers.remove(5) # removes 1st occurance of 5

popped_item = numbers.pop(2) # Removes and stores the element at index

index = numbers.index(6) # finds index of 6
# print(index)
# print(numbers)

count_5 = numbers.count(5) # count all the occurances of 5
print(count_5)

numbers.sort() # sort the list in ascending order

numbers.reverse() # Reverse the list order

new_numbers = numbers.copy() # creates the copy of the list
print(new_numbers)
new_numbers.clear()

print(new_numbers)










#Some Questions on List

# Print positive and negative elements of an List?
#  Mean of List elements?
#  Find the greatest element and print its index too?
#  Find the second greatest element?
#  Check if List is sorted or not.



# Print positive and negative elements of an List?
print("Positive elements in the list :- ", end='\t')
for i in l:
    if i >=0:
        print(f"{i}" , end="\t")

print("\n negative elements in the list :-  ", end='\t')
for i in l:
    if i <0:
        print(f"{i}" , end='\t')


# Mean of List elements?
sum=0
for i in l:
    sum+=i
print(f"mean = ",sum/(len(l)))


# Find the greatest element and print its index too?
idx=0
lar=l[0]
for i in range(len(l)):
    if lar < l[i] :
        idx=i
        lar=l[i]
print(f"largest ele :- {lar} and its index :- {idx}") 


# Find the second greatest element?


print(l)
idx=0
lar=l[0]
for i in range(len(l)):
    if lar < i :
        idx=i
        lar=l[i]
l.pop(idx)
idx=0
lar=l[0]
print(l)
for i in range(len(l)):
    if lar < i :
        idx=i
        lar=l[i]
print(f"2nd largest ele :- {lar} and its index :- {idx}") 


##2nd largest method2



# Check if List is sorted or not.
if sorted(l) == l:
    print("Sorted  list")
else :
    print("unsorted list")


print(l)




