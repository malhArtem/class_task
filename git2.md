Задание рассчитано на **2–2.5 часа** и включает:
- создание репозитория
- добавление коллабораторов
- клонирование в PyCharm
- работу в отдельных ветках
- Pull Request'ы
- код-ревью
- разрешение конфликтов
- финальную интеграцию

---

# 🧪 Лабораторная работа: «Командная разработка на Git и GitHub в PyCharm»

## 🎯 Цель работы

Научиться работать в команде над одним репозиторием:
- создавать и клонировать репозиторий
- настраивать права доступа (Collaborators)
- создавать ветки и переключаться между ними
- делать коммиты и пушить изменения
- открывать и сливать Pull Request'ы
- решать конфликты слияния
- синхронизировать свою локальную копию с удалённой

---

## 📦 Итоговый проект

**Название:** `team-data-processor`

**Описание:** Консольное приложение на Python, которое:
1. Загружает данные из CSV-файла
2. Очищает их (удаляет пустые строки, дубликаты)
3. Фильтрует (оставляет только совершеннолетних)
4. Вычисляет среднюю зарплату
5. Сохраняет результат в JSON-файл

Каждый студент отвечает за **один модуль** и работает в **своей ветке**.

---

## 👥 Распределение ролей

| Студент | Роль | Модуль / задача |
|---------|------|----------------|
| **А** | Team Lead / Maintainer | Создаёт репозиторий, проверяет и сливает PR, пишет финальный `main.py` |
| **Б** | Data Loader | `loader.py` – загрузка CSV |
| **В** | Data Cleaner | `cleaner.py` – удаление пустых строк и дубликатов |
| **Г** | Filter | `filter.py` – фильтр по возрасту (>18) |
| **Д** | Aggregator | `aggregator.py` – средняя зарплата |
| **Е** | Saver | `saver.py` – сохранение в JSON |
| **Ж** | Tester | `test_processor.py` – модульные тесты (pytest) |

> Если студентов больше — добавьте роли: «Логгер», «Валидатор данных», «Генератор отчёта» и т.д.

---

## 🧰 Требуемое ПО

- Установленный Python 3.9+
- Установленный PyCharm (Community или Professional)
- Аккаунт на GitHub
- Git (обычно уже идёт с PyCharm)

---

# 📝 Часть 1. Создание общего репозитория (Студент А)

**Время:** 15 минут  
**Кто выполняет:** Только студент А

---

### Шаг 1.1. Создать репозиторий на GitHub

