# Todo API — Python Clean Architecture

A RESTful To-Do list API built with Python and FastAPI, following Clean
Architecture principles with an in-memory database.

## Architecture

```
todo/
├── entities/        Pure domain model (Todo)
├── interfaces/      Repository contract
├── usecases/        Business logic (CRUD)
└── infrastructure/  In-memory repository
```

Each layer has a single responsibility:

| Layer | Responsibility |
|---|---|
| `entities/` | Pure domain model (`Todo`) |
| `interfaces/` | Repository contract |
| `usecases/` | Business logic (CRUD) |
| `infrastructure/` | In-memory repository |

## API Endpoints

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | /todos | List all todos | 200 |
| POST | /todos | Create a todo | 201 |
| GET | /todos/{id} | Get by ID | 200 |
| PUT | /todos/{id} | Update a todo | 200 |
| DELETE | /todos/{id} | Delete a todo | 204 |

## Todo Object

```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false,
  "created_at": "2026-03-12T11:00:00Z"
}
```

## Requirements

- Python 3.9+

## Setup & Run

```bash
pip install -r requirements.txt
uvicorn todo.main:app --port 8080 --reload
```

Server runs on `http://localhost:8080`.  
Interactive docs: `http://localhost:8080/docs`

## Testing

```bash
# Unit and functional tests
python -m pytest tests/ -v
```
