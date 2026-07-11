import json
from abc import ABC,abstractmethod
from pathlib import Path

database="school_data.json"
data={"Students":[],"Teachers":[]}

if Path(database).exists():
    with open(database,"r") as f:
        content=f.read()
        if content:
            data=json.loads(content)

def save():
    with open(database,'w') as f:
        json.dump(data,f,indent=4)

class persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def Validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

class Student(persons):
    
    def get_roles(self):
        return "Students"
    
    def register(self):
        name=input("Enter Student Name : ")
        age=int(input("Enter Student Age : "))
        email=input("Enter Student/Parent Email : ")
        roll_no=input("Enter Student Roll Number : ")

        if not persons.Validate_email(email):
            print("Invalid Email")
            return
        
        for i in data['Students']:
            if i['roll_no']==roll_no:
                print("student already exists")
                return
            
        data["Students"].append({
            "name":name,
            "age":age,
            "email":email,
            "roll_no":roll_no,
            "grades":{}
        })
        save()
        print(f"Student {name} Registered")

    def show_details(self):
        roll_no=input("Enter Roll Number: ")
        for s in data['Students']:
            if s["roll_no"]==roll_no:
                grades=s['grades']
                avg=sum(grades.values())/len(grades) if grades else 0

                print(f" \nName : {s['name']}")
                print(f"Roll no : {s['roll_no']}")
                print(f"Grades : {grades}")
                print(f"Average Marks : {avg:.1f}\n")
                return



    def add_grades(self):
        roll_no=input("Enter Roll number: ")
        subject=input("Enter Subject: ")
        marks=float(input("Enter Marks: "))

        for students in data['Students']:
            if students["roll_no"]==roll_no:
                students["grades"][subject]=marks
                save()
                print("Grade Added Successfully")
                return
        print("Student Not Found")

        

class Teacher(persons):
    def get_roles(self):
        return "Teachers"
    
    def register(self):
        name=input("Enter Teacher Name : ")
        age=int(input("Enter Teacher Age : "))
        email=input("Enter Teacher Email : ")
        emp_id=input("Enter Teacher ID : ")
        subject=input("Enter Subject :")

        if not persons.Validate_email(email):
            print("Invalid Email")
            return
        for i in data['Teachers']:
            if i['emp_id']==emp_id:
                print("Employee already exists")
                return
            
        data["Teachers"].append({
            "name":name,
            "age":age,
            "email":email,
            "subject":subject,
            "emp_id":emp_id,
        })
        save()
        print(f"Teacher {name} Registered")

    def show_details(self):
        emp_id=input("Enter Employee ID: ")
        for s in data['Teachers']:
            if s["emp_id"]==emp_id:
                print(f"\nName : {s['name']}")
                print(f"Employee ID : {s['emp_id']}")
                print(f"Subject : {'subject'}\n")
                return
    

stud=Student()
teach=Teacher()

print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show a student detail")
print("press 5 to show a teacher detail")
print("Exit")

choice=int(input("please enter your choice: "))

if choice ==1:
    stud.register()
elif choice ==2:
    teach.register()
elif choice==3:
    stud.add_grades()
elif choice==4:
    stud.show_details()
elif choice==5:
    teach.show_details()