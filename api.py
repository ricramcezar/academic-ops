from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import get_db
from repository import create_student_record
from schemas import ProcessStudentsRequest, ProcessStudentsResponse
from service import process_academic_records


app = FastAPI(title="Academic Ops API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "academic-ops",
    }


@app.post("/students/process", response_model=ProcessStudentsResponse)
def process_students_endpoint(
    request: ProcessStudentsRequest,
    db: Session = Depends(get_db),
) -> ProcessStudentsResponse:
    students = [student.model_dump() for student in request.students]

    results = process_academic_records(students)

    for result in results:
        create_student_record(db, result)

    return ProcessStudentsResponse(results=results)
