import pandas as pd
from datetime import datetime


file = '/Users/rajeshr/Desktop/employees.csv'
df = pd.read_csv(file)

class Employee():
    def __init__(self, name, salary, department, hire_date, manager):
        self.name = name
        self.salary = salary
        self.department = department
        self.hire_date = hire_date
        self.manager = manager
    
    def changeSalary(self, salary_to_add):
        self.salary += salary_to_add
        
    def changeDept(self, dept):
        self.department = dept
        
    def __str__(self):
        return "Name: {}, Salary: {}, Dept: {}".format(self.name, self.salary, self.department)
        
  
print('--------- FIRST SUBDIVISON ---------')
emp = Employee('Raj', 1000, 'CS', datetime(2020, 5, 17), None)
print(emp)

emp.changeSalary(200)
print(emp)

emp.changeDept('MS CS')
print(emp)



details = df[['FIRST_NAME', 'SALARY', 'DEPARTMENT_ID', 'HIRE_DATE', 'MANAGER_ID']].values
employee_details = [Employee(name, salary, dept_id, date,  manager) for name, salary, dept_id, date, manager in details]
print('--------- SECOND SUBDIVISON ---------')
print(employee_details[0].name)


date_format = "%d-%b-%y"
for emp in employee_details:
    if  datetime.strptime("1-Jan-03", date_format) > datetime.strptime(emp.hire_date, date_format):
        emp.changeSalary(60)
        
print('--------- THIRD SUBDIVISON ---------')
print(employee_details[11].salary)

print('--------- FOURTH SUBDIVISON ---------')
print('csv created')
employee_revised = [[emp.name, emp.salary, emp.department, emp.hire_date, emp.manager] for emp in employee_details]
pd.DataFrame(employee_revised).to_csv('/Users/rajeshr/Desktop/employee_updated.csv')


dictionary = {}

for emp in employee_revised:
    if emp[4] in dictionary:
        dictionary[emp[4]] += 1
    else:
        dictionary[emp[4]] = 1
        
manager_ids = [int(key) for key in dictionary if dictionary[key] > 3]
print('--------- FIFTH SUBDIVISON ---------')
print(df[df['EMPLOYEE_ID'].isin(manager_ids)])
