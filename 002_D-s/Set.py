
#Traversing

a={1,2,3,4,5,0,"Hello"}
print(a)

for i in a:
    print(i)


#methods
print()
a.add(7) # adds the ele in the set

a.remove(2) # removes the ele from the set 

a.discard(2) # removes 2 (no error )

popped_element = a.pop() #Removes a random element
print(popped_element)
a.clear() # Removes all elements

print(a)

# Actions between 2 sets

A = {1,2,3}
B = {3,4,5}

#method 1 
union_set = (A | B)
intersection_Set=(A & B)
differnce_set= (A-B)
symmetric_diff = (A^B)

print(f"{union_set} , {intersection_Set} , {differnce_set} , {symmetric_diff}")



#method 2

A = {1,2,3,4}
B = {3,4,5,6}

union_set = A.union(B)
intersection_Set=A.intersection(B)
differnce_set= A.difference(B)
symmetric_diff = A.symmetric_difference(B)

print(f"{union_set} , {intersection_Set} , {differnce_set} , {symmetric_diff}")

