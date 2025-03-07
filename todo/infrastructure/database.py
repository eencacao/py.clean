from todo.domain.todo import Task
from typing import Dict, List


class InMemoryDatabase:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.current_id = 1

    def get_next_id(self) -> int:
        task_id = self.current_id
        self.current_id += 1
        return task_id

    def save(self, task: Task):
        self.tasks[task.id] = task

    def get_all(self) -> List[Task]:
        return list(self.tasks.values())

    def delete(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
