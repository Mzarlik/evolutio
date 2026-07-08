---
name: Python Development Skill
description: Guidelines and commands for writing, testing, linting, and refactoring Python code and frameworks.
---

# Python Development Skill

This skill provides the execution patterns, commands, and best practices for developing Python applications in this codebase.

## Code Style & Formatting
*   Always format Python code before committing.
    *   **Black:** `black .`
    *   **Ruff:** `ruff format .`
*   Linting check:
    *   **Pylint:** `pylint <module_or_file>`
    *   **Ruff lint:** `ruff check .`

## Dependency Management
If a `pyproject.toml` is present, use `poetry`:
*   Add a dependency: `poetry add <package>`
*   Add dev dependency: `poetry add --group dev <package>`
*   Run command in environment: `poetry run <command>`

Otherwise, if `requirements.txt` is present:
*   Install requirements: `pip install -r requirements.txt`
*   Add dependency: Write package to `requirements.txt` and run `pip install <package>`

## Framework Best Practices

### FastAPI / Starlette
*   Always define query/path/body parameters using Pydantic schemas.
*   Implement custom error handlers for standard HTTP exceptions.
*   Ensure asynchronous endpoints use `async def` and non-async operations are run on threadpools or written as synchronous functions.

### Django
*   Keep logic inside services/models, not in views (skinny views, fat models/services).
*   Always run migrations: `python manage.py makemigrations` and `python manage.py migrate`.
*   Avoid raw SQL queries; use Django ORM unless strictly necessary for optimization.

### Flask
*   Structure applications using Blueprints for modularity.
*   Use Flask-SQLAlchemy or Flask-Migrate for database handling and schema migrations.

## Testing & Verification
*   Use `pytest` for all unit and integration testing.
*   Run all tests: `pytest`
*   Run specific test file: `pytest tests/test_filename.py`
*   Run test with coverage: `pytest --cov=src`
