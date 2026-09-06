from fastapi.testclient import TestClient

from api import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "academic-ops",
    }


def test_process_students_endpoint() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "Anna",
                    "grades": [8.0, 7.5, 9.0],
                },
                {
                    "name": "Brian",
                    "grades": [5.0, 6.0, 4.5],
                },
            ]
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "results": [
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
    }


def test_process_students_rejects_invalid_grades() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "Anna",
                    "grades": "invalid",
                }
            ]
        },
    )

    assert response.status_code == 422


def test_process_students_rejects_empty_grades() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "Anna",
                    "grades": [],
                }
            ]
        },
    )

    assert response.status_code == 422


def test_process_students_rejects_grade_above_ten() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "Anna",
                    "grades": [8.0, 15.0],
                }
            ]
        },
    )

    assert response.status_code == 422


def test_process_students_rejects_negative_grade() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "Anna",
                    "grades": [8.0, -2.0],
                }
            ]
        },
    )

    assert response.status_code == 422


def test_process_students_rejects_empty_name() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [
                {
                    "name": "   ",
                    "grades": [8.0, 7.5],
                }
            ]
        },
    )

    assert response.status_code == 422


def test_process_students_rejects_empty_student_list() -> None:
    response = client.post(
        "/students/process",
        json={
            "students": [],
        },
    )

    assert response.status_code == 422
