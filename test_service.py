from service import process_academic_records


def test_process_academic_records() -> None:
    students = [
        {
            "name": "Anna",
            "grades": [8.0, 7.5, 9.0],
        }
    ]

    results = process_academic_records(students)

    assert len(results) == 1
    assert results[0]["name"] == "Anna"
    assert results[0]["average"] == 8.17
    assert results[0]["status"] == "Approved"
