# Лабораторная работа: «Триггеры в SQLite (DB Browser for SQLite)»

## 1. Цель работы

Научиться:

- создавать триггеры `BEFORE`, `AFTER`, `INSTEAD OF`;
- использовать ссылки `NEW` и `OLD`;
- применять условие `WHEN`;
- прерывать операцию через `RAISE(ABORT, '...')`;
- вести аудит изменений данных;
- защищать данные от некорректных изменений и удалений;
- просматривать, проверять и удалять триггеры в **DB Browser for SQLite**.

---

## 2. Краткие теоретические сведения

**Триггер** — правило базы данных, которое автоматически выполняется при `INSERT`, `UPDATE` или `DELETE`.

Общий синтаксис:

```sql
CREATE TRIGGER имя_триггера
[BEFORE | AFTER | INSTEAD OF] {INSERT | UPDATE [OF столбец] | DELETE}
ON имя_таблицы
[WHEN условие]
BEGIN
    SQL-операторы;
END;
```

В SQLite:

- поддерживаются только построчные триггеры (фактически всегда `FOR EACH ROW`);
- `BEFORE` срабатывает до изменения строки;
- `AFTER` — после изменения;
- `INSTEAD OF` используется для представлений `VIEW`;
- `NEW.столбец` — новое значение;
- `OLD.столбец` — старое значение;
- `RAISE(ABORT, 'текст')` прерывает операцию с сообщением об ошибке.

Доступность `NEW` и `OLD`:

| Событие | `NEW` | `OLD` |
|---|---|---|
| `INSERT` | да | нет |
| `UPDATE` | да | да |
| `DELETE` | нет | да |

Ограничения SQLite:

- внутри триггера в `UPDATE` и `DELETE` нельзя использовать `ORDER BY` и `LIMIT`;
- порядок срабатывания нескольких триггеров на одно событие не гарантируется;
- при `DROP TABLE` связанные триггеры удаляются автоматически;
- `FOR EACH STATEMENT` не поддерживается.

---

## 3. Как устроена эта лабораторная

В одной базе данных `lab.db` живут **две независимые схемы**:

- **Библиотека** — используется **в демонстрациях**. Таблицы: `authors`, `books`, `loans`.
- **Университет** — используется **в заданиях, которые вы выполняете сами**. Таблицы: `students`, `courses`, `enrollments`.

Общая таблица `audit_log` используется и там, и там — но столбец `table_name` показывает, кто именно писал запись.

Смысл такого деления: на «библиотеке» вы **видите, как работает** готовый триггер, а на «университете» **пробуете сами** по аналогии. Это разные таблицы — вы не запутаетесь, где демонстрация, а где ваша работа.

---

## 4. Подготовка базы данных в DB Browser for SQLite

### 4.1. Создание базы

1. Откройте **DB Browser for SQLite**.
2. Нажмите **`New Database`** (или `File → New Database`).
3. Сохраните файл как `lab.db`.

### 4.2. Скрипт создания таблиц и тестовых данных

1. Перейдите на вкладку **`Execute SQL`**.
2. Вставьте скрипт ниже в верхнее поле.
3. Нажмите **`F5`**.
4. Нажмите **`Write Changes`** на панели инструментов.

> **Важно:** в DB Browser изменения сохраняются в файл базы только после нажатия **`Write Changes`**. Без этого данные и объекты останутся только в памяти и будут потеряны при закрытии программы.

