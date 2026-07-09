Expense={"Pizza": 250,
    "Burger": 120,
    "Coffee": 80,
    "Sandwich": 100,
    "Pasta": 200,
    "Momos": 60,
    "Juice": 50}

def add_expense():
    key=input("enter name of expense : ")
    value=int(input("enter the amount of expense"))
    Expense.update({key:value})

def view_expenses():
    if len(Expense)==0:
            print("No expense found")
    else:
        for key,value in Expense.items():
            print(key,":",value)
        

def calculate_total():
    a=sum((Expense.values()))
    if a==0:
        print("zero expense")
    else:
        print("Total expenses : ",a)
    

def delete_expense():
    key=input("enter name of expense to delete : ")
    a=Expense.pop(key,"NO expense found")
    if a=="NO expense found":
        print("NO expense found")
    else:
        print(key,"deleted successfully")

def search_expense():
    key=input("enter name of expense to search : ")
    print(Expense.get(key,"No expense found"))

print("welcome to expense tracker")

while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Exit")
    choice=int(input("choose from the options : "))
    match choice:
        case 1:
            add_expense()
        case 2:
            view_expenses()
        case 3:
           calculate_total()
        case 4:
            delete_expense()   
        case 5:
            search_expense()       
        case 6:
            break
        case _:
            print("Invalid option")