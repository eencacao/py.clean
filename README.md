# Todo API — Python Clean Architecture

A RESTful To-Do list API built with Python and FastAPI,
following Clean Architecture.

## Architecture

```
todo/
├── entities/        Pure domain model (Todo)
├── interfaces/      Repository contract
├── usecases/        Business logic (CRUD)
└── infrastructure/  In-memory database
```

## API Endpoints

| Method | Endpoint       | Description    |
|--------|----------------|----------------|
| GET    | /todos         | List all todos |
| POST   | /todos         | Create a todo  |
| GET    | /todos/{id}    | Get by ID      |
| PUT    | /todos/{id}    | Update a todo  |
| DELETE | /todos/{id}    | Delete a todo  |

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
- `pip install -r requirements.txt`

## Setup & Run

```bash
pip install -r requirements.txt
uvicorn todo.main:app --reload
```

Server runs on `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`
