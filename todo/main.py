from fastapi import FastAPI, HTTPException
from todo.usecases.todo_usecase import TodoUseCase
from todo.interfaces.todo_repository import TodoRepository
from todo.infrastructure.database import InMemoryDatabase

app = FastAPI()

db = InMemoryDatabase()
repository = TodoRepository(db)
todo_usecase = TodoUseCase(repository)


@app.post("/tasks/")
def create_task(title: str):
    task = todo_usecase.add_task(title)
    return {"id": task.id, "title": task.title, "completed": task.completed}


@app.get("/tasks/")
def get_tasks():
    tasks = todo_usecase.get_tasks()
    return [
        {"id": task.id, "title": task.title, "completed": task.completed}
        for task in tasks
    ]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = todo_usecase.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
