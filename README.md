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
- CSV import of student data
- Automated testing with pytest
- Manual or CSV input mode selection
- Graceful handling of missing and invalid CSV files
- End-to-end CSV processing workflow
- Service layer separating application flow from business logic
- FastAPI HTTP interface
- Health check endpoint (`GET /health`)
- Automated API testing with FastAPI TestClient

## Project Structure

- `main.py` - command-line application flow and user input
- `processor.py` - academic business logic and data processing
- `exporter.py` - CSV export functionality
- `test_processor.py` - tests for processing logic
- `test_exporter.py` - tests for CSV export
- `importer.py` - CSV input and student data parsing
- `test_importer.py` - tests for CSV import
- `test_main.py` - tests for CLI input selection and end-to-end workflows
- `students_input.csv` - sample CSV file for running the import workflow
- `service.py` - application service layer connecting interfaces to business logic
- `test_service.py` - tests for the application service layer
- `api.py` - FastAPI application and HTTP endpoints
- `test_api.py` - automated tests for the HTTP API


## Architecture

```text
CLI (main.py) ─────┐
                   ↓
                service.py
                   ↓
              processor.py

HTTP (api.py) ─────┘
```

The application supports separate interfaces while keeping the core academic business logic independent from the delivery layer.


## Running the Project

```bash
python main.py
```
Choose one of the available input methods:

```text
Input method (manual/csv):
```

For manual input, enter student information through the command line.

For CSV input, provide a file using this format:

```csv
name,grades
Anna,"8.0, 7.5, 9.0"
Brian,"5.0, 6.0, 4.5"
Clara,"2.0, 3.0, 1.0"
```

A sample file is included as `students_input.csv`.


The application generates:

```text
academic_results.csv
```

with the processed student results.


## Running the API

Install the runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn api:app --reload
```

Health check:

```text
GET http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "academic-ops"
}
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```


## Running the Tests

```bash
pytest
```

Current test suite:

```text
23 passed
```
