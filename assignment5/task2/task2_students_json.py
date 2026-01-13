import json

def calculate_average(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        students = json.load(file)

    for student in students:
        grades = student["grades"]
        student["average_grade"] = sum(grades) / len(grades)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


if __name__ == "__main__":
    calculate_average("task2/students.json", "task2/students_with_average.json")
