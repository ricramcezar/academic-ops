from sqlalchemy import Float, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class StudentRecord(Base):
    __tablename__ = "student_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    grades: Mapped[list[float]] = mapped_column(JSON, nullable=False)
    average: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)