flask-api-scaffold/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── auth.py
│   │       │   ├── users.py
│   │       │   └── health.py
│   │       └── schemas/
│   │           ├── __init__.py
│   │           ├── user.py
│   │           └── auth.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   └── token.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── user_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── validators.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── logging.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   └── test_users.py
│   └── integration/
│       └── test_auth.py
├── migrations/
├── scripts/
│   └── init_db.py
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── pyproject.toml
├── README.md
├── manage.py
├── wsgi.py
└── pytest.ini