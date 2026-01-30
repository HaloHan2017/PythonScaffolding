@echo off
REM make.bat - Windows batch file for development commands
REM Usage: make.bat [command]
setlocal enabledelayedexpansion
if "%1"=="" goto help
if "%1"=="help" goto help
if "%1"=="install" goto install
if "%1"=="run" goto run
if "%1"=="format" goto format
if "%1"=="lint" goto lint
if "%1"=="clean" goto clean
echo Unknown command: %1
echo.
goto help
:help
echo Available commands:
echo   make.bat help     - Show this help message
echo   make.bat install  - Install dependencies
echo   make.bat run      - Run development server
echo   make.bat format   - Format code
echo   make.bat lint     - Code quality checks
echo   make.bat clean    - Clean temporary files
goto end
:install
echo Installing dependencies...
set UV_LINK_MODE=copy
uv sync --extra local
if %ERRORLEVEL% neq 0 (
    echo Failed to install dependencies
    exit /b 1
)
echo Dependencies installed successfully!
goto end
:run
echo Starting development server...
uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
goto end
:format
echo Formatting code with ruff...
uv run ruff format src
if %ERRORLEVEL% neq 0 (
    echo Ruff formatting failed
    exit /b 1
)
uv run ruff check --fix src
if %ERRORLEVEL% neq 0 (
    echo Ruff linting failed
    exit /b 1
)
echo Code formatting completed!
goto end
:lint
echo Running code quality checks...
echo.
echo [1/3] Running ruff check...
uv run ruff check src
if %ERRORLEVEL% neq 0 (
    echo Ruff check failed
    set LINT_FAILED=1
)
echo.
echo [2/3] Running ruff format --check...
uv run ruff format --check src
if %ERRORLEVEL% neq 0 (
    echo Ruff format check failed
    set LINT_FAILED=1
)
echo.
echo [3/3] Running mypy...
uv run mypy src
if %ERRORLEVEL% neq 0 (
    echo Mypy check failed
    set LINT_FAILED=1
)
echo.
if defined LINT_FAILED (
    echo Lint checks failed! Please fix the issues above.
    exit /b 1
)
echo All lint checks passed!
goto end
:clean
echo Cleaning temporary files...
powershell -Command "Get-ChildItem -Path . -Include __pycache__,*.pyc,*.pyo,.DS_Store -Recurse -Force | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue"
powershell -Command "if (Test-Path .coverage) { Remove-Item .coverage -Force }; if (Test-Path htmlcov) { Remove-Item htmlcov -Recurse -Force }; if (Test-Path build) { Remove-Item build -Recurse -Force }; if (Test-Path dist) { Remove-Item dist -Recurse -Force }; if (Test-Path .venv) { Remove-Item .venv -Recurse -Force }; if (Test-Path uv.lock) { Remove-Item uv.lock -Force }; Get-ChildItem -Filter *.egg-info -Recurse | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue"
echo Cleanup completed!
goto end
:end
endlocal
