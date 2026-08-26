# Academic Operations Core Processor

def calculate_average(grades: list[float]) -> float:
    # Calculates and returns the arithmetic mean of a list of grades.
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)


def evaluate_status(average: float, passing_threshold: float = 7.0, exam_threshold: float = 4.0) -> str:
    # Evaluates the student academic standing based on final average.
    if average >= passing_threshold:
        return "Approved"
    elif average >= exam_threshold:
        return "Exam"
    return "Failed"


def process_student(student: dict) -> dict:
    average = calculate_average(student["grades"])
    status = evaluate_status(average)

    return {
        "name": student["name"],
        "grades": student["grades"],
        "average": average,
        "status": status
    }


def process_students(students: list[dict]) -> list[dict]:
    processed_students = []

    for student in students:
        processed_student = process_student(student)
        processed_students.append(processed_student)

    return processed_students


def format_student_result(student: dict) -> str:
    return (
        f"{student['name']} | "
        f"Average: {student['average']:.2f} | "
        f"Status: {student['status']}"
    )