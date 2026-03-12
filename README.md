# FastAPI TODO API with CI/CD
![CI](https://github.com/XCVI1/fastapi-todo-cicd/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/badge/version-v1.0-blue)

## Project Overview

A simple TODO REST API built with FastAPI and Python. Includes automated testing and Docker image publishing via GitHub Actions CI/CD pipeline.

### Features

- **REST API**: Full CRUD operations for TODO tasks.
- **Automated Testing**: pytest runs on every push to main.
- **Docker**: Containerized application with Docker Compose for local development.
- **CI/CD**: GitHub Actions pipeline that tests and builds Docker image on every push.

---

## Project Structure
```
.
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_main.py         # pytest tests
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions pipeline
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Getting Started

### Run locally with Docker
```sh
docker compose up -d
```

Open `http://localhost:8000/docs`

### Run locally without Docker
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

### Run tests
```sh
pytest tests/ -v
```

---

## CI/CD Pipeline

On every push to `main`:

1. **test** — installs dependencies and runs pytest
2. **build** — builds Docker image and pushes to Docker Hub

Docker image available at: `docker pull XCVI1/todo-api:latest`

---

## Roadmap

- [x] FastAPI REST API
- [x] pytest tests
- [x] Dockerfile
- [x] Docker Compose
- [x] GitHub Actions CI/CD
