from processor import process_students, format_student_result


def read_student() -> dict:
    name = input("Student name: ").strip()
    grades_input = input("Grades (comma-separated): ")

    grades = []

    for grade in grades_input.split(","):
        grades.append(float(grade.strip()))

    return {
        "name": name,
        "grades": grades
    }


def main() -> None:
    student_count = int(input("How many students? "))
    students = []

    for index in range(student_count):
        print(f"\nStudent {index + 1}")
        student = read_student()
        students.append(student)

    processed_students = process_students(students)

    print("\nResults")

    for student in processed_students:
        print(format_student_result(student))


if __name__ == "__main__":
    main()