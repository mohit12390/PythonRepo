
import employee


emp1 = employee.Employee("Mohit","m@gmail.com","SALES",5000)
emp1.emp_info()
print('*'*20)
emp1.change_dept("MARKETING")
emp1.emp_info()
print('*'*20)

print(emp1.COMPANY)

