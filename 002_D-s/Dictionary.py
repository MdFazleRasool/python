d={}
print(type(d))

# mutable(!key) , duplicates(!key) , insetion order , heterogeneous

d = {10:100, 20:200 , 30 : 300 ,'a':400 }
print(d['a']) 
d['a']='mfrasool' #updating value
print(d['a'])
print(d)

d.update({50:500}) # creating
print(d)

d['key']='creating' # creating
print(d)

del d[50] # delete
print(d)

d = {10:100, 20:200 , 30 : 300 ,'a':400 }

#loop in dict

for i in d:
    print(f"key :- {i}  values :- {d[i]}")

#only values in dict
print('val in dict')
for i in d.values():
    print(i)

# only keys in dict
print('keys in dict')
for i in d.keys():
    print(i)

#methods

#   help(dict) # to get all the methods of dictionary

d = {10:100, 20:200 , 30 : 300 ,'a':400 }
d.clear()
print(d)
d = {10:100, 20:200 , 30 : 300 ,'a':400 }


# Shallow copy and Deep Copy    

d = {10:100, 20:200 , 30 : 300 ,'a':400 }

#deep copy
a=d
print(f"dict before deep copy {d}")
a=d
a.clear()
print(f"dict before deep copy {d} and a.clear() using deep copy obj" , {})
#shallow copy
d = {10:100, 20:200 , 30 : 300 ,'a':400 }
s=d.copy()
print(f" s :- {s} shallow copy obj ")
s.clear()
print(f"s {s} and no chnages in d after s.clear() d {d}")
print(f"{d} dict after shallow copy")



d = {10:100, 20:200 , 30 : 300 ,'a':400 }

## methods in dictionary

#get

print(d.get(20))

# items 

print(d.items())


## Dictionary Questions


# Write a Python script to merge two Python dictionaries?
# Write a Python program to sum all the values in a dictionary?
# Count the frequency of each element in a list and print the answer?
# Write a Python program to combine two dictionary by adding values for common keys.


# Write a Python program to sum all the values in a dictionary?

d = {'a':100, 'b':200 , 'c' : 300 ,'d':400 }
sum=0
for i in d.values():
    sum+=i
else:
    print(f"sum of all values of dict :- {sum}")


# Write a Python script to merge two Python dictionaries?

dict1 = {'a':100, 'b':200 , 'c' : 300 ,'d':400 }
dict2 = {'e':600, 'f':700 , 'g' : 800 ,'d':500 }

for i in dict2 :
    dict1[i] = dict2[i] # if exist then update in d1 else create in d1
print(dict1)

# Count the frequency of each element in a list and print the answer?

list = [1,1,1,1,2,2,2,1,3,4,4,4,4,4,5,5]
d={}
for i in list :
    if i in d.keys():
        d[i]+=1
    else :
        d[i]=1
print(d)

# Write a Python program to combine two dictionary by adding values for common keys.

dict1 = {'a':100, 'b':200 , 'c' : 300 ,'d':400 , 'e':600 }
dict2 = {'e':600, 'f':700 , 'g' : 800 ,'d':500 }

for i in dict1:
    if i in dict2.keys():
        dict2[i]+=dict1[i]
    else :
        dict2