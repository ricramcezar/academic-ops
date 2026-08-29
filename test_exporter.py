import csv

from exporter import export_students_to_csv


def test_export_students_to_csv(tmp_path) -> None:
    students = [
        {
            "name": "Anna",
            "grades": [8.0, 7.5, 9.0],
            "average": 8.17,
            "status": "Approved",
        }
    ]

    output_file = tmp_path / "students.csv"

    export_students_to_csv(students, str(output_file))

    with open(output_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["name"] == "Anna"
    assert rows[0]["grades"] == "8.0, 7.5, 9.0"
    assert rows[0]["average"] == "8.17"
    assert rows[0]["status"] == "Approved"


def test_export_multiple_students_to_csv(tmp_path) -> None:
    students = [
        {
            "name": "Anna",
            "grades": [8.0, 7.5, 9.0],
            "average": 8.17,
            "status": "Approved",
        },
        {
            "name": "Brian",
            "grades": [5.0, 6.0, 4.5],
            "average": 5.17,
            "status": "Exam",
        },
    ]

    output_file = tmp_path / "students.csv"

    export_students_to_csv(students, str(output_file))

    with open(output_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Anna"
    assert rows[1]["name"] == "Brian"
    assert rows[1]["average"] == "5.17"
    assert rows[1]["status"] == "Exam"


def test_export_empty_student_list_to_csv(tmp_path) -> None:
    output_file = tmp_path / "students.csv"

    export_students_to_csv([], str(output_file))

    with open(output_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert rows == []
    assert reader.fieldnames == ["name", "grades", "average", "status"]