```sql
PRAGMA foreign_keys = OFF;

-- Сброс объектов, если скрипт запускается повторно
DROP VIEW IF EXISTS v_books_short;
DROP VIEW IF EXISTS v_students_public;
DROP TABLE IF EXISTS audit_log;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;

PRAGMA foreign_keys = ON;

-- ================= БИБЛИОТЕКА (для демонстраций) =================

CREATE TABLE authors (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    title     TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    year      INTEGER NOT NULL,
    price     REAL NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE loans (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id     INTEGER NOT NULL,
    reader      TEXT NOT NULL,
    loan_date   TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO authors (name) VALUES
('Лев Толстой'),
('Фёдор Достоевский');

INSERT INTO books (title, author_id, year, price) VALUES
('Война и мир', 1, 1869, 1500),
('Преступление и наказание', 2, 1866, 1200);

INSERT INTO loans (book_id, reader, loan_date) VALUES
(1, 'Анна', '2024-01-10');

-- ================= УНИВЕРСИТЕТ (для заданий) =================

CREATE TABLE students (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email     TEXT NOT NULL,
    age       INTEGER NOT NULL
);

CREATE TABLE courses (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id  INTEGER NOT NULL,
    grade      INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id)  REFERENCES courses(id)
);

INSERT INTO students (full_name, email, age) VALUES
('Анна Иванова', 'anna@example.com', 20),
('Борис Петров', 'boris@example.com', 19),
('Виктор Сидоров', 'viktor@example.com', 22);

INSERT INTO courses (title) VALUES
('Базы данных'),
('Программирование');

INSERT INTO enrollments (student_id, course_id, grade) VALUES
(1, 1, 90),
(2, 1, 75);

-- ================= ЖУРНАЛ АУДИТА (общий) =================

CREATE TABLE audit_log (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    operation  TEXT NOT NULL,
    row_id     INTEGER,
    old_value  TEXT,
    new_value  TEXT,
    changed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 4.3. Проверка

Выполните по очереди:

```sql
SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM loans;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM enrollments;
SELECT * FROM audit_log;
```

Все таблицы должны существовать, `audit_log` — пустая.

---

## 5. Демонстрации и задания

Для каждой темы:

- **5.x.1 Демонстрация** — сделайте это в DB Browser, посмотрите результат;
- **5.x.2 Задание** — сделайте сами, в отчёт приложите свой `CREATE TRIGGER` и проверку.

---

### 5.1. `AFTER INSERT` — аудит вставки

#### 5.1.1. Демонстрация на библиотеке

Логируем в `audit_log` каждого нового автора.

```sql
CREATE TRIGGER trg_demo_authors_ai
AFTER INSERT ON authors
BEGIN
    INSERT INTO audit_log (table_name, operation, row_id, new_value)
    VALUES ('authors', 'INSERT', NEW.id, 'name=' || NEW.name);
END;
```

**Пояснение.** `AFTER INSERT` срабатывает после того, как строка уже вставлена. `NEW.id` и `NEW.name` — значения новой строки. `||` — конкатенация строк. `row_id` и `new_value` — это просто наши столбцы в `audit_log`, их можно было назвать как угодно.

Проверка:

```sql
INSERT INTO authors (name) VALUES ('Антон Чехов');
SELECT * FROM audit_log WHERE table_name = 'authors';
```

Ожидание: в `audit_log` появилась одна строка с `operation = 'INSERT'`, `row_id = 3`, `new_value = 'name=Антон Чехов'`. Не забудьте `Write Changes`.

#### 5.1.2. Задание: аудит вставки студентов

**Требуется.** Создайте триггер с именем `trg_students_ai`, который после `INSERT` в `students` пишет запись в `audit_log`:

- `table_name` = `'students'`;
- `operation` = `'INSERT'`;
- `row_id` = `NEW.id`;
- `new_value` — строка вида `full_name=...; email=...; age=...`.

**Проверка:**

```sql
INSERT INTO students (full_name, email, age)
VALUES ('Тест Тестов', 'test@example.com', 20);

SELECT * FROM audit_log WHERE table_name = 'students';
```

Ожидание: одна новая строка в `audit_log` с корректно заполненными `row_id` и `new_value`.

> **Подсказка.** Возьмите демонстрационный триггер и замените таблицу, столбцы и `operation`. Никакой новой логики не требуется.

---

### 5.2. `BEFORE INSERT` + `RAISE(ABORT)` — запрет некорректной вставки

#### 5.2.1. Демонстрация на библиотеке

Запрещаем вставлять книгу, изданную до 1800 года.

```sql
CREATE TRIGGER trg_demo_books_bi_year
BEFORE INSERT ON books
BEGIN
    SELECT CASE
        WHEN NEW.year < 1800
        THEN RAISE(ABORT, 'Год издания не может быть меньше 1800')
    END;
