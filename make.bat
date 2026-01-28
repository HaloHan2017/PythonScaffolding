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
uv sync --all-extras
if %ERRORLEVEL% neq 0 (
    echo Failed to install dependencies
    exit /b 1
)
echo Dependencies installed successfully!
goto end
:run
echo Starting development server...
uv run flask --app src run --debug --host 0.0.0.0 --port 5000
goto end
:format
echo Formatting code with black and isort...
echo Running black...
uv run black src
if %ERRORLEVEL% neq 0 (
    echo Black formatting failed
    exit /b 1
)
echo Running isort...
uv run isort src
if %ERRORLEVEL% neq 0 (
    echo Isort formatting failed
    exit /b 1
)
echo Code formatting completed!
goto end
:lint
echo Running code quality checks...
echo.
echo [1/4] Running flake8...
uv run flake8 src
if %ERRORLEVEL% neq 0 (
    echo Flake8 check failed
    set LINT_FAILED=1
)
echo.
echo [2/4] Running mypy...
uv run mypy src
if %ERRORLEVEL% neq 0 (
    echo Mypy check failed
    set LINT_FAILED=1
)
echo.
echo [3/4] Running black --check...
uv run black --check src
if %ERRORLEVEL% neq 0 (
    echo Black check failed
    set LINT_FAILED=1
)
echo.
echo [4/4] Running isort --check...
uv run isort --check-only src
if %ERRORLEVEL% neq 0 (
    echo Isort check failed
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
