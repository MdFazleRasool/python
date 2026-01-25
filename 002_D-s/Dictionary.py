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