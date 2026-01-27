.PHONY: help install test lint format clean

help: ## Show this help message
	@echo 'Usage:'
	@echo 'make install      - Install dependencies (Local environment)'
	@echo 'make install-prod - Install dependencies (Cloud environment)'
	@echo 'make run          - Run Local server'
	@echo 'make run-prod     - Run Cloud server'
	@echo 'make test         - Run tests'
	@echo 'make lint         - Code quality checks'
	@echo 'make format       - Format code'
	@echo 'make clean        - Clean temporary files'

## Development
install: ## Install development dependencies (Local)
	uv sync --all-extras

install-prod: ## Install production dependencies (Cloud)
	uv sync --extra prod

run: ## Run Local server
	uv run flask --app src run --debug --host 0.0.0.0 --port 5000

run-prod: ## Run Cloud server with gunicorn
	uv run gunicorn -c gunicorn_config.py src.app:app

lint: ## Run code quality checks
	uv run flake8 src
	uv run mypy src
	uv run black --check src
	uv run isort --check-only src

format: ## Format code
	uv run black src
	uv run isort src


## Cleanup
clean: ## Clean up temporary files
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete
	rm -rf .coverage htmlcov build dist *.egg-info .venv uv.lock
