from processor import (
    calculate_average,
    evaluate_status,
    format_student_result,
    process_student,
    process_students,
)


def test_calculate_average() -> None:
    assert calculate_average([8.0, 7.0, 9.0]) == 8.0


def test_evaluate_status_approved() -> None:
    assert evaluate_status(8.0) == "Approved"


def test_evaluate_status_exam() -> None:
    assert evaluate_status(5.0) == "Exam"


def test_evaluate_status_failed() -> None:
    assert evaluate_status(3.0) == "Failed"


def test_evaluate_status_approved_at_threshold() -> None:
    assert evaluate_status(7.0) == "Approved"


def test_evaluate_status_exam_at_threshold() -> None:
    assert evaluate_status(4.0) == "Exam"


def test_calculate_average_empty_list() -> None:
    assert calculate_average([]) == 0.0


def test_process_student() -> None:
    student = {
        "name": "Anna",
        "grades": [8.0, 7.0, 9.0]
    }

    result = process_student(student)

    assert result["name"] == "Anna"
    assert result["average"] == 8.0
    assert result["status"] == "Approved"


def test_process_students() -> None:
    students = [
        {
            "name": "Anna",
            "grades": [8.0, 7.0, 9.0]
        },
        {
            "name": "Brian",
            "grades": [5.0, 6.0, 4.0]
        },
        {
            "name": "Clara",
            "grades": [2.0, 3.0, 1.0]
        }
    ]

    results = process_students(students)

    assert len(results) == 3
    assert results[0]["status"] == "Approved"
    assert results[1]["status"] == "Exam"
    assert results[2]["status"] == "Failed"


def test_format_student_result() -> None:
    student = {
        "name": "Anna",
        "grades": [8.0, 7.0, 9.0],
        "average": 8.0,
        "status": "Approved"
    }

    result = format_student_result(student)

    assert result == "Anna | Average: 8.00 | Status: Approved"


def test_calculate_average_rounds_to_two_decimals() -> None:
    assert calculate_average([8.0, 7.5, 9.0]) == 8.17