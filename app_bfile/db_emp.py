import pickle
import os
'''This is thebinry file persistent storage
using standard pickle module'''
FILE_NAME = 'employees_db.dat'
def read_employees():
    '''Read employees from db'''
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'rb') as input_file:
            employees = pickle.load(input_file)
            return employees
    
def write_employees(employees):
    '''
    write employees to db'''
    with open(FILE_NAME, 'wb') as output_file:
            pickle.dump(employees, output_file)
