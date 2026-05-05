

## Задание: Привести "Домашнюю библиотеку" к правильной архитектуре

Дан стартовый код (весь в одном файле main.py):

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

books_db = [
    Book(id=1, title="1984", author="Оруэлл", year=1949),
    Book(id=2, title="Мастер и Маргарита", author="Булгаков", year=1967),
]

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.post("/books", response_model=Book)
def create_book(book: Book):
    if book.year < 0 or book.year > 2025:
        raise HTTPException(status_code=400, detail="Invalid year")
    new_id = max(b.id for b in books_db) + 1 if books_db else 1
    new_book = Book(id=new_id, title=book.title, author=book.author, year=book.year)
    books_db.append(new_book)
    return new_book
```

---

### Часть 1. Анализ

1. Какая архитектура здесь используется (монолит/микросервисы)?
2. Назовите две проблемы этого кода с точки зрения архитектуры.

---

### Часть 2. Рефакторинг в монолитную MVC (35 минут)

* Цель: разнести код по правильным папкам и слоям. *

Создайте структуру:

```
library/
├── app/
│   ├── main.py                 # FastAPI() + include_router
│   ├── schemas/                # Pydantic: BookCreate, BookResponse
│   ├── routers/                # GET /books, POST /books
│   ├── services/               # BookService (бизнес-логика)
│   └── database.py.            # функции для работы с бд
```

Что сделать:

1. Заменить books_db на SQLite
2. Pydantic схемы: BookCreate (без id, валидация year 1500-2025), BookResponse (с id).
3. BookService содержит методы: get_all(), create(data).
4. routers/books.py вызывает сервис, возвращает HTTP-ответы.

Проверка: после запуска GET /books и POST /books работают как раньше.

---

.


---

Критерии сдачи (зачёт/незачёт)

Зачёт: структура папок соблюдена, сервис отделён от роутера, SQLite работает.
