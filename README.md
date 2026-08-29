# Academic Ops

Academic Ops is a Python CLI application for processing student data and academic business rules.

The project is being developed as part of my transition into backend development, automation, and API integration.

## Current Features

- Student name and grade input
- Input validation and error handling
- Grade average calculation
- Academic status evaluation
- Batch student processing
- CSV export of academic results
- Automated testing with pytest

## Project Structure

- `main.py` — command-line application flow and user input
- `processor.py` — academic business logic and data processing
- `exporter.py` — CSV export functionality
- `test_processor.py` — tests for processing logic
- `test_exporter.py` — tests for CSV export

## Running the Project

```bash
python main.py
```

The application generates:

```text
academic_results.csv
```

with the processed student results.

## Running the Tests

```bash
pytest
```

Current test suite:

```text
14 passed
```
