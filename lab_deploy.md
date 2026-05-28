## Лабораторная работа: Развёртывание FastAPI-приложения на Python

**Цель работы:**  
Закрепить навыки переноса Python-приложения на удалённый сервер с помощью FileZilla, создания виртуального окружения, установки зависимостей из `requirements.txt`, запуска веб-приложения на базе FastAPI.  
В условиях ограниченного сервера каждый студент работает в своей директории и запускает приложение на своём (уникальном) порту.

---

### Условия выполнения

- Каждый студент создаёт **свою папку** на сервере с именем `todo_ФАМИЛИЯ` (латиницей).  
- В коде приложения студент должен **вписать свою фамилию** (или ФИО), которая будет выводиться при обращении к корневому маршруту или к специальному маршруту `/student`.

---

- Адрес сервера: 192.168.89.99
- Имя пользователя: student
- Пароль: 1234

## Структура приложения

```
todo_IVANOV/            # вместо IVANOV – фамилия студента
├── main.py
├── models.py
├── routers.py
└── requirements.txt
```

### 1. Файл `models.py` (не требует изменений)

```python
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
```

### 2. Файл `routers.py` (не требует изменений)

```python
from fastapi import APIRouter, HTTPException
from typing import List, Dict
from models import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks_db: Dict[int, Task] = {}
counter = 1

@router.get("/", response_model=List[Task])
def get_all_tasks():
    return list(tasks_db.values())

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@router.post("/", response_model=Task, status_code=201)
def create_task(task: Task):
    global counter
    task.id = counter
    tasks_db[counter] = task
    counter += 1
    return task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    updated.id = task_id
    tasks_db[task_id] = updated
    return updated

@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task deleted"}
```

### 3. Файл `main.py` (требует индивидуальной настройки)

Каждый студент **должен изменить**:
- переменную `STUDENT_NAME` – вписать свою фамилию (или ФИО);
- параметр `port` в `uvicorn.run` – назначить **свой уникальный порт**.

```python
from fastapi import FastAPI
from routers import router

# --------------------------------------------
# ИНДИВИДУАЛЬНЫЕ НАСТРОЙКИ (ИЗМЕНИТЬ!)
STUDENT_NAME = "Иванов И.И."   # <- впишите свою фамилию и инициалы
MY_PORT = 8001                  # <- назначенный порт (уникальный для студента)
# --------------------------------------------

app = FastAPI(title="TODO API", description="Простое API для задач", version="1.0")
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": f"TODO API студента {STUDENT_NAME} работает. Go to /tasks",
        "student": STUDENT_NAME
    }

@app.get("/student")
def student_info():
    return {"student": STUDENT_NAME}

# Запуск приложения командой python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=MY_PORT, reload=True)
```

### 4. Файл `requirements.txt`

```
fastapi==0.115.0
uvicorn[standard]==0.30.0
pydantic==2.7.0
```

---

## Порядок выполнения работы

### Этап 1. Локальная подготовка

- Создайте на локальном компьютере папку с именем `todo_ФАМИЛИЯ` (латиницей, например `todo_IVANOV`).
- Внутри создайте файлы `main.py`, `models.py`, `routers.py`, `requirements.txt` с содержимым, указанным выше.
- В файле `main.py` **обязательно** замените `STUDENT_NAME` на свои фамилию и инициалы, а `MY_PORT` – на выданный порт.
- Убедитесь, что файлы сохранены в кодировке UTF-8.

### Этап 2. Перенос на сервер с помощью FileZilla

- Запустите FileZilla и подключитесь к серверу (хост, имя пользователя, пароль, порт 22).
- В правой панели (удалённый сервер) перейдите в свою домашнюю директорию.
- Скопируйте папку `todo_ФАМИЛИЯ` с локальной машины на сервер.

### Этап 3. Подключение к серверу по SSH и настройка окружения

- Подключитесь к серверу по SSH.
- Перейдите в свою папку `todo_ФАМИЛИЯ`.
- Убедитесь, что на сервере установлены `python3`, `python3-pip`, `python3-venv`. Если нет – установите.
- Создайте виртуальное окружение внутри папки приложения.
- Активируйте виртуальное окружение.
- Установите зависимости из `requirements.txt`.

### Этап 4. Запуск приложения

- Запустите приложение командой `python main.py`.
- Убедитесь, что в терминале появилось сообщение о запуске Uvicorn на указанном вами порту.

### Этап 5. Проверка работоспособности

- Откройте браузер на локальной машине и перейдите по адресу:
  ```
  http://IP_сервера:ВАШ_ПОРТ
  ```
  Должен отобразиться JSON с вашей фамилией.
- Перейдите к документации: `http://IP_сервера:ВАШ_ПОРТ/docs`.
- Протестируйте создание и получение задач через интерфейс `/docs` или через `curl`.

### Сообщеите преподавателю для проверки

### Этап 6. Остановка приложения

- Нажмите `Ctrl+C` в терминале, где запущено приложение.
- Деактивируйте виртуальное окружение.

---


---

**Примечание:** Если вы выполняете работу на локальной машине (вместо сервера), то этап с FileZilla пропускается. В этом случае используйте `localhost:ВАШ_ПОРТ`, но обязательно договоритесь с сокурсниками об использовании разных портов, чтобы не было конфликта.
