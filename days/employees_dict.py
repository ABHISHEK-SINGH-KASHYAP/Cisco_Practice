
employees = []

def add_employee(emp_id, name, title, salary):
    employee = {
        'id': emp_id,
        'name': name,
        'title': title,
        'salary': salary}
    employees.append(employee)
    print('Employee Added Successfully')

def search_employee(emp_id):
    for index, employee in enumerate(employees):
        if employee['id'] == emp_id:
            return index
    return -1

def update_employee(emp_id, salary):
    index = search_employee(emp_id)
    if index != -1:
        employees[index]['salary'] = salary
        print('Employee Updated Successfully')
    else:
        print('Employee Not Found')

def delete_employee(emp_id):
    index = search_employee(emp_id)
    if index != -1:
        employees.pop(index)
        print('Employee Deleted Successfully')
    else:
        print('Employee Not Found')

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
    print('Employee Not Found')

update_employee(104, 99200)
print("After Update:", employees)

add_employee(106, 'Mahesh', 'Python Trainer', 4200)
print("After Adding Mahesh:", employees)

delete_employee(106)
print("After Deleting Mahesh:", employees)