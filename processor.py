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

if __name__ == "__main__":
    # Test assertions for local verification
    sample_grades = [8.0, 9.0]
    avg = calculate_average(sample_grades)
    status = evaluate_status(avg)

    print(f"Test Average: {avg} | Status: {status}")