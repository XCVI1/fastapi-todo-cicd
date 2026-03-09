from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {"tasks": []}


def test_create_task():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test task"
    assert response.json()["done"] == False


def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200


def test_update_task():
    response = client.put("/tasks/1", json={"done": True})
    assert response.status_code == 200
    assert response.json()["done"] == True


def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200


def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
