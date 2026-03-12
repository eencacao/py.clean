from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Todo:
    id: int
    title: str
    completed: bool
    created_at: datetime
