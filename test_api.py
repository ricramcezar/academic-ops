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