END;
```

**Пояснение.** `BEFORE INSERT` — проверка **до** вставки. Конструкция `SELECT CASE WHEN ... THEN RAISE(ABORT, '...') END;` — идиома SQLite для проверки: если условие истинно, `RAISE(ABORT, ...)` прерывает операцию и возвращает сообщение. Если ложно — `CASE` не делает ничего.

Проверка:

```sql
-- Ошибка
INSERT INTO books (title, author_id, year, price)
VALUES ('Старая книга', 1, 1700, 500);

-- Успех
INSERT INTO books (title, author_id, year, price)
VALUES ('Книга XX века', 1, 1950, 800);
```

В нижней панели DB Browser, вкладка **`SQL log`**, при первой вставке появится:

```
Execution finished with errors.
Result: Год издания не может быть меньше 1800
```

#### 5.2.2. Задание: валидация студентов

**Требуется.** Создайте триггер `trg_students_bi_validate`, который **перед вставкой** в `students` проверяет:

- `age` не меньше 16;
- `email` содержит символ `@`.

Если проверка не проходит — прервать операцию и вернуть осмысленное сообщение об ошибке.

**Проверка:**

```sql
-- Ошибка: возраст < 16
INSERT INTO students (full_name, email, age)
VALUES ('Малолетний', 'kid@example.com', 15);

-- Ошибка: нет @
INSERT INTO students (full_name, email, age)
VALUES ('Плохой email', 'no-at-sign', 20);

-- Успех
INSERT INTO students (full_name, email, age)
VALUES ('Хороший', 'good@example.com', 18);
```

Ожидание: две первые команды завершаются ошибкой с вашим сообщением, третья — успешно.

> **Подсказка.** Две проверки можно поместить в один триггер в виде **двух** блоков `SELECT CASE WHEN ... THEN RAISE(ABORT, ...) END;`. Для проверки наличия `@` удобно `instr(NEW.email, '@') = 0` — это означает «символа `@` нет».

---

### 5.3. `AFTER UPDATE OF ... WHEN ...` — аудит только нужных изменений

#### 5.3.1. Демонстрация на библиотеке

Логируем изменение цены книги, но только если она действительно изменилась.

```sql
CREATE TRIGGER trg_demo_books_au_price
AFTER UPDATE OF price ON books
WHEN OLD.price <> NEW.price
BEGIN
    INSERT INTO audit_log (table_name, operation, row_id, old_value, new_value)
    VALUES (
        'books', 'UPDATE', NEW.id,
        'price=' || OLD.price,
        'price=' || NEW.price
    );
END;
```

**Пояснение.**

- `UPDATE OF price` — триггер срабатывает только если в `SET` упомянут столбец `price`. Если обновляют только `title`, триггер не сработает.
- `WHEN OLD.price <> NEW.price` — дополнительная проверка. Даже если `price` указан в `SET`, но значение то же самое — не логируем.

Проверка:

```sql
UPDATE books SET price = 1600 WHERE id = 1;
-- должно появиться в audit_log

UPDATE books SET price = 1600 WHERE id = 1;
-- значение не изменилось, в audit_log НЕ должно появиться

UPDATE books SET title = 'Война и мир (изд. 2)' WHERE id = 1;
-- price не в SET, в audit_log НЕ должно появиться
```

#### 5.3.2. Задание: аудит изменений email и возраста

**Требуется.** Создайте триггер `trg_students_au_contact`, который после `UPDATE` в `students` пишет запись в `audit_log`, если изменился `email` **или** `age`:

- `table_name` = `'students'`;
- `operation` = `'UPDATE'`;
- `row_id` = `NEW.id`;
- `old_value` — строка с `email` и `age` до изменения;
- `new_value` — строка с `email` и `age` после изменения.

Если `UPDATE` меняет только `full_name` или присваивает те же значения — записи в `audit_log` быть **не должно**.

**Проверка:**

```sql
-- Должна появиться запись
UPDATE students SET email = 'anna.new@example.com' WHERE id = 1;

