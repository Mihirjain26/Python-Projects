import streamlit as st
from pathlib import Path


def createfile():

    try:
        name = st.text_input("Please tell your file name:")
        data = st.text_area("What do you want to write:")

        if st.button("Create File"):

            path = Path(name)

            if not path.exists():

                with open(path, "w") as fs:
                    fs.write(data)

                st.success("File created successfully")

            else:
                st.error("Error: File name already exists")


    except Exception as err:
        st.error(f"An error has occurred: {err}")



def readfile():

    try:
        name = st.text_input("Please tell your file name:")

        if st.button("Read File"):

            path = Path(name)

            if path.exists():

                with open(path, "r") as fs:
                    content = fs.read()

                st.write("Your file content is:")
                st.text(content)

            else:
                st.error("Error: No such file exists")


    except Exception as err:
        st.error(f"Error occurred: {err}")



def updatefile():

    try:
        name = st.text_input("Enter your file name to update:")

        path = Path(name)

        if name:

            if path.exists():

                st.write("Operations you can do:")

                choice = st.selectbox(
                    "Enter your choice:",
                    [
                        "Rename the file",
                        "Append content",
                        "Overwrite the file"
                    ]
                )


                if choice == "Rename the file":

                    newname = st.text_input("Enter new file name:")

                    if st.button("Rename"):

                        new_path = Path(newname)

                        if not new_path.exists():

                            path.rename(new_path)
                            st.success("Rename successful")

                        else:
                            st.error("Error: File already exists")



                elif choice == "Append content":

                    data = st.text_area("Write the updated content:")

                    if st.button("Append"):

                        with open(path, "a") as fs:
                            fs.write("\n" + data)

                        st.success("Successfully appended")



                elif choice == "Overwrite the file":

                    data = st.text_area("Write the new content:")

                    if st.button("Overwrite"):

                        with open(path, "w") as fs:
                            fs.write(data)

                        st.success("Successfully overwritten")


            else:
                st.error("Error: File does not exist")


    except Exception as err:
        st.error(f"An error has occurred: {err}")




def deletefile():

    try:

        name = st.text_input("Enter file name to delete:")

        if st.button("Delete File"):

            path = Path(name)

            if path.exists():

                path.unlink()

                st.success("File deleted successfully")


            else:
                st.error("No such file exists")


    except Exception as err:
        st.error(f"An error has occurred: {err}")




# Main UI

st.title("📁 File Management System")

st.write("Python File Handling CRUD Project")


choice = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)



if choice == "Create File":

    createfile()


elif choice == "Read File":

    readfile()


elif choice == "Update File":

    updatefile()


elif choice == "Delete File":

    deletefile()