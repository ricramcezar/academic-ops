from typing import Annotated

from pydantic import BaseModel, Field, field_validator

Grade = Annotated[float, Field(ge=0, le=10)]

class StudentInput(BaseModel):
    name: str
    grades: list[Grade] = Field(min_length=1)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        name = value.strip()

        if not name:
            raise ValueError("name must not be empty")

        return name


class ProcessStudentsRequest(BaseModel):
    students: list[StudentInput] = Field(min_length=1)


class StudentResult(BaseModel):
    name: str
    grades: list[float]
    average: float
    status: str


class ProcessStudentsResponse(BaseModel):
    results: list[StudentResult]
