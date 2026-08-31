from main import main, read_input_mode
import csv


def test_read_input_mode_accepts_csv(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: " CSV ")

    mode = read_input_mode()

    assert mode == "csv"


def test_read_input_mode_retries_after_invalid_input(monkeypatch, capsys) -> None:
    answers = iter(["invalid", "manual"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    mode = read_input_mode()

    captured = capsys.readouterr()

    assert mode == "manual"
    assert "Please enter 'manual' or 'csv'." in captured.out


def test_main_handles_missing_csv_file(monkeypatch, capsys, tmp_path) -> None:
    missing_file = tmp_path / "missing.csv"
    answers = iter(["csv", str(missing_file)])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    main()

    captured = capsys.readouterr()

    assert f"File not found: {missing_file}" in captured.out


def test_main_processes_csv_input_end_to_end(
    monkeypatch, capsys, tmp_path
) -> None:
    input_file = tmp_path / "students.csv"

    input_file.write_text(
        'name,grades\n'
        'Anna,"8.0, 7.5, 9.0"\n'
        'Brian,"5.0, 6.0, 4.5"\n',
        encoding="utf-8",
    )

    answers = iter(["csv", str(input_file)])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    monkeypatch.chdir(tmp_path)

    main()

    captured = capsys.readouterr()

    assert "Anna | Average: 8.17 | Status: Approved" in captured.out
    assert "Brian | Average: 5.17 | Status: Exam" in captured.out

    output_file = tmp_path / "academic_results.csv"

    assert output_file.exists()

    with open(output_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Anna"
    assert rows[0]["average"] == "8.17"
    assert rows[0]["status"] == "Approved"
    assert rows[1]["name"] == "Brian"
    assert rows[1]["average"] == "5.17"
    assert rows[1]["status"] == "Exam"


def test_main_handles_invalid_csv_data(monkeypatch, capsys, tmp_path) -> None:
    input_file = tmp_path / "invalid.csv"

    input_file.write_text(
        'name,grades\n'
        'Anna,"8.0, abc, 9.0"\n',
        encoding="utf-8",
    )

    answers = iter(["csv", str(input_file)])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    main()

    captured = capsys.readouterr()

    assert f"Invalid CSV data: {input_file}" in captured.out
    