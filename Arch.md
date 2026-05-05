Хорошо, сжимаем задание до одного академического часа (60 минут). Оставляем только суть: проверка понимания принципов, минимум копипасты.

---

Задание (60 минут): Привести "Домашнюю библиотеку" к правильной архитектуре

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

Часть 1. Анализ (5 минут) — устно или 2-3 предложения письменно

1. Какая архитектура здесь используется (монолит/микросервисы)?
2. Назовите две проблемы этого кода с точки зрения архитектуры.

---

Часть 2. Рефакторинг в монолитную MVC (35 минут)

Цель: разнести код по правильным папкам и слоям.

Создайте структуру:

```
library/
├── app/
│   ├── main.py                 # FastAPI() + include_router
│   ├── models/                 # SQLAlchemy модель Book
│   ├── schemas/                # Pydantic: BookCreate, BookResponse
│   ├── routers/                # GET /books, POST /books
│   ├── services/               # BookService (бизнес-логика)
│   └── database.py             # engine + SessionLocal
└── requirements.txt            # fastapi, sqlalchemy, uvicorn
```

Что сделать:

1. Заменить books_db на SQLite через SQLAlchemy.
2. Pydantic схемы: BookCreate (без id, валидация year 1500-2025), BookResponse (с id).
3. BookService содержит методы: get_all(), create(data).
4. routers/books.py вызывает сервис, возвращает HTTP-ответы.

Проверка: после запуска GET /books и POST /books работают как раньше.

---

Часть 3. Мысленное выделение микросервиса (10 минут) — письменно

Вы решаете выделить Сервис авторов в отдельный микросервис.

1. Опишите одним предложением, как сервис книг получит имя автора, если у каждого своя БД.
2. Какой протокол/инструмент используете для общения между сервисами?
3. Назовите одну проблему, которая появится при этом разделении.

---

Часть 4. Добавление фичи (10 минут)

Добавьте фильтрацию GET /books?author=Оруэлл в ваш рефакторинг.

Что сдаёте: названия файлов, которые вы меняли, и одну строчку кода из сервиса.

---

Критерии сдачи (зачёт/незачёт)

· Зачёт: структура папок соблюдена, сервис отделён от роутера, SQLite работает.
· Дополнительный плюс: написан хотя бы один тест (pytest) на GET /books.

---

Формат сдачи

· Ссылка на GitHub (репозиторий) или архив с кодом.
· Файл ANSWERS.md с ответами на Части 1, 3, 4.

---

Если хочешь, я могу выдать готовый шаблон-заготовку (папки и пустые файлы), чтобы студенты не тратили время на создание структуры вручную. Напиши «Дай шаблон».
