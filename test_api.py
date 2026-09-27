from repository import list_student_records
import models
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api import app
from database import Base, get_db


client = TestClient(app)


@pytest.fixture
def database_client(tmp_path):
    database_file = tmp_path / "test_api.db"

    engine = create_engine(
        f"sqlite:///{database_file}",
        connect_args={"check_same_thread": False},
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app)

    yield test_client, TestingSessionLocal

    app.dependency_overrides.clear()


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "academic-ops",
    }


def test_process_students_endpoint(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_invalid_grades(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_empty_grades(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_grade_above_ten(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_negative_grade(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_empty_name(database_client) -> None:
    client, _ = database_client

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


def test_process_students_rejects_empty_student_list(database_client) -> None:
    client, _ = database_client

    response = client.post(
        "/students/process",
        json={
            "students": [],
        },
    )

    assert response.status_code == 422


def test_process_students_persists_records(database_client) -> None:
    client, TestingSessionLocal = database_client

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

    db = TestingSessionLocal()

    try:
        records = list_student_records(db)
    finally:
        db.close()

    assert len(records) == 2

    assert records[0].name == "Anna"
    assert records[0].average == 8.17
    assert records[0].status == "Approved"

    assert records[1].name == "Brian"
    assert records[1].average == 5.17
    assert records[1].status == "Exam"