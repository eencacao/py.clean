from todo.usecases.todo_usecase import TodoUseCase
from todo.interfaces.todo_repository import TodoRepository
from todo.infrastructure.database import InMemoryDatabase


def make_uc() -> TodoUseCase:
    return TodoUseCase(TodoRepository(InMemoryDatabase()))


def test_create():
    uc = make_uc()
    todo = uc.create("buy milk")
    assert todo.id == 1
    assert todo.title == "buy milk"
    assert todo.completed is False
    assert todo.created_at is not None


def test_get_all():
    uc = make_uc()
    assert uc.get_all() == []
    uc.create("a")
    uc.create("b")
    assert len(uc.get_all()) == 2


def test_get_by_id():
    uc = make_uc()
    uc.create("find me")
    assert uc.get_by_id(1).title == "find me"
    assert uc.get_by_id(99) is None


def test_update():
    uc = make_uc()
    uc.create("old")
    updated = uc.update(1, "new", True)
    assert updated.title == "new"
    assert updated.completed is True
    assert uc.update(99, "x", False) is None
