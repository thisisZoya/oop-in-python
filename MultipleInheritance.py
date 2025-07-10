class Person:
    def __init__(self, name, age):
        print("Initializing Person")
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        print("Initializing Employee")
        super().__init__(name, age)
        self.salary = salary

class Manager(Person):
    def __init__(self, name, age, department):
        print("Initializing Manager")
        super().__init__(name, age)
        self.department = department

class Executive(Manager, Person):
    def __init__(self, name, age, department, title):
        print("Initializing Executive")
        super().__init__(name, age, department)
        self.title = title

# test
executive = Executive("Ali", 40, "R&D", "Chief Technology Officer")

print(executive.name)
print(executive.age)
print(executive.department)
print(executive.title)
