import db_json as db
from log import logging #shortcut for logging module setup

employees = db.read_employees()

def add_employee(employee):
    try:
        employees.append(employee)
        logging.debug(f'Employees added to list: {employees}')
        db.write_employees(employees)
        logging.debug('Employees written to DB file')
        logging.info('Employee Added Successfully')

    except Exception as e:
        logging.exception(f'Error adding employee: {e}')

def search_employee(id): 
    I = 0
    for employee in employees: 
        if employee.id == id:
            logging.info('Employee Found Successfully')
            return I
        I += 1
        logging.info('Employee Not Found.')
    return -1 
 
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        employee.salary = salary
        db.write_employees(employees)
        logging.info('Employee Updated Successfully')
    else: 
        logging.info('Employee Not Found.')

def delete_employee(id):
    index = search_employee(id) 
    if index != -1:
        employees.pop(index)
        db.write_employees(employees)
        logging.info('Employee Deleted Successfully')
    else: 
        logging.info('Employee Not Found.')



'''
import db_emp as db #ensure db_emp.py is in same folder.

employees = db.read_employees()  #employee is object of attr (id, name, job_title, salary)
# list of objects -> save to file
# read from file -> list of objs

def add_employee(employee):
    employees.append(employee)
    db.write_employees(employees)
    logging.info('Employee Added Successfully')

def search_employee(id): 
    I = 0
    for employee in employees: 
        if employee.id == id:
            return I
        I += 1
    return -1 
 
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        employee.salary = salary
        db.write_employees(employees)
        logging.info('Employee Updated Successfully')        
    else: 
        logging.info('Employee Not Found.')

def delete_employee(id):
    index = search_employee(id) 
    if index != -1:
        employees.pop(index)
        db.write_employees(employees)
        logging.info('Employee Deleted Successfully')
    else: 
        logging.info('Employee Not Found.')

'''

#this was old repo
'''
employees = [] #employee is object of attr(id, name, job_title, salary)

def add_employee(employee):
    employees.append(employee)
    logging.info('Employee Added Successfully')

def search_employee(id): 
    I = 0
    for employee in employees: 
        if employee.id == id:
            return I
        I += 1
    return -1 
 
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        employee.salary = salary
        #new_employee = (employee[0], employee[1], employee[2], salary)
        #employees[index] = new_employee
        logging.info('Employee Updated Successfully')
    else: 
        logging.info('Employee Not Found.')

def delete_employee(id):
    index = search_employee(id) 
    if index != -1:
        employees.pop(index)
        logging.info('Employee Deleted Successfully')
    else: 
        logging.info('Employee Not Found.')
        '''