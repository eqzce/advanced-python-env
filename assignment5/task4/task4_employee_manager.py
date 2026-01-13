class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

    def get_total_salary(self):
        return self.get_salary()


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

    def get_total_salary(self):
        return self.get_salary() + self.bonus


def print_employees(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Total Salary: {emp.get_total_salary()}")


if __name__ == "__main__":
    employees = []

    n = int(input("How many employees? "))

    for i in range(n):
        role = input(f"Enter role for employee {i+1} (employee/manager): ").lower()
        salary = float(input("Enter salary: "))

        if role == "manager":
            bonus = float(input("Enter bonus: "))
            employees.append(Manager(salary, bonus))
        else:
            employees.append(Employee(salary))

    print("\nEmployees List:")
    print_employees(employees)
