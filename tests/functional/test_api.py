from fastapi.testclient import TestClient
from todo.main import app

client = TestClient(app)


def test_get_todos_empty():
    res = client.get("/todos")
    assert res.status_code == 200
    assert res.json() == []


def test_create_todo():
    res = client.post("/todos", json={"title": "test todo"})
    assert res.status_code == 201
    body = res.json()
    assert body["title"] == "test todo"
    assert body["completed"] is False
    assert "id" in body


def test_get_todo_by_id():
    res = client.get("/todos/1")
    assert res.status_code == 200
    assert res.json()["title"] == "test todo"


def test_update_todo():
    res = client.put(
        "/todos/1",
        json={"title": "updated", "completed": True},
    )
    assert res.status_code == 200
    body = res.json()
    assert body["title"] == "updated"
    assert body["completed"] is True


def test_delete_todo():
    res = client.delete("/todos/1")
    assert res.status_code == 204
    res2 = client.delete("/todos/1")
    assert res2.status_code == 404
