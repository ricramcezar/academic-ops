from processor import process_students, format_student_result


def main() -> None:
    students = [
        {
            "name": "Anna",
            "grades": [8.0, 7.5, 9.0]
        },
        {
            "name": "Brian",
            "grades": [5.0, 6.0, 4.5]
        },
        {
            "name": "Clara",
            "grades": [2.0, 3.5, 3.0]
        }
    ]

    processed_students = process_students(students)

    for student in processed_students:
        print(format_student_result(student))


if __name__ == "__main__":
    main()