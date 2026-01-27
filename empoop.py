class Employee:
    def __init__(self, emp_id, name, address, salary, domain):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.salary = salary
        self.domain = domain

    def display_employee(self):
        print("\n--- Employee Details ---")
        print("ID :", self.emp_id)
        print("Name :", self.name)
        print("Address :", self.address)
        print("Salary :", self.salary)
        print("Domain :", self.domain)

emp1 = Employee(101, "Dip", "Pune", 55000, "Python")
emp2 = Employee(102, "Shubh", "Mumbai", 60000, "Java")
emp3 = Employee(103, "yash", "Pune", 50000, "DevOps")
emp4 = Employee(104, "disha", "BLR", 65000, "Java")
emp5 = Employee(105, "riya", "Delhi", 70000, "AI")

emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp4.display_employee()
emp5.display_employee()
