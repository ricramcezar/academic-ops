from fastapi import FastAPI
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
) -> ProcessStudentsResponse:
    students = [student.model_dump() for student in request.students]

    results = process_academic_records(students)

    return ProcessStudentsResponse(results=results)
