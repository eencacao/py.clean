from datetime import datetime, timezone
from typing import List, Optional
from todo.entities.todo import Todo
from todo.interfaces.todo_repository import TodoRepository


class TodoUseCase:
    def __init__(self, repository: TodoRepository):
        self._repo = repository

    def create(self, title: str) -> Todo:
        todo = Todo(
            id=self._repo.next_id(),
            title=title,
            completed=False,
            created_at=datetime.now(timezone.utc),
        )
        self._repo.save(todo)
        return todo

    def get_all(self) -> List[Todo]:
        return self._repo.get_all()

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self._repo.get_by_id(todo_id)

    def update(self, todo_id: int, title: str, completed: bool) -> Optional[Todo]:
        todo = self._repo.get_by_id(todo_id)
        if todo is None:
            return None
        todo.title = title
        todo.completed = completed
        self._repo.save(todo)
        return todo

    def delete(self, todo_id: int) -> bool:
        return self._repo.delete(todo_id)
