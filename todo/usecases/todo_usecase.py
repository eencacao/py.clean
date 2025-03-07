from typing import List
from todo.domain.todo import Task
from todo.adapters.todo_repository import TodoRepository
from datetime import datetime


class TodoUseCase:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_task(self, title: str) -> Task:
        new_task = Task(
            id=self.repository.get_next_id(),
            title=title,
            completed=False,
            created_at=datetime.now(),
        )
        self.repository.save(new_task)
        return new_task

    def get_tasks(self) -> List[Task]:
        return self.repository.get_all()

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
