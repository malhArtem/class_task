
## 1. Составление грамотного технического задания (ТЗ)

Цель — перевести бизнес-требования в чёткие, проверяемые технические условия.

### Разделы ТЗ:
- **Цель и область применения** — что система делает и для кого.
- **Функциональные требования** — что именно должен уметь каждый endpoint (CRUD, поиск, фильтры, отчёты и т.д.).
- **Нефункциональные требования** — производительность (RPS, latency), безопасность (JWT, роли), объёмы данных, доступность.
- **Модели данных** — сущности, их атрибуты, связи (1:1, 1:N, N:N), ограничения целостности.
- **API спецификация** (можно в формате OpenAPI) — методы, URL, request/response body, коды ответов.
- **Сценарии использования** (Use Cases) — последовательности действий пользователя.
- **Технический стек** — Python 3.10+, FastAPI, БД (PostgreSQL, SQLite, MySQL), ORM (SQLAlchemy), миграции (Alembic).
- **Требования к окружению** — переменные окружения, контейнеризация (Docker), логирование, метрики.


## 2. Проектирование на основе ТЗ

До написания кода создайте архитектурные артефакты.

### 2.1. Проектирование БД
- ER-диаграмма (можно в dbdiagram.io или через миграции).
- Типы данных и дефолтные значения.

### 2.2. Проектирование API
- Разбиение на роутеры (users, products, orders и т.д.).
- Схемы Pydantic — отдельно для запросов (Create, Update) и ответов.
- Статус‑коды, структура ошибок (единый формат).

### 2.3. Архитектура приложения (стандарт для FastAPI)
```text
app/
├── core/         # конфиги, зависимость БД, исключения
├── models/       # SQLAlchemy модели
├── schemas/      # Pydantic схемы
├── crud/         # функции работы с БД (CRUD)
├── api/          # эндпоинты (версионирование /api/v1)
├── services/     # бизнес-логика (опционально)
├── dependencies/ # внедрение зависимостей
├── utils/        # helpers, хеширование, JWT
└── main.py       # создание app
```

### 2.4. Проектирование безопасности
- Механизм аутентификации (JWT, OAuth2).
- Контроль доступа (роли: admin, user, guest).

## 3. Порядок реализации (пошагово)

Выполняйте строго снизу вверх: сначала база, затем сервисы, потом API.

### Шаг 0. Подготовка окружения
- Создать виртуальное окружение, установить: `fastapi`, `uvicorn`, `sqlalchemy`, `alembic`, `pydantic`, `psycopg2-binary` (или `asyncpg`), `python-dotenv`, `pytest`.
- Настроить `.env` для разных окружений.
- Инициализировать Git, добавить `.gitignore`.

### Шаг 1. Настройка подключения к БД и конфигурация
- Файл `core/config.py` для чтения `DATABASE_URL`.
- Функция `get_db()` для получения сессии (синхронной или async).
- *Если используете async* — `async_sessionmaker` и dependency с `async with`.

### Шаг 2. Создание SQLAlchemy моделей (согласно ТЗ)
- Описать все сущности в `models/`.
- Определить связи (`relationship`), индексы, уникальности.

### Шаг 3. Pydantic схемы (в `schemas/`)
- Создать схемы для каждого эндпоинта: `UserCreate`, `UserUpdate`, `UserResponse` и т.д.
- Настроить вложенные схемы (для связанных данных).
- Добавить валидаторы (email, пароль, длина строк).

### Шаг 4. CRUD-функции (в `crud/`)
- Базовые функции: `get`, `get_multi` (с пагинацией, фильтрацией), `create`, `update`, `delete`.
- Каждая функция принимает `db` session и опции.

### Шаг 5. Бизнес-логика (сервисный слой — опционально)
- Если логика выходит за рамки CRUD (расчёт скидки, проверка прав), вынесите в `services/`.
- Сервисы используют `crud` и не зависят напрямую от эндпоинтов.

### Шаг 6. Эндпоинты (роутеры в `api/v1/endpoints/`)
- Создать файлы: `users.py`, `items.py`.
- Использовать `APIRouter(prefix="/users", tags=["users"])`.
- Внедрить зависимости (`Depends(get_db)`, `Depends(get_current_user)`).
- Применить Pydantic схемы для request/response, установить статус‑коды.

### Шаг 7. Глобальные обработчики и зависимости
- `dependencies/auth.py` — извлечение и проверка JWT, получение текущего пользователя.
- Обработчики ошибок в `core/exceptions.py` (переопределить `HTTPException` для единого формата ответа).
- Middleware (логирование, CORS).

### Шаг 8. Тестирование (параллельно с пп. 4–7)
- Настроить `pytest` и фикстуры (клиент FastAPI, test DB).
- Написать тесты на каждый endpoint и на CRUD отдельно.
- Проверить граничные условия и ошибки валидации.

