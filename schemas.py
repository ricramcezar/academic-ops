from pydantic import BaseModel


class StudentInput(BaseModel):
    name: str
    grades: list[float]


class ProcessStudentsRequest(BaseModel):
    students: list[StudentInput]


class StudentResult(BaseModel):
    name: str
    grades: list[float]
    average: float
    status: str


class ProcessStudentsResponse(BaseModel):
    results: list[StudentResult]
