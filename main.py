from service import process_academic_records
from processor import format_student_result
from exporter import export_students_to_csv
from importer import import_students_from_csv


def read_positive_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")


def read_student_name() -> str:
    while True:
        name = input("Student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue

        if not all(
            character.isalpha() or character in " -'"
            for character in name
        ):
            print("Student name contains invalid characters.")
            continue

        return name


def read_grades(expected_count: int) -> list[float]:
    while True:
        grades_input = input(
            f"Enter {expected_count} grade(s), comma-separated: "
        )

        try:
            grades = []

            for grade in grades_input.split(","):
                grades.append(float(grade.strip()))

        except ValueError:
            print("All grades must be valid numbers.")
            continue

        if len(grades) != expected_count:
            print(
                f"Expected {expected_count} grade(s), "
                f"but received {len(grades)}."
            )
            continue

        if any(grade < 0 or grade > 10 for grade in grades):
            print("Grades must be between 0 and 10.")
            continue

        return grades

def read_student(expected_grade_count: int) -> dict:
    name = read_student_name()
    grades = read_grades(expected_grade_count)

    return {
        "name": name,
        "grades": grades
    }


def read_input_mode() -> str:
    while True:
        mode = input("Input method (manual/csv): ").strip().lower()

        if mode in {"manual", "csv"}:
            return mode

        print("Please enter 'manual' or 'csv'.")


def main() -> None:
    print("Academic Operations")
    print("-------------------")

    mode = read_input_mode()

    students = []

    if mode == "manual":
        student_count = read_positive_integer("How many students? ")
        grade_count = read_positive_integer("How many grades per student: ")

        for index in range(student_count):
            print(f"\nStudent {index + 1}")
            student = read_student(grade_count)
            students.append(student)

    else:
        filename = input("CSV filename: ").strip()

        try:
            students = import_students_from_csv(filename)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return
        except (KeyError, ValueError):
            print(f"Invalid CSV data: {filename}")
            return

    processed_students = process_academic_records(students)

    print("\nAcademic Results")
    print("------------------")

    for student in processed_students:
        print(format_student_result(student))

    export_students_to_csv(processed_students, "academic_results.csv")
    print("\nResults exported to academic_results.csv")


if __name__ == "__main__":
    main()
