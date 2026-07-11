import streamlit as st
import json
from pathlib import Path

DATABASE = "school_data.json"


# ---------------------- Load Data ---------------------- #
def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            content = f.read()
            if content:
                return json.loads(content)

    return {"Students": [], "Teachers": []}


# ---------------------- Save Data ---------------------- #
def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


data = load_data()

st.set_page_config(
    page_title="School Management System",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 School Management System")

menu = st.sidebar.radio(
    "Menu",
    [
        "Register Student",
        "Register Teacher",
        "Add Grades",
        "Show Student",
        "Show Teacher",
    ],
)

# ==========================================================
# Register Student
# ==========================================================

if menu == "Register Student":

    st.header("Register Student")

    name = st.text_input("Student Name")
    age = st.number_input("Age", 1, 100)
    email = st.text_input("Email")
    roll = st.text_input("Roll Number")

    if st.button("Register Student"):

        if "@" not in email or "." not in email:
            st.error("Invalid Email")

        else:

            exists = False

            for student in data["Students"]:
                if student["roll_no"] == roll:
                    exists = True
                    break

            if exists:
                st.warning("Student already exists")

            else:

                data["Students"].append(
                    {
                        "name": name,
                        "age": age,
                        "email": email,
                        "roll_no": roll,
                        "grades": {},
                    }
                )

                save_data(data)

                st.success("Student Registered Successfully")

# ==========================================================
# Register Teacher
# ==========================================================

elif menu == "Register Teacher":

    st.header("Register Teacher")

    name = st.text_input("Teacher Name")
    age = st.number_input("Age", 20, 100)
    email = st.text_input("Email")
    emp = st.text_input("Employee ID")
    subject = st.text_input("Subject")

    if st.button("Register Teacher"):

        if "@" not in email or "." not in email:
            st.error("Invalid Email")

        else:

            exists = False

            for teacher in data["Teachers"]:
                if teacher["emp_id"] == emp:
                    exists = True
                    break

            if exists:
                st.warning("Teacher already exists")

            else:

                data["Teachers"].append(
                    {
                        "name": name,
                        "age": age,
                        "email": email,
                        "subject": subject,
                        "emp_id": emp,
                    }
                )

                save_data(data)

                st.success("Teacher Registered Successfully")

# ==========================================================
# Add Grades
# ==========================================================

elif menu == "Add Grades":

    st.header("Add Grades")

    roll = st.text_input("Roll Number")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", 0.0, 100.0)

    if st.button("Add Grade"):

        found = False

        for student in data["Students"]:

            if student["roll_no"] == roll:

                student["grades"][subject] = marks

                save_data(data)

                found = True

                break

        if found:
            st.success("Grade Added Successfully")

        else:
            st.error("Student Not Found")

# ==========================================================
# Show Student
# ==========================================================

elif menu == "Show Student":

    st.header("Student Details")

    roll = st.text_input("Roll Number")

    if st.button("Search Student"):

        found = False

        for student in data["Students"]:

            if student["roll_no"] == roll:

                found = True

                grades = student["grades"]

                average = (
                    sum(grades.values()) / len(grades)
                    if grades
                    else 0
                )

                st.subheader(student["name"])

                st.write("**Roll Number:**", student["roll_no"])
                st.write("**Email:**", student["email"])
                st.write("**Age:**", student["age"])

                st.write("### Grades")

                if grades:

                    st.table(
                        {
                            "Subject": list(grades.keys()),
                            "Marks": list(grades.values()),
                        }
                    )

                else:
                    st.info("No grades available.")

                st.metric("Average Marks", f"{average:.2f}")

        if not found:
            st.error("Student Not Found")

# ==========================================================
# Show Teacher
# ==========================================================

elif menu == "Show Teacher":

    st.header("Teacher Details")

    emp = st.text_input("Employee ID")

    if st.button("Search Teacher"):

        found = False

        for teacher in data["Teachers"]:

            if teacher["emp_id"] == emp:

                found = True

                st.subheader(teacher["name"])

                st.write("**Employee ID:**", teacher["emp_id"])
                st.write("**Email:**", teacher["email"])
                st.write("**Age:**", teacher["age"])
                st.write("**Subject:**", teacher["subject"])

        if not found:
            st.error("Teacher Not Found")
