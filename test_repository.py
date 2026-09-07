from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from repository import create_student_record, list_student_records


def test_create_and_list_student_records(tmp_path) -> None:
    database_file = tmp_path / "test.db"

    engine = create_engine(
        f"sqlite:///{database_file}",
        connect_args={"check_same_thread": False},
    )

    Base.metadata.create_all(bind=engine)

    TestSessionLocal = sessionmaker(bind=engine)
    db = TestSessionLocal()

    student = {
        "name": "Anna",
        "grades": [8.0, 7.5, 9.0],
        "average": 8.17,
        "status": "Approved",
    }

    created = create_student_record(db, student)
    records = list_student_records(db)

    assert created.id == 1
    assert created.name == "Anna"

    assert len(records) == 1
    assert records[0].name == "Anna"
    assert records[0].grades == [8.0, 7.5, 9.0]
    assert records[0].average == 8.17
    assert records[0].status == "Approved"

    db.close()


def test_list_student_records_returns_empty_list(tmp_path) -> None:
    database_file = tmp_path / "empty.db"

    engine = create_engine(
        f"sqlite:///{database_file}",
        connect_args={"check_same_thread": False},
    )

    Base.metadata.create_all(bind=engine)

    TestSessionLocal = sessionmaker(bind=engine)
    db = TestSessionLocal()

    records = list_student_records(db)

    assert records == []

    db.close()
