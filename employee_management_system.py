import os

def clear():
    os.system("clear")

employee_info = []

def add_employee():
    try:
        name = input("Enter Employee Name Here: ").lower()
        age = input("Enter Employee Age Here: ")
        job = input("Enter Employee Job Type Here: ").lower()
        email = input("Enter Employee Email Here: ").lower()

        employee = {'name': name, 'age': age, 'job': job, 'email': email}

        employee_info.append(employee)
        clear()
        print(f"Employee {name} Details Added Successfully")
    except Exception as e:
        print(f"Error: {e}")
        print("Invalid input. Please try again.")

def display_details():
    try:
        print("___Employee Details Records___")
        if not employee_info:
            clear()
            print("\nEmployee detail records are empty.\n")
        else:
            for i in employee_info:
                clear()
                print(f"\nName: {i['name']}\n Age: {i['age']}\n Job: {i['job']}\n Email: {i['email']}")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while displaying employee details.")

def search_employee():
    try:
        search_name = input("Enter Name For Searching Employee Details: ")
        found = False
        for i in employee_info:
            if i['name'].lower() == search_name.lower():
                clear()
                print("Details Fetched Successfully\n")
                print(f"\nName: {i['name']}\n Age: {i['age']}\n Job: {i['job']}\n Email: {i['email']}")
                found = True
                break

        if not found:
            print("Invalid Name or No Employee Found!")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while searching for employee details.")

def delete_employee():
    try:
        search_delete = input("Enter Employee Name For Deletion: ")
        for i in employee_info:
            if i['name'].lower() == search_delete.lower():
                employee_info.remove(i)
                clear()
                print("Employee Details Deleted Successfully")
                break
        else:
            print("Invalid Name or No Employee Found For Deletion")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while deleting employee details.")

def main():
    clear()
    while True:
        print("\n_Employee Management System_\n")
        print("Enter 1 to Add Employee Details")
        print("Enter 2 to Display Employees Detail Records")
        print("Enter 3 to Search Employee")
        print("Enter 4 to Delete Employee Details")
        print("Enter 5 to Exit")

        try:
            user_selection = int(input("Enter Your Selection Here: "))

            if user_selection == 1:
                add_employee()

            elif user_selection == 2:
                display_details()

            elif user_selection == 3:
                search_employee()

            elif user_selection == 4:
                delete_employee()

            elif user_selection == 5:
                clear()
                print("Thank You For Using The Employee Management System!")
                break

            else:
                print("Invalid Selection!")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