-- НЕ должно появиться записи (значение не изменилось)
UPDATE students SET email = 'anna.new@example.com' WHERE id = 1;

-- НЕ должно появиться записи (full_name не отслеживается)
UPDATE students SET full_name = 'Анна Иванова (изм.)' WHERE id = 1;

SELECT * FROM audit_log WHERE table_name = 'students' AND operation = 'UPDATE';
```

Ожидание: в `audit_log` ровно одна запись про это изменение.

> **Подсказка.** Скомбинируйте `UPDATE OF email, age` (два столбца через запятую) и `WHEN OLD.email <> NEW.email OR OLD.age <> NEW.age`.

---

### 5.4. `BEFORE DELETE` + `RAISE(ABORT)` — защита от удаления

#### 5.4.1. Демонстрация на библиотеке

Запрещаем удалять автора, у которого есть книги.

```sql
CREATE TRIGGER trg_demo_authors_bd
BEFORE DELETE ON authors
BEGIN
    SELECT CASE
        WHEN (SELECT COUNT(*) FROM books WHERE author_id = OLD.id) > 0
        THEN RAISE(ABORT, 'Нельзя удалить автора, у которого есть книги')
    END;
END;
```

**Пояснение.** `BEFORE DELETE` срабатывает **до** удаления. `OLD.id` — id удаляемой строки. В подзапросе считаем, сколько книг ссылается на этого автора. Если больше нуля — прерываем удаление.

Проверка:

```sql
-- Ошибка (у автора id = 1 есть книги)
DELETE FROM authors WHERE id = 1;

-- Успех (у нового автора нет книг)
INSERT INTO authors (name) VALUES ('Временный Автор');
DELETE FROM authors WHERE name = 'Временный Автор';
```

#### 5.4.2. Задание: защита от удаления студента с курсами

**Требуется.** Создайте триггер `trg_students_bd_enrolled`, который **не позволяет** удалить студента, если на него есть хотя бы одна запись в `enrollments`. Сообщение об ошибке — осмысленное.

**Проверка:**

```sql
-- Ошибка (у студента id = 1 есть курсы)
DELETE FROM students WHERE id = 1;

-- Успех (нет курсов)
INSERT INTO students (full_name, email, age)
VALUES ('Без Курсов', 'nocourse@example.com', 20);
DELETE FROM students WHERE email = 'nocourse@example.com';
```

> **Подсказка.** Демонстрационный триггер полностью подходит по структуре — нужно только заменить таблицу и связанную таблицу на `enrollments`, а `author_id` — на `student_id`.

---

### 5.5. `BEFORE UPDATE OF ...` — проверка значения при обновлении

#### 5.5.1. Демонстрация на библиотеке

Запрещаем выставлять дату возврата книги раньше даты выдачи.

```sql
CREATE TRIGGER trg_demo_loans_bu_dates
BEFORE UPDATE OF return_date ON loans
BEGIN
    SELECT CASE
        WHEN NEW.return_date IS NOT NULL
         AND NEW.return_date < NEW.loan_date
        THEN RAISE(ABORT, 'Дата возврата не может быть раньше даты выдачи')
    END;
END;
```

**Пояснение.** Даты хранятся как строки `YYYY-MM-DD`, и такие строки корректно сравниваются лексикографически — то есть `'2024-02-01' < '2024-01-10'` ложно, а `'2023-12-01' < '2024-01-10'` истинно. Условие `NEW.return_date IS NOT NULL` обязательно: пока книга не возвращена, `return_date` может быть `NULL`, и это допустимо.

Проверка:

```sql
-- Ошибка
UPDATE loans SET return_date = '2023-12-01' WHERE id = 1;