### Шаг 9. Документация и утилиты
- FastAPI автоматически генерирует Swagger и ReDoc — настройте заголовки, описание.
- Напишите `README.md` с инструкцией локального запуска и миграций.
- Добавьте скрипты в `pyproject.toml` или Makefile.

### Шаг 10. Подготовка к деплою
- Dockerfile: сборка образа, использование `gunicorn` + `uvicorn` workers.
- `docker-compose.yml` для БД + приложения.
- Переменные окружения для продакшена.
- Настройка логирования в файл/ELK.

> **Важно:** На каждом шаге, начиная с Шага 4, выполняйте **минимальный цикл**: написал модель → изменил БД → написал CRUD → один эндпоинт → тест. Так вы быстро найдёте ошибки в проектировании, не откладывая интеграцию на потом.

## Пример последовательности для одного модуля (User)
1. Модель `User` в `models/user.py`
2. Изменение БД
3. Pydantic: `UserCreate`, `UserResponse`
4. CRUD: `create_user`, `get_user_by_email`
5. Сервис: хеширование пароля
6. Эндпоинт `POST /register`
7. Тест на регистрацию

После того как все модули работают изолированно — связываете их через роутеры и зависимости (например, `POST /orders` требует авторизованного пользователя).





Ниже приведён **минимальный пример ТЗ** и результат **проектирования** для простого FastAPI-приложения с БД. Возьмём классический домен — **управление задачами (Todo)**.

## 1. Минимальное ТЗ

### 1.1. Цель
Создать REST API для управления задачами: создание, просмотр, редактирование, удаление, отметка о выполнении.

### 1.2. Функциональные требования
| Метод | Endpoint            | Описание                          | Входные данные           | Выходные данные        |
|-------|---------------------|-----------------------------------|--------------------------|------------------------|
| POST  | `/tasks`            | Создать задачу                    | `{title, description?}`  | созданная задача с ID  |
| GET   | `/tasks`            | Получить список всех задач        | параметры: `completed?` (фильтр) | массив задач      |
| GET   | `/tasks/{id}`       | Получить задачу по ID             | –                        | одна задача или 404    |
| PUT   | `/tasks/{id}`       | Полностью обновить задачу         | `{title, description, completed}` | обновлённая задача |
| PATCH | `/tasks/{id}`       | Частично обновить задачу          | любое из полей           | обновлённая задача     |
| DELETE| `/tasks/{id}`       | Удалить задачу                    | –                        | 204 No Content         |

### 1.3. Модель данных (задача)
- `id` — целое число, автоинкремент, первичный ключ
- `title` — строка, не более 100 символов, обязательное
- `description` — текст, необязательное
- `completed` — булево, по умолчанию `false`
- `created_at` — дата и время создания (заполняется автоматически)

### 1.4. Нефункциональные требования
- БД: SQLite (для простоты) или PostgreSQL
- Асинхронный режим FastAPI (опционально)
- Автоматическая документация OpenAPI
- Базовая валидация входных данных

### 1.5. Технический стек
- Python 3.10+
- FastAPI, Uvicorn
- SQLAlchemy 2.0 (Core или ORM)
- Alembic (миграции)
- Pydantic для схем

---

## 2. Проектирование на основе ТЗ

### 2.1. Проектирование БД (ER)
Одна таблица `tasks`:

| Колонка       | Тип          | Ограничения                      |
|---------------|--------------|----------------------------------|
| id            | INTEGER      | PRIMARY KEY AUTOINCREMENT        |
| title         | VARCHAR(100) | NOT NULL                         |
| description   | TEXT         | NULL                             |
| completed     | BOOLEAN      | NOT NULL DEFAULT FALSE           |
| created_at    | DATETIME     | NOT NULL DEFAULT CURRENT_TIMESTAMP |

### 2.2. SQLAlchemy модель
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
```

### 2.3. Pydantic схемы (запросы/ответы)
```python
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TaskResponse(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True   # для Pydantic v1; в v2 – from_attributes = True
```

### 2.4. CRUD-функции (схематично)
```python
def get_tasks(db, skip: int = 0, limit: int = 100, completed: bool = None):
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.offset(skip).limit(limit).all()

def create_task(db, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
# ... update, delete, get_by_id
```

### 2.5. Эндпоинты FastAPI
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(completed: bool = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, completed=completed)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(404)
    return task

# ... PUT, PATCH, DELETE аналогично
```

### 2.6. Структура проекта (минимальная)
```
todo_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py          # engine, SessionLocal
│   └── dependencies.py      # get_db
├── migrations/              # Alembic
├── .env
└── requirements.txt
```


## 3. Порядок реализации (шаги для этого примера)
1. Настроить виртуальное окружение, установить библиотеки.
2. Создать файлы `database.py`, `models.py`.
3. Настроить Alembic и применить миграцию.
4. Написать Pydantic схемы `schemas.py`.
5. Реализовать `crud.py` (базовые функции работы с БД).
6. Создать `main.py`, прописать эндпоинты.
7. Запустить `uvicorn` и проверить через /docs.
8. Добавить тесты с `pytest` (опционально).

