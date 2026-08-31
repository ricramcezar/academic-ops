import csv


def import_students_from_csv(filename: str)-> list[dict]:
    students = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            grades = [
                float(grade.strip())
                for grade in row["grades"].split(",")
            ]

            students.append(
                {
                    "name": row["name"].strip(),
                    "grades": grades,
                }
            )

    return students
