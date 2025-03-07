# CLEAN

### Exercise: To-Do List API

An application with the following layers:  
- Entities (Domain Layer) → Pure business logic, independent of frameworks.   
- Use Cases (Application Layer) → Orchestrates business logic and defines application behavior.   
- Adapters (Interface Layer) → Controllers, presenters, and UI elements.   
- Infrastructure (Data Layer) → External services (database, APIs, frameworks).     
    

```
./
│── todo/                       # Application package
│   │── domain/                 # Entities
│   │   ├── todo.py
│   │── usecases/               # Application Logic
│   │   ├── todo_usecase.py
│   │── adapters/               # Interfaces (Repository, Controllers)
│   │   ├── todo_repository.py
│   │── infrastructure/         # Frameworks & Database
│   │   ├── database.py
│   ├── main.py                 # Entry point (FastAPI)
│── .gitignore
│── LICENSE
│── README.md
└── requirements.txt
```
    
### Requirements

Python >= **3.9**

### Init

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
uvicorn todo.main:app --reload
```

### Test

`http://127.0.0.1:8000/docs`
