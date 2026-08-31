from importer import import_students_from_csv


def test_import_students_from_csv(tmp_path) -> None:
    input_file = tmp_path / "students.csv"

    input_file.write_text(
        'name,grades\n'
        'Anna,"8.0, 7.5, 9.0"\n'
        'Brian,"5.0, 6.0, 4.5"\n',
        encoding="utf-8",
    )

    students = import_students_from_csv(str(input_file))

    assert len(students) == 2

    assert students[0]["name"] == "Anna"
    assert students[0]["grades"] == [8.0, 7.5, 9.0]

    assert students[1]["name"] == "Brian"
    assert students[1]["grades"] == [5.0, 6.0, 4.5]


def test_import_empty_csv(tmp_path) -> None:
    input_file = tmp_path / "students.csv"

    input_file.write_text(
        "name,grades\n",
        encoding="utf-8",
    )

    students = import_students_from_csv(str(input_file))

    assert students == []
