 # CRUD operation which we can appy on a file


# r=open("create.txt",'w') # creates file or overwrite it 
r=open("create.txt",'a') # append - add to the end of the file 
r.write("Hello this is akarsh and I am writing inside  this file")
r.write("   and i am appending on the file ")
r.close()


with open("Readme.md","r") as f :
    content = f.read()
    print(content)