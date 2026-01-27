# abc module is used for defining abstract base classes
from abc import ABC, abstractmethod

# -------------------------------
# 1. ABSTRACTION
# -------------------------------
class CompanyRules(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


# -------------------------------
# 2. CLASS + ENCAPSULATION
# -------------------------------
class Employee(CompanyRules):
    def __init__(self, emp_id, name, address, salary, domain):
        # Instance variables (data stored in object)
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.__salary = salary   # private variable (encapsulation)
        self.domain = domain

    # Public method
    def display(self):
        print("\n--- Employee Details ---")
        print("ID      :", self.emp_id)
        print("Name    :", self.name)
        print("Address :", self.address)
        print("Domain  :", self.domain)

    # Getter method (access private data)
    def get_salary(self):
        return self.__salary

    # Setter method (modify private data)
    def set_salary(self, new_salary):
        self.__salary = new_salary

    # Abstract method implementation
    def calculate_salary(self):
        print("Final Salary:", self.__salary)


# -------------------------------
# 3. INHERITANCE
# -------------------------------
class Manager(Employee):
    def __init__(self, emp_id, name, address, salary, domain, bonus):
        super().__init__(emp_id, name, address, salary, domain)
        self.bonus = bonus

    # ---------------------------
    # 4. POLYMORPHISM
    # ---------------------------
    def calculate_salary(self):
        total = self.get_salary() + self.bonus
        print("Manager Total Salary:", total)


# -------------------------------
# 5. OBJECT CREATION
# -------------------------------
emp1 = Employee(101, "Rahul", "Bangalore", 50000, "Python")
emp2 = Employee(102, "Anita", "Hyderabad", 60000, "Java")

mgr1 = Manager(201, "Suresh", "Pune", 80000, "Management", 20000)


# -------------------------------
# 6. ACCESSING OBJECT DATA
# -------------------------------
emp1.display()
emp1.calculate_salary()

emp2.display()
emp2.calculate_salary()

mgr1.display()
mgr1.calculate_salary()


# -------------------------------
# 7. ENCAPSULATION DEMO
# -------------------------------
print("\nOld Salary:", emp1.get_salary())
emp1.set_salary(55000)
print("Updated Salary:", emp1.get_salary())
