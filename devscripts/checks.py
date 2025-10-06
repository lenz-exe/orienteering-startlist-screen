import subprocess
import sys


def format_tests_and_checks():
    commands = [
        "poetry run ruff format",
        "poetry run ruff format --check",
        "poetry run ruff check",
        "poetry run mypy src/orienteering_startlist_screen",
        "poetry run pytest",
    ]

    for cmd in commands:
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            sys.exit(result.returncode)


def checks_and_tests():
    commands = [
        "poetry run ruff format --check",
        "poetry run ruff check --output-format=gitlab --output-file report_ruff.json",
        "poetry run mypy src/orienteering_startlist_screen",
        "poetry run pytest --junitxml=report_pytest.xml",
    ]
    for cmd in commands:
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            sys.exit(result.returncode)
