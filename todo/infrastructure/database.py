from typing import Dict, List, Optional
from todo.entities.todo import Todo


class InMemoryDatabase:
    def __init__(self):
        self._store: Dict[int, Todo] = {}
        self._counter: int = 0

    def next_id(self) -> int:
        self._counter += 1
        return self._counter

    def save(self, todo: Todo) -> None:
        self._store[todo.id] = todo

    def get_all(self) -> List[Todo]:
        return list(self._store.values())

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self._store.get(todo_id)

    def delete(self, todo_id: int) -> bool:
        if todo_id not in self._store:
            return False
        del self._store[todo_id]
        return True
