from todo.usecases.todo_usecase import TodoUseCase
from todo.interfaces.todo_repository import TodoRepository
from todo.infrastructure.database import InMemoryDatabase


def make_uc() -> TodoUseCase:
    return TodoUseCase(TodoRepository(InMemoryDatabase()))


def test_delete():
    uc = make_uc()
    uc.create("bye")
    assert uc.delete(1) is True
    assert uc.delete(1) is False