-- Успех
UPDATE loans SET return_date = '2024-02-15' WHERE id = 1;
```

#### 5.5.2. Задание: проверка оценки

**Требуется.** Создайте триггер `trg_enrollments_bu_grade`, который при **обновлении оценки** в `enrollments` не позволяет выставить значение вне диапазона `0..100`. Значение `NULL` (оценка ещё не выставлена) должно оставаться допустимым.

**Проверка:**

```sql
-- Ошибка
UPDATE enrollments SET grade = 101 WHERE student_id = 1 AND course_id = 1;

-- Ошибка
UPDATE enrollments SET grade = -5 WHERE student_id = 1 AND course_id = 1;

-- Успех
UPDATE enrollments SET grade = 95 WHERE student_id = 1 AND course_id = 1;

-- Успех (сброс оценки)
UPDATE enrollments SET grade = NULL WHERE student_id = 1 AND course_id = 1;
```

> **Подсказка.** Используйте `BEFORE UPDATE OF grade` и проверьте `NEW.grade IS NOT NULL AND (NEW.grade < 0 OR NEW.grade > 100)`.

---

### 5.6. `INSTEAD OF INSERT` — вставка через представление

#### 5.6.1. Демонстрация на библиотеке

Создаём «сокращённое» представление книг (только название и год) и разрешаем вставку через него — при этом в базовой таблице `books` заполняются значения по умолчанию для `author_id` и `price`.

```sql
CREATE VIEW v_books_short AS
SELECT title, year FROM books;

CREATE TRIGGER trg_demo_v_books_ins
INSTEAD OF INSERT ON v_books_short
BEGIN
    INSERT INTO books (title, author_id, year, price)
    VALUES (NEW.title, 1, NEW.year, 0);
END;
```

**Пояснение.** В `v_books_short` нет столбцов `author_id` и `price`, а в `books` они обязательны. Прямая вставка в представление невозможна — SQLite не может автоматически додумать, что куда подставлять. `INSTEAD OF INSERT` перехватывает вставку в представление и сам вставляет строку в `books`.

Проверка:

```sql
INSERT INTO v_books_short (title, year) VALUES ('Новая повесть', 2024);

SELECT * FROM v_books_short WHERE title = 'Новая повесть';
SELECT * FROM books WHERE title = 'Новая повесть';
```

Ожидание: в `books` появилась строка с `author_id = 1` и `price = 0`; в `v_books_short` она видна.

#### 5.6.2. Задание: представление «публичные данные студента»

**Требуется.**

1. Создайте представление `v_students_public`, которое показывает только `full_name` и `email` студентов.
2. Создайте триггер `trg_v_students_public_ins`, который **через это представление** позволяет вставлять новых студентов — при этом в таблицу `students` `age` записывается равным `18`.

**Проверка:**

```sql
INSERT INTO v_students_public (full_name, email)
VALUES ('Студент Через View', 'view@example.com');