1. Зайдите на [github.com](https://github.com) и авторизуйтесь.
2. Нажмите зелёную кнопку **«New»** или перейдите по ссылке: `https://github.com/new`
3. Заполните поля:
   - **Repository name:** `team-data-processor`
   - **Description:** (необязательно) «Совместный проект для отработки Git и GitHub»
   - **Public / Private:** выберите **Public** (преподаватель сможет проверить)
   - **Initialize this repository with:** **НИЧЕГО НЕ ВЫБИРАЙТЕ** (оставьте пустым: нет README, нет .gitignore, нет лицензии)
4. Нажмите **«Create repository»**

> ✅ **Почему пустой?** Мы создадим всю структуру через PyCharm — так удобнее и нагляднее.

---

### Шаг 1.2. Клонировать репозиторий в PyCharm

1. На странице созданного репозитория нажмите зелёную кнопку **«<> Code»**
2. Скопируйте HTTPS-ссылку (например, `https://github.com/StudentA/team-data-processor.git`)
3. Откройте **PyCharm**
4. На стартовом экране выберите: **«Get from VCS»** (или File → New Project → Get from Version Control)
5. В поле **URL** вставьте скопированную ссылку
6. В поле **Directory** выберите папку, куда сохранить проект
7. Нажмите **«Clone»**

> ✅ После клонирования PyCharm автоматически откроет проект.

---

### Шаг 1.3. Создать структуру проекта

В корневой папке проекта создайте следующую структуру.  
Создавать можно через:
- правой кнопкой мыши на папке → New → File / Directory
- или через встроенный терминал (`Alt+F12`)

```
team-data-processor/          # корень репозитория
├── data/
│   └── data.csv
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── cleaner.py
│   ├── filter.py
│   ├── aggregator.py
│   └── saver.py
├── tests/
│   └── test_processor.py
└── README.md
```

#### Файл `data/data.csv` (создайте именно с таким содержимым):

```csv
name,age,salary
Alice,25,50000
Bob,17,30000
Charlie,30,65000
David,16,20000
Eva,28,55000
```

#### Файл `README.md`:

```markdown
# Team Data Processor

Командный проект для изучения Git, GitHub и PyCharm.

## Участники
- А – Maintainer
- Б – Data Loader
- В – Cleaner
- Г – Filter
- Д – Aggregator
- Е – Saver
- Ж – Tester

## Запуск
```bash
python src/main.py
```

## Тесты
```bash
pytest tests/
```

#### Файл `src/__init__.py` — **пустой** (нужен, чтобы Python распознавал папку как пакет).

---

### Шаг 1.4. Сделать первый коммит и пуш

В PyCharm:

1. Нажмите `Ctrl+K` (или `Cmd+K` на Mac) — откроется окно коммита.
2. Выберите **все файлы** (отметьте галочками).
3. Напишите сообщение коммита:  
   `Initial project structure`
4. Нажмите **«Commit»**.
5. После коммита нажмите `Ctrl+Shift+K` (или Git → Push), чтобы отправить изменения на GitHub.

> ✅ Теперь на GitHub в вашем репозитории появились все файлы.

---

### Шаг 1.5. Добавить остальных студентов как Collaborators

> ⚠️ **Важно:** Это действие делает студент А, и оно необходимо, чтобы остальные могли пушить в общий репозиторий.

1. На **GitHub** перейдите в ваш репозиторий `team-data-processor`
2. Нажмите на вкладку **«Settings»** (в правой части меню, почти в конце)
3. В левом меню выберите **«Collaborators»** (или «Access» → «Collaborators»)
4. Нажмите кнопку **«Add people»**
5. Введите **GitHub-username** каждого студента (Б, В, Г, Д, Е, Ж).  
   *(Имена можно разделять запятыми или добавлять по одному)*
6. Нажмите **«Add [username] to this repository»**
7. Каждый студент получит приглашение на почту. Оно должно быть **принято** (обычно нужно зайти на GitHub и подтвердить).

> ✅ После этого все студенты смогут **пушить** в этот репозиторий и создавать Pull Request'ы.

---

**Конец части 1 (только для студента А).**

---

# 📥 Часть 2. Клонирование репозитория (Студенты Б, В, Г, Д, Е, Ж)

**Время:** 10 минут  
**Кто выполняет:** Все студенты, кроме А

---

### Шаг 2.1. Принять приглашение (если прислали на почту)

- Проверьте почту, привязанную к GitHub
- Перейдите по ссылке **«View invitation»** → **«Accept invitation»**

---

### Шаг 2.2. Клонировать общий репозиторий

> **Важно:** Клонируем **оригинальный** репозиторий Студента А, а не свою копию. Форк мы **НЕ** делаем.

1. Попросите Студента А скинуть ссылку на репозиторий  
   (или найдите его в GitHub через поиск)
2. На странице репозитория нажмите **«<> Code»** → скопируйте HTTPS-ссылку
3. Откройте **PyCharm** → Get from VCS
4. Вставьте ссылку → выберите папку → Clone

---

### Шаг 2.3. Проверить, что всё работает

Откройте встроенный терминал PyCharm (`Alt+F12` или View → Tool Windows → Terminal) и выполните:

```bash
git remote -v
```

Вы должны увидеть:

```
origin  https://github.com/StudentA/team-data-processor.git (fetch)
origin  https://github.com/StudentA/team-data-processor.git (push)
```

> ✅ Это значит, что у вас один удалённый репозиторий (`origin`) — общий.

---

**Конец части 2 (для всех, кроме А).**

---

# 🌿 Часть 3. Создание веток и написание кода

**Время:** 30 минут  
**Кто выполняет:** Каждый студент (включая А) создаёт **свою** ветку

**Правила:**
- Все работают **от main**
- Название ветки: `feature/своя_роль`
- Не трогайте чужие файлы

---

## 👤 Студент А (Team Lead) – ветка `feature/main_integration`

### Задача: подготовить `src/main.py` (пока без вызовов функций)

Создайте файл `src/main.py`:

```python
def main():
    print("Team Data Processor запущен")
    print("Программа будет завершена после подключения модулей")

if __name__ == "__main__":
    main()
```

### Коммит и пуш:

```bash
git checkout -b feature/main_integration
git add src/main.py
git commit -m "Add main.py skeleton"
git push origin feature/main_integration
```

---

## 👤 Студент Б – ветка `feature/loader`

### Задача: написать функцию загрузки CSV в `src/loader.py`

Создайте файл `src/loader.py`:

```python
import csv

def load_data(filepath):
    """Загружает данные из CSV-файла и преобразует типы."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['age'] = int(row['age'])
            row['salary'] = int(row['salary'])
            data.append(row)
    return data
```

### Коммит и пуш:

```bash
git checkout main
git pull origin main              # убедиться, что main актуальна
git checkout -b feature/loader
git add src/loader.py
git commit -m "feat: add CSV loader"
git push origin feature/loader
```

> Аналогично работают остальные студенты, меняя название своей ветки и файла.

---

## 👤 Студент В – ветка `feature/cleaner`

### Файл `src/cleaner.py`:

```python
def clean_data(data):
    """Удаляет пустые строки и дубликаты по полю name."""
    seen = set()
    cleaned = []
    for row in data:
        if row['name'] not in seen and all(row.values()):
            seen.add(row['name'])
            cleaned.append(row)
    return cleaned
```

---

## 👤 Студент Г – ветка `feature/filter`

### Файл `src/filter.py`:

```python
def filter_adults(data):
    """Оставляет только записи с возрастом > 18."""
    return [row for row in data if row['age'] > 18]
```

---

## 👤 Студент Д – ветка `feature/aggregator`

### Файл `src/aggregator.py`:

```python
def average_salary(data):
    """Вычисляет среднюю зарплату."""
    if not data:
        return 0
    total = sum(row['salary'] for row in data)
    return total / len(data)
```

---

## 👤 Студент Е – ветка `feature/saver`

### Файл `src/saver.py`:

```python
import json

def save_to_json(data, filename="output.json"):
    """Сохраняет данные в JSON-файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
```

---

## 👤 Студент Ж – ветка `feature/tests`

### Файл `tests/test_processor.py`:

```python
import pytest
from src.loader import load_data
from src.filter import filter_adults

def test_load_data():
    data = load_data("data/data.csv")
    assert len(data) == 5
    assert data[0]['name'] == 'Alice'

def test_filter_adults():
    sample = [{'age': 20}, {'age': 16}, {'age': 18}]
    result = filter_adults(sample)
    assert len(result) == 1   # только 20
```

---

## 🧠 Важное пояснение про команды

| Команда | Что делает |
|---------|-------------|
| `git checkout main` | переключиться на ветку main |
| `git pull origin main` | скачать свежие изменения из main **перед** созданием ветки |
| `git checkout -b feature/...` | создать новую ветку и переключиться на неё |
| `git add <файл>` | добавить файл под версионный контроль |
| `git commit -m "..."` | зафиксировать изменения локально |
| `git push origin feature/...` | отправить ветку в общий репозиторий |

---

**Конец части 3.**

---

# 🔁 Часть 4. Создание и слияние Pull Request'ов

**Время:** 20 минут  
**Кто выполняет:** Каждый студент (создаёт PR) + Студент А (проверяет и сливает)

---

## Шаг 4.1. Каждый студент (кроме А) открывает Pull Request

1. Зайдите на **GitHub** → репозиторий `team-data-processor`
2. Вы увидите жёлтое уведомление:  
   `"feature/loader had recent pushes less than a minute ago"`  
   → нажмите **«Compare & pull request»**
3. Откроется форма PR:
   - **base:** `main`  
   - **compare:** `feature/ваша_ветка`
   - **Title:** `Добавить загрузчик данных` (например)
   - **Description:** напишите, что сделано, и какие файлы изменены
4. Нажмите **«Create pull request»**

> Если GitHub не предложил кнопку — перейдите вручную во вкладку **«Pull requests»** → **«New pull request»**.

---

## Шаг 4.2. Студент А проверяет PR

1. Перейдите во вкладку **«Pull requests»**
2. Откройте первый PR
3. Посмотрите на вкладку **«Files changed»** — там отображаются все изменения
4. Если всё правильно:
   - Напишите комментарий: `Looks good, merging!`
   - Нажмите **«Merge pull request»** → **«Confirm merge»**
5. Если нужно исправить:
   - Напишите замечания (например: «Добавь docstring к функции»)
   - Автор исправляет в своей ветке, пушит — PR обновится автоматически

> ⚠️ **Важно:** После каждого слияния PR, остальные студенты **не должны** сразу пушить свои PR, иначе возможны конфликты. Лучше дождаться, пока А примет все PR.

---

## Шаг 4.3. Обновление ветки main после каждого PR (делает А)

После слияния PR **Студент А** (или любой другой) должен обновить свою локальную `main`:

```bash
git checkout main
git pull origin main
```

Но для простоты лучше дождаться, пока **все PR** будут приняты, а затем сделать одно обновление.

---

**Конец части 4.**

---

# ⚠️ Часть 5. Разрешение конфликтов (если возникнут)

**Время:** 15 минут  
**Кто выполняет:** Студент А или автор конфликтующей ветки

Конфликт возникает, если два студента изменили **один и тот же файл** в одной строке.  
Например, если студенты Б и В оба добавили `import` в `main.py`.

---

## Шаг 5.1. GitHub показывает конфликт

При создании PR вы увидите красную надпись:  
`«Can’t automatically merge»`

---

## Шаг 5.2. Решение конфликта в PyCharm (простой способ)

1. Переключитесь на свою ветку:
   ```bash
   git checkout feature/loader
   ```
2. Слейте в неё актуальную `main`:
   ```bash
   git pull origin main
   ```
3. PyCharm покажет окно конфликта:
   - Нажмите **«Resolve conflicts»**
   - Откроется окно с тремя панелями (слева — ваш код, справа — код из main, посередине — результат)
   - Вручную выберите нужные строки (обычно нужно оставить оба изменения)
   - Нажмите **«Apply»**
4. Сделайте коммит слияния:
   ```bash
   git commit -m "Merge main into feature/loader and resolve conflict"
   git push origin feature/loader
   ```
5. Теперь PR можно сливать — конфликт решён.

---

## Шаг 5.3. Альтернативный способ (через GitHub)

- На странице PR нажмите **«Resolve conflicts»**
- Редактируйте файл прямо в браузере
- Удалите `<<<<<<<`, `=======`, `>>>>>>>`
- Нажмите **«Mark as resolved»** → **«Commit merge»**

---

**Конец части 5.**

---

# 🧩 Часть 6. Финальная интеграция (Студент А)

**Время:** 15 минут  
**Кто выполняет:** Студент А (после слияния всех feature-веток в main)

Теперь, когда все модули (loader, cleaner, filter, aggregator, saver) лежат в `main`, нужно написать **главный файл `src/main.py`**, который использует их все.

---

### Шаг 6.1. Переключиться на актуальную main

```bash
git checkout main
git pull origin main
```

---

### Шаг 6.2. Переписать `src/main.py`

Замените содержимое `src/main.py` на:

```python
from loader import load_data
from cleaner import clean_data
from filter import filter_adults
from aggregator import average_salary
from saver import save_to_json

def main():
    print("1. Загрузка данных...")
    data = load_data("data/data.csv")
    print(f"   Загружено записей: {len(data)}")
    
    print("2. Очистка данных...")
    data = clean_data(data)
    print(f"   После очистки: {len(data)}")
    
    print("3. Фильтрация (возраст > 18)...")
    data = filter_adults(data)
    print(f"   После фильтрации: {len(data)}")
    
    print("4. Подсчёт средней зарплаты...")
    avg = average_salary(data)
    print(f"   Средняя зарплата: {avg:.2f}")
    
    print("5. Сохранение результата...")
    save_to_json({
        "average_salary": avg,
        "filtered_count": len(data),
        "processed_records": data
    }, "output.json")
    
    print("✅ Готово! Результат сохранён в output.json")

if __name__ == "__main__":
    main()
```

---

### Шаг 6.3. Запустить и проверить

В терминале PyCharm:

```bash
python src/main.py
```

Ожидаемый вывод:

```
1. Загрузка данных...
   Загружено записей: 5
2. Очистка данных...
   После очистки: 5
3. Фильтрация (возраст > 18)...
   После фильтрации: 3
4. Подсчёт средней зарплаты...
   Средняя зарплата: 56666.67
5. Сохранение результата...
✅ Готово! Результат сохранён в output.json
```

---

### Шаг 6.4. Заключительный коммит и пуш

```bash
git add src/main.py
git commit -m "Integrate all modules into main.py"
git push origin main
```

---

**Конец части 6.**

---

# ✅ Часть 7. Итоговая синхронизация (все студенты)

**Время:** 5 минут  
**Кто выполняет:** Все студенты

Каждый студент должен обновить свою локальную копию проекта, чтобы получить финальную версию `main.py`.

```bash
git checkout main
git pull origin main
```

> После этого у всех в PyCharm появится полностью рабочий проект.

---

# 🧪 Часть 8. Запуск тестов (Студент Ж и все)

**Время:** 5 минут

Установите pytest (ещё не установлен):

```bash
pip install pytest
```

Запустите тесты:

```bash
pytest tests/test_processor.py -v
```

Ожидаемый результат — **2 passed**.

---

# 📋 Критерии оценки (максимум 10 баллов)

| № | Критерий | Баллы | Кто проверяет |
|---|----------|-------|----------------|
| 1 | Репозиторий создан, есть README, структура папок | 1 | Преподаватель |
| 2 | Студент А добавил всех Collaborators | 1 | GitHub Insights |
| 3 | Каждый студент клонировал репозиторий и показал `git remote -v` | 1 | Студент (скриншот) |
| 4 | Каждый студент создал свою feature-ветку и запушил её | 1 | GitHub → Branches |
| 5 | Каждый студент открыл Pull Request с понятным описанием | 1 | Список PR |
| 6 | Все PR приняты и слиты в `main` | 1 | Статус merged |
| 7 | Финальный `src/main.py` работает без ошибок | 2 | Запуск на компьютере А |
| 8 | Тесты проходят (pytest) | 1 | Вывод pytest |
| 9 | Все студенты выполнили `git pull origin main` в конце | 1 | Устный опрос |

---

# 🗣️ Контрольные вопросы (на защиту)

Каждому студенту может быть задан **один** из этих вопросов:

1. **Зачем нужна команда `git pull` перед созданием новой ветки?**
2. **Что такое Pull Request и зачем он нужен, если у всех есть доступ к репозиторию?**
3. **Как в PyCharm переключиться на другую ветку?** (показать)
4. **Что означает конфликт слияния? Приведите пример.**
5. **Чем отличается `git merge` от `git rebase`?** (для сильных студентов)
6. **Как посмотреть историю коммитов в PyCharm?** (VCS → Show Git Log)
7. **Что произойдёт, если сделать `git push origin main` без предварительного `git pull`?**
8. **Зачем нужен файл `__init__.py` в папке `src`?**

---

# 📚 Шпаргалка для студентов (можно добавить в README)

```bash
# Клонировать репозиторий (делается один раз)
git clone https://github.com/StudentA/team-data-processor.git

# Убедиться, что main актуальна
git checkout main
git pull origin main

# Создать и переключиться на новую ветку
git checkout -b feature/своя_роль

# Добавить файлы и сделать коммит
git add .
git commit -m "feat: описание изменений"

# Отправить ветку на GitHub
git push origin feature/своя_роль

# Переключиться обратно на main
git checkout main

# Обновить main (после того, как PR принят)
git pull origin main
```

---

# 🎉 Заключение

Вы успешно:
- создали общий репозиторий
- настроили командную работу через Collaborators
- работали в ветках
- открывали и сливали Pull Request'ы
- интегрировали код нескольких разработчиков
- разрешили возможные конфликты
- получили работающий продукт

**Этот процесс полностью повторяет реальный рабочий цикл в IT-командах.**
