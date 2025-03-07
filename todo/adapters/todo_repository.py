from todo.domain.todo import Task
from todo.infrastructure.database import InMemoryDatabase


class TodoRepository:
    def __init__(self, db: InMemoryDatabase):
        self.db = db

    def get_next_id(self) -> int:
        return self.db.get_next_id()

    def save(self, task: Task):
        self.db.save(task)

    def get_all(self):
        return self.db.get_all()

    def delete(self, task_id: int) -> bool:
        return self.db.delete(task_id)
