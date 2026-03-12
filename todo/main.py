from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from todo.usecases.todo_usecase import TodoUseCase
from todo.interfaces.todo_repository import TodoRepository
from todo.infrastructure.database import InMemoryDatabase

app = FastAPI(title="Todo API")
_uc = TodoUseCase(TodoRepository(InMemoryDatabase()))


class CreateBody(BaseModel):
    title: str


class UpdateBody(BaseModel):
    title: str
    completed: bool


@app.get("/todos")
def list_todos():
    return _uc.get_all()


@app.post("/todos", status_code=201)
def create_todo(body: CreateBody):
    return _uc.create(body.title)


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todo = _uc.get_by_id(todo_id)
    if todo is None:
        raise HTTPException(404, detail="not found")
    return todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, body: UpdateBody):
    todo = _uc.update(todo_id, body.title, body.completed)
    if todo is None:
        raise HTTPException(404, detail="not found")
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if not _uc.delete(todo_id):
        raise HTTPException(404, detail="not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("todo.main:app", host="0.0.0.0", port=8080)
