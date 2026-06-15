from pathlib import Path
import os
def readfilefolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")



def createfile():
    try:
        readfilefolder()
        name = input("Please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file :- ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY ")
    except Exception as err:
        print(f"An error occured as {err}")
def readfile():
    try:
        readfilefolder()
        name = input("which file you want to read ")
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed sucessfully")
        else:
            print("the file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatingfile():
    try:
        readfilefolder()
        name = input("tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the your file :- ")
            print("press 2 for overwriting the data of your file :- ")
            print("press 3 for appending some content in your file :- ")
            res = int(input("tell your response"))

            if res == 1:
                name2 = input("tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p,'w') as fs:
                    data = input("tell what yo want to write this is overwrite")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input("tell what yo want to write this is overwrite")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error occured as {err}")
def deletefile():
    readfilefolder()
    name = input("which file you want to delete :- ")
    p = Path(name)

    if p.exists() and p.is_file():
        os.remove(p)

        print("file remove sucessfully ")
    else:
        print("no such file exist")

print("press 1 for the Creating  a file")
print("press 2 for the Reading  a file")
print("press 3 for the Updating  a file")
print("press 4 for the Deletion a file")

check =  int(input("please tell your response :- "))


if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatingfile()

if check == 4:
    deletefile()