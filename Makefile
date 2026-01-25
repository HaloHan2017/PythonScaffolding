.PHONY: help install test lint format clean docker-up docker-down

help: ## Show this help message
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

## Development
install: ## Install development dependencies
	pip install -r requirements/dev.txt
	pip install -e .

run: ## Run development server
	python manage.py run-dev

test: ## Run tests
	pytest -v --cov=app tests/

test-cov: ## Run tests with coverage report
	pytest --cov=app --cov-report=html tests/

lint: ## Run code quality checks
	flake8 app tests
	mypy app
	black --check app tests
	isort --check-only app tests

format: ## Format code
	black app tests
	isort app tests

## Database
init-db: ## Initialize database
	python manage.py init-db

migrate: ## Create migration
	flask db migrate -m "Migration message"

upgrade: ## Apply migrations
	flask db upgrade

seed: ## Seed database
	python manage.py seed-db

## Docker
docker-up: ## Start docker containers
	docker-compose up -d

docker-down: ## Stop docker containers
	docker-compose down

docker-build: ## Build docker image
	docker-compose build

docker-logs: ## View docker logs
	docker-compose logs -f

## Cleanup
clean: ## Clean up temporary files
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete
	rm -rf .coverage htmlcov build dist *.egg-info