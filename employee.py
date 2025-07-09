class Employee:
    _total_employees = 0 
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee._total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls._total_employees

    @staticmethod
    def is_valid_salary(salary):
        if salary > 5000:
            return True
        return False
    
    def __str__(self):
        return f"Employee: {self.__name}, salary: {self.__salary}"


# create instances of Employee
emp1 = Employee("Zahra" 7500)
emp2 = Employee("sara", 4800)

# print Employee
print("Employee information:")
print(emp1)  
print(emp2)

print("-" * 20)

# get total employees
print(Employee.get_total_employees())