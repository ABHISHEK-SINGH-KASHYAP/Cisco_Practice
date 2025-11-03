# employees.py - Object-Oriented version

class Employee:
    def __init__(self, emp_id, name, title, salary):
        self.id = emp_id
        self.name = name
        self.title = title
        self.salary = salary

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', title='{self.title}', salary={self.salary})"


# List to store Employee objects
employees = []

def add_employee(emp_id, name, title, salary):
    employee = Employee(emp_id, name, title, salary)
    employees.append(employee)
    print('Employee Added Successfully')

def search_employee(emp_id):
    for index, employee in enumerate(employees):
        if employee.id == emp_id:
            return index
    return -1

def update_employee(emp_id, salary):
    index = search_employee(emp_id)
    if index != -1:
        employees[index].salary = salary
        print('Employee Updated Successfully')
    else:
        print('Employee Not Found.')

def delete_employee(emp_id):
    index = search_employee(emp_id)
    if index != -1:
        employees.pop(index)
        print('Employee Deleted Successfully')
    else:
        print('Employee Not Found.')


# Test the functions
add_employee(101, 'Pratik', 'Software Engineer', 56000)
add_employee(102, 'Abhishek', 'Software Automation Engineer', 40000)
add_employee(103, 'Rishabh', 'Software Automation Engineer', 99000)
add_employee(104, 'Nihar', 'Software Automation Engineer', 99)
add_employee(105, 'Divya', 'Business Analyst', 45000)

print("\nAll Employees:", employees)

emp_index = search_employee(104)
if emp_index != -1:
    print('Searched Employee:', employees[emp_index])
else:
    print('Employee Not Found.')

update_employee(104, 99200)
print("\nAfter Update:", employees)

add_employee(106, 'Mahesh', 'Python Trainer', 4200)
print("\nAfter Adding Mahesh:", employees)

delete_employee(106)
print("\nAfter Deleting Mahesh:", employees)