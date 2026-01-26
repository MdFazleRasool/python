from pathlib import Path
import os
import sys
def readFileAndFolder():
    path = Path('.')/'File_Handling'
    items  = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"{i+1} : { items}")

def createFile():
    try:
        readFileAndFolder()
        name = input("please tell your file name ")
        folder=Path('File_Handling')
        p=folder/name
        if not p.exists():
            with open (p,"w") as fs :
                data = input("what do you want to write  in this file :- ")
                fs.write(data)
            print("file created successfully")
        else :
            print("File already Exist")
    except Exception as err:
        print(f"An Error occured as {err}")

def readFile():
    try:
        readFileAndFolder()
        name = input("Which file do u want to read :- ")
        folder=Path('File_Handling')
        p=folder/name
        if p.exists() and p.is_file() :
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"An Error occured as {err}")
        

def updateFile():
    try:
        readFileAndFolder()
        name = input("tell which  file do u want to update :- ")
        folder=Path('File_Handling')
        p=folder/name
        if p.exists() and p.is_file() :
            print("press 1 for updating the name of the file")
            print("press 2 for over-Writing the data of the file")
            print("press 3 for appending some content in  the file")

            res = int(input("Enter your Choice :- "))
            if res == 1:
                name = input("Tell me the new file name to change :- ")
                folder = Path('File_Handling')  
                p2=folder/name
                p.rename(p2)
                readFileAndFolder()  
            if res == 2:
                with open(p,'a') as fs:
                    data = input('tell me what do u want to write in the file Existing content will be overWrite :-  ')
                    fs.write(data)
                    print(data)
                print("data changed  Successfully")
            if res == 3:
                with open(p,'w') as fs:
                    data = input('tell me what do u want to Add(Append) in the file Existing content will be overWrite :- ')
                    fs.write(" "+data)
                    print(data)
                print("data changed  Successfully")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"An Error occured as {err}")
        
def deleteFile():
    try:
        readFileAndFolder()
        name = input("Tell me which file do u want to delete :-  ")
        folder = Path('File_handling')
        p=folder/name
        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("No Such File Exist")
    except Exception as err:
        print(f"Exception Occurred As {err}")


while(True):
    print(" press 1 for creating a file")
    print(" press 2 for reading a file")
    print(" press 3 for updating a file")
    print(" press 4 for deleting a file")
    print(" Press 5 to exit")

    check = int(input("Tell Your    reasponse :-  "))

    while(check):
        if check == 1:
            createFile()
        elif check == 2:
            readFile()
        elif check == 3:
            updateFile()
        elif check == 4:
            deleteFile()
        elif check == 5 :
            sys.exit()
        else :
            print("Wrong input !! try Again")