SELECT * FROM students WHERE email = 'view@example.com';
```

Ожидание: в `students` появилась строка с `age = 18`.

> **Подсказка.** Структура та же, что в демонстрации, но триггер ссылается на `v_students_public` и `students`.

---

## 6. Дополнительные задания (для самостоятельной работы)

Выполните **2–3 задания на выбор**. Решения в отчёте — ваш собственный код.

1. **`AFTER DELETE` на `students`.** Создайте триггер, который после успешного удаления студента пишет запись в `audit_log`: `operation = 'DELETE'`, `old_value` — строка с `full_name` и `email` удалённого студента.
   - **Проверка:** добавьте студента без курсов, удалите его, проверьте `audit_log`.

2. **Запрет удаления курса, на который есть записи.** Триггер `BEFORE DELETE` на `courses` должен прерывать удаление, если в `enrollments` есть `course_id = OLD.id`.
   - **Проверка:** попробуйте удалить `courses.id = 1` (ошибка) и добавьте/удалите новый курс без записей (успех).

3. **Аудит изменения оценки.** Триггер `AFTER UPDATE OF grade` на `enrollments` пишет в `audit_log` старую и новую оценку. Срабатывать только когда оценка действительно изменилась (используйте `WHEN OLD.grade <> NEW.grade`).

4. **Проверка при вставке оценки.** Триггер `BEFORE INSERT ON enrollments`: `grade` (если не `NULL`) должен быть `0..100`. Иначе — `RAISE(ABORT, ...)`.
   - **Проверка:** вставка с `grade = 150` — ошибка; вставка с `grade = 80` — успех.

5. **Логирование только повышения возраста.** Триггер `AFTER UPDATE OF age` на `students` пишет в `audit_log`, только если `NEW.age > OLD.age`. При понижении — не пишет. Проверьте оба случая.

6. **`INSTEAD OF UPDATE` для `v_students_public`.** Создайте триггер, который через представление `v_students_public` разрешает **обновлять email** — фактически обновляя столбец `email` в `students` по `full_name`.
   - **Проверка:** `UPDATE v_students_public SET email = 'new@example.com' WHERE full_name = 'Анна Иванова';` затем `SELECT * FROM students WHERE full_name = 'Анна Иванова';`.

---

## 7. Контрольные вопросы

1. Чем отличается `BEFORE`-триггер от `AFTER`-триггера?
2. В каких событиях доступны `NEW` и `OLD`?
3. Для чего используется `INSTEAD OF`?
4. Что делает `RAISE(ABORT, '...')`?
5. Зачем нужен `WHEN` в триггере?
6. Почему в SQLite нельзя создать `FOR EACH STATEMENT`-триггер?
7. Что произойдёт с триггерами при удалении таблицы `DROP TABLE`?
8. Почему порядок срабатывания нескольких триггеров на одно событие нельзя считать надёжным?
9. Чем отличается `UPDATE OF price` от `UPDATE` без `OF`?
10. Почему в задании 5.5 нужно проверять `NEW.return_date IS NOT NULL`, а не только сравнение дат?

---

## 8. Требования к отчёту

Отчёт должен содержать:

- **для каждого задания (5.1–5.6):**
  - ваш SQL-код `CREATE TRIGGER`;
  - скриншоты или текстовые результаты всех проверочных запросов;
  - для ошибочных запросов — сообщение из `SQL log`;
- **для 2–3 дополнительных заданий:** код, объяснение, проверка;
- ответы на контрольные вопросы;
---


## 10. Советы по работе в DB Browser for SQLite

- **`Write Changes`** — обязательный шаг после любых успешных `CREATE`, `INSERT`, `UPDATE`, `DELETE`. Без него изменения не сохранятся в файл.
- **Выполнить один запрос.** Если в поле несколько команд, выделите нужную и нажмите `F5`. Если вы создаёте триггер — **выделяйте весь блок** от `CREATE TRIGGER` до `END;`.
- **Где искать ошибку.** Сообщения, в том числе от `RAISE(ABORT, ...)`, отображаются в нижней панели, вкладка **`SQL log`**.
- **Просмотр данных.** Табличный просмотр — вкладка **`Browse Data`**, выбрать таблицу из выпадающего списка.
- **Просмотр структуры и триггеров.** Вкладка **`Database Structure`**. Слева раскройте ветку **`Triggers`** — там список всех созданных триггеров. Клик по триггеру показывает его `CREATE`.
- **Проверка через SQL.**
    ```sql
    SELECT name, tbl_name, sql FROM sqlite_master WHERE type = 'trigger';
    ```
- **Удалить триггер.**
    ```sql
    DROP TRIGGER имя_триггера;
    ```
    Затем `Write Changes`.
- **Повторный запуск начального скрипта.** Начальный скрипт содержит `DROP ... IF EXISTS`, поэтому его можно выполнить заново — база сбросится к исходному состоянию. Не забудьте: скрипт сначала `DROP`-ает таблицы, поэтому созданные вами триггеры будут автоматически удалены вместе с таблицами.
- **Не запутайтесь в схемах.** Триггеры для библиотеки (`trg_demo_*`) — только демонстрации. Ваши решения — триггеры с именами `trg_students_*`, `trg_enrollments_*`, `trg_v_students_public_*`.
- **Горячие клавиши.** `F5` или `Ctrl+R` — выполнить SQL; в некоторых версиях также `Ctrl+Enter`.
