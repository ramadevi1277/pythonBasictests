
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name} - {self.salary}"


employee = [
    Employee("Rama", 1000),
    Employee("devi", 5000),
    Employee("subbu", 10000),
    Employee("taswik", 10000)
]

sorted_employee = sorted(employee, key = lambda e: (e.salary, e.name))

print(sorted_employee)