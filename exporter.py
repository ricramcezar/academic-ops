import csv

def export_students_to_csv(students: list[dict], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "grades", "average", "status"])

        for student in students:
            writer.writerow(
                [
                    student["name"],
                    ", ".join(str(grade) for grade in student["grades"]),
                    student["average"],
                    student["status"],
                ]
            )
