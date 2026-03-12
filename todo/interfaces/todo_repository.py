from typing import List, Optional
from todo.entities.todo import Todo
from todo.infrastructure.database import InMemoryDatabase


class TodoRepository:
    def __init__(self, db: InMemoryDatabase):
        self._db = db

    def next_id(self) -> int:
        return self._db.next_id()

    def save(self, todo: Todo) -> None:
        self._db.save(todo)

    def get_all(self) -> List[Todo]:
        return self._db.get_all()

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self._db.get_by_id(todo_id)

    def delete(self, todo_id: int) -> bool:
        return self._db.delete(todo_id)
