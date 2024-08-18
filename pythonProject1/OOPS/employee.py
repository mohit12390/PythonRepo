class Employee:
    COMPANY = "QNET PVT.LTD"

    def __init__(self,name,email,dept,salary):
        # print("Constructor called")
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary

    def emp_info(self):
        print("Email of the employee " , self.email)
        print("Dept of the employee " , self.dept)
        print("Name of the employee ", self.name)
        print("Salary of the employee " , self.salary)

    def change_dept(self, new_dept):
        self.dept = new_dept
        print("Dept change ", self.dept)

    def change_salary(self, new_sal):
        self.salary = new_sal
        print("Sal change ", self.salary)

    def change_name(self, new_name):
        self.name = new_name
        print("Name change ", self.name)

    def change_email(self, new_email):
        self.email = new_email
        print("Email change ", self.email)


