from pathlib import Path


def createfile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)

        if not path.exists():
            data = input("What do you want to write: ")

            with open(path, "w") as fs:
                fs.write(data)

            print("File created successfully")

        else:
            print("Error: File name already exists")

    except Exception as err:
        print(f"An error has occurred: {err}")



def readfile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)

        if path.exists():

            with open(path, "r") as fs:
                content = fs.read()

            print(f"Your file content is:\n{content}")

        else:
            print("Error: No such file exists")

    except Exception as err:
        print(f"Error occurred: {err}")



def updatefile():
    try:
        name = input("Enter your file name to update: ")
        path = Path(name)

        if path.exists():

            print("\nOperations you can do:")
            print("1. Rename the file")
            print("2. Append content")
            print("3. Overwrite the file")

            choice = int(input("Enter your choice: "))


            if choice == 1:
                newname = input("Enter new file name: ")
                new_path = Path(newname)

                if not new_path.exists():
                    path.rename(new_path)
                    print("Rename successful")

                else:
                    print("Error: File already exists")


            elif choice == 2:
                data = input("Write the updated content: ")

                with open(path, "a") as fs:
                    fs.write("\n" + data)

                print("Successfully appended")


            elif choice == 3:
                data = input("Write the new content: ")

                with open(path, "w") as fs:
                    fs.write(data)

                print("Successfully overwritten")


            else:
                print("Invalid choice")

        else:
            print("Error: File does not exist")


    except Exception as err:
        print(f"An error has occurred: {err}")



def deletefile():
    try:
        name = input("Enter file name to delete: ")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("File deleted successfully")

        else:
            print("No such file exists")


    except Exception as err:
        print(f"An error has occurred: {err}")




print("\n===== File Management System =====")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


try:
    choice = int(input("\nTell your response: "))


    if choice == 1:
        createfile()

    elif choice == 2:
        readfile()

    elif choice == 3:
        updatefile()

    elif choice == 4:
        deletefile()

    else:
        print("Invalid choice")


except Exception as err:
    print(f"Invalid input: {err}")