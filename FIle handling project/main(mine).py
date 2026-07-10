from pathlib import Path


def createfile():
    try:
        name=input("please tell your file name:-")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("what you wanna write :- ")
                fs.write(data)
            print("file created successfully")
        else:
            print("Error: File name already exists")
    except Exception as err:
        print(f"an error has occured as{err}")

def readfile():
    try:
        name=input("please tell your file name :- ")
        path=Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content=fs.read()
                print(f"Your file content is\n{content}")
        else:
            print("Error: no such file exists")
    except Exception as err:
        print(f"error occured as {err}")

def updatefile():
    try:
        name=input("enter your file name to update:- ")
        path=Path(name)
        if path.exists():
            print("operation you can do")
            print("1. Renaming the file")
            print("2. Appending the content")
            print("3. Overwriting the file")
            choice=int(input("enter your choice:- "))
            if choice==1:
                newname=input("tell the new file name")
                new_path=Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("rename successful")
                else:
                    print("error:file already exists")


            elif choice==2:
                with open(path,"a") as fs:
                    data=input(" write the updated things here:-")
                    fs.write("\n"+data)
                    print("successfully appended")
            
            elif choice==3:
                with open(path,"w") as fs:
                    data=input(" write the new thing here:-")
                    fs.write("\n"+data)
                    print("successfully overwritten")
    except Exception as err:
        print(f"an error has occured as {err}")

def deletefile():
    try:
        name=input("enter file nameto delete :- ")
        path=Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an error has occured as {err}")        


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")


choice=int(input("\ntell your response :-"))

if choice==1:
    createfile()
if choice==2:
    readfile()
if choice==3:
    updatefile()
if choice==4:
    deletefile()