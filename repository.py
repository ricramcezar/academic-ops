from sqlalchemy import select
from sqlalchemy.orm import Session

from models import StudentRecord


def create_student_record(
    db: Session,
    student: dict,
) -> StudentRecord:
    record = StudentRecord(
        name=student["name"],
        grades=student["grades"],
        average=student["average"],
        status=student["status"],
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def list_student_records(db: Session) -> list[StudentRecord]:
    statement = select(StudentRecord).order_by(StudentRecord.id)

    return list(db.scalars(statement).all())
