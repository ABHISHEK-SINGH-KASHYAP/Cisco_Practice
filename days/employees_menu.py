class Employee:
    def __init__(self, emp_id, name, title, salary):
        self.id = emp_id
        self.name = name
        self.title = title
        self.salary = salary

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', title='{self.title}', salary={self.salary})"

employees = []

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    title = input("Enter Job Title: ")
    salary = float(input("Enter Salary: "))
    employee = Employee(emp_id, name, title, salary)
    employees.append(employee)
    print("Employee Added Successfully")

def search_employee(emp_id):
    for index, employee in enumerate(employees):
        if employee.id == emp_id:
            return index
    return -1

def update_employee():
    emp_id = int(input("Enter Employee ID to Update: "))
    index = search_employee(emp_id)
    if index != -1:
        new_salary = float(input("Enter New Salary: "))
        employees[index].salary = new_salary
        print("Employee Updated Successfully")
    else:
        print("Employee Not Found.")

def delete_employee():
    emp_id = int(input("Enter Employee ID to Delete: "))
    index = search_employee(emp_id)
    if index != -1:
        employees.pop(index)
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found.")

def display_employees():
    if employees:
        print("All Employees:")
        for emp in employees:
            print(emp)
    else:
        print("No employees found.")


while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Display All Employees")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        emp_id = int(input("Enter Employee ID to Search: "))
        index = search_employee(emp_id)
        if index != -1:
            print("Employee Found:", employees[index])
        else:
            print("Employee Not Found.")
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        display_employees()
    elif choice == '6':
        print("Exit successfully")
        break
    else:
        print("Invalid choice.")