class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Person: {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def get_info(self):
        return f"Student: {self._name}, ID: {self.student_id}"


if __name__ == "__main__":
    name = input("Enter name: ")
    student_id = input("Enter student ID: ")

    student = Student(name, student_id)
    print(student.get_info())